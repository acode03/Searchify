import csv
import re
import json
#--------------------------------------------------------------------------------

"""
    TEST BLAH BLAH aaaa:

    ----------------------------------------
        [Function Description]
    ----------------------------------------
    Args:
        [parameter name] ([parameter type]): [parameter description]
    ----------------------------------------
    Returns:
        [returned value name if applicable] ([value type]): [returned value description]
    ----------------------------------------
"""

#--------------------------------------------------------------------------------

def load_data(dataset_name):
    """
    ----------------------------------------
        Loads data from a csv file and copies it onto 2d array
    ----------------------------------------
    Args:
        dataset_name: file name of the dataset to be loaded
    ----------------------------------------
    Returns:
        data ([]): 2d array containing the data from the csv file
    ----------------------------------------
    """

    data = []

    if dataset_name != "mini.csv" and dataset_name != "high_popularity.csv" and dataset_name != "low_popularity.csv":
        return "Not a valid dataset"
    with open('Data/'+dataset_name, mode = 'r', encoding='utf8') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            data.append(row)

    for row in data[1:]:
        for i in range(len(row)):
            try:
                row[i] = float(row[i])  # Try converting to float
            except ValueError:
                pass
    
    return data

#--------------------------------------------------------------------------------

def max_or_min(variable, num, max_or_min, data):
    """
    ----------------------------------------
        Returns a list a of length NUM containing songs sorted by VARIABLE taken from DATA.csv
    ----------------------------------------
    Args:
        variable (str): the variable to sort by (eg "tempo", "energy")
        num (int): the number of songs of the chosen variable to return
        max_or_min (str): either "max" or "min" to sort by either the highest or lowest value of the variable
        data ([]): a 2d array containing the data from the csv file 
    ----------------------------------------
    Returns:
        results ([]): a list of length NUM containing songs sorted by VARIABLE
    ----------------------------------------
    """

    dataset_list = ["mini.csv", "high_popularity.csv", "low_popularity.csv"]

    if type(data) is not list:
        return "Invalid dataset inputted."
    #checks if the number enterered is an int and not greater than the length of the dataset
    if type(num) != int or num > len(data)-1 or num <= 0:
        return "invalid number"

    #finds the index of the inputed variable name
    index = "none"
    for i in range(len(data[0])):
        if data[0][i] == variable:
            index = i       

    # makes sure that the variable name they entered actually exists
    if index == "none":
        return "Error: statistic not found"        

    results = []

    #sorts by the input variable excluding the first row of titles
    #also ensures only max or min are entered
    if max_or_min == "min":
        sorted_data = sorted(data[1:], key=lambda x: x[index])
    elif max_or_min == "max":
        sorted_data = sorted(data[1:], key=lambda x: x[index], reverse = True)
    else:
        return "receives only 'max' or 'min'"
    
    #gets only the first num rows
    selectedRows = sorted_data[:num]

    for i in range(len(selectedRows)):
        # 17 = artist name, 7 = song name
        results.append(str(selectedRows[i][17])+" - "+str(selectedRows[i][7])+": "+str(selectedRows[i][index]))

    return results

#--------------------------------------------------------------------------------

def map_simplified_data_name_to_file(dataset_name):
    """
    ----------------------------------------
        Maps simple user input to the actual file name of the dataset
    ----------------------------------------
    Args:
        dataset_name (str): the simplified name of the dataset
    ----------------------------------------
    Returns:
        dataset (str): the full file name of the corresponding dataset
    ----------------------------------------
    """
    dataset_map = {
        "high": "high_popularity.csv",
        "low": "low_popularity.csv",
        "mini": "mini.csv"
    }

    # if dataset_name not in dataset_map:
    #     #raise ValueError(f"Invalid dataset name: {dataset_name}. Please select 'high', 'low', or 'mini'.")
    #     return "Invalid dataset selection. Please select 'high', 'low', or 'mini'."
    
    return dataset_map.get(dataset_name)    

#--------------------------------------------------------------------------------

def formatted_2d_list(lst):
    """
    --------------------------------------
        Formats a 2D list into a multi-line string for Flask display.
    ----------------------------------------
    Args:
        lst (2d list): The 2D list to format
    ----------------------------------------
    Returns:
        (str): The formatted string
    ----------------------------------------"""
    if not lst:
        return "Empty matrix"
    
    # Determine column width based on the longest element in each column
    col_widths = [max(len(str(item)) for item in col) for col in zip(*lst)]

    # Build the formatted table string
    lines = [" | ".join(f"{str(item):>{width}}" for item, width in zip(row, col_widths)) for row in lst]
    
    # Join lines with newline characters for multi-line formatting
    return "\n".join(lines)

#--------------------------------------------------------------------------------

def formatted_1d_numbered_list(lst):
    """
    ----------------------------------------
        Formats a 1D list into a multi-line string for Flask display.
    ----------------------------------------
    Args:
        lst (1d list): The 1d list to format
    ----------------------------------------
    Returns:
        (str): The formatted string
    ----------------------------------------
    """
    # Join the list elements with a newline character to display each item on a new line
    formatted_string = "\n".join(f" {str(item)}" for i, item in enumerate(lst))
    # removed {i+1}.
    
    return formatted_string
#--------------------------------------------------------------------------------


#Temporary testing code
# data = load_data("mini.csv")
# test = max_or_min("energy", 1, "max", data)





def byte_to_cleaned_string(byte_data):
    """
    Converts a byte object to a string, removes whitespace, keeps only letters,
    and strips the string 'pre' (case-insensitive).
    
    Args:
        byte_data (bytes): The byte object to convert.
        
    Returns:
        str: A cleaned string containing only letters (no whitespace or special characters),
             and without 'pre'.
    """
    # Decode the byte object to a string (assuming UTF-8 encoding)
    decoded_str = byte_data.decode('utf-8')

    # Remove whitespace
    no_whitespace_str = decoded_str.replace(" ", "").replace("\n", "").replace("\t", "")

    # Remove all characters except letters (using regex)
    cleaned_str = re.sub(r'[^a-zA-Z]', '', no_whitespace_str)

    # Remove 'pre' (case-insensitive)
    cleaned_str = re.sub(r'(?i)pre', '', cleaned_str)

    return cleaned_str


def clean_string(input_str):
    """
    Removes all whitespace and non-letter characters from the input string.
    
    Args:
        input_str (str): The string to clean.
        
    Returns:
        str: A cleaned string containing only letters (no whitespace or special characters).
    """
    # Remove all whitespace
    no_whitespace_str = input_str.replace(" ", "").replace("\n", "").replace("\t", "")

    # Remove all characters except letters (using regex)
    cleaned_str = re.sub(r'[^a-zA-Z]', '', no_whitespace_str)

    return cleaned_str






def flatten_2d_list(lst):
    """
    Flattens a 2D list into a 1D list.

    Args:
        lst (list): A 2D list (list of lists).

    Returns:
        list: A flattened 1D list.
    """
    return [item for sublist in lst for item in sublist]

def flatten_byte_list(byte_data):
    """
    Decodes a byte object, parses it as a 2D list, and flattens it into a 1D list.

    Args:
        byte_data (bytes): The byte object representing a 2D list.

    Returns:
        list: A flattened 1D list.
    """
    # Decode bytes to a string
    decoded_str = byte_data.decode('utf-8')

    # Convert the string to a Python list (assuming it's in JSON format)
    try:
        nested_list = json.loads(decoded_str)
    except json.JSONDecodeError:
        raise ValueError("Invalid byte format: Expected a JSON list.")

    # Flatten the 2D list
    return [item for sublist in nested_list for item in sublist]