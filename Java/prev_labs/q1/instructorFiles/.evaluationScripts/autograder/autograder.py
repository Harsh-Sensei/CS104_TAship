#Identify the interfaces implemented by java.lang.String 
#Code in file given as "MyClass.java" Create a new file named as "output.txt" and write your answer in it.
#write each interface in new line 
# Example : 
#A
#B
#C
#D 

#Give a newline after your last interface



# student soltution in output.txt
# expected soltuion in solution.txt

import os
import json



overall = {
    "data": []
}

data = []


#------------------------------test case 1---------------------------
msg = ""
total = 0
result = {
      "testid": "1",
      "status": "failed",
      "score": 0,
      "maximum marks" : 1,
      "message": ""
    }


# file1 = open('solution.txt', 'r')
# Lines1 = file1.readlines()
try:
	os.system("javac Solution.java")
	os.system("java Solution")
	file2 = open('output.txt', 'r')
	Lines2 = file2.readlines()
except Exception as e:
	result["message"] = str(e) 
	data.append(result)
	overall['data'] = data
	print(json.dumps(overall, indent=4))
	with open('../evaluate.json', 'w') as f:
		json.dump(overall,f,indent=4)
	exit()
	


#present = 0

Lines1 = ["Comparable<String>\n" , "Serializable\n" , "CharSequence\n"]
Lines1.sort()
Lines2.sort()
# print(" expected : ")
# print(Lines1)
# print(" your : ")
# print(Lines2)
if Lines1 == Lines2:
    msg = "Correct"
    total=1

else:
    msg = "Incorrect"
    total = 0


if(total == 1) :
    result["status"] = "success"  
result["testid"] = 1
result["score"] = total
result["message"] = msg

data.append(result)

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)
