import math
import sys
from os import rename

import pip._vendor.requests
from pip._vendor import requests


r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
