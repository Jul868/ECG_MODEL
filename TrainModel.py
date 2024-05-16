import biosppy
import numpy as np

# Pad signal


# Assume `ecg_signal` is your loaded ECG data array and `sampling_rate` is the rate at which the data was sampled.
ecg_signal = [0.1, -0.1, 0.2, -0.2, 0.3, -0.3, 0.4, -0.4]  # Example ECG data
sampling_rate = 1000  # Example sampling rate in Hz

pad_length = 4503  # Length required by the filter
if len(ecg_signal) < pad_length:
    pad_size = pad_length - len(ecg_signal)
    ecg_signal_padded = np.pad(ecg_signal, (pad_size, pad_size), 'constant', constant_values=(0, 0))

# Now filter the padded signal


# Processing the ECG signal to find R-peaks
signals, info = biosppy.signals.ecg.ecg(signal=ecg_signal, sampling_rate=sampling_rate, show=True)

# `signals` contains the filtered ECG signal
# `info` is a dictionary containing various outputs from the ECG processing, including the R-peaks
r_peaks = info['rpeaks']  # array of indices where R-peaks are located in the ECG signal

print("Detected R-peak indices:", r_peaks)
