not_self = []
for i in range(1,10001,1):
    sum_ = i
    i = str(i)
    for k in range(len(i)):
        sum_ += int(i[k])
    not_self.append(sum_)
for k in range(1,10001):
    if k not in not_self:
        print(k)