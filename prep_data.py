import os
import json
import itertools


with open("data/winowhy.txt") as f:
    data = f.read()
file = json.loads(data)

con2_dataset = []
con1_dataset = []
con0_dataset = []

con3_masked_dataset = []
con2_masked_dataset = []
con1_masked_dataset = []
con0_masked_dataset = []

robust_dataset_2 = []
robust_dataset_3 = []

winowhy = []
answers = []

options = []

reasons_final = {}
prons = {}
options_final = {}

answers_final = {}

#Code below exports the winograd sentences and reasons
for text in file:
    reasons = []
    if 'A' in text['correctAnswer'].upper():
        answers.append(text['answers'][0])
    else:
        answers.append(text['answers'][1])
    options.append([text['answers'][0],text['answers'][1]])
    temp_reas = []
    for reas in text['reasons']:
        if reas[3].__eq__('Valid') and float(reas[2]) == 1.0 and reas[1].__eq__('human') and not reas[1].__eq__('reverse'): #if reason is valid with high rating
            reasons.append(reas)

    if len(reasons)==3:
        wino = text['text']['txt1'] + ' ' + text['text']['pron'] + ' ' + text['text']['txt2']
        answers_final["In the following sentence: \'"+wino+"\'"] = answers[len(answers)-1]
        prons[wino] = text['text']['pron']
        options_final[wino] = [text['answers'][0],text['answers'][1]]
        reasons_final[wino] = []
        for reas in reasons:
            reasons_final[wino].append(reas[0].replace(".","").lower())
    else:
        print("\'"+text['text']['txt1'] + ' ' + text['text']['pron'] + ' ' + text['text']['txt2']+"\' was excluded as it lacked a minimum of 3 context prompts")
print("Number of winogrand samples used = "+str(len(winowhy)))

#code below saves partitions of WinoWhy
# with open("data/reasons.json","w") as file1:
#     file1.write(json.dumps(reasons_final))
#
# with open("data/prons.json","w") as file2:
#     file2.write(json.dumps(prons))
#
# with open("data/options.json","w") as file3:
#     file3.write(json.dumps(options_final))

# with open("data/answers.json","w") as file4:
#     file4.write(json.dumps(answers_final))

#loading in WinoWhy data to generate WinoContext
with open("data/reasons.json", 'r') as j:
    dataset = json.loads(j.read())

with open("data/prons.json","r") as p:
    prons = json.loads(p.read())

with open("data/options.json","r") as o:
    options = json.loads(o.read())

#below is old code for generating prompts without masking
# for wino in dataset.keys():
#     cont_prompts = list(itertools.combinations(dataset[wino],r=2))
#     con0_dataset.append("In the following sentence: \'"+wino+"\' Which does \'"+prons[wino]+"\' more likely refer to, \'"+options[wino][0]+"\' or \'"+options[wino][1]+"\'?")
#     for reas in dataset[wino]:
#         con1_dataset.append("Given "+reas+". In the following sentence: \'"+wino+"\' Which does \'"+prons[wino]+"\' more likely refer to, \'"+options[wino][0]+"\' or \'"+options[wino][1]+"\'?")
#     for reas_pair in cont_prompts:
#         con2_dataset.append("Given "+reas_pair[0]+" and "+reas_pair[1]+". In the following sentence: \'"+wino+"\' Which does \'"+prons[wino]+"\' more likely refer to, \'"+options[wino][0]+"\' or \'"+options[wino][1]+"\'?")

#below saves the old non-masked WinoContext
# with open("data/2_context.json","w") as file4:
#     file4.write(json.dumps(con2_dataset))
#     print("2_context.json saved")
# with open("data/1_context.json","w") as file5:
#     file5.write(json.dumps(con1_dataset))
#     print("1_context.json saved")
# with open("data/0_context.json","w") as file6:
#     file6.write(json.dumps(con0_dataset))
#     print("0_context.json saved")


