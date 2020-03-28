# 1. Составить список из чисел от 1 до 1000, которые имеют в своём составе 7.
numbers_7 = [x for x in range(1, 1000) if (str(x)).find('7') != -1]
print(numbers_7)

# 2. Взять предложение **Would it save you a lot of
# time if I just gave up and went mad now?** и сделать его же без
# гласных. **up:** можно оставить в виде списка слов и не собирать строку.
sentence = 'Would it save you a lot of time' \
           ' if I just gave up and went mad now?'
sentence_cons = [x for x in sentence if x not in 'aeuoa']
print(*sentence_cons, sep='')

# 3. Для предложения The ships hung in the
# sky in much the same way that bricks don't
# составить словарь, где слову соответствует его длина.
sentence_3 = "The ships hung in the sky in much the same way that bricks don't"
sentence_3_list = sentence_3.split(' ')
sentence_3_dict = {el: len(el) for el in sentence_3_list}
print(sentence_3_dict)

# 4*. Для чисел от 1 до 1000 наибольшая цифра, на которую они делятся (1-9).
numbers_1000 = {x: i for x in range(1, 1001)
                for i in range(1, 10) if x % i == 0}
print(numbers_1000)
numbers_9 = [max([i for i in range(1, 10) if x % i == 0])
             for x in range(1, 1001)]
print(numbers_9)

# 5*. Список всех чисел от 1 до 1000,
# не имеющих делителей среди чисел от 2 до 9.
numbers_simple = [x for x in range(1, 1001)
                  if len([i for i in range(1, 10) if x % i == 0]) == 1]
print(numbers_simple)
