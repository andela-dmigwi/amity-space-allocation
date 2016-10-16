
## [Amit Space Allocation System]

Visit [Amit Space Allocation System](http://andela-dmigwi.github.io/amity-space-allocation/) for more information.

[![Build Status](https://travis-ci.org/andela-dmigwi/amity-space-allocation.svg?branch=develop-refactor)](https://travis-ci.org/andela-dmigwi/amity-space-allocation)
[![Coverage Status](https://coveralls.io/repos/github/andela-dmigwi/amity-space-allocation/badge.svg?branch=develop-refactor)](https://coveralls.io/github/andela-dmigwi/amity-space-allocation?branch=develop-refactor)
[![Issue Count](https://codeclimate.com/github/andela-dmigwi/amity-space-allocation/badges/issue_count.svg)](https://codeclimate.com/github/andela-dmigwi/amity-space-allocation)


Amity is an [Andela](http://andela.com) facility that has several rooms in it. A room can be
either a **Living Space** or an **Office Space**. An Office Space can accomodate a maximum of
6 people and the Living Space can accomodate a maximum of 4 at ago.  

The Amity Space Allocation allocate people either The Living Space or The Office Space randomly  

A room can be allocated to a staff or a fellow at Andela.Staff cannot be allocated living spaces.
 Fellows have a choice to choose a living space or not. 

### Installation
Clone `git clone https://github.com/andela-dmigwi/amity-space-allocation.git`

### Virtual Environment
Navigate to the root folder `amity-room-allocation` and:
 - Install virtual environment `virtualenv --python=python3 a-venv` 
 - Activate it by `source a-venv/bin/activate`
 
### Run the Test
 run `nosetests`

### Run the system 
 run `interactive.py --interactive` or `interactive.py -i`


# Usage
 
## Create Room
`create_room <room_name>...`  
 - Creates rooms in Amity. This command allows one to create room  
   single room: `create_room Dojo` -> Create room called **Dojo**  
   multiple rooms: `create_room Dojo,Krypton,Valhala` -> Creates three rooms: **Dojo**, **Krypton** and **Valhala**

 - After typing the create command, you will be prompted to type:  
   `O` for Office   
          or    
   `L` for Living Space  

 *This will be done for every room you create*


## Add Person
 `add_person <person_name> <FELLOW|STAFF> [wants_accommodation]`
 - Adds a person to the system and allocates the person to a random room. wants_accommodation here is an optional argument which can be either ``Y`` or ``N``.  
The default value if it is not provided is N.  

## Reallocate Person
 `reallocate_person <person_identifier> <new_room_name>`
 - Reallocate the person with person_name to new_room_name.

## Load People
`load_people `
- Adds people to rooms from a txt file.  
    
    ``OLUWAFEMI FELLOW Y``

    ``DOMINIC STAFF``
 
    ``PATTERSON FELLOW Y``
 
    ``DOMINIC STAFF`` 
    
    ``PATTERSON FELLOW Y``
    
    ``LAWRENCE FELLOW Y``


## Print Allocations
`print_allocations [filename]`
 - Prints a list of allocations onto the screen. The file name is optional, if its not provided, data is not printed in a file.  
  
    ``ROOM NAME``

    ``-------------------------------------``
    
    ``-------------------------------------``

    ``MEMBER 1, MEMBER 2, MEMBER 3``
   
    ``ROOM NAME``

    ``-------------------------------------``
    
    ``-------------------------------------``
    
    ``MEMBER 1, MEMBER 2``
  

## Print Unallocated
`print_unallocated [filename]`
 - Prints a list of unallocated rooms to the screen. The file name is optional, if its not provided, data is not printed in a file.

## Print Room
`print_room <room_name>`
 - Prints the names of all the people in ``room_name`` on the screen.

## Save State
`save_state `
 - Persists all the data stored in the app to a SQLite database. Retrieves all the data held in the application and saves it in the database

## Load State
`load_state `
 - Loads data from a database into the application.

**@Done By Migwi-Ndung'u**  
[my github repo](http://www.github.com/andela-dmigwi)



