from ProductionCode.helperFunctions import * 

class FilterTopModel: 
    """
    This class is an abstract model for the view_dataset page
    """
    def __init__(self, variable, number, parameter, dataset):
        """
        ----------------------------------------
        Initializes the ViewDatasetModel object
        ----------------------------------------
        Args:
            dataset (str): The simplified alias of a dataset (mini, high, low)
        ----------------------------------------
        """
        self.dataset = map_simplified_data_name_to_file(dataset) # filename of dataset
        self.formatted_dataset = self._format_dataset(variable, number, parameter, dataset) # formatted dataset for Flask display

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
    
    def _format_dataset(self, variable, number, parameter, dataset):
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
        # placeholder empty variables to load and filter data into
        data = None
        results = None

        def _load_dataset_file_to_data():
            # loads dataset from file into data variable
            nonlocal data
            data = load_data(self.dataset)

        def _filter_data_to_results(): 
            # filters data into results variable
            nonlocal results
            results = max_or_min(variable, number, parameter, data)
        
        def _format_results():
            # formats results to look better in flask
            nonlocal results
            results = formatted_1d_numbered_list(results)
        
        _load_dataset_file_to_data() 
        _filter_data_to_results()
        _format_results()
        
        return results

