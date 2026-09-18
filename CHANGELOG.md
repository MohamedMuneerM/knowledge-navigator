# Changelog

Versions follow `data/manifest.json`. Content changes that add chapters or roadmaps bump the
minor version; fixes bump the patch version.

## 1.0.0: first public release

- 11 disciplines, 1,432 chapters, 14,439 topics, audited against MSC2020, APS PhySH, CS2023,
  ACS/RSC, ABET/NCEES, the NASA Technology Taxonomy and university curricula
  ([docs/AUDIT.md](docs/AUDIT.md)).
- Every chapter has a level, priority, summary and direct prerequisites (2,430 links, 332 across
  disciplines).
- 13 prerequisite-complete goal roadmaps.
- Dashboard: roadmaps, discipline learning order, path finder, progress, notes and links.
- One JSON file per chapter; `scripts/build.py` validation, `scripts/check_ids.py` id protection,
  and redirects for renamed ids.
- CI validation on pull requests, GitHub Pages deployment, release zips.
