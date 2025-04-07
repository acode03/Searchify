from ProductionCode.helperFunctions import * 

class ViewDatasetModel: 
    """
    This class is an abstract model for the view_dataset page
    """
    def __init__(self, dataset):
        """
        ----------------------------------------
        Initializes the ViewDatasetModel object
        ----------------------------------------
        Args:
            dataset (str): The simplified alias of a dataset (mini, high, low)
        ----------------------------------------
        """
        self.dataset = map_simplified_data_name_to_file(dataset) # filename of dataset
        self.formatted_dataset = self._format_dataset() # formatted dataset for Flask display

    def get_formatted_dataset(self):
        """
        ----------------------------------------
        Getter method for formatted_dataset
        ----------------------------------------
        Args:
            None 
        ----------------------------------------
        Returns:
            self.formatted_dataset (str): The formatted dataset for Flask display
        ----------------------------------------
        """
        return self.formatted_dataset
    
    def _format_dataset(self):
        """
        ----------------------------------------
        Formats dataset into a 2d list for Flask display
        ----------------------------------------
        Args:
            None 
        ----------------------------------------
        Returns:
            Formatted multi-line string of the dataset
        ----------------------------------------
        """
        data = None # placeholder empty variable to load data into

        def _load_dataset_file_to_data():
            # loads dataset from file to data variable
            nonlocal data
            data = load_data(self.dataset)
        
        def _format_data():
            # formats data so it looks good in the browser
            nonlocal data
            data = formatted_2d_list(data)
        
        # run the functions to process data
        _load_dataset_file_to_data()
        _format_data()
        return data

