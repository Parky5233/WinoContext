import json

with open("responses/resp_0_masked.json","r") as file1:
    resp_0 = json.loads(file1.read())

with open("responses/resp_1_masked.json","r") as file2:
    resp_1= json.loads(file2.read())

with open("responses/resp_2_masked.json","r") as file3:
    resp_2 = json.loads(file3.read())

with open("responses/resp_3_masked.json","r") as file5:
    resp_3 = json.loads(file5.read())

with open("responses/resp_0_masked_repro.json","r") as file6:
    resp_0_repro = json.loads(file6.read())

with open("responses/resp_1_masked_repro.json","r") as file7:
    resp_1_repro= json.loads(file7.read())

with open("responses/resp_2_masked_repro.json","r") as file8:
    resp_2_repro = json.loads(file8.read())

with open("responses/resp_3_masked_repro.json","r") as file9:
    resp_3_repro = json.loads(file9.read())

resp_0_repacc = 0
for key in resp_0:
    if resp_0[key] in resp_0_repro[key] or resp_0_repro[key] in resp_0[key]:
        resp_0_repacc += 1
    else:
        print(resp_0[key]+" - "+resp_0_repro[key])
print("Consistency for 0-Context = "+str(resp_0_repacc/len(list(resp_0.keys()))))

resp_1_repacc = 0
for key in resp_1:
    if resp_1[key] in resp_1_repro[key] or resp_1_repro[key] in resp_1[key]:
        resp_1_repacc += 1
    else:
        print(resp_1[key]+" - "+resp_1_repro[key])
print("Consistency for 1-Context = "+str(resp_1_repacc/len(list(resp_1.keys()))))

resp_2_repacc = 0
for key in resp_2:
    if resp_2[key] in resp_2_repro[key] or resp_2_repro[key] in resp_2[key]:
        resp_2_repacc += 1
    else:
        print(resp_2[key]+" - "+resp_2_repro[key])
print("Consistency for 2-Context = "+str(resp_2_repacc/len(list(resp_2.keys()))))

resp_3_repacc = 0
for key in resp_3:
    if resp_3[key] in resp_3_repro[key] or resp_3_repro[key] in resp_3[key]:
        resp_3_repacc += 1
    else:
        print(resp_3[key]+" - "+resp_3_repro[key])
print("Consistency for 3-Context = "+str(resp_3_repacc/len(list(resp_3.keys()))))