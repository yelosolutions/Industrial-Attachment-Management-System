# **Industrial Attachment Management System**
---
## **Introduction**

An Industrial Attachment Management System(IAMS) is a complete web application, intergrating data storage, a back-end API and a front-end interfacing.  
It will eventually enable undergraduate students to select a company,apply for attachment and register their details and of their supervisors. 
It links industries with learning institutions, easing the placement of students in workplaces for
the acquisition of practical skills and appropriate work-ethics.

A student will therefore be able to easily apply for an attachment position and get placed to the respective institutions or industries.

---
## Authors

- [@yelosolutions](https://www.github.com/yelosolutions)

## **IAMS console**
### Description

This is the initial stage of my project to develop an Industrial Attachment Management System(IAMS).

The IAMS console is a command line interpreter that permits management of the backend of IAMS.
It can be used to handle and all classes utilized by the application.

It consists of a custom command-line interface, a file storage and the base class along other model classes to define the structure of my data.

The console allows me to create, update, and destroy objects, as well as manage file storage. This is basically a tool that I will use later on to see what does and doesn't work with storage.

The file storage is an abstacted storage engine. A system of JSON serialization/deserialization will make the storage maintain persistency between sessions.

### Files and Directories

| File/Directory 	| Type	    | Description						   |
| :-------------------- | :-------- | :----------------------------------------------------------- |
| `models`	 	| Directory | Will contain all classes used for the entire project.A class,|
		 	 	      called "model" in an OOP project is the representation of an |
		 		      object/instance.					           |
| `console.py`		| File      | This is the entry point of my command line interpreter.      |
| `models/base_model.py`| File      | Defiles parent(base) class to be inherited by all of my model|
 		        	      classes It has the following elements:     		   |
 				      - attributes: id, created_at and updated_at                  |
 			              - methods: save() and to_json 				   |
| `models/engine`       | Directory | Will contain all storage classes. Has file_storage.py file   |

### Project Implementation
I will manipulate a storage system to give an abstraction between objects and how they are stored and persisted. To achieve this, I will:

* Put in place a parent class(called BaseModel) to take care of initialization, serialization and deserialization of future instances
* Create a flow of serialization/deserialization: instance <-> Dictionary <->JSON string <-> file
* Create classes used for IAMS(Student, Place_Of_Attachment, County) that inherit from BaseModel
* Create an abstracted storage engine of the project: File storage.
* Create all unittests to validate all of my classes and storage engine.
* Create a data model
* Manage (create, update, destroy etc) ocjects via a console/command interpreter.
* Store and persist objects to files(JSON files)
---
### General Use
First clone this repository.

Once the repository is cloned locate the "console.py" file and run it as follows:

```
$ ./console.py 
```
When this command is run the following prompt should appear:
``` 
(iams)
```
This prompt designates you are in the "IAMS" console. There are a variety of commands available within the console program.

### Commands
* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)

```
