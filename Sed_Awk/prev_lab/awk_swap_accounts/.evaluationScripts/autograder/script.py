# -*- coding: utf-8 -*-
"""publicAwk1Script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kJwgdYehqEEVUhgqZMuasvC33-GDL7k7
"""

import os
import json

overall = {
    "data": []
}

data = [];

os.system("rm TestCase1/out.txt")
#------------------------------test case 1---------------------------
msg = "Correct output."
total = 1
result = {
      "testid": "1",
      "status": "success",
      "score": 0,
      "maximum marks" : 1,
      "message": ""
    }

os.system("./swap_accounts.awk TestCase1/sample.txt > TestCase1/out.txt")
file1 = open('TestCase1/output.txt', 'r')
Lines1 = file1.readlines()
file2 = open('TestCase1/out.txt', 'r')
Lines2 = file2.readlines()

if len(Lines1) < len(Lines2) :
    total = 0
    msg = "Wrong output, Your output genrates some extra lines"
elif len(Lines1) > len(Lines2) :
    total = 0
    msg = "Wrong output, Some statments are missing"
else :
    for i in range(len(Lines1)) :
        if Lines1[i].strip() != Lines2[i].strip() :
            total = 0
            msg = "Wrong output, Expected statment : '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
            break
    
result["testid"] = 1
result["score"] = total
result["message"] = msg

data.append(result)
os.system("rm TestCase1/out.txt")






overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)
