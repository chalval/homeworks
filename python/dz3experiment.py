iii = [{'ключи': 0.3},
 {'кошелек': 0.2},
 {'ключи': 0.3, 'кошелек': 0.2},
 {'телефон': 0.5},
 {'ключи': 0.3, 'телефон': 0.5},
 {'кошелек': 0.2, 'телефон': 0.5},
 {'ключи': 0.3, 'кошелек': 0.2, 'телефон': 0.5},
 {'зажигалка': 0.1},
 {'зажигалка': 0.1, 'ключи': 0.3},
 {'зажигалка': 0.1, 'кошелек': 0.2},
 {'зажигалка': 0.1, 'ключи': 0.3, 'кошелек': 0.2},
 {'зажигалка': 0.1, 'телефон': 0.5},
 {'зажигалка': 0.1, 'ключи': 0.3, 'телефон': 0.5},
 {'зажигалка': 0.1, 'кошелек': 0.2, 'телефон': 0.5},
 {'ключи': 0.3, 'кошелек': 0.2, 'телефон': 0.5}]

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
# backpack
backpack = {}
# for i in range(2**len(items)):
#     print(i, type(i), id(i))


for number in range(2**len(items)):
    s = bin(number)[2:]
    ddd = []
    for i in s:
        ddd.append(int(i))
    print(ddd)
    max_weight1 = max_weight
    for key, value in items.items():
        #if s[]
        if (max_weight1 - value) >= 0:
            backpack[key] = value
            max_weight1 -= value
    print(backpack)






    print(f"{s}  {number = }  number = {number:0b}  {s}")





# max_weight1 = max_weight
# for key, value in items.items():
#     if (max_weight1 - value) >= 0:
#         backpack[key] = value
#         max_weight1 -= value
# print(backpack)







