from get_hh_vacansions import HHApiEngine, hh_vac_info_validation, hh_data_formatting
from get_sj_vacansions import SJApiEngine, sj_vac_info_validation, sj_data_formatting
from data_json import JsonOperator
from user import UserInterface

if __name__ == "__main__":
    print(f"Здравствуйте, давайте определимся с платформой и необходимой вакансией\n")
    while True:
        platform_input = input(f"Выберите одну из платформ:\n1 - HeadHunter\n2 - SuperJob\n0 - Выйти\n> ")
        if platform_input not in ["0", "1", "2"]:
            print(f"Пожалуйста повнимательнее. Попробуйте еще раз!")
            print()
        else:
            platform = {
                "1": "HeadHunter",
                "2": "SuperJob"
            }
            if platform_input == "0":
                print("До следующего раза!")
                break
            else:
                print(f"Отлично! Вы выбрали платформу {platform[platform_input]}\n")
                city_name_input = input(f"Введите название города, в котором необходимо найти вакансии\n"
                                        f"(Внимательно вводите название города, без ошибок!!!)"
                                        f"\n> ").capitalize()
                prof_input = input(f"Введите пожалуйста название профессии"
                                   f"\n> ").capitalize()
                if platform_input == "1":
                    hh_block = HHApiEngine(city_name_input, prof_input)
                    vac_source = hh_block.get_vacancies()  # Получение вакансий с HeadHunter
                    hh_valid_vac = hh_vac_info_validation(vac_source)  # Валидация вакансий
                    fin_valid_list = hh_data_formatting(hh_valid_vac)  # Приведение к общему виду

                elif platform_input == "2":
                    sj_block = SJApiEngine(city_name_input, prof_input)
                    vac_source = sj_block.get_vacancies()  # Получение вакансий с SuperJob
                    sj_valid_vac = sj_vac_info_validation(vac_source)  # Валидация вакансий
                    fin_valid_list = sj_data_formatting(sj_valid_vac)  # Приведение к общему виду

            json_list = JsonOperator(fin_valid_list)
            json_list.save_to_json()
            work_vac_list = json_list.get_json()
            user_instance = UserInterface(work_vac_list)
            user_instance.functions_exe()







