
import json
from src.constants import feature_matrix_file_path as f_matrix
from src.constants import version
from src.constants import resolution_200_features_names, resolution_700_features_names
from src.constants import accuracy_features_names, dirt_features_names, isotopic_presence_features_names
from src.constants import instrument_noise_tic_features_names as noise_features_names
from src.constants import transmission_features_names, fragmentation_features_names


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
    """ This method calculates metric of the dirtiness.
        It sums up absolute intensities of the chemical noise scan. All the expected peaks there are excluded. """

    chem_noise_signal_sum = 0.

    for feature in dirt_features_names:
        chem_noise_signal_sum += ms_run['features_values'][ms_run['features_names'].index(feature)]

    qc_values.append(chem_noise_signal_sum)
    qc_names.append('chemical_dirt')


def add_noise_metrics(qc_values, qc_names, ms_run):
    """ This method calculates metric of the instrument noise.
        It sums up absolute intensities of the instrument noise scan."""

    instrument_noise_signal_sum = 0.

    for feature in noise_features_names:
        instrument_noise_signal_sum += ms_run['features_values'][ms_run['features_names'].index(feature)]

    qc_values.append(instrument_noise_signal_sum)
    qc_names.append('instrument_noise')


def add_isotopic_abundance_metrics(qc_values, qc_names, ms_run):
    """ This method calculates metrics of the isotopic presence.
        It finds the average of isotopic intensities ratios diffs (absolute percent diffs for all the isotopes). """

    ratios_diffs_sum = 0.

    for feature in isotopic_presence_features_names:
        ratios_diffs_sum += abs(ms_run['features_values'][ms_run['features_names'].index(feature)])

    ratios_diffs_mean = ratios_diffs_sum / len(isotopic_presence_features_names)

    qc_values.append(ratios_diffs_mean)
    qc_names.append('isotopic_presence')


def add_transmission_metrics(qc_values, qc_names, ms_run):
    """ This method calculates the metric of transmission.
        It finds the ratio of the intensities of two ions: the light one (~ mz305) and the heavy one (~ mz712). """

    intensity712, intensity305 = transmission_features_names

    transmission = ms_run['features_values'][ms_run['features_names'].index(intensity712)] / ms_run['features_values'][
        ms_run['features_names'].index(intensity305)]

    qc_values.append(transmission)
    qc_names.append('transmission')


def add_fragmentation_metrics(qc_values, qc_names, ms_run):
    """ This method saves the metrics of fragmentation (nothing is calculated, just directly passed).
        Fragmentation intensity ratios of two ions are taken: mz305(to mz191) & mz712 (to mz668). """

    ratio305, ratio712 = fragmentation_features_names

    fragmentation305 = ms_run['features_values'][ms_run['features_names'].index(ratio305)]
    fragmentation712 = ms_run['features_values'][ms_run['features_names'].index(ratio712)]

    qc_values.append([fragmentation305, fragmentation712])
    qc_names.append(['fragmentation305', 'fragmentation712'])


if __name__ == '__main__':

    with open(f_matrix) as general_file:
        f_matrix = json.load(general_file)

    q_matrix = {'qc_runs': []}

    for run in f_matrix['ms_runs']:

        qc_values = []
        qc_names = []

        add_resolution_metrics(qc_values, qc_names, run)
        add_accuracy_metrics(qc_values, qc_names, run)
        add_dirt_metrics(qc_values, qc_names, run)
        add_noise_metrics(qc_values, qc_names, run)
        add_isotopic_abundance_metrics(qc_values, qc_names, run)
        add_transmission_metrics(qc_values, qc_names, run)
        add_fragmentation_metrics(qc_values, qc_names, run)


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



