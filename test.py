import sys
import json

def vj_read(manoj):
    del manoj[-1]
    test = dict()
    test['name']=manoj
    return test
content=sys.stdin.read().split('\n')
output=vj_read(content)   
print(output)
data = open("open.json","w")
json.dump(output,data)
data.close


