import re
from colorama import Fore, init
import requests

# inizialize colorama after every execution
init(autoreset=True)

web_site = "https://www.vulnhub.com"

result = requests.get(web_site)
content = result.text

# print(content)

pattern = r"/entry/[\w-]*"

machine_repeated = re.findall(pattern, content)

# print(machine_repeated)

without_duplicates = list(set(machine_repeated))

# print(without_duplicates)

final_machine = []

for i in without_duplicates:
    name_machine = i.replace("/entry/", "")
    final_machine.append(name_machine)

# print(final_machine) 

for i in final_machine:
    print(i)


########
    
print("---------------------------------------")
    
# last machine in the page
machine_noob = "noob-1"
exist_noob = False

for a in final_machine:
    if a == machine_noob:
        exist_noob = True
        break


color_green = Fore.GREEN
color_yellow = Fore.YELLOW


if exist_noob == True:
    print("answer: " + color_yellow + "There isn't new machine")
else:
    print("answer: " + color_green + "New Machine!")

