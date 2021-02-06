## Introduction

This is an application implementation for game engine of Tower of Hanoi. It exposes REST API for client to interact and modify the state of a game following the rules: https://en.wikipedia.org/wiki/Tower_of_Hanoi

## Requirements

- Enforce the rules of the game (as stated in the article above) and report an error if any attempted move violates the rules
- Apply the effects of any valid move to the game state
- Provide the client with the complete state of the rods and disks
- Determine if the victory conditions have been met
- The game engine must support 4 disks

## Implementation Details

Current implementation will initialize only one game at a time with 3 robs, index is from 0-2, and 4 disks with size of 4(bottom), 3, 2, 1(top), stacked on the first rob which is index 0. It defines following REST API path for user to play the game on generated default local host http://127.0.0.1:5000 or http://localhost:5000:
- GET /hanoi/create: to create/initialize a game; every time this API is called, the game state will be reset
- GET /hanoi/state: to fetch the complete state of current game of robs and disks ie. {"rob0":[4,3,2], "rob1":[1], "rob2":[]}
- PUT /hanoi/move?source=num&target=num: to move a disk from source rob to target rob. If it is a valid move, the effects will be saved; otherwise a proper error message will be displayed 
- GET /hanoi/win: to check if user has won the game
If user try to play the game before creating the game, an error message will be displayed to inform the user the game is not created yet.
- Some edges cases handling, such as move disk when source and target rob is not defined or empty; must creategame first before other API calls etc.
 
Note: All the responses message for these API requests are in Json format.


## Instructions to run the application and sample play

1. make sure python3 and pip is already installed
2. clone git repository and go to the package
3. create a python virtual environment and activate virtual environment
   
   `python3 -m venv env`
   `. env/bin/activate`
   
4. install the requirements file

   `pip3 install -r requirement.txt`
   
5. run the application

   `python3 src/app.py`
   
   You will see following output if it is successful: 
   > Serving Flask app "app" (lazy loading)
   
   > Environment: production
   
   > WARNING: This is a development server. Do not use it in a production deployment.
   
   > Use a production WSGI server instead.
   
   > Debug mode: on
   
   > Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   
   > Restarting with stat
   
   > Debugger is active!
   
   > Debugger PIN: 830-297-478
   

6. open a browser and access http://127.0.0.1:5000/hanoi/create to create the first game
![screenshot](https://github.com/bluecoatmatrix/tower_of_hanoi/blob/main/screenshots/create.png)
   or from console: 

   `curl -X GET "http://127.0.0.1:5000/hanoi/create"`
![screenshot](https://github.com/bluecoatmatrix/tower_of_hanoi/blob/main/screenshots/createcli.png)

7. Try to get initial state of the game: http://127.0.0.1:5000/hanoi/state
![screenshot](https://github.com/bluecoatmatrix/tower_of_hanoi/blob/main/screenshots/initialstate.png)
   
   or 
   
`curl -X GET "http://127.0.0.1:5000/hanoi/state"`
![screenshot](https://github.com/bluecoatmatrix/tower_of_hanoi/blob/main/screenshots/Screen%20Shot%202021-02-06%20at%202.35.14%20AM.png)

8. Try to make an invalid move with source=-1 from any browser tool can perform put request or run following command; then you will get invalid source error message.
	`curl -X PUT "http://127.0.0.1:5000/hanoi/move?source=-1&target=1"`
![screenshot](invalid source)

9. Similarly try on invalid target=4
	`curl -X PUT "http://127.0.0.1:5000/hanoi/move?source=0&target=4"`
![screenshot](invalid target)

10. Try on source and target are equal
	`curl -X PUT "http://127.0.0.1:5000/hanoi/move?source=0&target=0"`
![screenshot](equal)

11. Try to move from source has empty disks
	`curl -X PUT "http://127.0.0.1:5000/hanoi/move?source=2&target=1"`
![screenshot](empty source)

12. Now make a valid move 
	`curl -X PUT "http://127.0.0.1:5000/hanoi/move?source=0&target=1"`
![screenshot](succ move)

13. Try to move a bigger disk to a small disk by repeat the last move again
	`curl -X PUT "http://127.0.0.1:5000/hanoi/move?source=0&target=1"`
![screenshot](invalid move)

14. Try to check if you have won the game now(not yet) from browser: http://127.0.0.1:5000/hanoi/win
![screenshot](nowin)
    or 
    `curl -X GET "http://127.0.0.1:5000/hanoi/win"` 
![screenshot](nowin cli)

15. Try all moves from file movestowin.txt to reach winning state. You can try to get any in progress state anytime you want
![screenshot](inprogress) 

16. Once reached winning state, try to get the winning state: http://127.0.0.1:5000/hanoi/state
![screenshot](win state)
    or 
    `curl -X GET "http://127.0.0.1:5000/hanoi/state"`
![screenshot](win state cli)

17. Now you are winner! http://127.0.0.1:5000/hanoi/win
![screenshot](win)
    or 
    `curl -X GET "http://127.0.0.1:5000/hanoi/win"`
![screenshot](win cli)


## Other invalid user cases handling

1. Move disk when source and target arguments are not defined or empty
![screenshot](emptysourpara)
![screenshot](emptytargetparam)

2. Use wrong REST API methods 
![screenshot](wrongmethod)

3. Try to check win or get state before the game is created
![screenshot](beforecreate)



## To run tests using Pytest with coverage plug-in:

Follwing is an example to run Unit tests and integration tests together

1. Go to tests/ directory: `cd tests`
2. run:
	```pytest --cov disk --cov rob --cov hanoi --cov app --cov-report term-missing```
![screenshot](https://github.com/bluecoatmatrix/tower_of_hanoi/blob/main/screenshots/pytest.png)

Note: The app.py coverage missing is due to last line is the __main__ function all. Maybe I can move that call to anohter file. Also it is really hard to find a scenario to trigger exception of create API call.



## Future improvemnts:

#### API response body handling

   Current response body only show a simple message. It would be better to have body format standard and to show more information for all API. 

#### More disks

   There are only 4 disks created in current game. We can let client to customerize the game to have any number of disks they prefer.

#### Multiple game instances
	
   Right now, every time there is only one game can be initialized. We can add support to create multiple games at the same time. We can add sessionID to API design to give the option to access different game instances.   

#### Security
	
   It would be better to have authentication to prevent unauthorized users to modify the game state. Furthermore, it would be a good idea to use encryption in the possible deployment to secure communication channels.
