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

Task 10: Student to JSON with Filter       
Description: This script defines a Student class that retrieves a dictionary representation of itself. The to_json method selectively retrieves attributes if a list of attribute names is provided.           
Attributes: first_name, last_name, age             
Method: to_json(self, attrs=None)               

Task 11: Student to Disk and Reload             
Description: Extends the Student class from the previous task. It adds the reload_from_json method, which updates the instance's attributes from a given dictionary.        
Method: reload_from_json(self, json)         

Task 12: Pascal's Triangle               
Description: Implements a function pascal_triangle(n) that returns a list of lists representing the Pascal's triangle up to the nth row.           
Return: An empty list if n <= 0.              

Task 13: Search and Update                 
Description: Defines a function append_after that inserts a line of text to a file after each line containing a specific string.               
Prototype: def append_after(filename="", search_string="", new_string="")             

Task 14: Log Parsing            
Description: A script that reads stdin line by line and computes metrics related to file size and the count of status codes.            
Input Format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>          
