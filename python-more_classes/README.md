Python - More Classes and Objects       
This project has solutions to various exercises on Python classes. The tasks focus on the creation and manipulation of the Rectangle class, demonstrating object-oriented programming principles such as instance attributes, methods, magic methods, and more.      

Task Breakdown    
0. Simple Rectangle     
Objective: Create an empty class Rectangle that defines a rectangle.     
Requirements:      
No module imports allowed.     
The class should not have any attributes or methods at this stage.        
1. Real Definition of a Rectangle      
Objective: Define the Rectangle class with private instance attributes width and height. Implement property getters and setters for both attributes.       
Requirements:         
Raise TypeError if the width or height is not an integer.        
Raise ValueError if the width or height is less than 0.       
Include an optional constructor to initialize width and height.         
2. Area and Perimeter          
Objective: Add two methods to the Rectangle class: area() and perimeter().                
Requirements:       
area() should return the area of the rectangle.        
perimeter() should return the perimeter of the rectangle.        
If either width or height is 0, the perimeter should be 0.              
3. String Representation             
Objective: Modify the Rectangle class to include a string representation method.                   
Requirements:         
Override __str__() and __repr__() to return a string representation of the rectangle.              
The string representation should use # characters to draw the rectangle, unless width or height is 0 (in which case return an empty string).        
4. Eval is Magic                  
Objective: Implement a magic method to allow an instance of Rectangle to be recreated using eval().         
Requirements:                   
The __repr__() method should return a string representation of the rectangle that can be used to recreate the object via eval().             
5. Detect Instance Deletion               
Objective: Detect when an instance of Rectangle is deleted and print a message.         
Requirements:         
Override __del__() to print "Bye rectangle..." when an instance is deleted.        
6. How Many Instances             
Objective: Track how many instances of the Rectangle class exist.           
Requirements:                  
Use a class attribute number_of_instances to track the number of Rectangle instances.          
Increment the attribute when an instance is created and decrement when it is deleted.         
Print the current number of instances when deleting a rectangle.             
7. Change Representation                
Objective: Allow the symbol used to represent the rectangle to be dynamically changed.        
Requirements:             
Add a class attribute print_symbol, initialized to #, to control the symbol used in the string representation.          
Allow instances to modify this attribute.            
If width or height is 0, return an empty string.
         
Setup and Usage    

Clone the repository:     
git clone https://github.com/arietteK/alu-higher_level_programming.git     

Navigate to the python-more_classes directory:       
cd python-more_classes         
Each task is implemented in its respective file (e.g., 0-rectangle.py, 1-rectangle.py, etc.).      
You can run the tests by executing the corresponding main.py files        
