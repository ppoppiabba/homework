import re

try:
    fhand = open("mbox.txt")
except:
    print("파일을 열 수 없습니다.")
    exit()

count = 0
total_revision_numbers = 0

for line in fhand:
    line = line.rstrip()
    match = re.search("^New Revision: (\d+)", line)
    if match:
        count += 1
        revision_number = int(match.group(1))
        total_revision_numbers += revision_number

fhand.close()

if count > 0:
    average_revision = total_revision_numbers / count
    print(f"Total {count} lines are matched")
    print(f"Average: {average_revision:.4f}")
else:
    print("일치하는 라인이 없습니다.")
