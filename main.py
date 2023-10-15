from data_hh import HHUserInterface
from data_superjob import SJUserInterface


if __name__ == "__main__":
    print(f"Здравствуйте! В нашем приложении предлагаем с двух платформ получить информацию по интересующим вакансиям!\n")
    while True:
        platform_input = input(f"Выбери платформу:\n1 - сайт HeadHunter\n2 - сайт SuperJob\n3 - Выйти\n> ")
        if platform_input == "1":
            hh_block = HHUserInterface()
            hh_block.user_interaction()

        elif platform_input == "2":
            sj_block = SJUserInterface()
            sj_block.user_interaction()

        elif platform_input == "3":
            print("Удачного дня!")
            break

        else:
            print(f"Введите корректный код. Попробуйте еще раз!")
            print()







