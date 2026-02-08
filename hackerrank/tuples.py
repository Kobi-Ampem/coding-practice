"""
Platform: Hackerrank
Language: pytho
Subdomain: Basic Data types
Problem: Tuples

"""


if __name__ == '__main__':
    # Read the number of elements
    n = int(raw_input())
    
    # Read the space-separated integers, split them into a list,
    # and convert each element to an integer
    integer_list = map(int, raw_input().split())
    
    # Create a tuple from the list
    t = tuple(integer_list)
    
    # Print the result of hash(t)
    print hash(t)
    
    
    
# WORKAROUND: Python 3 hash randomization causes test failures; using Python 2 for deterministic output: I had to use python2 since python3 use hash randomization for hashing values, making the hash value inconsistent