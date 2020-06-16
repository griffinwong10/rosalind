# Griffin Wong
# 12/09/2019

"""
Organizing Strings
When cataloguing a collection of genetic strings, we should have an 
established system by which to organize them. The standard method is 
to organize strings as they would appear in a dictionary, so that "APPLE" 
precedes "APRON", which in turn comes before "ARMOR".
Problem

Assume that an alphabet 𝒜 has a predetermined order; that is, we write
the alphabet as a permutation 𝒜=(a1,a2,…,ak), where a1<a2<⋯<ak. For 
instance, the English alphabet is organized as (A,B,…,Z). Given two 
strings s and t having the same length n, we say that s precedes t 
in the lexicographic order (and write s<Lex t) if the first symbol 
s[j] that doesn't match the[j] satisfies sj<tj in 𝒜.
 
Given: A collection of at most 10 symbols defining an ordered 
alphabet, and a positive integer n (where n≤10).
 
Return: All strings of length n that can be formed from the alphabet,
ordered lexicographically (use the standard order of symbols in the English alphabet).
 
Sample Dataset
A C G T
2

Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT



"""


import itertools
 
def lexico_ordering(string, n):
   list_one = (map(str,string.split())) # Returns list of containing each single character
   list_two = ((itertools.product(list_one, repeat=n))) # Returns list of tuples containing characters <= n
   for tuple in list_two: # Prints tuple items in list_two by unpacking each tuple
       print(*[''.join(tuple)], sep='\n')
 
if __name__ == "__main__":
   string='A C G T'
   n = 2
   lexico_ordering(string, n)