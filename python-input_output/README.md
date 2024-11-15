Python - Input/Output         
Overview              
The project involves multiple tasks that helps to increase our understanding of file handling and JSON processing in Python. These tasks are essential for scenarios where data needs to be read from or written to files, processed, and serialized/deserialized.                          

Tasks             
Task 0: Read File            
Functionality: Reads a UTF-8 encoded text file and prints its content to stdout.                
Prototype: def read_file(filename=""):                
Highlights:Uses the with statement for resource management and no module imports allowed.            

Task 1: Write to a File             
Functionality: Writes a string to a UTF-8 encoded text file and returns the number of characters written.                 
Prototype: def write_file(filename="", text=""):               
Highlights:Overwrites existing file content. Creates the file if it doesn't exist.                 

Task 2: Append to a File             
Functionality: Appends a string to the end of a UTF-8 text file and returns the number of characters added.                
Prototype: def append_write(filename="", text=""):              
Highlights:Creates the file if it does not exist.             

Task 3: To JSON String                   
Functionality: Converts a Python object to its JSON string representation.               
Prototype: def to_json_string(my_obj):           
Highlights:Ensures JSON serialization.             

Task 4: From JSON String to Object             
Functionality: Returns a Python object represented by a JSON string.             
Prototype: def from_json_string(my_str):                
Highlights:Converts JSON strings back to Python data structures.                

Task 5: Save Object to a File                
Functionality: Writes an object to a text file using JSON representation.              
Prototype: def save_to_json_file(my_obj, filename):             
Highlights:Saves structured data as JSON.              

Task 6: Create Object from a JSON File              
Functionality: Creates a Python object from a JSON file.           
Prototype: def load_from_json_file(filename):               
Highlights:Reads JSON data and converts it to a Python object.              

Task 7: Load, Add, Save           
Functionality: Script that adds all arguments to a Python list and saves them to a file as JSON.            
Filename: 7-add_item.py        
Dependencies:Uses save_to_json_file and load_from_json_file functions.              

Task 8: Class to JSON               
Functionality: Converts an object to a dictionary representation suitable for JSON serialization.                
Prototype: def class_to_json(obj):              
Highlights:Handles basic data structures.           

Task 9: Student to JSON         
Functionality: Defines a Student class with methods for JSON serialization.        
Public Attributes:first_name, last_name, age         
Method: to_json()          
