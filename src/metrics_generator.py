
import json
from src.constants import feature_matrix_file_path as f_matrix
from src.constants import version
from src.constants import resolution_200_features_names, resolution_700_features_names
from src.constants import accuracy_features_names


def add_resolution_metrics(qc_values, qc_names, ms_run):
    """ This method calculates resolutions metric for two ions (at around 200 m/z and 700 m/z).
        It's m/z divided by width of the peak at 50% height."""

    mz200, width200 = resolution_200_features_names

    resolution200 = ms_run['features_values'][ms_run['features_names'].index(mz200)] / ms_run['features_values'][
        ms_run['features_names'].index(width200)]

    mz700, width700 = resolution_700_features_names
    resolution700 = ms_run['features_values'][ms_run['features_names'].index(mz700)] / ms_run['features_values'][
        ms_run['features_names'].index(width700)]

    qc_values.extend([resolution200, resolution700])
    qc_names.extend(['resolution200', 'resolution700'])


def add_accuracy_metrics(qc_values, qc_names, ms_run):
    """ This method calculates accuracy metrics for QC run.
        It's average of the absolute m/z diff values for all the expected ions. """

    diff_sum = 0.

    for feature in accuracy_features_names:
        diff_sum += ms_run['features_values'][ms_run['features_names'].index(feature)]

    average_accuracy = diff_sum / len(accuracy_features_names)

    qc_values.append(average_accuracy)
    qc_names.append('average_accuracy')


def add_dirt_metrics(qc_values, qc_names, ms_run):
    """  """


    pass


if __name__ == '__main__':

    with open(f_matrix) as general_file:
        f_matrix = json.load(general_file)

    q_matrix = {'qc_runs': []}

    for run in f_matrix['ms_runs']:

        qc_values = []
        qc_names = []

        add_resolution_metrics(qc_values, qc_names, run)
        add_accuracy_metrics(qc_values, qc_names, run)





        q_matrix['qc_runs'].append({
            'date': run['date'],
            'original_filename': run['original_filename'],
            'chemical_mix_id': run['chemical_mix_id'],
            'msfe_version': run['msfe_version'],
            'scans_processed': run['scans_processed'],
            'qcm_version': version,
            'qc_values': qc_values,
            'qc_names': qc_names
        })



