year = int(input()) + 1

while len(set(str(year))) != len(str(year)):
    year += 1

print(year)

# 100 / 100
# start_year = int(input())
# happy_year = start_year + 1
#
# while len(set(str(happy_year))) != len(str(happy_year)):
#     happy_year += 1
#
# print(happy_year)


# start_year = int(input())
# happy_year = start_year + 1
# year_is_unique = False
#
# while not year_is_unique:
#     for digit in str(happy_year):
#         if str(happy_year).count(digit) > 1:
#             happy_year += 1
#             year_is_unique = False
#             break
#         else:
#             year_is_unique = True
#
# print(happy_year)

# start_year = int(input())
# happy_year = start_year + 1
# year_is_unique = False
#
# while True:
#     for digit in str(happy_year):
#         if str(happy_year).count(digit) > 1:
#             year_is_unique = False
#             break
#         else:
#             year_is_unique = True
#
#     if year_is_unique:
#         print(happy_year)
#         break
#     else:
#         happy_year += 1
