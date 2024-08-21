'''
Accept average score from the student of his exam and print his result as follows:

0 to 49 fail
50 to 74 is second class 
75 to 90 is first class
91 to 100 is distinction 
Also check for invalid score 
'''

avg_score = int(input('Enter your average score to print the result: '))
if avg_score >= 0 and avg_score <= 49:
    print('Result is fail')
elif avg_score <= 74:
    print('Result is second class')
elif avg_score <= 90:
    print('Result is first class')
elif avg_score <= 100:
    print('Result is distinction') 
else:
    print('Result is Invalid')
 
 