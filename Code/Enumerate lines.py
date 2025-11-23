Code = '''
def UserInput(text: str, DATAtype):
    variable = None
    if DATAtype == float:  # Принимаем на ввод дробные числа
        while variable == None:
            variable = input(text)
            try:
                variable = float(variable)

            except ValueError:
                print(
                    f"'{variable}' не является корректным значением. Если вы вводите дробное значеине, вводите его через точку(Пр.: 4.5)"
                )
                variable = None
                continue
        return variable

    elif DATAtype == int:  # Получим целое число
        while variable == None:
            variable = input(text)
            if "." in variable:
                print(
                    """                    
Вы ввели дробное значение.
Пожалуйста, введите целое значение.     
"""
                )
                variable = None
            else:
                try:
                    variable = int(variable)
                except ValueError:
                    print(f"'{variable}' не является корректным значением.")
                    variable = None

        return variable

    elif DATAtype == str:  # Полчить строковое значение
        variable = input(text)
        return variable

    else:
        raise TypeError(
            f"""{DATAtype} is wrong type of value!
                            Allowed types: str, int, float"""
        )
'''
lines = Code.strip("\n").split("\n")
for i, line in enumerate(lines, start=1):
    print(f"{i:>3}: {line}")
