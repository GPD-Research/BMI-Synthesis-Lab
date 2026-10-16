import os
matches = []
for root, dirs, files in os.walk('..'):
    for f in files:
        if 'fix' in f.lower():
            matches.append(os.path.relpath(os.path.join(root, f), '..'))
print("Matches:", matches)
