from Page_Object_Model.singleton import Singleton
import random
import string


def determining_position_of_object_in_drop_down_list(object_list, value_object):  # Определение позиции обьекта в выпадающем списке
    position = 0
    for country_or_city in object_list:
        if country_or_city.get_attribute("value") == value_object:
            singleton = Singleton()
            singleton.position_object = str(position)
            break
        else:
            position += 1


def generate_alphanum_random_string(length):  # генерация буквенно-цифровой случайной строки
    letters_and_digits = string.ascii_letters + string.digits
    random_string = ''.join(random.sample(letters_and_digits, length))
    return random_string
