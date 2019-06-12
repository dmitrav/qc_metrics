
version = '0.0.4'

feature_matrix_file_path = '/Users/andreidm/ETH/projects/ms_feature_extractor/res/test1/feature_matrix.json'

# features names
resolution_200_features_names = ['absolute_mass_accuracy_Caffeine_i1_mean', 'widths_Caffeine_i1_1_mean']  # 193.0725512871
resolution_700_features_names = ['absolute_mass_accuracy_Perfluorotetradecanoic_acid_i1_mean', 'widths_Perfluorotetradecanoic_acid_i1_1_mean']  # 712.94671694


accuracy_features_names = ['absolute_mass_accuracy_Caffeine_i1_mean', 'absolute_mass_accuracy_Caffeine_i2_mean', 'absolute_mass_accuracy_Caffeine_i3_mean', 'absolute_mass_accuracy_Caffeine_f1_mean',
                           'absolute_mass_accuracy_Fluconazole_i1_mean', 'absolute_mass_accuracy_Fluconazole_i2_mean', 'absolute_mass_accuracy_Fluconazole_i3_mean', 'absolute_mass_accuracy_Fluconazole_f1_mean',
                           'absolute_mass_accuracy_3-(Heptadecafluorooctyl)aniline_i1_mean', 'absolute_mass_accuracy_3-(Heptadecafluorooctyl)aniline_i2_mean', 'absolute_mass_accuracy_3-(Heptadecafluorooctyl)aniline_i3',
                           'absolute_mass_accuracy_Albendazole_i1_mean', 'absolute_mass_accuracy_Albendazole_i2_mean', 'absolute_mass_accuracy_Albendazole_i3_mean', 'absolute_mass_accuracy_Albendazole_f1_mean', 'absolute_mass_accuracy_Albendazole_f2_mean',
                           'absolute_mass_accuracy_Triamcinolone_acetonide_i1_mean', 'absolute_mass_accuracy_Triamcinolone_acetonide_i2_mean', 'absolute_mass_accuracy_Triamcinolone_acetonide_i3_mean', 'absolute_mass_accuracy_Triamcinolone acetonide_f1_mean', 'absolute_mass_accuracy_Triamcinolone acetonide_f2_mean',
                           'absolute_mass_accuracy_Perfluorodecanoic_acid_i1_mean', 'absolute_mass_accuracy_Perfluorodecanoic_acid_i2_mean', 'absolute_mass_accuracy_Perfluorodecanoic_acid_i3_mean', 'absolute_mass_accuracy_Perfluorodecanoic acid_f1_mean',
                           'absolute_mass_accuracy_Tricosafluorododecanoic_acid_i1_mean', 'absolute_mass_accuracy_Tricosafluorododecanoic_acid_i2_mean', 'absolute_mass_accuracy_Tricosafluorododecanoic_acid_i3_mean', 'absolute_mass_accuracy_Tricosafluorododecanoic acid_f1_mean',
                           'absolute_mass_accuracy_Perfluorotetradecanoic_acid_i1_mean', 'absolute_mass_accuracy_Perfluorotetradecanoic_acid_i2_mean', 'absolute_mass_accuracy_Perfluorotetradecanoic_acid_i3_mean', 'absolute_mass_accuracy_Perfluorotetradecanoic acid_f1_mean', 'absolute_mass_accuracy_Perfluorotetradecanoic acid_f2_mean',
                           'absolute_mass_accuracy_Pentadecafluoroheptyl_i1_mean', 'absolute_mass_accuracy_Pentadecafluoroheptyl_i2_mean', 'absolute_mass_accuracy_Pentadecafluoroheptyl_i3_mean']

dirt_features_names = ['intensity_sum_chem_50_150', 'intensity_sum_chem_150_250', 'intensity_sum_chem_250_350', 'intensity_sum_chem_350_450', 'intensity_sum_chem_450_550',
                       'intensity_sum_chem_550_650','intensity_sum_chem_650_750', 'intensity_sum_chem_750_850', 'intensity_sum_chem_850_950', 'intensity_sum_chem_950_1050']


