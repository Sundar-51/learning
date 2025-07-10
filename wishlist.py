# def wishlist(wish_list):
#     for i in wish_list:
#         for l in i:
#             u=l[i:].upper()
#             print(u)

def wishlist(wish_list):
    for word in wish_list:
        if word:
            first = word[0].upper()
            rest = ''
            for c in word[1:]:
                rest += c.lower() if 'A' <= c <= 'Z' else c
            print(first + rest)




wish_list = ["1billion"]

a = wishlist(wish_list)
