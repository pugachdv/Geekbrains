# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
#
# Примечания:
#
# * в сумму не включаем пустую строку и строку целиком;
#
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.


def count_substring(s: str):
    set_hash = set()

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            set_hash.add(hash(s[i:j]))

    counter = len(set_hash) - 1
    return counter


my_string = input('Введите строку:')
count = count_substring(my_string)
print(f'В строке "{my_string}" есть {count} подстрок')
