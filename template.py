from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from random import randint, sample


def create_characters(template, clases_skills, character, amount):
    for _ in range(amount):
        character['name'] = input('Имя: ')
        character['race'] = input('Расса: ')
        character['class'] = input('Класс: ')
        character['strength'] = randint(1, 3)
        character['agility'] = randint(1, 3)
        character['intelligence'] = randint(1, 3)
        character['luck'] = randint(1, 3)
        character['temper'] = randint(1, 3)
        match character['class'].lower():
            case 'маг':
                character['intelligence'] = 15
                character['img'] = '/images/wizard.png'
                character['skills'] = sample(clases_skills['Маг'], 3)
            case 'воин':
                character['strength'] = 15
                character['img'] = '/images/warrior.png'
                character['skills'] = sample(clases_skills['Воин'], 3)
            case 'охотник':
                character['agility'] = 15
                character['img'] = '/images/archer.png'
                character['skills'] = sample(clases_skills['Охотник'], 3)
            case 'ассасин':
                character['luck'] = 15
                character['img'] = '/images/assasin.png'
                character['skills'] = sample(clases_skills['Ассасин'], 3)
            case 'бард':
                character['temper'] = 15
                character['img'] = '/images/bard.png'
                character['skills'] = sample(clases_skills['Бард'], 3)

        rendered_page = template.render(
            name=character['name'],
            race=character['race'],
            character_class=character['class'],
            strength=character['strength'],
            agility=character['agility'],
            intelligence=character['intelligence'],
            luck=character['luck'],
            temper=character['temper'],
            image=character['img'],
            first_skill=character['skills'][0],
            second_skill=character['skills'][1],
            third_skill=character['skills'][2],
        )

        index = 1
        filename = os.path.join("characters", f"{character['name']}_{index}.html")
        while os.path.exists(filename):
            index += 1
            filename = os.path.join("characters", f"{character['name']}_{index}.html")

        with open(filename, "w", encoding="utf8") as file:
            file.write(rendered_page)

        print(f'Сохранено: {filename}')


def main():
    env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')
    clases_skills = {'Маг' : ['Стрела ледяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Обледенение', 'Ледяное копье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
                    'Воин' : ['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
                    'Охотник' : ['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
                    'Ассасин' : ['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
                    'Бард' : ['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием']
                    }
    character = {}
    amount = int(input('Введите, сколько страниц персонажей вы хотите сделать: '))
    create_characters(template, clases_skills, character, amount)


if __name__ == '__main__':
    main()