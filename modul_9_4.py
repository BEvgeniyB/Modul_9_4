first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y : x == y, first, second)))

def  get_advanced_writer(file_name):
    """Так файл очищается или создается если нету """
    with open(file_name,mode= 'w',encoding='utf8'):
        pass
    def write_everything(*data_set):
        print(data_set)
        with open(file_name, mode='a', encoding='utf8') as fyle_my:
            for i in data_set:
                fyle_my.write(str(i)+ '\n')
                # if isinstance(i,int|str|float):
                #     fyle_my.write(str(i)+ '\n')
                # elif isinstance(i,dict):
                #     for key, value in i.items():
                #         fyle_my.write(str(key)+' : '+value + '\n')
                # else:
                #     for k in i:
                #         fyle_my.write(str(k)+'\n')
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'],{'А это':"список"})

from random import choice
class MysticBall:
    def __init__(self,*words):
        self.words = words
    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное',"Примерно","Наверняка")
print(first_ball())
print(first_ball())
print(first_ball())
