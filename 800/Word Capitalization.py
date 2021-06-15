capital = input()
string_list = list(capital) 
nw = capital[0].upper()
string_list[0] = nw
ns = "".join(string_list)
print(ns)