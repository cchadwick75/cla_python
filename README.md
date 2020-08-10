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

### 1.  --iloc

In your terminal window navigate to the directory you cloned the project and run the command below.  
```
python pycommand.py --loc
```
This will show you the current location of the ISS

### 2.  --pass

This argument takes parameters of Latitude and Longitude, enter the Latitude first always.  
This Latitude and Longitude in this snippit are just examples, use your own Latitude and Longitude. 

```
python pycommand.py --pass -22.9465 -85.6556
```
This will display dates and times in the near future that the ISS will pass over the coordinates entered

### 3.  --people
In your terminal window navigate to the directory you cloned the project and run the command below.  
```
python pycommand.py --people
```
This displays how many people are currently in space, the spacecraft, and names.

## Readme Concluded.
