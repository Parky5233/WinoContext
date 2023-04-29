import json

with open("responses/consist_resp_2.json","r") as file1:
    resp_0 = json.loads(file1.read())

with open("responses/consist_resp_3.json","r") as file2:
    resp_1 = json.loads(file2.read())

keys = list(resp_0.keys())

count = 0

for i in range(0,len(keys)-1,2):
    if (resp_0[keys[i]].replace(".","") in resp_0[keys[i+1]].replace(".","")) or (resp_0[keys[i+1]].replace(".","")  in resp_0[keys[i]].replace(".","")) :
        count += 1


print("Consistency of Resp 2 = "+str(count/(len(keys)/2)))

keys = list(resp_1.keys())

count = 0
for i in range(0,len(keys)-1,2):
    if (resp_1[keys[i]].replace(".","") in resp_1[keys[i+1]].replace(".","")) or (resp_1[keys[i+1]].replace(".","")  in resp_1[keys[i]].replace(".","")) :
        count += 1

print("Consistency of Resp 3 = "+str(count/(len(keys)/2)))