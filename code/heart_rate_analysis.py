import os # for processing all signals from a directory
import numpy as np # contiguous C arrays
import wfdb.processing

# function for averaging all heart rates for a specified signal

def compute_heart_rate(heart_rates):
    avg_heart_rate = 0
    no_of_relevant_heart_rates = 0
    for i in heart_rates:
        if not np.isnan(i):
            avg_heart_rate += i
            no_of_relevant_heart_rates += 1
    return avg_heart_rate / no_of_relevant_heart_rates

if __name__ == '__main__':

    # Get current working directory
    current_working_directory = os.getcwd()

    # The download directory for the arrhythmia database
    directory_database1 = os.path.join(current_working_directory, 'mitdb')

    # The download directory for the hypertension database
    directory_database2 = os.path.join(current_working_directory, 'shareedb')

    # Initialize heart rate values

    overall_heart_rate_arrhythmia = 0
    average_heart_rate_arrhythmia = 0.0
    no_of_signals_arrhythmia = 0

    overall_heart_rate_hypertension = 0
    average_heart_rate_hypertension = 0.0
    no_of_signals_hypertension = 0

    # Iterate through all signals in the arrhythmia database

    for filename in os.listdir(directory_database1):
        if filename.endswith(".dat"):

            record = wfdb.rdrecord('mitdb/' + os.path.splitext(filename)[0], sampfrom=100000, sampto=104000)
            annotation = wfdb.rdann('mitdb/' + os.path.splitext(filename)[0], 'atr', sampfrom=100000, sampto=104000)

            # Detect QRS complex

            qrs_locations = wfdb.processing.gqrs_detect(record.p_signal[:, 0], fs=record.fs)

            # Compute all heart rates for the signal

            heart_rates = wfdb.processing.compute_hr(sig_len=record.sig_len, qrs_inds=qrs_locations, fs=record.fs)

            overall_heart_rate_arrhythmia += compute_heart_rate(heart_rates)
            no_of_signals_arrhythmia += 1

    # Iterate through all signals in the arrhythmia database

    for filename in os.listdir(directory_database2):
        if filename.endswith(".dat"):

            record = wfdb.rdrecord('shareedb/' + os.path.splitext(filename)[0], sampfrom=100000, sampto=104000)
            annotation = wfdb.rdann('shareedb/' + os.path.splitext(filename)[0], 'qrs', sampfrom=100000, sampto=104000)

            # Detect QRS complex

            qrs_locations = wfdb.processing.gqrs_detect(record.p_signal[:, 0], fs=record.fs)

            # Compute all heart rates for the signal

            heart_rates = wfdb.processing.compute_hr(sig_len=record.sig_len, qrs_inds=qrs_locations, fs=record.fs)

            overall_heart_rate_hypertension += compute_heart_rate(heart_rates)
            no_of_signals_hypertension += 1

    # Calculate average heart rates

    average_heart_rate_arrhythmia = overall_heart_rate_arrhythmia / no_of_signals_arrhythmia

    average_heart_rate_hypertension = overall_heart_rate_hypertension / no_of_signals_hypertension

    # Print results

    print('Overall average heart rate for all arrhythmia signals is: ' + str(average_heart_rate_arrhythmia) + ' bpm.')

    print('Overall average heart rate for all hypertension signals is: ' + str(average_heart_rate_hypertension) + ' bpm.')

    print('Overall average difference in heart rates in the databases is: ' + str(abs(average_heart_rate_arrhythmia - average_heart_rate_hypertension)) + ' bpm.')
