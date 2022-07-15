import collections

s = input()
s = s.upper()

counts = collections.Counter(s)

if len(counts)==1:
    print(counts.most_common(1)[0][0])

elif counts.most_common(2)[0][1] == counts.most_common(2)[1][1]:
    print('?')

else:
    print(counts.most_common(1)[0][0])