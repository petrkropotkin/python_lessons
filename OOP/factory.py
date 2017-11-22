def factory(aClass, *args):
    return aClass(*args)


class ToDo:

    def __init__(self,data1,data2):
        self.data1 = data1
        self.data2 = data2

    def __str__(self):
        return '{} is {}'.format(self.data1, self.data2)


class ToDo2:

    def __init__(self,data1,data2):
        self.data1 = data1
        self.data2 = data2

    def __str__(self):
        return '{} is not {}'.format(self.data1, self.data2)


if __name__ == '__main__':

    user_answer = input('Choice the name of Class(ToDo or ToDo2): ')
    if user_answer == 'ToDo':
        user_answer2 = input('Enter your name: ')
        user_answer3 = input ('Enter some adjective: ')
        ex1 = factory (ToDo,user_answer2,user_answer3)
        print (ex1)
    elif user_answer == 'ToDo2':
        user_answer2 = input ('Enter your name: ')
        user_answer3 = input ('Enter some adjective: ')
        ex1 = factory (ToDo2,user_answer2,user_answer3)
        print (ex1)

    else:
        print('Hasta la vista baby!')



