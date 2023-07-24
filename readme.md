# CSV Merger Script

This Python script merges two CSV files based on a common column. The files to merge and the common column are provided by the user when running the script. The merged data is then written to a new CSV file.

## Requirements

This script requires Python 3 and the pandas library. If you don't have pandas installed, you can install it using pip:

```bash
pip install pandas
```
## Usage

To use this script, follow the steps below:

1. **Run the script**

    Open your command line, navigate to the directory where the `csv_merger.py` file is located, and then enter the following command:
    ```bash
    python csv_merger.py
    ```

2. **Enter the name of the first CSV file**

    When prompted, type the name of the first CSV file. If this file is not in the same directory as the script, make sure to include the full path to the file.

3. **Enter the name of the second CSV file**

    You will then be prompted to enter the name of the second CSV file. Like with the first file, make sure to include the full path if it's not in the same directory as the script.

4. **Enter the name of the common column**

    Finally, enter the name of the column that the two CSV files share.

After you've entered all the necessary information, the script will merge the two CSV files based on the common column and write the merged data to a new CSV file named 'merged_file.csv' in the same directory as the script.

## Notes

- **Column order**: The order of the columns in the output file is based on the order they appear in the input files.

- **Error handling**: This script does not include comprehensive error handling. Therefore, ensure that the input files exist, are valid CSV files, and that the common column is present in both files. Any discrepancies may lead to runtime errors.

- **File paths**: When providing the file paths, make sure to use the correct format for your operating system. For example, on Windows, use backslashes (`\`) and on UNIX-based systems like Linux or Mac, use forward slashes (`/`).

- **Python and pandas**: This script requires both Python and pandas to be installed on your system. You can check if they're installed by typing `python --version` and `pip show pandas` into your command line.

