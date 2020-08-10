import requests
import sys
import json
import datetime

argument = sys.argv

def convert_time(time_var):
    '''
    :param time_var:
    :return date and time formatted from Unix :
    '''
    return datetime.datetime.fromtimestamp(int(time_var)).strftime('%Y-%m-%d %H:%M:%S')

def get_names(people):
    '''
    :param people:
    :return a string of comma seperated names:
    '''
    return ', '.join([x['name'] for x in people if 'name' in x])

def get_craft(craft):
    '''
    :param craft:
    :return a string of crafts without duplicates:
    '''
    return  ', '.join(set([x['craft'] for x in craft if 'craft' in x]))

if '--loc' in argument:
    response = requests.get('http://api.open-notify.org/iss-now.json')

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        print(f"The ISS current location at {convert_time(response_dict['timestamp'])} is "
              f"[{response_dict['iss_position']['latitude']}, {response_dict['iss_position']['longitude']}]")
    else:
        print(f"Bad response from API, status code:{response.status_code} ")

elif '--pass' in argument:

    latitude = argument[2]
    longitude = argument[3]

    response = requests.get(f'http://api.open-notify.org/iss-pass.json?lat={latitude}&lon={longitude}')
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        if response_dict['message'] == 'success':
            for x in response_dict['response']:
                print(f"The ISS will be overhead {latitude}, {longitude} at {convert_time(x['risetime'])} for {x['duration']} seconds")
        else:
            print(f"error returned from ISS, see message ->:{response_dict['message']} ")
    else:
        print(f"Bad response from API, status code:{response.status_code} ")

elif '--people' in argument:
    response = requests.get(f'http://api.open-notify.org/astros.json')

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        if response_dict['message'] == 'success':
            print(f"There are {response_dict['number']} people aboard the {get_craft(response_dict['people'])}.  They are {get_names(response_dict['people'])}.")
        else:
            print(f"error returned from ISS, see message ->:{response_dict['message']} ")
    else:
        print(f"Bad response from API, status code:{response.status_code} ")
else:
    print(f"Command {argument[1]}:  Not recognized, recheck spelling, only lower case excepted.")









