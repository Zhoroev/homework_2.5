import random
names = ['dhhgfjjhsa.txt', 'hhdsdahffh.txt', 'afdgdhjsds.txt',
         'sggjghddss.txt', 'fjdjgdghdf.txt', 'sjssahjfga.txt',
         'agsgdjhhfj.txt', 'gafadhadda.txt', 'hdagajfhhj.txt',
         'fhjhafhdfa.txt']

file = open(f'{names[random.randint(0, 10)]}', 'w')


def func(argument):
    for name in argument:
        try:
            with open(f'{name}', 'r+') as f:
                f.write('Erzhan')
        except FileNotFoundError:
            print(f'Такого файла {name} не существует')


func(names)
