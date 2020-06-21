# AUTHOR: Griffin Wong
# DATE: 06/20/2020
# PURPOSE: Enumerating Gene Orders

"""
Rearrangements Power Large-Scale Genomic Changes

Point mutations can create changes in populations of 
organisms from the same species, but they lack the 
power to create and differentiate entire species. 
This more arduous work is left to larger mutations 
called genome rearrangements, which move around huge 
blocks of DNA. Rearrangements cause major genomic change,
and most rearrangements are fatal or seriously damaging 
to the mutated cell and its descendants (many cancers 
derive from rearrangements). For this reason, rearrangements 
that come to influence the genome of an entire species are 
very rare.

Because rearrangements that affect species evolution occur 
infrequently, two closely related species will have very similar 
genomes. Thus, to simplify comparison of two such genomes, 
researchers first identify similar intervals of DNA from the 
species, called synteny blocks; over time, rearrangements have
created these synteny blocks and heaved them around across
the two genomes (often separating blocks onto different 
chromosomes, see Figure 1.).

A pair of synteny blocks from two different species 
are not strictly identical (they are separated by the action 
of point mutations or very small rearrangements), but for the sake
of studying large-scale rearrangements, we consider them to be 
equivalent. As a result, we can label each synteny block with a 
positive integer; when comparing two species' genomes/chromosomes,
we then only need to specify the order of its numbered synteny blocks.

"""

"""
Problem

A permutation of length n is an ordering of the positive 
integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, 
followed by a list of all such permutations (in any order)
"""

"""
Sample Dataset: 3

Sample Output:

6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

import itertools
list_ = []

# Read file data into the script
def read_data(filename: str):
    with open(filename, 'r') as fp:
        string = fp.readline().replace('\n', '')
    return (string)

# Calculate factorial
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

# Create list of permutations
def perm_list(n):
    if n == 0:
        return list_
    else:
        list_.append(n)
        n -= 1
        return perm_list(n)

# Print output and unpackage tuples
def print_output(perms_list, n):
    list_two = [j for j in perms_list]
    for a, *b in list_two:
        print(a, ' '.join(map(str, b)))

# Call all functions
if __name__ == '__main__':
    filename='rosalind_perm.txt'
    n = read_data(filename)
    permutation_object = itertools.permutations(perm_list(int(n)))
    perms_list = (list(permutation_object))
    print(factorial(int(n)))
    print_output(perms_list, n)