import matplotlib.pyplot as plt # for plotting graphs
import wfdb.processing # processing ECG signals

if __name__ == '__main__':

    # Load record and annotation for the sample arrhythmia signal

    record_arrhythmia = wfdb.rdrecord('mitdb/100', sampfrom=0, sampto=4000)
    annotation_arrhyhthmia = wfdb.rdann('mitdb/100', 'atr', sampfrom=0, sampto=4000)

    # Plot signal

    wfdb.plot_items(signal=record_arrhythmia.p_signal, ann_samp=[annotation_arrhyhthmia.sample], title='MIT-BIH Record 100',
                    time_units='samples', figsize=(10, 4))

    # Load record and annotation for the sample hypertension signal

    record_hypertension = wfdb.rdrecord('shareedb/01911', sampfrom=0, sampto=104000)
    annotation_hypertension = wfdb.rdann('shareedb/01911', 'qrs', sampfrom=0, sampto=104000)

    # Plot signal

    wfdb.plot_items(signal=record_hypertension.p_signal, ann_samp=[annotation_hypertension.sample],
                    title='SHARE-EDB Record 01911',
                    time_units='samples', figsize=(10, 4))

    # Read arrhythmia signal as a list of samples for plotting

    signal_arrhythmia, fields = wfdb.rdsamp('mitdb/100', channels=[0], sampfrom=100000, sampto=104000)

    # Read hypertension signal as a list of samples for plotting

    signal_hypertension, fields = wfdb.rdsamp('shareedb/01911', channels=[0], sampfrom=100000, sampto=104000)

    # Plot both signals on one plot

    plt.plot(range(4000), signal_arrhythmia, 'b')
    plt.plot(range(4000), signal_hypertension, 'g')

    plt.show()
