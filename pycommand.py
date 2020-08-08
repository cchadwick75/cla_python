import requests
import sys
import json
import datetime


def convert_time(time_var):
    return datetime.datetime.fromtimestamp(int(time_var)).strftime('%Y-%m-%d %H:%M:%S')
# argument = sys.argv[1:]
# print(argument)

argument = ['-pass', -18.9240, 96.6139]
if argument == '-loc':

    response = requests.get('http://api.open-notify.org/iss-now.json')

    if response.status_code == 200:
        response_dict = json.loads(response.text)
        print(f"The ISS current location at {convert_time(response_dict['timestamp'])} is "
              f"[{response_dict['iss_position']['latitude']}, {response_dict['iss_position']['longitude']}]")

elif '-pass' in argument:
    latitude = argument[1]
    longitude = argument[2]

    response = requests.get(f'http://api.open-notify.org/iss-pass.json?lat={latitude}&lon={longitude}')
    response_dict = json.loads(response.text)
    for future_pass in response_dict['request']:
        if
    print(f"The ISS current location at {convert_time(response_dict['timestamp'])} is "
          f"[{response_dict['iss_position']['latitude']}, {response_dict['iss_position']['longitude']}]")


elif argument == '-people':
    pass








