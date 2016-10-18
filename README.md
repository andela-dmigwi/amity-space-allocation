
## [Amit Space Allocation System]

Visit [Amit Space Allocation System](http://andela-dmigwi.github.io/amity-space-allocation/) for more information.

[![Build Status](https://travis-ci.org/andela-dmigwi/amity-space-allocation.svg?branch=develop-refactor)](https://travis-ci.org/andela-dmigwi/amity-space-allocation)
[![Coverage Status](https://coveralls.io/repos/github/andela-dmigwi/amity-space-allocation/badge.svg?branch=develop-refactor)](https://coveralls.io/github/andela-dmigwi/amity-space-allocation?branch=develop-refactor)
[![Issue Count](https://codeclimate.com/github/andela-dmigwi/amity-space-allocation/badges/issue_count.svg)](https://codeclimate.com/github/andela-dmigwi/amity-space-allocation)


Amity is an [Andela](http://andela.com) facility that has several rooms in it. A room can be
either a **Living Space** or an **Office Space**. An Office Space can accomodate a maximum of
6 people and the Living Space can accomodate a maximum of 4 at ago.  

The Amity Space Allocation allocate people either The Living Space or The Office Space randomly  

A room can be allocated **ONLY** to a staff or a fellow at Andela. Staff cannot be allocated living spaces.
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
*Command:* `create_room <room_name>...`  
 - Creates rooms in Amity. This command allows one to create room  
   **Single room**: `create_room Dojo` -> Create room called **Dojo**  
   **Multiple rooms**: `create_room Dojo,Krypton,Valhala` -> Creates three rooms: **Dojo**, **Krypton** and **Valhala**

 - After typing the create command, you will be prompted to type:  
   `O` for Office   
       or  
   `L` for Living Space  

 *This will be repeated for every room you create*  


## Add Person
 *Command:* `add_person <person_name> <FELLOW|STAFF> [wants_accommodation]`  
 - Adds a person to the system and allocates the person to a random room. wants_accommodation here is an optional argument which can be either ``Y`` or ``N``.  
The default value if it is not provided is `N`.  

## Reallocate Person
 *Command:* `reallocate_person <person_identifier> <new_room_name>`  
 - Reallocate the person with person_name to new_room_name.  

## Load People
*Command:* `load_people `  
- Adds people to rooms from a txt file.  
    
    ``OLUWAFEMI_FELLOW Y``  
    ``DOMINIC_STAFF``  
    ``PATTERSON_FELLOW Y``  
    ``DOMINIC_STAFF``  
    ``PATTERSON_FELLOW Y``  
    ``LAWRENCE_FELLOW Y``  


## Print Allocations
*Command:* `print_allocations [filename]`  
 - Prints a list of allocations onto the screen. The file name is optional, if its not provided, data is not printed in a file.  
  
    ``Room Name:  Narnia ``  
    ``-------------------------------------``  
    ``MEMBER 1, MEMBER 2, MEMBER 3``  

   
    ``Room Name:  Krypton``  
    ``-------------------------------------``  
    ``MEMBER 1, MEMBER 2``  


    ``Room Name:  Krypton``  
    ``-------------------------------------``  
    ``MEMBER 1, MEMBER 2``  
  
## Print Empty Rooms
*Command:* `print_empty_rooms [filename]`  
 - Prints a list of unallocated rooms to the screen. The file name is optional, if its not provided, data is not printed in a file.  

## Print Room
*Command:* `print_room <room_name>`  
 - Prints the names of all the people in ``room_name`` on the screen.  

## Print Unallocated
*Command:* `print_unallocated [filename]`  
 - Prints a list of unallocated people to the screen. The file name is optional, if its not provided, data is not printed in a file.  

## Save State
*Command:* `save_state `  
 - Persists all the data stored in the app to a SQLite database. Retrieves all the data held in the application and saves it in the database  

## Load State
*Command:* `load_state `  
 - Loads data from a database into the application.  

**@Done By Migwi-Ndung'u**  
[my github repo](http://www.github.com/andela-dmigwi)  



