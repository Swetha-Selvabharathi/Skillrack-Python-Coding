"""
Top Scoring Batsman Name
ID:2571

The runs scored by N batsmen of a cricket team is passed as the input to the program. The program must print the name of the batsman who scored the highest runs. (You can assume that no two batsmen will be the top scorers).
Input Format:
The first line denotes the value of N.
Next N lines will contain the name of the batsman and the runs score (both separated by a comma)
Output Format:
The first line contains the name of the batsman with the top score.
Boundary Conditions:
2 <= N <= 11
The length of the names will be from 3 to 100.
The value of the runs will be from 0 to 500.
Example Input/Output 1:
Input:
5
BatsmanA,45
BatsmanB,52
BatsmanC,12
BatsmanD,9
BatsmanE,78
Output:
BatsmanE
"""

num = int(input())
a,b = [],[]
max_val = 0
for i in range(n):
    x,y = input().split(",")
    a.append(x)
    b.append(int(y))
    
for j in range(len(y)):
    if y[j]>max_val:
        max_val = y[j]
        index = j
print(a[index])        









        





    





