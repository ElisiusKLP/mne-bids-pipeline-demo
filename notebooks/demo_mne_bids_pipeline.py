import marimo

__generated_with = "0.23.3"
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
    The following notebook is a guide/tutorial on how to use the full config-based mne-bids-pipeline package.

    This notebook is a guided introduction to the MNE BIDS Pipeline. The MNE BIDS Pipeline is a Python Library based on MNE that offers a full-scale processing pipeline based on a single configuration file to specify what steps to run and their parameter settings,
    https://mne.tools/mne-bids-pipeline/stable/.

    This guide shows two related things: first, how a non-BIDS dataset can be converted into BIDS, using CTF data as an example; second, how to run the pipeline on BIDS-formatted data. Tranforming non-BIDS to BIDS data is highly dependent on the relevant non-BIDS structure. Therefore, the CTF section is illustrative and is not intended as the recommended starting point for running the pipeline locally.
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
    The notebook is made using the marimo notebook library. https://marimo.io/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## TODO: Before You Start

    Use this notebook if you want a guided tour of the full MNE BIDS Pipeline workflow.

    What you need:
    - A BIDS-formatted dataset, or for example, a raw CTF data like the one that has been used in this demo.
    - A working Python environment with `mne`, `mne-bids`, `mne-bids-pipeline`, and `marimo`.
    - A terminal available for running the pipeline and, if needed, a local web server for HTML reports.

    What this notebook will help you do:
    - Understand why the pipeline expects BIDS input.
    - Convert one dataset into BIDS format.
    - Create and edit a pipeline config.
    - Run preprocessing and inspect the reports.
    - Complete ICA rejection manually when needed.

    If you already have BIDS data, you can skim the conversion section and jump ahead to the config and pipeline steps.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Guide
    ## 0. Introduction

    MNE BIDS Pipeline is a full-scale electrophysiological EEG/MEG processing pipeline. It is configuration based meaning that all parameters are set from a single configuration file which is then specfied when running the pipeline using a terminal/CLI command.

    The pipeline consists of a series of sequential processing steps that range from preprocessing to analyses.
    These steps include:
    - Preprocessing
    - Sensor-space analysis
    - Source-space analysis
    - Freesurfer-related processing (Surface reconstruction via FreeSurfer. Not run by deafult)

    See: [List of processing steps](https://mne.tools/mne-bids-pipeline/stable/features/steps.html)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Convert raw data to BIDS format (Optional)

    mne_bids_pipeline is built upon a main assumption to function correctly. That you input neuroimaging data is given in the BIDS (Brain Imaging Data Structure) compatible format. The BIDS format has become the governing data standard for neuroimaging data repositories.

    If you already know about BIDS and have your data in BIDS format you can skip step 1.

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
    ### 1.1 CTF to BIDS example
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The following section demonstrates how a non-BIDS MEG dataset can be converted into BIDS format. We use CTF here only as an example of a dataset that needs conversion before it can be processed by MNE BIDS Pipeline. If your data is already in BIDS format, you can skip this section and move directly to the pipeline configuration and run steps.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The following function was made to convert data collected from a CTF scanner into a BIDS format.

    The raw CTF data is structured like this:
    ```
    0001_effortlearning_20250805_01.ds
    │   ├── 0001_effortlearning_20250805_01.acq
    │   ├── 0001_effortlearning_20250805_01.eeg
    │   ├── 0001_effortlearning_20250805_01.hc
    │   ├── 0001_effortlearning_20250805_01.hist
    │   ├── 0001_effortlearning_20250805_01.infods
    │   ├── 0001_effortlearning_20250805_01.infods.bak
    │   ├── 0001_effortlearning_20250805_01.meg4
    │   ├── 0001_effortlearning_20250805_01.newds
    │   ├── 0001_effortlearning_20250805_01.res4
    │   ├── BadChannels
    │   ├── ChannelGroupSet.cfg
    │   ├── ClassFile.cls
    │   ├── MarkerFile.mrk
    │   ├── bad.segments
    │   └── hz.ds
    │       ├── BadChannels
    │       ├── hz.acq
    │       ├── hz.hc
    │       ├── hz.hist
    │       ├── hz.infods
    │       ├── hz.meg4
    │       ├── hz.newds
    │       └── hz.res4
    ├── 0001_effortlearning_20250805_02.ds
    (...)
    ```

    After running the create_bids_directory as defined below, the data is transformed into the following BIDS structure:
    ```
    ── README
    ├── dataset_description.json
    ├── participants.json
    ├── participants.tsv
    ├── sub-01
    │   ├── ses-01
    │   │   ├── meg
    │   │   │   ├── sub-01_ses-01_coordsystem.json
    │   │   │   ├── sub-01_ses-01_task-effort_channels.tsv
    │   │   │   ├── sub-01_ses-01_task-effort_events.json
    │   │   │   ├── sub-01_ses-01_task-effort_events.tsv
    │   │   │   ├── sub-01_ses-01_task-effort_meg.fif
    │   │   │   └── sub-01_ses-01_task-effort_meg.json
    │   │   └── sub-01_ses-01_scans.tsv
    │   ├── ses-02
    │   │   ├── meg
    │   │   │   (...)
    │   ├── ses-03
    │   └── ses-04
    └── sub-02
        ├── ses-01
        ├── ses-02
        ├── ses-03
        └── ses-04
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ```python
    import numpy as np
    from pathlib import Path
    import mne
    from mne_bids import BIDSPath, write_raw_bids

    def create_bids_directory(
        n_subjects, n_sessions,
        input_dir_path, bids_dir_path,
        event_dict):
        for i in range(n_subjects):
            i += 1  # subject numbering starts at 1
            for j in range(n_sessions):
                j += 1  # session numbering starts at 1
                # we set a file pattern to match the raw CTF files for each subject i and session j which are named e.g. "0001_effortlearning_20250101_01.ds"
                pattern = f"{i:04d}_effortlearning_*_{j:02d}.ds"
                # find the file matching the pattern
                matches = list(input_dir_path.glob(pattern))  # Store as a list
                if not matches:  # Check if the list is empty
                    raise FileNotFoundError(f"No file found matching pattern: {pattern}")
                print(f"Matches: {matches}")
                print(f"Number of matches: {len(matches)}")
                filepath = matches[0]  # Use the stored list
                print(f"Filepath: {filepath}")
                # read the raw CTF file
                raw_ctf = mne.io.read_raw_ctf(filepath, preload=True)


                # Remove unwanted Tr1 annotations
                ## Tr1 annotations are system-generated trigger markers from the CTF recording/import process,
                ## not task events we want to keep for BIDS conversion.
                ## We remove them here so event extraction only uses the meaningful experimental markers.
                if raw_ctf.annotations is not None:
                    # Filter out 'Tr1' annotations, keep only our true events
                    annot = raw_ctf.annotations
                    mask = annot.description != 'Tr1'
                    raw_ctf.set_annotations(annot[mask])

                # Extract events for renaming
                events = mne.find_events(raw_ctf, shortest_event=1)

                # Create new event dict with items from event dict, and where all other events are labeled as the event id (e.g., 30039 -> "30039")
                ## We could also isolate the data to only the events of interest,
                ## but for now we will keep all events in case we want to use them later on for something else.
                new_event_dict = event_dict.copy()
                unique_triggers = np.unique(events[:, 2])
                for trigger_id in unique_triggers:
                    if trigger_id not in new_event_dict.values():
                        new_event_dict[str(trigger_id)] = int(trigger_id)

                print(f"New event dict: {new_event_dict}")

                # setup bids-path for subject-session
                bids_path = BIDSPath(subject=f"{i:02d}", session=f"{j:02d}", task="effort", root=bids_dir_path)
                write_raw_bids(
                    raw_ctf,
                    bids_path,
                    events=events,
                    event_id=new_event_dict,
                    overwrite=True,
                    allow_preload=True,
                    format="FIF")

    event_dict = {
        "force_start": 4,
        "feedback_onset": 8,
        "cue_onset": 19
    }
    n_subjects = 2
    n_sessions = 4
    root = Path.cwd()
    bids_dir_path = root / "data/effort_bids"
    input_dir_path = root / "foreign_data/effort"

    create_bids_directory(n_subjects, n_sessions, input_dir_path, bids_dir_path, event_dict)
    ```
    """)
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
    A template configuration file can be created using the following terminal command: ``mne_bids_pipeline --create-config=/path/to/your/custom_config.py``.
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
    ## 4. ICA Exclusion (Requires Manual Intervention)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next we have to specify what ICA components correspond to artifacts through 3 steps:

    1. Find bad components in the subject HTML report.
    2. In the TSV, for each bad component row, change status from good to bad. Optionally, update status_description with your reason.
    3. Run the apply_ica step

    After running --steps=preprocessing the ICA components can be check inside each of the ``**_report.html`` files.

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
    ### How to identify ICA artifacts

    We can identify eye blinks and heartbeats fairly quickly form a plot_components() plot as the one below. Here it is clear that ICA000 and ICA001 are blinks and heartbeats respectively.

    ![alt text](media/ica_plot.png)
    Ref: [MNE Documentation](https://mne.tools/stable/auto_tutorials/preprocessing/40_artifact_correction_ica.html)

    Additionally, one can attempt to remove muscle artifacts caught up by EEG (not MEG).
    See: [Removing muscle ICA components](https://mne.tools/stable/auto_examples/preprocessing/muscle_ica.html#ex-muscle-ica)

    ### But are there not any automatic ICA artifact labelling options?

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Try It Yourself with BIDS data
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
