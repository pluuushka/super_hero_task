# super_hero_task

- super_hero.py - основный скрипт
- test_super_hero.py - файл с тестами
    - test_find_the_best - проверка работы функции на всевозможных случаях
    - test_result_structure - проверка итогового случая

Чтобы работала программа нужно:
    1. python3 -m venv venv - для создания окружения, потом включаем его

    2. pip install -r requirements.txt - все скачали, все круто

Чтобы запустить тесты достаточно:
    1. Если нужно всё запустить pytest или pytest -v (для более подробного вывода)
    
    2. Если отдельно-  pytest test_super_hero.py::название_функции. Например, pytest test_super_hero.py::test_find_the_best

    3. Конкретный случай у определенного теста. Например, test_super_hero.py::test_find_the_best[Female-False-result3-expectation3]
