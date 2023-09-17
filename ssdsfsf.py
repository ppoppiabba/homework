import re
try:
    fhand=open("mbox.txt")
except:
    print("file cannot be opened")
    exit()
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search("^New Revision:",line):
        count=count+1

print("total%d lines are matched" %count)
# print("Average :%d "%)