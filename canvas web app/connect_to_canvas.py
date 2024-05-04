import requests
import json
from key import key

headers = {'Authorization': f"Bearer {key}" }
# params = {'enrollment_state' : 'active'}
params1 = {'bucket' : 'unsubmitted'}
# params2 = {'bucket' : 'unsubmitted'}

# response = requests.get("https://canvas.instructure.com/api/v1/courses", headers=headers, params=params)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    with open("dump.json", "w") as file:
        file.write(text)

# response = requests.get("https://canvas.instructure.com/api/v1/courses/36890000000050914/assignments", headers=headers, params=params1)
# jprint(response.json())
response2 = requests.get("https://canvas.instructure.com/api/v1/courses/36890000000050914/assignments", headers=headers)
jprint(response2.json())