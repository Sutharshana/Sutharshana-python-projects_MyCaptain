

# print frequency of a letters in string
s = str(input("Enter String : "))
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
var = most_frequent(s)
print(var)
for key in var:
    print(key, "=", var[key])
