def is_prime(num):
    if num==1 or num==2:
        print("its a prime number")
        return True
        if (num % 2) != 0:
            print("its a not prime number")
            return True
    else:
        print("its prime number")
        return False



def prime_num_upto_range(limit):
    for i in range(1, limit + 1):  # Loop from 1 to limit
        result = is_prime(i)
        print(i, result)


a = int(input("Enter the number: "))
prime_num_upto_range(a)


# def prime_num_upto_range(limit):
#     for i in limit:
#         if i < limit:
#             result=is_prime(i)
#             i+=1
#             print(i,result)

a=int(input("Enter the number: "))
prime_num_upto_range(a)


