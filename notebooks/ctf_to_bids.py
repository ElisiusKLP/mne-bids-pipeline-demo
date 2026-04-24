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
    # imports
    import mne
    from pathlib import Path
    from fontTools.misc.symfont import n
    from mne_bids import BIDSPath, write_raw_bids
    import numpy as np

    return BIDSPath, Path, mne, np, write_raw_bids


@app.cell
def _(Path):
    # path to one raw file
    root = Path.cwd().parent
    print(root)
    rel_path = "foreign_data/effort/0001_effortlearning_20250805_01.ds"
    fpath = root / Path(rel_path)
    return (root,)


@app.cell
def _(raw):
    raw.info
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we need to create a function that can extract the files at from the CTF data structure.

    First we know that the mne read_raw_ctf takes a filepath such as the .meg, but it actually loads in the parent directory and combines all the files from that parent directory into a single combined data structure, with eeg, meg etc.

    So we just need for each subject-session pair to load in the .meg4 file, use the BIDSPath structure to create a BIDS compliant data path that can go into the mne_bids function write_raw_bids.

    To do this we utilise the filepattern `pattern = f"{i:04d}_effortlearning_*_{j:02d}.ds"` and loop over subjects and sessions (in this case we choose 2 subjects and there are 4 sessions for all).

    Because the CTF data is weird we need to rename the relevant events to use manually before writing to BIDS otherwise we will not load all events.

    We choose to still store all events with their basic numerical event_id but override the ones that are relevant to our experimental conditions as defined in `event_dict`.
    """)
    return


@app.cell
def _(BIDSPath, mne, np, root, write_raw_bids):


    def create_bids_directory(
        n_subjects, n_sessions, 
        input_dir_path, bids_dir_path,
        event_dict):
        for i in range(n_subjects):
            i += 1  # subject numbering starts at 1
            for j in range(n_sessions):
                j += 1  # session numbering starts at 1
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
                if raw_ctf.annotations is not None:
                    # Filter out 'Tr1' annotations, keep only our true events
                    annot = raw_ctf.annotations
                    mask = annot.description != 'Tr1'
                    raw_ctf.set_annotations(annot[mask])

                # extract events for renaming
                events = mne.find_events(raw_ctf, shortest_event=1)

                # create new event dict with items from event dict, and where all other events are labeled as there event id (e.g., 30039 -> "30039")
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
    bids_dir_path = root / "data/effort_bids"
    input_dir_path = root / "foreign_data/effort"

    create_bids_directory(n_subjects, n_sessions, input_dir_path, bids_dir_path, event_dict)

    return


if __name__ == "__main__":
    app.run()