#below generates WinoContext
# for wino in dataset.keys():
#     cont_prompts = list(itertools.combinations(dataset[wino],r=2))
#     con0_masked_dataset.append("In the following sentence: \'"+wino+"\' Between \'"+options[wino][0]+"\' and \'"+options[wino][1]+"\', the term \'"+prons[wino]+"\' more likely refers to <MASKED>")
#     con3_masked_dataset.append("Given "+dataset[wino][0]+", "+dataset[wino][1]+", and "+dataset[wino][2]+". In the following sentence: \'"+wino+"\' Between \'"+options[wino][0]+"\' and \'"+options[wino][1]+"\', the term \'"+prons[wino]+"\' more likely refers to <MASKED>")
#     for reas in dataset[wino]:
#         con1_masked_dataset.append("Given "+reas+". In the following sentence: \'"+wino+"\' Between \'"+options[wino][0]+"\' and \'"+options[wino][1]+"\', the term \'"+prons[wino]+"\' more likely refers to <MASKED>")
#     for reas_pair in cont_prompts:
#         con2_masked_dataset.append("Given "+reas_pair[0]+" and "+reas_pair[1]+". In the following sentence: \'"+wino+"\' Between \'"+options[wino][0]+"\' and \'"+options[wino][1]+"\', the term \'"+prons[wino]+"\' more likely refers to <MASKED>")
#

#below generates the robustency-checking data
for wino in dataset.keys():
    cont_prompts = list(itertools.combinations(dataset[wino],r=2))
    cont_prompts_3 = list(itertools.combinations(dataset[wino],r=3))

    for reas_pair in cont_prompts:
        robust_dataset_2.append("Given "+reas_pair[0]+" and "+reas_pair[1]+". In the following sentence: \'"+wino+"\' Between \'"+options[wino][0]+"\' and \'"+options[wino][1]+"\', the term \'"+prons[wino]+"\' more likely refers to <MASKED>")
        robust_dataset_2.append("Given " + reas_pair[1] + " and " + reas_pair[0] + ". In the following sentence: \'" + wino + "\' Between \'" + options[wino][0] + "\' and \'" +options[wino][1] + "\', the term \'" + prons[wino] + "\' more likely refers to <MASKED>")
    for reas_triple in cont_prompts_3:
        robust_dataset_3.append("Given " + reas_triple[0] + ", " + reas_triple[1] + ", and " + reas_triple[2] + ". In the following sentence: \'" + wino + "\' Between \'" + options[wino][0] + "\' and \'" +options[wino][1] + "\', the term \'" + prons[wino] + "\' more likely refers to <MASKED>")
        robust_dataset_3.append("Given " + reas_triple[2] + ", " + reas_triple[0] + ", and " + reas_triple[1] + ". In the following sentence: \'" + wino + "\' Between \'" + options[wino][0] + "\' and \'" +options[wino][1] + "\', the term \'" + prons[wino] + "\' more likely refers to <MASKED>")

#the code below saves the data for prompting GPT for robustness
with open("data/rob_masked_2.json","w") as file420:
    file420.write(json.dumps(robust_dataset_2))

with open("data/rob_masked_3.json","w") as file360:
    file360.write(json.dumps(robust_dataset_3))

print("robustness files saved")

#the code below saves WinoWhy
# with open("data/2_context_masked.json","w") as file4:
#     file4.write(json.dumps(con2_masked_dataset))
#     print("2_context_masked.json saved")
# with open("data/1_context_masked.json","w") as file5:
#     file5.write(json.dumps(con1_masked_dataset))
#     print("1_context_masked.json saved")
# with open("data/0_context_masked.json","w") as file6:
#     file6.write(json.dumps(con0_masked_dataset))
#     print("0_context_masked.json saved")
# with open("data/3_context_masked_.json","w") as file7:
#     file7.write(json.dumps(con3_masked_dataset))
#     print("3_context_masked.json saved")