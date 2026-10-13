def sub(num1, num2):
    return print(num1 - num2)


def week_day(day):
    day = int(input("Enter a number:"))
    if day == 1:
        return "you guessed sunday"
    elif day == 2:
        return "you guessed monday"
    elif day == 3:
        return "you guessed tuesday"
    elif day == 4:
        return "you guessed wednesday"
    elif day == 5:
        return "you guessed thursday"
    elif day == 6:
        return "you guessed friday"
    elif day == 7:
        return "you guessed saturday"
    else:
        return None


print(week_day(0))


def last_el(list_el):
    if len(list_el) > 0:
        return list_el[-1]
    else:
        return None


def number_compare(num1, num2):

    if num1 == num2:

        return "Numbers are equal"
    elif num2 > num1:
        return "Second is greater"

    else:
        return "First is greater"


def single_letter_count(word, letter):
    return word.count(letter)


def multiple_letter_count(word):
    count = {}
    for val in word:
        if val not in count:
            count[val] = word.count(val)

    return count


print(multiple_letter_count("banana"))


def list_manipulation(something, command, location, num):
    if command == "remove":
        if location == "end":
            return something.pop(-1)
        else:
            return something.pop(0)
    elif command == "add":
        if location == "end":
            something.append(num)
            return something
        else:
            something.insert(0, num)
            return something


def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def is_palindrome(phrase):
    phrase = "".join(char.lower() for char in phrase if char.isalnum())
    if phrase == phrase[::-1]:
        return True
    else:
        return False


def fequency(num_list, term):
    return num_list.count(term)


def flip_case(word, letter):
    new_word = ""
    for val in word:
        if val == letter or val == letter.upper():
            if val == letter:
                val = val.upper()
            else:
                val = val.lower()
        new_word += val

    return new_word


def multiply_even_numbers(num_list):
    product = 1
    for val in num_list:
        if val % 2 == 0:
            product *= val

    if product == 1:
        return None
    else:
        return product


def mode(num_list):
    high_num = 0
    most_common = 0
    for val in num_list:
        print(val, num_list.count(val))
        if num_list.count(val)>high_num:
            high_num = num_list.count(val)
            most_common = val

    return most_common

def capitilize(name):
    return name.capitalize()

def compact(phrase):
    new_phrase=[]
    for val in phrase:
        if val:
            new_phrase.append(val)

    return new_phrase


def partition(something, fun())
    return False
   #This function accepts a list and a callback function (which you can assume returns True or False). The function should iterate over each element in the list and invoke the callback function at each iteration. If the result of the callback function is True, the element should go into one list if it’s False, the element should go into another list. When it’s finished, partition should return both lists inside of one larger list.



def intersection():

def once():

def once_bonus():

