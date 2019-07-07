import wfdb # for physionet tools
import os # for downloading samples from databases
from IPython.display import display # for displaying physionet libraries

if __name__ == '__main__':

    # Make download directories in your current working directory
    current_working_directory = os.getcwd()

    # the download directory for the arrhythmia database
    directory_database1 = os.path.join(current_working_directory, 'mitdb')

    # the download directory for the hypertension database
    directory_database2 = os.path.join(current_working_directory, 'shareedb')

    # Download all the WFDB content
    #wfdb.dl_database('mitdb', dl_dir=directory_database1)
    wfdb.dl_database('shareedb', dl_dir=directory_database2)

    # Display the downloaded content in the folders
    display(os.listdir(directory_database1))
    display(os.listdir(directory_database2))

