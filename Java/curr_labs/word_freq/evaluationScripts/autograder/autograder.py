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
      "status": "success",
      "score": 0,
      "maximum marks" : 1,
      "message": ""
    }


# file1 = open('solution.txt', 'r')
# Lines1 = file1.readlines()
os.system("javac Solution.java")
os.system("java Solution")
file2 = open('output.txt', 'r')
Lines2 = file2.readlines()

present = 0

Lines1 = ["Comparable<String>\n" , "Serializable\n" , "CharSequence\n"]
Lines1.sort()
Lines2.sort()
# print(" expected : ")
# print(Lines1)
# print(" your : ")
# print(Lines2)
if Lines1 == Lines2:
    msg = "Correct "
    total=1

else:
    msg = "Incorrect"
    total = 0


# if len(Lines1) < len(Lines2) :
#     total = 0
#     msg = "Wrong output, You have written extra interface '" + Lines2[len(Lines2) - 1].strip() +"' is extra or not in a correct place"
# elif len(Lines1) > len(Lines2) :
#     total = 0
#     msg = "Wrong output, Some interfaces are missing'"
# else :
#     for i in range(len(Lines1)) :
#         if Lines1[i].strip() != Lines2[i].strip() :
#             total = 0
#             msg = "Wrong output, Expected statment : '" + Lines1[i].strip() + "' Your output : '" + Lines2[i].strip() + "'"
#             break

if(total != 1) :
    result["status"] = "fail"  
result["testid"] = 1
result["score"] = total
result["message"] = msg

data.append(result)






overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)