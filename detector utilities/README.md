# detector utilities
## list_files
list the paths of original images (need to change the directory)

## resize
resize original images (need to change the scale of multiplication, and the resample option in resize method)

## list_files_after_edit
list the paths of editted images (need to change the directory)

## add_column (run after run_detect.bat finishes)
python add_column.py quick_test_ultraface.csv quick_test_ultraface_2.csv

## compute_csv_file (run after run.bat finishes)
python compute_csv_file.csv quick_test_ultraface_2.csv ./templates quick_test_deep_features.csv