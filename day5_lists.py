#Задача 1
statuses = [200, 404, 500, 201, 302, 204]

print(statuses[0], statuses[-1])
print(statuses[1:3])
print(statuses[::-1])
print(len(statuses))

#Задача 2
codes_lst = [200, 404, 500, 201, 302, 204]

success = []

for code in codes_lst:
    if 200 <= code < 300:
        success.append(code)

print(success)

#Задача 3
codes = [200, 404, 500, 404, 201, 404]

print(codes.count(404))
print(500 in codes)
print(codes.index(404))

#Задача 4
codes_1 = [500, 200]
codes_2 = [404, 201, 302]

codes_3 = codes_1 + codes_2
codes_3.sort()

print(codes_3)
print(codes_3[::-1])