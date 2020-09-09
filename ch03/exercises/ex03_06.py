# Turing Test: whether machine could exhibit intelligent behaviour.

print('What is your problem?')
print('Have you had this problem before (yes or no)?')

userAns = input()

if userAns == 'yes' or userAns == 'Yes' or userAns == 'YES':
    print('Well, you have it again.')
elif userAns == 'no' or userAns == 'No' or userAns == 'NO':
    print('Well, you have it now.')
