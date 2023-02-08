# imports for this function
import os, pandas as pd, numpy as np
# define the path to the data
file_path = "../data/data/raw/NorthwindTradersTables.xlsx"

def read_xlsx(file_path):
    """
    read_xlsx is a function that reads an XLSX file and returns dataframes where each sheet is a dataframe, each column of each df should be type-cast based on the values from the corresponding sheet in the second row, and the column names are in the first row. The function should save these dataframes in a folder called `extracted_dfs` with each sheet in its own folder named after the sheet's name in the file. Within these folders, the function should save the dataframe as a pickle file. The function should return a dictionary with the sheet names as keys and the dataframe information as values.

    The libraries used in this function are: `os`, `pandas`, `numpy`.

    :param file_path: _description_
    :type file_path: _type_
    :return: _description_
    :rtype: _type_
    """
    # Read in the file
    with pd.ExcelFile(file_path) as xlsx:
        # Get the sheet names
        sheet_names = xlsx.sheet_names

        # Create an empty dictionary to store the dataframes
        dfs = {}

        # Iterate through the sheets
        for sheet in sheet_names:
            # Get the dataframe from the sheet
            df = pd.read_excel(xlsx, sheet_name=sheet)

            # Get the second row of the dataframe
            second_row = df.iloc[1]

            # Get the first row of the dataframe
            first_row = df.iloc[0]

            # Get the column names from the first row
            df.columns = first_row

            # Drop the first two rows
            df = df.iloc[2:]

            # Iterate through the columns in the second row
            for col in second_row.index:
                # Get the type of the value in the second row
                col_type = type(second_row[col])

                # Cast the column to the type of the second row value
                df[col] = df[col].astype(col_type)

            # Create a folder for the sheet if it doesn't exist
            os.makedirs(f"../data/processed/extracted_dfs/{sheet}", exist_ok=True)

            # Save the dataframe as a pickle file in the sheet folder
            df.to_pickle(f"../data/processed/extracted_dfs/{sheet}/{sheet}.pkl")

            # Add the dataframe to the dictionary
            dfs[sheet] = df

    # Return the dictionary
    return dfs