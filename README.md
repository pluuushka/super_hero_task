# super_hero_task

- super_hero.py - основный скрипт
- test_super_hero.py - файл с тестами
    - test_find_the_best - проверка работы функции на всевозможных случаях
    - test_invalid_sex - проверка на некорректный ввод пола
    - test_result_structure - проверка итогового случая

Чтобы запустить тесты достаточно:
    1. Если нужно всё запустить pytest или pytest -v (для более подробного вывода)
    
    2. Если отдельно-  pytest test_super_hero.py::название_функции. Например, pytest test_super_hero.py::test_find_the_best

    3. Конкретный случай у определенного теста. Например, pytest -k "test_result_structure and Male-True"
