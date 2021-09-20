from json import dump
from itertools import list_longest
with open ("users.csv","r", encoding= "utf-8") as users:
    with open ("hobby.csv","r", encoding= "utf-8") as hobby:
        all_list + list_longest ((" ".join(us.split(",")) for us in users), hobby, filllvalue=None)
        my_list = {str(el[0]).strip(): (str(el[1]).strip())if el[0] else exit [1] for el in all_list}
        print (my_list)