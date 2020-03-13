from code.class_node import Class_Node
import pymongo

# TODO - replace default values with actual values for the database
client = pymongo.MongoClient('hostname', 27017) 

db = client['database_name']

collection = db['collection_name']

def top_sort():
    pass

def load_classes(prerec: Class_Node):
    """
    Loads the given class table from the database into a Class_Node object and returns it
    """
    query = {"prerec": prerec.number}

    classes = collection.find(query)

    return classes