instrument_noise_tic_features_names = ['intensity_sum_bg_50_250', 'intensity_sum_bg_250_450', 'intensity_sum_bg_450_650', 'intensity_sum_bg_650_850', 'intensity_sum_bg_850_1050']

instrument_noise_percentiles_features_names = ['percentiles_bg_50_250_1', 'percentiles_bg_250_450_1', 'percentiles_bg_450_650_1', 'percentiles_bg_650_850_1', 'percentiles_bg_850_1050_1']

isotopic_presence_features_names = ['intensity_ratios_diffs_Caffeine_i1_0_mean', 'intensity_ratios_diffs_Caffeine_i1_1_mean', 'intensity_ratios_diffs_Caffeine_i1_2_mean',
                                    'intensity_ratios_diffs_Fluconazole_i1_0_mean', 'intensity_ratios_diffs_Fluconazole_i1_1_mean', 'intensity_ratios_diffs_Fluconazole_i1_2_mean',
                                    'intensity_ratios_diffs_3-(Heptadecafluorooctyl)aniline_i1_0_mean', 'intensity_ratios_diffs_3-(Heptadecafluorooctyl)aniline_i1_1_mean', 'intensity_ratios_diffs_3-(Heptadecafluorooctyl)aniline_i1_2_mean',
                                    'intensity_ratios_diffs_Albendazole_i1_0_mean', 'intensity_ratios_diffs_Albendazole_i1_1_mean', 'intensity_ratios_diffs_Albendazole_i1_2_mean',
                                    'intensity_ratios_diffs_Triamcinolone_acetonide_i1_0_mean', 'intensity_ratios_diffs_Triamcinolone_acetonide_i1_1_mean', 'intensity_ratios_diffs_Triamcinolone_acetonide_i1_2_mean',
                                    'intensity_ratios_diffs_Perfluorodecanoic_acid_i1_0_mean', 'intensity_ratios_diffs_Perfluorodecanoic_acid_i1_1_mean', 'intensity_ratios_diffs_Perfluorodecanoic_acid_i1_2_mean',
                                    'intensity_ratios_diffs_Tricosafluorododecanoic_acid_i1_0_mean', 'intensity_ratios_diffs_Tricosafluorododecanoic_acid_i1_1_mean', 'intensity_ratios_diffs_Tricosafluorododecanoic_acid_i1_2_mean',
                                    'intensity_ratios_diffs_Perfluorotetradecanoic_acid_i1_0_mean', 'intensity_ratios_diffs_Perfluorotetradecanoic_acid_i1_1_mean', 'intensity_ratios_diffs_Perfluorotetradecanoic_acid_i1_2_mean',
                                    'intensity_ratios_diffs_Pentadecafluoroheptyl_i1_0_mean', 'intensity_ratios_diffs_Pentadecafluoroheptyl_i1_1_mean', 'intensity_ratios_diffs_Pentadecafluoroheptyl_i1_2_mean']

transmission_features_names = ['intensity_Perfluorotetradecanoic_acid_i1_mean', 'intensity_Fluconazole_i1_mean']

fragmentation_features_names = ['fragments_ratios_Fluconazole_i1_0_mean',
                                'fragments_ratios_Perfluorotetradecanoic_acid_i1_0_mean']

baseline_150_250_features_names = ['percentiles_chem_150_250_0', 'percentiles_chem_150_250_1']
baseline_650_750_features_names = ['percentiles_chem_650_750_0', 'percentiles_chem_650_750_1']

signal_features_names = [feature_name.replace('absolute_mass_accuracy', 'intensity') for feature_name in accuracy_features_names]


s2b_features_names = ['intensity_3-(Heptadecafluorooctyl)aniline_i1_mean', 'percentiles_norm_500_550_0']

s2n_features_names = ['intensity_3-(Heptadecafluorooctyl)aniline_i1_mean', 'percentiles_norm_500_550_0', 'percentiles_norm_500_550_1']
