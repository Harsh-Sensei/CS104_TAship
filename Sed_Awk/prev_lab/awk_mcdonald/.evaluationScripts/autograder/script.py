import os
import json

overall = {
    "data": []
}

data = [];

os.system("rm out.txt")
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

os.system("./mcdonald.awk < input1.txt > out.txt")
file1 = open('output1.txt', 'r')
Lines1 = file1.readlines()
file2 = open('out.txt', 'r')
Lines2 = file2.readlines()

if len(Lines1) < len(Lines2) :
    total = 0
    msg = "Wrong output, Your output genrates some extra lines. '" + Lines2[len(Lines2) - 1].strip() +"' is extra or not in a correct place"
elif len(Lines1) > len(Lines2) :
    total = 0
    msg = "Wrong output, Some statments are missing. '" + Lines1[len(Lines2)].strip() +"' is missing or not in a correct place"
else :
    for i in range(len(Lines1)) :
        if Lines1[i].strip() != Lines2[i].strip() :
            total = 0
            msg = "Wrong output, Expected statment : '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
            break

if(total != 1) :
    result["status"] = "fail"    
result["testid"] = 1
result["score"] = total
result["message"] = msg

data.append(result)
os.system("rm out.txt")

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)