import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Debugging Pipeline Derivative
    """)
    return


@app.cell
def _():
    import mne

    return (mne,)


@app.cell
def _(mne):
    file = "/Users/peli/Projects/Repositories/mne_bids_demo/data/effort_bids/derivatives/mne-bids-pipeline/sub-01/ses-01/meg/sub-01_ses-01_task-effort_proc-filt_raw.fif"

    raw = mne.io.read_raw_fif(file, preload=True)
    print(raw.info)
    return


@app.cell
def _(epochs, picks):

    print(f"Epochs shape: {epochs.get_data().shape}")
    print(f"Picks: {picks}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
