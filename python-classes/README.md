Python - Classes and Objects        
This repository contains various Python classes that define and manipulate a Square object. Each task demonstrates the creation, validation, and manipulation of square objects in Python, including handling private attributes, validation, and area calculation.           

Project Tasks                
0. My First Square        
File: 0-square.py        
Description: Defines an empty Square class.           
Prototype: class Square:         
Key Feature: The class is initialized with no properties, and the object can be created successfully.         

1. Square with Size        
File: 1-square.py           
Description: Defines a square with a private instance attribute size. The square is instantiated with a size.       
Prototype: class Square:       
Key Feature: The size attribute is private and cannot be accessed directly from outside the class.           

2. Size Validation         
File: 2-square.py            
Description: Defines a square with a private size attribute. The square can be instantiated with an optional size. The size must be an integer and greater than or equal to 0.      
Prototype: class Square:         
Key Feature: Includes validation for the size attribute, raising exceptions if invalid values are provided.             

3. Area of a Square           
File: 3-square.py             
Description: Defines a square with a private size attribute and a public method area() that returns the area of the square.          
Prototype: class Square:         
Key Feature: The area() method computes and returns the area of the square based on its size.           

4. Access and Update Private Attribute       
File: 4-square.py      
Description: Defines a square with private size and provides getter and setter methods for the size attribute. Includes validation for the size.          
Prototype: class Square:        
Key Feature: Provides getter and setter for the size attribute, enforcing type and value validation.       

5. Printing a Square          
File: 5-square.py          
Description: Defines a square and includes a method my_print() that prints the square using # characters.         
Prototype: class Square:       
Key Feature: The my_print() method prints the square, and if the size is 0, it prints an empty line.         

6. Coordinates of a Square          
File: 6-square.py          
Description: Defines a square with both size and position attributes. The position is a tuple of two integers that determines the location of the square when printed.       
Prototype: class Square:       
Key Feature: The position attribute is validated and controls how the square is printed with respect to spaces.      

How to Run the Project   

Clone the repository:   
git clone https://github.com/arietteK/alu-higher_level_programming.git      

Navigate to the project directory:    
cd alu-higher_level_programming/python-classes     

Run the tests      
