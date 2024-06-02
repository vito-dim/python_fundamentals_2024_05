# tail = input()
# body = input()
# head = input()
#
# body_list = list()
# body_list.append(head)
# body_list.append(body)
# body_list.append(tail)
# print(body_list)

# body_list = []
# tail = body_list.append(input())
# body = body_list.append(input())
# head = body_list.append(input())
#
# body_list[0], body_list[-1] = body_list[-1], body_list[0]
# print(body_list)

body_list = list()
for _ in range(3):
    body_list.append(input())

body_list[0], body_list[-1] = body_list[-1], body_list[0]
print(body_list)
