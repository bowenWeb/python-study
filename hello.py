number = 1
if number%2 == 0:
    print('偶数')
else:
    if number > 3:
        print('大于3的')
    else:
        print('小于3的')
    print('奇数')


# print(f"Hello Python: {age}")
# match age:
#     case x if x < 10:
#         print(f'< 10 years old: {x}')
#     case 10:
#         print('10 years old.')
#     case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
#         print('11~18 years old.')
#     case 19:
#         print('19 years old.')
#     case _:
#         print('not sure.')