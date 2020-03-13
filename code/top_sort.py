from code.class_node import Class_Node
import pymongo

# TODO - replace default values with actual values for the database
client = pymongo.MongoClient('hostname', 27017) 

db = client['database_name']

def top_sort():
    pass

def load_class():
    """
    Loads the given class table from the databse into a Class_Node object and returns it
    """
    pass