#!/usr/bin/env python3
"""
Browser test for the dashboard: pinned header and sidebar while scrolling, no sideways
scrolling on phones, the main interactions, and no JavaScript errors. Desktop and phone sizes.

  pip install playwright && python -m playwright install chromium   (once)
  python scripts/build.py && python scripts/ui_test.py               test the local copy
  python scripts/ui_test.py https://example.org/                     test a deployed copy
  python scripts/ui_test.py -v                                       also list passing checks
"""
import functools, http.server, pathlib, sys, threading
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
urls = [a for a in sys.argv[1:] if not a.startswith('-')]
if urls:
    BASE = urls[0]
else:
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    BASE = f'http://127.0.0.1:{server.server_address[1]}/index.html'
problems, notes = [], []


def check(cond, msg):
    (notes if cond else problems).append(('OK   ' if cond else 'FAIL ') + msg)


with sync_playwright() as p:
    try:
        browser = p.chromium.launch(channel='chrome', headless=True)   # installed Chrome, if any
    except Exception:
        browser = p.chromium.launch(headless=True)                     # Playwright's own Chromium
    for label, vp in [('desktop', {'width': 1400, 'height': 900}), ('mobile', {'width': 390, 'height': 844})]:
        ctx = browser.new_context(viewport=vp)
        page = ctx.new_page()
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.on('console', lambda m: m.type == 'error' and errors.append(m.text))

        for route in ['#/', '#/d/electronics', '#/r/rocket-science', '#/path/ph-general-relativity', '#/d/math']:
            page.goto(BASE + route)
            page.wait_for_selector('#view .card, #view .item, #view h1')
            height = page.evaluate('document.documentElement.scrollHeight')
            for y in [vp['height'] * 1.5, height / 2, height - vp['height']]:
                page.evaluate(f'window.scrollTo(0, {int(y)})')
                page.wait_for_timeout(80)
                top = page.evaluate("document.querySelector('.topbar').getBoundingClientRect().top")
                check(abs(top) < 1, f'{label} {route}: top bar pinned at scroll {int(y)} (top={top:.0f})')
                if label == 'desktop':
                    nav = page.evaluate("document.querySelector('.sidenav').getBoundingClientRect().top")
                    check(abs(nav - 58) < 2, f'{label} {route}: side nav pinned at scroll {int(y)} (top={nav:.0f})')
            overflow = page.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')
            check(overflow <= 0, f'{label} {route}: no horizontal scroll (overflow={overflow}px)')

        # Interactions
        page.goto(BASE + '#/r/rocket-science')
        page.wait_for_selector('.item')
        page.click('.item.next')
        page.wait_for_selector('#drawer.open')
        check(page.is_visible('#drawer .dr-title'), f'{label}: roadmap item opens the chapter panel')
        page.click('#drawer .status-seg [data-s="in-progress"]')
        check(page.eval_on_selector('#drawer .status-seg [data-s="in-progress"]', 'e => e.classList.contains("on")'),
              f'{label}: status change sticks')
        page.click('#drawer [data-tid]')
        check(page.eval_on_selector('#drawer [data-tid]', 'e => e.checked'), f'{label}: topic checkbox ticks')
        page.keyboard.press('Escape')
        page.wait_for_timeout(250)
        check(not page.is_visible('#drawer.open'), f'{label}: Escape closes the panel')

        if label == 'mobile':
            page.click('#menuBtn')
            page.wait_for_timeout(250)
            check(page.eval_on_selector('#sidenav', 'e => e.classList.contains("open")'), 'mobile: menu button opens navigation')
            page.click('#sidenav a[href="#/d/physics"]')
            page.wait_for_timeout(250)
            check(not page.eval_on_selector('#sidenav', 'e => e.classList.contains("open")'), 'mobile: navigation closes after choosing')

        page.goto(BASE + '#/')
        page.fill('#q', 'rocket engine')
        page.wait_for_selector('#results.open .result')
        page.keyboard.press('Enter')
        page.wait_for_selector('#drawer.open')
        check('?c=' in page.url, f'{label}: search + Enter opens a chapter')

        page.keyboard.press('Escape')
        page.wait_for_timeout(250)
        before = page.evaluate('document.documentElement.dataset.theme')
        page.click('#themeBtn')
        after = page.evaluate('document.documentElement.dataset.theme')
        check(before != after and after in ('light', 'dark'), f'{label}: theme toggles ({before} -> {after})')

        page.goto(BASE + '#/path/ae-liquid-rocket-engines')
        page.wait_for_selector('.stage-num')
        check(page.locator('.stage-num').count() > 5, f'{label}: path finder shows steps')

        check(not errors, f'{label}: no console/page errors {errors[:3]}')
        ctx.close()
    browser.close()

print('\n'.join(problems + notes if '-v' in sys.argv else problems) or 'no failures')
print(f'{len(notes)} passed, {len(problems)} failed')
sys.exit(1 if problems else 0)
