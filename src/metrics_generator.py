
import json
from src.constants import feature_matrix_file_path as f_matrix


if __name__ == '__main__':

    with open(f_matrix) as general_file:
        f_matrix = json.load(general_file)

    print()

    # f_matrix['ms_runs'].append({
    #     'date': ms_run_ids['date'],
    #     'original_filename': ms_run_ids['original_filename'],
    #     'chemical_mix_id': chemical_mix_id,
    #     'msfe_version': msfe_version,
    #     'scans_processed': scans_processed,
    #     'features_values': extracted_features,
    #     'features_names': features_names
    # })


