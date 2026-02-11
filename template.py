from jinja2 import Environment, FileSystemLoader, select_autoescape
import random
import os
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('template.html')


def main():
    races = ["Орк", "Эльф", "Гном", "Человек", "Хоббит", "Дварф"]

    classes_base = {
        "Маг": {
            "image": "images/wizard.png",
            "skills": ["Магия огня", "Телекинез", "Иллюзии"],
            "high_stat": "intelligence"
        },
        "Воин": {
            "image": "images/warrior.png",
            "skills": ["Атака мечом", "Защита щитом", "Критический удар"],
            "high_stat": "strength"
        },
        "Охотник": {
            "image": "images/archer.png",
            "skills": ["Стрельба из лука", "Следопыт", "Выживание"],
            "high_stat": "agility"
        },
        "Ассасин": {
            "image": "images/assasin.png",
            "skills": ["Скрытность", "Отравление", "Быстрая атака"],
            "high_stat": "luck"
        },
        "Бард": {
            "image": "images/bard.webp",
            "skills": ["Игра на лютне", "Красноречие", "Вдохновение"],
            "high_stat": "temper"
        }
    }

    characters_dir = 'characters'
    if not os.path.exists(characters_dir):
        os.makedirs(characters_dir)

    num_characters = int(input("Сколько персонажей создать?: "))

    for character_num in range(1, num_characters + 1):
        character_name = input(f"Введите имя персонажа {character_num}: ")

        print("Доступные расы:")
        for i, race in enumerate(races, 1):
            print(f"{i}. {race}")

        max_race_choice = len(races)

        while True:
            race_choice = int(input(f"Выберите номер расы для персонажа {character_num} (1-{max_race_choice}): "))
            if 1 <= race_choice <= max_race_choice:
                character_race = races[race_choice - 1]
                break
            else:
                print(f"Неверный выбор! Пожалуйста, выберите номер от 1 до {max_race_choice}.")

        print("\nДоступные классы:")
        class_list = list(classes_base.keys())

        for i, class_name in enumerate(class_list, 1):
            print(f"{i}. {class_name}")

        max_class_choice = len(class_list)

        while True:
            class_choice = int(input(f"Выберите номер класса для персонажа {character_num} (1-{max_class_choice}): "))
            if 1 <= class_choice <= max_class_choice:
                character_class = class_list[class_choice - 1]
                break
            else:
                print(f"Неверный выбор! Пожалуйста, выберите номер от 1 до {max_class_choice}.")

        class_data = classes_base[character_class]
        character_image = class_data["image"]
        character_skills = class_data["skills"]
        high_stat = class_data["high_stat"]

        stats = {
            "strength": random.randint(1, 3) if high_stat != "strength" else 15,
            "agility": random.randint(1, 3) if high_stat != "agility" else 15,
            "intelligence": random.randint(1, 3) if high_stat != "intelligence" else 15,
            "luck": random.randint(1, 3) if high_stat != "luck" else 15,
            "temper": random.randint(1, 3) if high_stat != "temper" else 15
        }

        rendered_page = template.render(
            name=character_name,
            race=character_race,
            character_class=character_class,
            image=character_image,
            strength=stats["strength"],
            agility=stats["agility"],
            intelligence=stats["intelligence"],
            luck=stats["luck"],
            temper=stats["temper"],
            first_skill=character_skills[0],
            second_skill=character_skills[1],
            third_skill=character_skills[2]
        )

        filename = os.path.join(characters_dir, f"index{character_num}.html")
        with open(filename, 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == "__main__":
    main()
