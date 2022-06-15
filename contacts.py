import math
import os
import random
import re
import sys

def add(contacts, name):
    pos = None
    print(name)
    for letter in name:
        if pos is None:
            if letter not in contacts.keys():
                contacts[letter] = {}
            pos = contacts[letter]
        else:
            if letter not in pos.keys():
                pos[letter] = {}
            pos = pos[letter]
        print(contacts)
        print(pos)
        
        if 'count' not in pos.keys():
            pos['count'] = 1
        else:
            pos['count'] += 1

def find_partial(contacts, partial_name):
    found = True
    pos = None
    for letter in partial_name:
        if pos is None:
            if letter not in contacts.keys():
                found = False
                break
            pos = contacts[letter]
        else:
            if letter not in pos.keys():
                found = False
                break
            pos = pos[letter]
    if found:
        return pos['count']
    return 0

def contacts(queries):
    contacts_dict = {}
    finds = []
    for x in range(len(queries)):
        op, name = queries[x][0], queries[x][1]
        if op == 'add':
            add(contacts_dict, name)
        elif op == 'find':
            #print(find_partial(contacts_dict, name))
            finds.append(find_partial(contacts_dict, name))
            print(finds)
    return finds

if __name__ == '__main__':
    file_path = "C:\\Users\\micha\\Documents\\GitHub\\python_sql_programs\\testing.txt"
    fptr = open(file_path, 'w')

    n = int(input().strip())
    queries = []

    for _ in range(n):
        queries.append(input().rstrip().split())
        
    result = contacts(queries)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()