with open('input.txt', 'r') as f:
    msgs = f.read().splitlines()

farr = []
for msg in msgs:
    for ltr in msg:
        if i in 