# OOP Basics - :taco:

This class if the basics of OOP 

## Topics to cover

**4 pillars**:
- Abstraction
- Inheritance
- Polymorphism
- Encapsulation

Other learning Objectives:
- Git + Github
- Documentation and Markdown Files
- Best practises and orginastions


#### Definitions

##### Class
Class is a blueprint for objects. 
Inside we define object's characteristics and behaviours it can do.

With classes, you can create an instance of that class

##### attributes
They are variables/constants that are attached to a object of a specific class.

##### instances
The occurrence of an object of a specific class.

##### methods
Is like a function  but can only run on a specific datatype or object of its own class

##### the __init__method
is a method that runs everytime you inititate/create a class.
Also known as a constructor method in other languages


##### self 
refers the instance 
in a method, self is the specific instance.

## Pillars
This is the definition for the pillars.

#### Abstraction
This is hiding complexity and giving our users only what they need to make things work.
Think of it like a black box.
in code the moethods: .split() or .append() for strings and list are abstracted. We only see the documentation

I will do the same.
- Separating it from our class definition from running it
- Provide some documentation on the available methods.


#### Inheritance
The ability to inherit all the behaviours and characteristics of parent class

````
class Reptile(Animal):
````

