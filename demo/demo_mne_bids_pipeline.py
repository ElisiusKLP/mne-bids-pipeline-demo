import marimo

__generated_with = "0.23.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # DEMO: MNE BIDS Pipeline

    **April 2026**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The following notebook is a guide/tutorial on how to use the full config-based mne-bids-pipeline package. https://mne.tools/mne-bids-pipeline/stable/

    The notebook is made using the marimo notebook library. https://marimo.io/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The notebook will go through the following steps:

    1. Converting raw data to BIDS format.
    2. Setup a configuration file.
    3. Running the pipeline
    4. Optional: Manual Intervention (ICA Exclusion)
    5. QC Report Investigation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Guide
    ## 1. Convert raw data to BIDS format
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    mne_bids_pipeline is built upon a main assumption to function correctly. That you input neuroimaging data is given in the BIDS (Brain Imaging Data Structure) compatible format. The BIDS format has become the governing data standard for neuroimaging data repositories.

    To learn more see the official BIDS page, https://bids.neuroimaging.io/. Or browse OpenNeuro to look at different datasets, https://openneuro.org/.

    The MNE ecosystem also provides the mne_bids package which works as a nice way to handle BIDS data inside Python.
    https://mne.tools/mne-bids/stable/index.html

    Different MEG (or EEG) systems can output varying data, where some are more common than other. The most widely used being the Elekta Neuromag while other systems are CTF, Ricoh, Yokogawa or other OPM systems.

    Elekta neuromag is therefore often the default supported system in MNE Python and other neuroimaging processing libraries. Other systems might therefore require some additional data wrangling and debugging to fit into BIDS and the required format for mne_bids_pipeline.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example of CTF to BIDS
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Setup a configuration file
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Running the pipeline
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We run the pipeline from the terminal cli using the ``mne_bids_pipeline`` and pass our config + what processing steps we want to run.

    List of processing steps:
    https://mne.tools/mne-bids-pipeline/stable/features/steps.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An example of running only preprocessing:
    ```bash
    mne_bids_pipeline --config=config/config_effort.py --steps=preprocessing
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. ICA Exclusion (Reqires Manual Intervention)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we have to specify what ICA components correspond to artifacts through 3 steps:

    1. Find bad components in the subject HTML report.
    2. In the TSV, for each bad component row, change status from good to bad. Optionally, update status_description with your reason.
    3. Run the apply_ica step

    After running --steps=preprocessing the ICA components can be check inside each of the **_report.html files.

    Each subdirectory that we are iterating over (either sub-xy/ or sub-xy/ses-xy/) contains a **_proc-ica_components.tsv file.
    See: [ICA requires manual intervention!](https://mne.tools/mne-bids-pipeline/stable/settings/preprocessing/ssp_ica.html#mne_bids_pipeline._config.spatial_filter:~:text=ICA%20requires%20manual,to%20be%20updated!)

    In this file you can change status from ``good -> bad`` and optionally add a description for the artifact e.g. blinks, heart etc.

    The edited rows could look like this:
    ```tsv
    component	type	description	status	status_description
    3	ica	Independent Component	bad	Manual: blink artifact
    7	ica	Independent Component	bad	Manual: cardiac artifact
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Re-run the "apply ICA" step after specifying ICA exclusion file.

    !Important: Make sure that each of the .tsv files are saved before applying the ICA. To be sure, close down all open tabs with tsvs.

    ```bash
    mne_bids_pipeline --config=/path/to/your/custom_config.py --steps=preprocessing/apply_ica
    ```

    Note: If it seems like the step i getting skipped due to cache or you changed anything in the .tsv's, you can add the flag ``--no-cache``.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **But are there not any automatic ICA artifact labelling options?**

    MNE BIDS Pipeline currently (1.10) supports ICLabel for EEG data ONLY (not MEG). It can classify ICA components with label for artifacts ("blink", "heartbeat" etc.) with a probability and the user can define a rejection threshold. This will automatically mark it as "bad" in the tsv.

    MNE-ICALabel also implemented MEGNet for automated ICA-based artifact removal, but this has not been implemented into MNE BIDS Pipeline currently (24. april 2026 v1.10).
    See: https://mne.tools/mne-icalabel/stable/api/megnet.html
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. QC Report Investigation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
