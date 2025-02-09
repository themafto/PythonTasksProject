def make_adder(add_value):
    def adder(num):
        return num + add_value
    return adder
   
incrementer = make_adder(1)
result = incrementer(5)

print(adder(5))