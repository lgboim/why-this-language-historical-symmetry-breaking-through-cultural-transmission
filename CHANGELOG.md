# Changelog

All notable public changes to this repository are documented here. Scientific changes between manuscript versions are in `replication/CHANGELOG_v2.md`.

## Unreleased

## 2.0.0 — 2026-09-05

- First curated public repository, assembled from the Version 2.0.0 working tree archived at https://doi.org/10.5281/zenodo.22338797.
- Added the Version 2.0 manuscript, supplement, revision notes and their Markdown sources (`paper/`), the four publication figures with every plotted statistic (`figures/`), the simulation code, evaluators, pre-registrations, verdict reports and saved evaluator inputs (`replication/`), and the independent data verification of 5 September 2026 (`verification/`).
- Added citation, research-software, reproducibility, contribution, security and licence metadata, a SHA-256 manifest with a checker, issue and pull-request templates, and an automated repository-quality workflow.
- Fixed a reporting bug in `replication/confirm4.py`: when no gen-0/gen-5 lineage data are present, the script now exits with its intended message instead of a `NameError`. No result is affected.
- Rewrote the absolute local paths in the verification documents as repository-relative links.

## 2.0 / 2.0.0 (Zenodo) — 2026-09-05

- Corrected release after an independent data verification. Preprint: https://doi.org/10.5281/zenodo.22338453. Code and results: https://doi.org/10.5281/zenodo.22338797. Every change is listed in `replication/CHANGELOG_v2.md`.

## 1.0 / 1.0.0 (Zenodo) — 2026-09-04

- First public release. Preprint: https://doi.org/10.5281/zenodo.22305643. Code and results: https://doi.org/10.5281/zenodo.22305564. Superseded by Version 2.0; kept immutable for the record.
