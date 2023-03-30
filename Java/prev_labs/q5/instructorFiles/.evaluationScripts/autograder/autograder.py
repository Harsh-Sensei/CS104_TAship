# Read the log file and parse each line. 
# You would have to use BufferedReader, String, and StringTokenizer (from the java library) as part of this process.
# Insert the entries which you have read into an appropriate data structure, 
# from the existing collections framework. While inserting, ensure that duplicates are not stored 
# (hint: use something which implements the Set interface or its extension).
# print after removing duplicates on stdout in same format as given in log.txt
 


import os
import json



overall = {
    "data": []
}

data = []


#------------------------------test case 1---------------------------
msg = "Correct output."
total = 1
result = {
      "testid": "1",
      "status": "undetermined",
      "score": 0,
      "maximum marks" : 1,
      "message": ""
    }

os.system("javac Parse3.java")
os.system("java Parse3 log.txt > output.txt")



file1 = open('ans.txt', 'r')
Lines1 = file1.readlines()
file2 = open('output.txt', 'r')
Lines2 = file2.readlines()

present = 0



# Lines1.sort()
# Lines2.sort()



if len(Lines1) < len(Lines2) :
    total = 0
    msg = "Wrong output, extra lines '" + Lines2[len(Lines2) - 1].strip() +"' is extra or not in a correct place"
elif len(Lines1) > len(Lines2) :
    total = 0
    msg = "Wrong output, Some lines are missing'"
else :
    for i in range(len(Lines1)) :
        if Lines1[i].strip() != Lines2[i].strip() :
            total = 0
            msg = "Wrong output, Expected statment : '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
            break

if(total != 1) :
    result["status"] = "fail"  
else:
    result["status"] = "success"
result["testid"] = 1
result["score"] = total
result["message"] = msg

data.append(result)


overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)
