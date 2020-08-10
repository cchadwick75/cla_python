# International Space Station Command Line Arguments 
This project will allow you to see International Space Station information using Python Command Line Arguments.  This project was created using the open APIs from Space.
http://open-notify.org/


## Installation

### 1.  Clone Repository CLA repository
```
git clone https://github.com/cchadwick75/cla_python
```

### 2.  Activate Virtual Environment

        Navigate to cla_python directory and run the following command

        ```source venv/bin/activate```

### 3.  Install requirements.txt while inside (venv)
        b.  ```pip3 install -r requirements.txt```

### Installation Complete

## How To Use Each Argument
It should be noted that each argument should only be run individually.

### 1.  Location shows the current location of the ISS

In your terminal window navigate to the directory you cloned the project and run the command below.  
```
python pycommand.py --loc
```


### 2.  Pass display next dates, times of ISS coordinates pass over.

This argument takes parameters of Latitude and Longitude, enter the Latitude first always.  
This Latitude and Longitude in this snippit are just examples, use your own Latitude and Longitude. 

```
python pycommand.py --pass -22.9465 -85.6556
```

### 3.  People displays count of people in space, spacecraft, and names.

In your terminal window navigate to the directory you cloned the project and run the command below.
```
python pycommand.py --people
```


## Readme Concluded.
