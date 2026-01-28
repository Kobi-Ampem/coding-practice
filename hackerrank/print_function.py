"""
Platform: Hackerrank
Language: Python
Subdomain: Introduction
Problem: Print Function
"""

#from a given integer n, print without any string methods or spaces, 123...n, where n represents the consecutive values in between 

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")

#The end parameter tells the print() function what to put after whatever it is priinting. eg end="," will put comma after eacch item it prints.
