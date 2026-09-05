# Contributing

Corrections that improve reproducibility, documentation, portability, or the accuracy of the public record are welcome.

## Before opening an issue

- Read `README.md`, `REPRODUCIBILITY.md` and `LICENSE-SCOPE.md`.
- Check existing issues for the same question.
- Run commands from `replication/` in an isolated Python environment with the packages in `requirements.txt`.
- Do not upload credentials, private paths, or generated run files of several hundred megabytes; describe run files by cell, seed and SHA-256 instead.

## Good issue reports

A useful report includes:

- the affected file and, where possible, line number;
- the expected and observed behaviour;
- the exact command used and its environment variables (`K_OUT`, `K_SEEDS`, `K_ARCH`, `FIG_OUT`);
- operating system, Python and PyTorch versions;
- a minimal traceback or the regenerated table next to the shipped one;
- hashes for shipped inputs when a mismatch is involved.

## Pull requests

Keep changes narrowly scoped. Explain whether the change affects code, saved inputs, verdict reports, prose, metadata or licensing. Run the repository quality checks locally where practical:

```bash
python verify_manifest.py --check
python -m compileall -q replication
python -m json.tool codemeta.json >/dev/null
python -c "import yaml; yaml.safe_load(open('CITATION.cff', encoding='utf-8'))"
cd replication && python tests.py
```

A change to any tracked file must be followed by `python verify_manifest.py --write` so that `public_manifest.json` stays current.

If a change alters a verdict report or a figure, state which inputs and scripts produced it, and keep the original next to it as `replication/corrections_v2/` does. Do not silently replace the immutable Zenodo artefacts. Corrections should be documented in `CHANGELOG.md`, and substantive corrections in a dated changelog like `replication/CHANGELOG_v2.md`, then released as a new version.

## Research and citation scope

Issues and pull requests should distinguish among pre-registered confirmations, pre-registered failures, exploratory descriptives and interpretation. A new empirical claim requires a stated outcome, the seed as the independent unit, paired comparisons where the design pairs seeds, and a reproducible derivation from named inputs. The registrations in `replication/results_*/PREREG.md` and the thresholds in `replication/manifest_k.json` are historical documents and are not edited; corrections to how they were evaluated are recorded next to them.

By contributing, you agree that original code contributions are licensed under MIT and original documentation, figures or result-table contributions are licensed under CC BY 4.0, consistent with `LICENSE-SCOPE.md`.
