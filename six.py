"""A simple CLI to get a Hacker News profile"""

import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--profile')
args = parser.parse_args()

res = requests.get(f'http://hn.algolia.com/api/v1/users/{args.profile}', data=None)
res_json = json.dumps(res.json(), indent=2)
print(res_json)
