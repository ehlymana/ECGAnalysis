# ECGAnalysis

*ECG Analysis* is an app made in Python programming language. It uses the **wfdb** library which enables easy PhysioNet signal processing and analysis.

The two target databases for analysis are:

1. *MIT-BIH Arrhythmia Database* (database containing ECG signals of patients who suffer from arrhythmia);
2. *Smart Health for Assessing the Risk of Events via ECG (SHAREE) Database* (database containing ECG signals of patients who suffer from high blood pressure).

This repository contains the following files:

- **download_databases.py** - Automatically downloads all samples from the two above mentioned databases.

- **heart_rate_analysis.py** - Computes the overall average heart rates from all database samples and calculates the difference between the databases.

- **plot_signals.py** - Allows plotting of single signals from each database and then plotting both signals on the same plot.

- **xqrs_analysis.py** - Computes the overall average QRS widths from all database samples and calculates the difference between the database.

2019. © Krupalija Ehlimana

*University of Sarajevo*

*Faculty of Electrical Engineering Sarajevo*

*Department of Computing and Informatics*
