s = 'saitarunsan'
org = []
[org.append(i) for i in s if i not in org]
print(''.join(org))
