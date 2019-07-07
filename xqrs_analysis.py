import os # for processing all signals from a directory
import wfdb.processing # processing ECG signals
import wfdb # for physionet tools

if __name__ == '__main__':

    # Get current working directory
    current_working_directory = os.getcwd()

    # The download directory for the arrhythmia database
    directory_database1 = os.path.join(current_working_directory, 'mitdb')

    # The download directory for the hypertension database
    directory_database2 = os.path.join(current_working_directory, 'shareedb')

    # Initialize qrs width values

    overall_qrs_width_arrhythmia = 0
    average_qrs_width_arrhythmia = 0.0
    no_of_signals_arrhythmia = 0

    overall_qrs_width_hypertension = 0
    average_qrs_width_hypertension = 0.0
    no_of_signals_hypertension = 0

    # Iterate through all signals in the arrhythmia database

    for filename in os.listdir(directory_database1):
        if filename.endswith(".dat"):

            signal, fields = wfdb.rdsamp('mitdb/' + os.path.splitext(filename)[0], channels=[0], sampfrom=100000, sampto=104000)
            ann_ref = wfdb.rdann('mitdb/' + os.path.splitext(filename)[0], 'atr')
            xqrs = wfdb.processing.XQRS(sig=signal[:, 0], fs=fields['fs'])
            xqrs.detect()

            overall_qrs_width_arrhythmia += xqrs.qrs_width
            no_of_signals_arrhythmia += 1

    # Iterate through all signals in the arrhythmia database

    for filename in os.listdir(directory_database2):
        if filename.endswith(".dat"):

            signal, fields = wfdb.rdsamp('shareedb/' + os.path.splitext(filename)[0], channels=[0], sampfrom=100000, sampto=104000)
            ann_ref = wfdb.rdann('shareedb/' + os.path.splitext(filename)[0], 'qrs')
            xqrs = wfdb.processing.XQRS(sig=signal[:, 0], fs=fields['fs'])
            xqrs.detect()

            overall_qrs_width_hypertension += xqrs.qrs_width
            no_of_signals_hypertension += 1

    # Calculate average qrs widths

    average_qrs_width_arrhythmia = overall_qrs_width_arrhythmia / no_of_signals_arrhythmia

    average_qrs_width_hypertension = overall_qrs_width_hypertension / no_of_signals_hypertension

    # Print results

    print('Overall average qrs width for all arrhythmia signals is: ' + str(average_qrs_width_arrhythmia) + ' bpm.')

    print('Overall average qrs width for all hypertension signals is: ' + str(average_qrs_width_hypertension) + ' bpm.')

    print('Overall average difference in qrs widths in the databases is: ' + str(abs(average_qrs_width_arrhythmia - average_qrs_width_hypertension)) + ' bpm.')
