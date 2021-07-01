# AirBnB_clone - The Console

![airbnb_img](https://i.imgur.com/U8B8g4H.png)

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.
After 4 months, you will have a complete web application composed by:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

And the final data diagram looks like this:

![data_diagram](https://i.imgur.com/4qOQO1A.png)
# Create a command interpreter.

This is the first step towards building the first full web application: the AirBnB clone.
The other following projects: HTML/CSS templating, database storage, API, front-end integration…


## Execution

The hbnb command interpreter should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C):

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: ``` $ echo "python3 -m unittest discover tests" | bash ```


- **create command**:
   If you want to create a new object type the following:
   
    `create <object class>`
	
   So the classes that we manage are:
     
     1. BaseModel
     2. User
     3. Amenity
     4. City
     5. Place
     6. State
     7. Review


   So you have to take care of the capital letters when you call the class. Once the object was created it will return the the id number:

- **all command**: With this command you will be able to print all the created objects that exists, by typiying:
    
  `all` or `.all()`

  But if you want to print all the objects of a specific class you have to type:
	 
  `all <class name>` like `all User` or `<class name>.all()` like `City.all()`
	   
- **count command**:
  With count you can print the number of objects that belong to a specific class, by typiying:
  
  `count <class name>` like `count Place` or `<class name>.count()` like `Review.count()`
  
- **show command**:
  This command prints the string representation of a specific objects, by typiying:
  `show <class name> <id>` ex: `show Review 12345678`or the second way `<class name>.show("id")` like `Review.show("12345678")`.
  
- **destroy command**:
  This command deletes a specific objects. To remove the object type:
  `destroy <class name> <id>` ex: `destroy Review 12345678`or `<class name>.destroy("id")` like `Review.destroy("12345")`.
  
- **update command**:
  This command updates a specific objects. To update the object type one of these three way to do it:
  
  1. `update <class name> <id> <name> "<value>"` ex: `update Review 12345678 name "Goku"`
  2. `<class name>.update("id", "<name>", "<value>")` ex: `City.update("12345678", "item", "bed")`
  3.  `<class name>.update("id", {'<name1>: "<value1>", '<name2>': "<value2>"})` ex `City.update("12345678", {'item1': "bed", 'item2': "bathroom"})`
  
   if the attribute of the class exists it will be replace with the new value, otherwise it will create a new attribute for the specified instance.
   
- **commands to exit the program**
   if you want to exit the program type:
   
    `quit` or `Ctrl+D` or `EOF`
