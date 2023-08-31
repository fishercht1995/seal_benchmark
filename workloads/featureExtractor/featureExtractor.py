
import time
from datetime import datetime
import re
import sys
def f(n):

    start = round(time.time(),6)

    data = open("/data/shakespeare_dataset.txt","r").read()
    cleanup_re = re.compile('[a-z]+')
    result = cleanup_re.findall(data)
    print(result)
    end = round(time.time(),6)
    #print("{} {}, {}, {}, {}, {}".format(id_n, n, pred, start, end, end-start))
    #print(result)
if __name__ == "__main__":
    event = sys.argv[1]
    f(event)