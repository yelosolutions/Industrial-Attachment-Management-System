# **Industrial Attachment Management System**
---
## **Introduction**

An Industrial Attachment Management System is a system that enables undergraduate students to 
select a company,apply for attachment and register their details and of their supervisors. 
This links industries and learning institutions easing the placement of students in workplaces for
the acquisition of practical skills and appropriate work-ethics.

A student will therefore easily apply for an attachment position and get placed to the respective institutions or industries.

---

## **The Console**

### Usage

## Description

This repository contains the initial stage of my project to develop an Industrial Attachment Management System(IAMS).

This stage implements the backend interface(console), to manage program data.

It consists of a custom command-line interface, a file storage and the base class along other model classes to define the structure of my data.

The console allows me to create, update, and destroy objects, as well as manage file storage. This is basically a tool that I will use later on to see what does and doesn't work with storage.

The file storage is an abstacted storage engine. A system of JSON serialization/deserialization will make the storage maintain persistency between sessions.


## To do

* Put in place a parent class(BaseModel) to take care of initialization, serialization and deserialization of future instances
* Create a flow of serialization/deserialization: instance <-> Dictionary <->JSON string <-> file
* Create classes used for IAMS(Student, Place_Of_Attachment, County) that inherit from BaseModel
* Create an abstracted storage engine of the project: File storage.
* Create all unittests to validate all of my classes and storage engine. 
---

* 1. **Models**
	* BaseModel
	* Student
	* Place_Of_Atachment
	* County

* 2. **Console.py**

* 3. **File storage**

##Tests

