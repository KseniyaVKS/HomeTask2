from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        count_ingridients = int(file.readline())
        ingridients_list = []
        for i in range(count_ingridients):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingridients_list.append({
                'ingridient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish.strip()] = ingridients_list
    # pprint(cook_book)

dishes_0 = ['Омлет', 'Фахитос']
dishes_1 = ['Запеченный картофель', 'Омлет']
dishes_2 = ['Омлет', 'Утка по-пекински', 'Фахитос']
dishes_3 = ['Запеченный картофель', 'Утка по-пекински']
def get_shop_list_by_dishes(dishes, person_count):
    ingrs_dict = {}
    for dish, ingrs in cook_book.items():
        for ingr in ingrs:
            if dish in dishes:
                name = ingr['ingridient_name']
                measure = ingr['measure']
                quantity = int(ingr['quantity']) * person_count
                if name in ingrs_dict:
                    ingrs_dict[name]['quantity'] += quantity
                else: ingrs_dict[name] = {'measure': measure, 'quantity': quantity}
    pprint(ingrs_dict)
get_shop_list_by_dishes(dishes_0, 2)
print('-------------------------------------------------')
get_shop_list_by_dishes(dishes_1, 3)
print('-------------------------------------------------')
get_shop_list_by_dishes(dishes_2, 5)
print('-------------------------------------------------')
get_shop_list_by_dishes(dishes_3, 4)