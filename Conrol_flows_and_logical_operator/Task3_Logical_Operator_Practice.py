a = True
b = False
c = True
print(a and b)           # False   Result will be False, because both of them aren't true
print(a or b)            # True    Result will be True, because A is True
print(not b)             # True    Result will be True, because B is False
print((a and c) or b)    # True    Result will be True, because A and C are True, and we don't care about B because we have operator "OR"
print(a and (b or c))    # True    Result will be True, because A and C are True, and we don't care about B because we have operator "OR" between B and C