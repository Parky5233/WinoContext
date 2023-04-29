import json

with open("responses/resp_0_masked.json","r") as file1:
    resp_0 = json.loads(file1.read())

with open("responses/resp_1_masked.json","r") as file2:
    resp_1= json.loads(file2.read())

with open("responses/resp_2_masked.json","r") as file3:
    resp_2 = json.loads(file3.read())

with open("responses/resp_3_masked.json","r") as file5:
    resp_3 = json.loads(file5.read())

with open("data/answers.json","r") as file4:
    ans = json.loads(file4.read())

resp_2_acc = 0
resp_1_acc = 0
resp_0_acc = 0

resp_0_ans = {}
resp_1_ans = {}
resp_2_ans = {}
resp_3_ans = {}

def get_acc(responses,resp_dict,context):
    acc = 0
    for query in responses:
        for query_a in ans:
            if (query_a.lower() in query.lower()):
                resp_dict[query_a] = [ans[query_a].lower(), responses[query].lower().replace("\n", "")]
                if (ans[query_a].lower() in responses[query].lower()):
                    acc += 1
    print(str(acc) + "/" + str(len(responses)))
    print("Acc w/ "+str(context)+" Context = " + str(acc / len(responses)))

get_acc(resp_0,resp_0_ans,0)
get_acc(resp_1,resp_1_ans,1)
get_acc(resp_2,resp_2_ans,2)
get_acc(resp_3,resp_3_ans,3)

# for query in resp_0:
#     for query_a in ans:
#         if (query_a.lower() in query.lower()):
#             resp_0_ans[query_a] = [ans[query_a].lower(),resp_0[query].lower().replace("\n","")]
#             if (ans[query_a].lower() in resp_0[query].lower()):
#                 resp_0_acc += 1
#
# for query in resp_1:#for prompt with 1 piece of context
#     for query_a in ans:#for wino question
#         if (query_a.lower() in query.lower()):#if the prompt contains the right wino question and answer is correct
#             resp_1_ans[query_a] = [ans[query_a].lower(),resp_1[query].lower()]
#             if (ans[query_a].lower() in resp_1[query].lower()):
#                 resp_1_acc += 1
#
# for query in resp_2:#for prompt with 2 pieces of context
#     for query_a in ans:#for wino question
#         if (query_a.lower() in query.lower()):#if prompt contains the right wino question and answer is correct
#             resp_2_ans[query_a] = [ans[query_a].lower(), resp_2[query].lower()]
#             if (ans[query_a].lower() in resp_2[query].lower()):
#                 resp_2_acc +=1
#
# print(str(resp_0_acc)+"/"+str(len(resp_0)))
# print("Acc w/ 0 Context = "+str(resp_0_acc/len(resp_0)))
# print(str(resp_1_acc)+"/"+str(len(resp_1)))
# print("Acc w/ 1 Piece of Context = "+str(resp_1_acc/len(resp_1)))
# print(str(resp_2_acc)+"/"+str(len(resp_2)))
# print("Acc w/ 2 Pieces of Context = "+str(resp_2_acc/len(resp_2)))

for key in resp_2_ans:
    if not resp_0_ans[key] == resp_1_ans[key] == resp_2_ans[key] == resp_3_ans[key]:
        print(key+" 0 - "+resp_0_ans[key][0]+" - "+resp_0_ans[key][1])
        print(key+" 1 - "+resp_1_ans[key][0]+" - "+resp_1_ans[key][1])
        print(key+" 2 - "+resp_2_ans[key][0]+" - "+resp_2_ans[key][1])
        print(key+" 3 - "+resp_3_ans[key][0]+" - "+resp_3_ans[key][1])
        print("")