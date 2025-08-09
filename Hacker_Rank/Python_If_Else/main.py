if __name__ == '__main__':
    n = int(input().strip())

# if 1 <= n <= 100:
#     if n % 2 != 0:
#         print("Weird")
#     else:
#         if 2 <= n <= 5:
#             print("Not weird")
#         elif 6 <= n <= 20:
#             print("Weird")
#         elif n > 20:
#             print("Not Weird")
# else:
#     print("Number must be between 1 and 100")

if 1 <= n <= 100:
    if n % 2 != 0 or (6 <= n <= 20):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Number must be between 1 and 100")