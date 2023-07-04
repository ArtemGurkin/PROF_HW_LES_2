from pprint import pprint
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# print(contacts_list)
# pprint(contacts_list)

new_list = []
new_list.append(contacts_list[0])
for i in range(1, len(contacts_list)):
    stroka = " ".join(contacts_list[i][0:3]).split(" ")[0:3]
    new_list.append(stroka + contacts_list[i][3:])

# pprint(new_list)
# print(new_list)
upd_list = []
dictionary = {}
upd_list.append(contacts_list[0])
for i in range(1, len(new_list)):
    stroka = new_list[i][0] + " " + new_list[i][1]
    if stroka not in dictionary:
        dictionary[stroka] = new_list[i]
    else:
        lst = []
        for j in range(len(dictionary[stroka])):
            #print(new_list[i])
            if dictionary[stroka][j] == "":
                lst.append(new_list[i][j])
            elif new_list[i][j] == "":
                lst.append(dictionary[stroka][j])
            else:
                lst.append(dictionary[stroka][j])
        dictionary[stroka] = lst
upd_list = []
for i in dictionary:
    upd_list.append(dictionary[i])




for i in range(1, len(upd_list)):
    upd_list[i] = upd_list[i][:-1]
    sub_1 = re.sub(r'\D', '', upd_list[i][5])
    match = re.match(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})(\d{1,4})?$', sub_1)
    if match:
        if match.group(6):
            upd_list[i][
                5] = f'+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)} доб. {match.group(6)}'
        else:

            upd_list[i][5] = f'+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}'
    upd_list[i] = [';'.join(upd_list[i])]
#pprint(upd_list)

with open("phonebook.csv", "w", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(upd_list)
