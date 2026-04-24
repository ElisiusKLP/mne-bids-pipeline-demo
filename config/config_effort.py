# CONFIG
# Runtime Settings
n_jobs = 1
parallel_backend = "loky" # used by joblib 

# General Settings
bids_root = "data/effort_bids/"
sessions = "all"
task = "effort"
allow_missing_sessions = False
subjects = ["01","02"]
exclude_subjects = []

ch_types = ["meg"]
data_type = "meg"
eog_channels = None # only uses actual EOG channels
plot_psd_for_runs = "all"
random_state = 912

# Preprocessing
find_breaks = False # Can find breaks with no events in the data, mark them and ignore the periods in the following processing steps.
find_flat_channels_meg = True
find_noisy_channels_meg = True
# maxwell filtering (and head compensation)
use_maxwell_filter = False
mf_cal_missing = "warn"
mf_ctc_missing = "warn"
mf_mc = False

# Filtering
l_freq = 1
h_freq = 60
zapline_fline = 50.0 # removes 50 Hz line noise

# Resampling
raw_resample_sfreq = None

# Epochs
epochs_tmin = -0.2
epochs_tmax = 1
baseline = (None, 0)
conditions = ["force_start", "feedback_onset", "cue_onset"]

# Artifact removal
regress_artifact = None # Custom reference electrode channels for artifacts e.g. stord in ["MISC 001" (...)] 
spatial_filter = "ica"
# SSP can be used for faster and more automatic rejection but with higher risk of removing neural signal. 
process_raw_clean = True # If false only applies to epochs, which is faster than clean.
ica_reject = None # with no interpolation # set to None (did not work)
ica_algorithm = "picard-extended_infomax"
ica_l_freq = 1.0
ica_h_freq = 100
ica_n_components = 20
ica_use_ecg_detection = True
ica_ecg_threshold = 0.1
ica_use_eog_detection = True
ica_eog_threshold = 3.0
ica_use_icalabel = False # Set to False (only works with EEG) TODO: Setup with MEGNET for MEG

process_empty_room = False # We don't have empty room recordings for this dataset

# Sensor-level Analysis

# Source-level Analysis

