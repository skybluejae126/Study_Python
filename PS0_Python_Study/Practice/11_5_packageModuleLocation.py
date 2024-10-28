# 모듈이나 패키지가 어느 위치에 있는지 확인하는 방법

from travel_11_2 import *

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))