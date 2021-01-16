# список пользователей
list_users = []
# словарь пользователя

while True:
    print("Меню")
    print("1. Добавить пользователя")
        surname = input("surname: ")
        username = input("username: ")
        password = input("password: ")
        ...
        # print(f"Пользователь {surname} {name} добавлен в базу")
        # поиск мах id
        max_id = 0
        for find_user in list_users:
            if find_user['id'] > max_id:
                max_id = find_user['id']
                print("max_id:", max_id)
        #
        dic_user = {}
        dic_user['id'] = max_id + 1
        dic_user['name'] = name
        dic_user['surname'] = surname
        dic_user['username'] = username
        dic_user['password'] = password
        dic_user['name'] = name
        list_users.append(dic_user)
        print(f"Пользователь {surname} {name} добавлен в базу")
   #     print(list_users)
    elif choice == "2":
        print("****Удаление пользователя****")
        id = int(input('id: '))
        ...
        # print(f"Пользователь {surname} {name} с id:{id} удален из базы")
        # print(f"Пользователь с id: {id} не найден")
        flag = 0
        for index, item in enumerate(list_users):
            if item['id'] == id:
                surname = item['surname']
                name = item['name']
                list_users.pop(index)
                flag = 1
        if flag:
            print(f"Пользователь {surname} {name} с id:{id} удален из базы")
        else:
            print(f"Пользователь с id: {id} не найден")

    elif choice == "3":
        print("****Список всех пользователей****")
        ...
        # 12: Иванов И. [vanyok]
        for item in list_users:
            print(f"{item['id']}: {item['surname']} {item['name'][0]}. [{item['username']}]")

    elif choice == "4":
        print("****Редактирование пользователя****")
