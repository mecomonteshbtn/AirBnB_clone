<img src="https://is5-ssl.mzstatic.com/image/thumb/Purple123/v4/fd/ac/b4/fdacb4f9-4c73-1ca6-5595-ef18f821ee62/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/246x0w.png">
<img src="https://image.shutterstock.com/image-illustration/clone-icon-illustration-creative-sign-260nw-1497218057.jpg">

# 0x00 AirBnB clone - The console

In this directory you will find a implementation of a AirBnB clone.
In this first step is implemented the Console. Commands for create, update, destroy, show and manage diferent classes and attributes for the items that the app will be offer and for the users.

### The console ###
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

### Command interpreter ###

Our command interpreter looks like a mini shell and allow us manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Objectives of project ###

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

### Content of Directory ###
* Models Folder: Classes of the project. BaseModel is the parent Class. The other classes (amenity, city, place, review, state, user) inherit from BaseModel and specify others attributes for itselfs.
* Tests Folder : Unittests for the project
* AUTHORS: Information about the authors
* console.py: Eceutable file for the console
* file.json: JSON file with all information of instances

---

## Table of Contents

- [Examples and Usage](#ExamplesandUsage)
- [Installation](#installation)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Team](#team)
- [Support](#support)
- [License](#license)


---

## Examples of Usage

### Execution ###
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
### create ###
Creat an instance and show us the id number
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py 
(hbnb) create BaseModel
e37cf8df-351a-4df6-9d15-fd9331a5bfb2
(hbnb) 
```

### Show ###
Show the Class, object if the id is especified and its attributes
```
(hbnb) show BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
[BaseModel] (e37cf8df-351a-4df6-9d15-fd9331a5bfb2) {'id': 'e37cf8df-351a-4df6-9d15-fd9331a5bfb2', 'created_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695895), 'updated_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695945)}
(hbnb) 
```
### all ###
shows all the instances
```
(hbnb) all BaseModel
["[BaseModel] (5c8ebd08-a708-4823-b9a2-29d58b87c063) {'id': '5c8ebd08-a708-4823-b9a2-29d58b87c063', 'created_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 926171), 'updated_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 926179)}", "[BaseModel] (e576e179-8bb6-4229-a8be-90585b0c1d01) {'id': 'e576e179-8bb6-4229-a8be-90585b0c1d01', 'created_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 896687), 'updated_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 896706)}", "[BaseModel] (0763761f-4534-4a02-8097-79a4ab935ecb) {'id': '0763761f-4534-4a02-8097-79a4ab935ecb', 'created_at': datetime.datetime(2020, 7, 1, 4, 8, 48, 451468), 'updated_at': datetime.datetime(2020, 7, 1, 4, 8, 48, 451881)}", "[BaseModel] (f794d1ba-6688-42b8-ae08-0b307125643a) {'id': 'f794d1ba-6688-42b8-ae08-0b307125643a', 'created_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 922410), 'updated_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 923071)}", "[BaseModel] (ef9b217c-b58c-4d5f-b797-0dbbed80dedd) {'id': 'ef9b217c-b58c-4d5f-b797-0dbbed80dedd', 'created_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 930489), 'updated_at': datetime.datetime(2020, 7, 1, 5, 4, 54, 930504)}", "[BaseModel] (e37cf8df-351a-4df6-9d15-fd9331a5bfb2) {'id': 'e37cf8df-351a-4df6-9d15-fd9331a5bfb2', 'created_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695895), 'updated_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695945)}", "[BaseModel] (82f3d1a2-c28d-4327-be5f-0bceb29b0eb9) {'id': '82f3d1a2-c28d-4327-be5f-0bceb29b0eb9', 'created_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 888932), 'updated_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 889340)}", "[BaseModel] (e029daa8-9083-4097-b2bd-a66fe4895532) {'id': 'e029daa8-9083-4097-b2bd-a66fe4895532', 'created_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 892554), 'updated_at': datetime.datetime(2020, 7, 1, 5, 5, 38, 892561)}"
(hbnb) 
```
### update ###
update an instance
```
(hbnb) show BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
[BaseModel] (e37cf8df-351a-4df6-9d15-fd9331a5bfb2) {'id': 'e37cf8df-351a-4df6-9d15-fd9331a5bfb2', 'created_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695895), 'updated_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695945)}
(hbnb) update BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2 first_name "CharlieMeco"
(hbnb) show BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
[BaseModel] (e37cf8df-351a-4df6-9d15-fd9331a5bfb2) {'first_name': '"CharlieMeco"', 'id': 'e37cf8df-351a-4df6-9d15-fd9331a5bfb2', 'created_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695895), 'updated_at': datetime.datetime(2020, 7, 1, 18, 50, 15, 695945)}
(hbnb) 
```
### Destroy ###
Delete an instance
```
(hbnb) destroy BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
(hbnb) show BaseModel e37cf8df-351a-4df6-9d15-fd9331a5bfb2
** no instance found **
(hbnb) 
```
---

## Installation

* Clone the repository. git clone https://github.com/mecomonteshbtn/AirBnB_clone.git
* Open the /AirBnB_clone directory and execute console.py

### Setup

* You need Python interpreter.
IMPORTANT: The project was created in UBUNTU 14.04.3 LTS and Python 3.4.3.

---

## Documentation 

<a href="https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw">`cmd module`</a><br>
<a href="https://intranet.hbtn.io/rltoken/jKl9WFpKA-fPt7_guv9_3Q">`packages`</a><br>
<a href="https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g">`uuid module`</a><br>
<a href="https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q">`datetime`</a><br>
<a href="https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g">`unittest module`</a><br>
<a href="https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg">`args/kwargs`</a><br>
<a href="https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A">`Python test cheatsheet`</a><br>
---

## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using 

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using. 
---

## Team

<a href="https://github.com/mecomonteshbtn">`mecomonteshbtn`</a>
<a href="https://github.com/Charliemur2">`Charliemur2`</a>


---

## Support

Feel free to contact us!

- GitHub at <a href="https://github.com/Charliemur2">`Charliemur2`</a>
- GitHub at <a href="https://github.com/mecomonteshbtn">`mecomonteshbtn`</a>
- Twitter at <a href="https://twitter.com/charliesoka">`@charliesoka`</a>
- Twitter at <a href="https://twitter.com/mecomontes">`@mecomontes`</a>

---

## License

Free Source Code
