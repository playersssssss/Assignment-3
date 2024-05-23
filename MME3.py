a = 10
b = 3
c = 17

expression_i = not((a - 7) > b) and (2*b + a < c)
expression_ii = not(((a - 7) > b) and (2*b + a < c)) and (a == 11)

print("Expression i evaluates to:", expression_i)
print("Expression ii evaluates to:", expression_ii)


