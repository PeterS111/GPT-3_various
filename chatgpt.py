## This script allows to run ChatGPT from terminal
## You have to install openai first using "pip install openai"
##
## author: PeterS  v 0.1

import os
import openai
import datetime

openai.api_key = "YOUR_KEY_HERE"


def run_gpt3_5(msg_list):

    response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       temperature=1,
       messages=msg_list
    )
   
    answer = response["choices"][0]["message"]["content"]
    return answer


def write_list_to_file(in_list):

    index = 1
    out_file = "GPT-3_5_"      
    out_file_name = out_file + str(index) + ".txt"

    while out_file_name in os.listdir():
        index +=1
        out_file_name = out_file + str(index) + ".txt"
        if out_file_name not in os.listdir():
            break

    f= open(out_file_name, "a", encoding = "utf-8")
    for i in in_list:       
        write_str = i["role"] + " :  "  + i["content"] + "\n\n"
        f.write(write_str)
    f.close() 
    
msg_list = [{"role": "system", "content": "You are a helpful assistant."}]    

print("\nEnter your prompt. Enter 'q' to quit and write the dialogue to file.\n")

while True:
    user_talk = input(">>>") 
        
    if user_talk == "q":
        break
    
    user_dict = {"role": "user", "content": user_talk}    
    msg_list.append(user_dict)
    system_talk = run_gpt3_5(msg_list)
    print("\n" + system_talk + "\n")
    system_dict = {"role": "assistant", "content": system_talk}
    msg_list.append(system_dict)
 
write_list_to_file(msg_list) 















