import openai
import json
import time

token = ''#add your token here

def askGPT(text):
    openai.api_key = token

    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.0,
        max_tokens = 150,
    )
    return response.choices[0].text

#to calculate token cost - https://platform.openai.com/tokenizer

#opening various files
# with open("data/2_context.json","r") as file1:
#     context_2 = json.loads(file1.read())
#
# with open("data/1_context.json","r") as file2:
#     context_1 = json.loads(file2.read())
#
# with open("data/0_context.json","r") as file3:
#     context_0 = json.loads(file3.read())

#loading masked dataset
with open("data/3_context_masked_.json","r") as file1:
    context_masked_3 = json.loads(file1.read())

with open("data/2_context_masked.json","r") as file4:
    context_masked_2 = json.loads(file4.read())

with open("data/1_context_masked.json","r") as file5:
    context_masked_1 = json.loads(file5.read())

with open("data/0_context_masked.json","r") as file6:
    context_masked_0 = json.loads(file6.read())

#loading data we prompt for robustency
with open("data/rob_masked_2.json", "r") as file7:
    robust_masked_2 = json.loads(file7.read())

with open("data/rob_masked_3.json", "r") as file8:
    robust_masked_3 = json.loads(file8.read())

resp_0 = {}
resp_1 = {}
resp_2 = {}
resp_3 = {}
robust_resp_2 = {}
robust_resp_3 = {}

def prompt_dataset(prompts,response_dict,save_file):
    '''
    This code prompts GPT and saves the responses as a dictionary
    with key - value pairs where the key is the prompt and the value
    is the response
    :param prompts: A list of prompts in string format
    :param response_dict: a dictionary for saving responses
    :param save_file: a desired file name for saving response_dict
    :return:
    '''
    for prompt in prompts:
        print(prompt)
        resp = askGPT(prompt)
        print(resp.replace("\n",""))
        print("")
        response_dict[prompt] = resp.replace("\n","")
        time.sleep(7)

    with open(save_file,"w") as file:
        file.write(json.dumps(response_dict))

#the code below prompts GPT-3 for the various amounts of context
# prompt_dataset(context_masked_0,resp_0,"responses/resp_0_masked_repro.json")
prompt_dataset(context_masked_1,resp_1,"responses/resp_1_masked_repro.json")
prompt_dataset(context_masked_2,resp_2,"responses/resp_2_masked_repro.json")
prompt_dataset(context_masked_3,resp_3,"responses/resp_3_masked_repro.json")

#the code below prompts GPT-3 to check for robustness
# prompt_dataset(robust_masked_2,robust_resp_2,"responses/rob_resp_2.json")
# prompt_dataset(robust_masked_3,robust_resp_3,"responses/rob_resp_3.json")

print("Responses saved")