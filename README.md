# AirBnB_clone

![N|Solid](https://process.filestackapi.com/resize=width:200/https://cdn.filestackcontent.com/4EAxE8NfTNGVsqHFIXVF)

# DESCRIPTION

This project consists of taking the commands and classes that the user writes to interpret and execute them, the result will be a json file that will show the instance created, the id with current date and time
Finally, it gives the user the possibility to continue writing, creating, observing, destroying and updating the information of the classes.
Possible errors when executing commands are:

- use an illegal item.
- can't find a item
- not using the commands correctly
- items in bad use
- does not use class and id when viewing content

# INSTALATION

To install the AirBnb clone developed in the project:
1- clone the git hub of ...
2- use the command chmod u+x console or python3 console  
3- open the console using ./console



# USAGE EXAMPLES

Initially, the user enters the command to execute (./console).
Among the most used commands we have:
Among the used commands we have:
- create: to create an instance use, create (class)
- show: show: create a dictionary type list with class name, id, current date and time
- destroy: destroy the class that was created with create
- all: show all data saved in json
- update: update the data that is already entered in the json file
in the same command line the user can use the different options that belong to each example:
- create BaseModel: as a result it will give us an id:
 BaseModel - id:cfd693f9-6ebf-4094-a558-b182ddd4c0cd.
- show it will show us the data it contains:
  BaseModel cfd693f9-6ebf-4094-a558-b182ddd4c0cd  :it will show us the data it contains.
- all: show all data saved in json:
 ["[BaseModel] (3a79218b-1c56-465c-8ebd-f1a8881da447) {'id': '3a79218b-1c56-465c-8ebd-f1a8881da447', 'updated_at': datetime.datetime(2020, 11, 5, 1, 38, 9, 364626), 'created_at': datetime.datetime(2020, 11, 5, 1, 38, 9, 364596)}"].
- destroy: destroy the class that was created with create and id.
- update BaseModel cfd693f9-6ebf-4094-a558-b182ddd4c0cd
  update old data with user added data

# AUTHOR

Christian bedoya <1642@holbertonschool.com>
Christian Campos <1566@holbertonschool.com>