import argparse
import ProductionCode.helperFunctions as hf
from ProductionCode.dataSource import DataSource

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise argparse.ArgumentError(None, message)

def parser_intializer():
    '''
    Creates a parser, adds arguments to it for use as parameters in max_or_min function, then returns the parser.
    This is separated from the main function for organization purposes.
    '''
    # Create the parser
    parser = CustomArgumentParser(description="Process some variables from the dataset.")

    # Add the arguments here
   # parser.add_argument("--data", type=str, required=True, help="Dataset selection: 'high', 'low', 'mini'")
    parser.add_argument("--var", type=str, required=True, help="Type the variable that you want to access. Eg. tempo, energy")
    parser.add_argument("--sort", type=str, required=True, help="'max' to sort high to low, 'min' to sort low to high")
    parser.add_argument("--n", type=int, required=True, help="Number of top values to be displayed")

    return parser

def main():
    data_source = DataSource()

    '''
    Creates a parser, parses the arguments, then prints results of max_or_min function according to command line input.
    Raises errors if invalid input is given.

    --------------------------------------------------------------------------------------------
    USAGE: python3 command_line.py --data <dataset> --var <variable> --sort <sort method> --n <# of tracks to display>

    POSSIBLE SELECTIONS:
        | dataset: 'high', 'low', 'mini'
        | variable: 'tempo', 'energy', 'danceability', 'valence', 'loudness', 
        'acousticness', 'liveness', 'speechiness', 'instrumentalness', 
        'key', 'mode', 'time_signature', 'duration_ms', 'popularity'
        | sort method: 'max', 'min'
        | # tracks to display: any int from 1 to size of dataset
    --------------------------------------------------------------------------------------------
    '''

    try:
        # Create the parser
        parser = parser_intializer()

        # Parse the arguments
        args = parser.parse_args()

        # Set usage message
        parser.usage = main.__doc__

        # Parameters that the max_or_min function uses. They are set according to command line input
        selected_variable = args.var.lower() # variable to sort by (tempo, etc)
        selected_sort = args.sort.lower() # sort by max or min
        selected_n = args.n # number of top values to display

        # ----------------N SELECTION LOGIC----------------
        if selected_n < 1:
            parser.error("Invalid number selection. Please select a number between 1 and 100")
        
        if selected_n > data_source.get_row_count() - 1:
            parser.error("Invalid number selection. Please select a number less than the number of rows in the dataset.")

        # Print the result of the get_query function
        results = data_source.get_query(selected_variable, selected_n, selected_sort)
        
    except argparse.ArgumentError as e:
        # print(f"Argument error: {e}")
        print("error. Go back to homepage.")
    except Exception as e:
        # print(f"An error occurred: {e}")
        print("error. Go back to homepage.")

if __name__ == "__main__":
    main()

