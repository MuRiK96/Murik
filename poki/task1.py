# task6
# from os import strerror
# try:
#     with open('C:/Users/7/Documents/GitHub/Murik/poki/content1.txt') as file:
#         text = file.read()

# except IOError as err:
#     print(f'фаил не открылся{strerror(err.errno)}')
# print(text)
# word_f = input('введите слово,для изменения')
# word_c = input('введите слово,для замены')

# text = text.replace(word_f,word_c)
# print(text)
# try:
#     with open('C:/Users/7/Documents/GitHub/Murik/poki/content1.txt','w') as file:
#         file.write(text)
# except IOError as err:
#     print(f'фаил так и не открылся {strerror(err.errno)}')


# task5
# with open('C:/Users/7/Documents/GitHub/Murik/poki/content1.txt') as file:
#         text = file.read()

# word_s = input('введите слово для подсчета ')
# word_n = text.count(word_s)

# print(f'в тексте слово {word_s} есть {word_n} раз')

# task4
# from os import strerror
# try:
#     with open('C:/Users/7/Documents/GitHub/Murik/poki/content1.txt') as file:
#         max_l = 0
#         for i in file:
#             if len(i) > max_l:
#                 max_l = len(i)
#         print(max_l)
# except IOError as err:
#     print(f'фаил не открылся{strerror(err.errno)}')
