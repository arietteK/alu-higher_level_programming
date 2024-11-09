Python - Exceptions   

 This project has many Python functions that demonstrate the handling of exceptions, safe printing, and division operations. Each task is used to practice the usage of try, except, finally, and other exception handling techniques in Python.

Project Tasks
1. Safe List Printing
File: 0-safe_print_list.py  
Description: Prints x elements from a list safely, handling cases where x is larger than the list length.     
Prototype: def safe_print_list(my_list=[], x=0)   
Key Feature: Uses try/except to handle index out of range situations.    
2. Safe Printing of an Integer    
File: 1-safe_print_integer.py     
Description: Prints an integer using "{:d}".format() while handling non-integer values.    
Prototype: def safe_print_integer(value)      
Key Feature: Uses try/except to print integers and return True/False.       
3. Print and Count Integers        
File: 2-safe_print_list_integers.py       
Description: Prints the first x integers from a list, skipping non-integer elements.       
Prototype: def safe_print_list_integers(my_list=[], x=0)      
Key Feature: Uses try/except to handle non-integer values and out-of-bounds access.        
4. Integers Division with Debug        
File: 3-safe_print_division.py       
Description: Divides two integers safely and handles division errors.        
Prototype: def safe_print_division(a, b)        
Key Feature: Uses try/except/finally to print division results and handle errors like division by zero.         
5. Divide a List        
File: 4-list_division.py         
Description: Divides elements of two lists element by element, handling exceptions like wrong types, division by zero, and out of range.        
Prototype: def list_division(my_list_1, my_list_2, list_length)         
Key Feature: Uses try/except/finally to handle various division errors.            
6. Raise Exception        
File: 5-raise_exception.py             
Description: Raises a TypeError exception.        
Prototype: def raise_exception()          
Key Feature: Demonstrates raising exceptions manually.            
7. Raise a Message         
File: 6-raise_exception_msg.py         
Description: Raises a NameError exception with a custom message.           
Prototype: def raise_exception_msg(message="")           
Key Feature: Allows raising a NameError with a specific message.      
8. Safe Integer Print with Error Message       
File: 100-safe_print_integer_err.py        
Description: Prints an integer safely and outputs an error message to stderr if the value is not an integer.           
Prototype: def safe_print_integer_err(value)      
Key Feature: Uses try/except to handle non-integer values and print error messages.             
9. Safe Function             
File: 101-safe_function.py         
Description: Executes a function safely, returning None if any exceptions are raised.         
Prototype: def safe_function(fct, *args)        
Key Feature: Uses try/except to execute a function safely and handle exceptions.        
10. ByteCode to Python          
File: 102-magic_calculation.py             
Description: Performs calculations based on Python bytecode.         
Prototype: def magic_calculation(a, b)          
Key Feature: Recreates the functionality of the given bytecode in Python.
       
How to Run the Project         
Clone the repository:        
git clone https://github.com/your-username/alu-higher_level_programming.git     

Navigate to the project directory:      
cd alu-higher_level_programming/python-exceptions       

Run the tests:        
python3 0-main.py   
python3 1-main.py    
python3 2-main.py     
python3 3-main.py              
