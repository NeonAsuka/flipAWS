# coding: utf-8

# In[19]:


import json
import csv
import os

# Some hints for writing csv2sdf


# In[8]:


# Learn how to read content from csv file

with open('/Users/Asuka/Downloads/00/in.csv') as csv_file:
    print("Success!\n")
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row[0])
            print(row[1])
            print(row[2])
            line_count += 1
        else:
            print(row[0])
            print(row[1])
            print(row[2])
            line_count += 1
    print("The end\n")
    print(line_count)


# In[18]:


# Learn how to write content to json object
final_list = []

for i in range(4):
    fields = {}
    tmp_dic = {}
    fields['marketplace_id'] = str(i)
    fields['ASIN'] = 'ASIN'+str(i)
    fields['SKU'] = 'SKU'+str(i)
    tmp_dic['type']="add"
    tmp_dic['id']='123'
    tmp_dic['fields']=fields
    final_list.append(tmp_dic)
    
json_string = json.dumps(final_list, indent=3)
json_out = json.dumps(final_list)
print(json_string)

with open('/Users/Asuka/Downloads/00/out.json', 'w') as outfile:
    json.dump(json_out, outfile)

print("The End")
   


# In[22]:


# learn how to write system command: run aws cli and wait
os.system("echo 'Start'")
os.system('sleep 5')
os.system("echo 'Wait'")


# In[ ]:


# run: sh test.sh

#!/bin/bash
echo 'Start'
sleep 5
echo 'Wait'
