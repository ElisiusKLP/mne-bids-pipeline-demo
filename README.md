# MNE BIDS Pipeline Demo

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/ElisiusKLP/mne-bids-pipeline-demo/blob/main/notebooks/demo_mne_bids_pipeline.py)

This repository contains a guided marimo notebook that walks through the MNE BIDS Pipeline workflow end to end. It is meant to be read as a tutorial first, and then used as a small hands-on demo if you want to try the pipeline locally with the bundled example data.

## How to use this repo

If you want to read the notebook as a guide, open it directly in Molab:

https://molab.marimo.io/github/ElisiusKLP/mne-bids-pipeline-demo/blob/main/notebooks/demo_mne_bids_pipeline.py

If you want to run the demo locally and try the notebook cells yourself, clone the repository and open it in VS Code or another editor that supports marimo notebooks.

```bash
git clone https://github.com/ElisiusKLP/mne-bids-pipeline-demo.git
cd mne-bids-pipeline-demo
```

## What the notebook covers

The notebook in [notebooks/demo_mne_bids_pipeline.py](notebooks/demo_mne_bids_pipeline.py) is organized into two parts:

1. A tutorial-style walkthrough of the MNE BIDS Pipeline.
2. A small demo section that loads BIDS data, inspects events, and runs preprocessing steps.

It shows how to:

- convert non-BIDS MEG data into BIDS,
- define a pipeline configuration,
- run preprocessing,
- inspect ICA components,
- and apply ICA exclusions.

## Demo data

The demo uses OpenNeuro-style BIDS data and expects the `data/` folder structure included in this repository. The final cells in the notebook are intended for a small tryout on a single subject/session once the data has been retrieved.

## Requirements

The project is built around:

- `marimo`
- `mne`
- `mne-bids`
- `mne-bids-pipeline`

To setup the virtual environment, it is recommended that you use uv. https://docs.astral.sh/uv/#installation. When you have clone the repository you can simply run ``uv sync`` from the location of the repository.

## Notes

- The notebook is easiest to follow in Molab if you just want to browse the workflow.
- The local demo cells are best used after cloning the repository so the example `data/` directory and config files are available.
- Some cells are intentionally exploratory and may need small edits depending on the exact dataset you download.

