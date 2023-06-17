
from pprint import pprint 
import csv
import re

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

new_list = []
new_list.append(contacts_list[0])
for i in range(1, len(contacts_list)):
  stroka = contacts_list[i][0].split(';')
  if len(stroka[0].split()) == 3:
    new_list.append(stroka[0].split() + stroka[3:])
  elif len(stroka[0].split()) == 2:
    new_list.append(stroka[0].split() + [stroka[2]] + stroka[3:])
  elif len(stroka[0].split()) == 1:
    if len(stroka[1].split()) == 2:
      new_list.append([stroka[0]] + stroka[1].split() + stroka[3:])
    else:
      new_list.append([stroka[0]] + [stroka[1]] + [stroka[2]] + stroka[3:])
# pprint(new_list)

upd_list = []
upd_list.append(contacts_list[0])
for i in range(1, len(new_list)):
  for g in upd_list:
    if new_list[i][0] in g and new_list[i][1] in g:
      for q in range(len(new_list[i][2:])):
        if new_list[i][q] == "":
          new_list[i][q] = g[q]
      # upd_list[-1] = new_list[i] 
      upd_list[upd_list.index(g)] = new_list[i]
      break
  else:
    upd_list.append(new_list[i])

for i in range(1, len(upd_list)):
  upd_list[i] = upd_list[i][:-1]
  sub_1 = re.sub(r'\D', '', upd_list[i][5])
  match = re.match(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})(\d{1,4})?$', sub_1)
  if match:
    if match.group(6):
      upd_list[i][5] = f'+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)} доб. {match.group(6)}'
    else: 
      upd_list[i][5] = f'+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}'
  upd_list[i] = [';'.join(upd_list[i])]
pprint(upd_list)

with open("phonebook.csv", "w", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(upd_list)

