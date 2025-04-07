import psycopg2
import ProductionCode.psqlConfig as config

class DataSource:
    def __init__(self):
        self.connection = self.connect()
	
    def connect(self):
        '''Arguments: None
        Returns: None
        Purpose: Connects to the database in stearns'''
        try:
            connection = psycopg2.connect(database=config.database, user=config.username, password = config.password, host="localhost")
        except Exception as e:
            #print("Connection error: ", e)
            exit()

        return connection
    
    def asc_or_desc(self, category, number, order):
        '''Arguments: variable, number of songs, parameter (max or min)
        Returns: get_query called with the same arguments + the sorting order
        Purpose: Takes in the arguments, and interprets the parameter as an SQL-callable sorting order.'''
        if order == "high-low":
                sort = 'DESC'
        elif order == "low-high":
                sort = 'ASC'
        return self.get_query(category, number, sort)


    
    def get_query(self, category, number, sort):
        '''Arguments: variable, number of songs, sorting order
        Returns: Results of a SQL query based on the inputs.
        Purpose: Takes in the arguments, runs a SQL query on our database, and returns the results.'''

        if number.isnumeric() == False:
            return ("invalid number")

        try:
            cursor = self.connection.cursor()

            query = "SELECT track_name, track_artist, " + category + " FROM high_pop ORDER BY " + category + " " + sort + " LIMIT " + str(number)
      
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            return ("Something went wrong when executing the query: ", e)
        
        
    def get_all(self):
        '''Arguments: None
        Returns: All rows in the database
        Purpose: Returns all rows in the database.'''
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM high_pop"
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            #print ("Something went wrong when executing the query: ", e)
            return ("ERROR. failed fetching")
        
    def get_row_count(self):
        '''Arguments: None
        Returns: Number of rows in the database
        Purpose: Returns the number of rows in the database.'''
        try:
            cursor = self.connection.cursor()
            query = "SELECT COUNT(*) FROM high_pop"
            cursor.execute(query)
            return cursor.fetchone()[0]
        except Exception as e:
            #print ("Something went wrong when executing the query: ", e)
            return None