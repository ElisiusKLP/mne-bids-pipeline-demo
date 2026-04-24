import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
def _():
    import mne
    from pathlib import Path

    # path to one raw file
    root = Path.cwd().parent
    print(root)
    fpath = root / Path("foreign_data/effort/0001_effortlearning_20250805_01.ds/0001_effortlearning_20250805_01.meg4")

    # load raw file
    raw = mne.io.read_raw_fif(fpath, preload=True)
    return mne, raw, root


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tasks**

    - High Arousal Low Valence (HALV)
    - High Arousal High Valence (HAHV)
    - Low Arousal Low Valence (LALV)
    - Low Arousal High Valence (LAHV)
    """)
    return


@app.cell
def _(mne, raw):
    # find all events in the raw file


    events = mne.find_events(raw, shortest_event=1)
    # find their names / ids
    event_id = mne.events_from_annotations(raw)[1]
    # what does the stimuli refer to?
    print(event_id)
    return (events,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I don't really get anything from the MNE file metadata, i will try instead with the BIDS metadata.
    """)
    return


@app.cell
def _(root):
    from mne_bids import read_raw_bids, BIDSPath

    bids_root = root / "data/ds007640"
    bids_path = BIDSPath(subject="01", session="01", task="HAHV", datatype="meg", root=bids_root)
    raw_bids = read_raw_bids(bids_path)
    print(raw_bids.info)

    # inspect the events
    return


@app.cell
def _(events, mne, raw):
    """
    TRIGGER_MAPPING = {
        "19" : ["cue_onset", -1.0, 1.0],
        "4" : ["force_start", -0.5, 5.0],
        "8" : ["feedback_onset", -1.0, 1.5]
    }
    """

    event_dict = {
        "cue_onset": 19,
        "force_start": 4,
        "feedback_onset": 8
    }

    # plot the events
    fig = mne.viz.plot_events(
        events, sfreq=raw.info["sfreq"], first_samp=raw.first_samp, event_id=event_dict
    )
    return


@app.cell
def _(events, mne, raw):

    # Plot the events
    mne.viz.plot_events(events, sfreq=raw.info['sfreq'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I am pretty sure the presentation of the video lie as split into four in sequences across the ids 33-36 in the levels as described in the  survey_data description.

        "Levels": {
          "1": "01, 11, 21, 31",
          "10": "10, 20, 30, 40",
          "2": "02, 12, 22, 32",
          "3": "03, 13, 23, 33",
          "4": "04, 14, 24, 34",
          "5": "05, 15, 25, 35",
          "6": "06, 16, 26, 36",
          "7": "07, 17, 27, 37",
          "8": "08, 18, 28, 38",
          "9": "09, 19, 29, 39"
        }

    But still these could not all be High arousal high valence as this is the only task I have loaded in now.
    """)
    return


@app.cell
def _(mne, raw):
    # inspect the chpi coil data
    mne.chpi.get_chpi_info(raw.info)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    HCI coils lives in the CTF system data as HLC (Head Localization Coordinates)
    https://www.fieldtriptoolbox.org/example/sensor/headmovement_meg/.
    """)
    return


@app.cell
def _(raw):
    print(f"CTF compensation: {raw.info.get('ctf_head_t')}")
    print(f"Compensation grade: {raw.info.get('comp_grade')}")
    print(f"2. Compensation history: {raw.info.get('compensation_history')}")
    return


@app.cell
def _(raw):
    # lets get all the channels in the raw file
    print(raw.info["ch_names"])
    # lets see if there are any channels starting with "HLC"
    hlc_channels = [ch for ch in raw.info["ch_names"] if ch.startswith("HLC")]
    print(f"Are there any HLC channels? {any(hlc_channels)}")
    print(f"There are {len(hlc_channels)} HLC channels")
    print(hlc_channels)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
