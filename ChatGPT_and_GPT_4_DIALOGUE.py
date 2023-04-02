# You have to run "pip install --upgrade openai" if using GPT-4 for the first time. 

# author: PeterS

# version: 02/04/2023


import os
import json
import openai


openai.api_key = "YOUR_KEY_HERE"

setup_str = "You are a helpful assistant."

msg_list = [{"role": "system", "content": setup_str}]


## This will work only if you have access to GPT-4 through APIs.
## Otherwise, use "gpt-3.5-turbo"

model = "gpt-4"
# model = "gpt-3.5-turbo"

started = False

##################################

out_file_name = ""
index = 1
out_file = "GPT-4_"      
out_file_name = out_file + str(index) + ".txt"

while out_file_name in os.listdir():
    index +=1
    out_file_name = out_file + str(index) + ".txt"
        
################################

def run_gpt(msg_list, model):

    response = openai.ChatCompletion.create(
       model=model,
       temperature=0,
       messages=msg_list
    )
   
    answer = response["choices"][0]["message"]["content"]
    return answer



def write_list_to_file(in_list, out_file_name):

    f= open(out_file_name, "a", encoding = "utf-8")
    for i in in_list:       
        write_str = i["role"] + " :  "  + i["content"] + "\n\n"
        f.write(write_str)
    f.close()
    
    
        
print("\nEnter your prompt. Enter 'q' to quit.\n")

while True:
    user_talk = input(">>>")        
    if user_talk == "q":
        break
    
    user_dict = {"role": "user", "content": user_talk}    
    msg_list.append(user_dict)
    system_talk = run_gpt(msg_list, model)
    print("USER: " + user_talk + "\n\n" + "GPT-4: " + system_talk)
    system_dict = {"role": "assistant", "content": system_talk}
    msg_list.append(system_dict)
    
    if not started: 
        write_list_to_file(msg_list, out_file_name) 
        started = True        
    else:    
        write_list_to_file(msg_list[-2:], out_file_name)