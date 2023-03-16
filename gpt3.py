## This script allows to run GPT-3 from terminal
## You have to install openai first using "pip install openai"
##
## author: PeterS  v 0.1

import os
import openai
import datetime

openai.api_key = "YOUR_KEY_HERE"

def run_gpt3(in_str):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt = in_str,
      max_tokens=1500,
      temperature=1,
    
    )
    
    answer = response["choices"][0]["text"].strip() 
    return answer
    
    
print("\nEnter your prompt. Enter 'q' to quit and write the dialogue to file.\n")

while True:
    user_talk = input(">>>") 
        
    if user_talk == "q":
        break

    system_talk = run_gpt3(user_talk)
    print("\n" + system_talk + "\n")
    
    out_file_name = "GPT-3_SIMPLE.txt"
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    to_write = "\n\n" + str(current_time) + "\n\n" + user_talk + "\n\n" + system_talk

    f= open(out_file_name, "a", encoding = "utf-8")
    f.write(to_write)
    f.close()
    

        
