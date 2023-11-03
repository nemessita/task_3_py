def hesablama(operator):
    if operator == 1:
        try:
            num1 = float(input("Eded daxil edin: "))
            num2 = float(input("Eded daxil edin: "))
            result = num1 * num2
            print(f"Cavab: {num1} * {num2} = {result}")
        except ValueError:
            print("Xahiş edirik yalnız rəqəm daxil edin.")
        except ZeroDivisionError:
            print("0-a bölməyin qarşısını al.")
    elif operator == 2:
        try:
            num1 = float(input("Eded daxil edin: "))
            num2 = float(input("Eded daxil edin: "))
            result = num1 - num2
            print(f"Cavab: {num1} - {num2} = {result}")
        except ValueError:
            print("Xahiş edirik yalnız rəqəm daxil edin.")
    elif operator == 3:
        try:
            num1 = float(input("Eded daxil edin: "))
            num2 = float(input("Eded daxil edin: "))
            result = num1 + num2
            print(f"Cavab: {num1} + {num2} = {result}")
        except ValueError:
            print("Xahiş edirik yalnız rəqəm daxil edin.")
    elif operator == 4:
        try:
            num1 = float(input("Eded daxil edin: "))
            num2 = float(input("Eded daxil edin: "))
            if num2 == 0:
                print("0-a bölməyin qarşısını al.")
            else:
                result = num1 / num2
                print(f"Cavab: {num1} / {num2} = {result}")
        except ValueError:
            print("Xahiş edirik yalnız rəqəm daxil edin.")
        except ZeroDivisionError:
            print("0-a bölməyin qarşısını al.")
    else:
        print("Düzgün əməliyyat seçilməyib.")

while True:
    print("Daxil Edin\nVurma (1), Çıxma (2), Toplama (3), Bölmə (4)")
    try:
        operation = int(input("Daxil edildi: "))
        if operation in [1, 2, 3, 4]:
            hesablama(operation)
        else:
            print("Düzgün əməliyyat seçilməyib.")
    except ValueError:
        print("Düzgün əməliyyat seçilməyib.")

