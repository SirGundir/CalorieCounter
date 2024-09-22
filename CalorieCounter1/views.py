from django.shortcuts import render
from .translator import *
import requests
from fatsecret import Fatsecret
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

fs = Fatsecret('0bc9b0aa02a646b9871bab150432cb79', '5eda05138efc439c83d367a684ecbbb4')

def fooder(name):
    foods = fs.foods_search(russian_to_english(name))
    current_list = []
    i = 0
    if foods:
        for food in foods:
            food_id = food['food_id']
            food_name = food['food_name']

            # Получение подробной информации о продукте
            params = {'method': 'food.get.v2', 'food_id': food_id, 'format': 'json'}
            response = fs.session.get(fs.api_url, params=params)
            food_data = response.json()

            if 'food' in food_data and 'servings' in food_data['food']:
                servings = food_data['food']['servings']['serving']
                if isinstance(servings, list):  # Если servings является списком
                    serving = servings[0]
                    calories = serving.get('calories', 0)
                    protein = serving.get('protein', 0)
                    fat = serving.get('fat', 0)
                    carbs = serving.get('carbohydrate', 0)
                    current_list.append([english_to_russian(food_name), calories, protein, fat, carbs])
                    print(f"Название: {food_name}")
                    print(f"Калорий: {calories} ккал")
                    print(f"Белки: {protein} г")
                    print(f"Жиры: {fat} г")
                    print(f"Углеводы: {carbs} г")
                    print()
                elif isinstance(servings, dict):  # Если servings является словарем
                    calories = servings.get('calories', 0)
                    protein = servings.get('protein', 0)
                    fat = servings.get('fat', 0)
                    carbs = servings.get('carbohydrate', 0)
                    current_list.append([english_to_russian(food_name), calories, protein, fat, carbs])
                    print(f"Название: {food_name}")
                    print(f"Калорий: {calories} ккал")
                    print(f"Белки: {protein} г")
                    print(f"Жиры: {fat} г")
                    print(f"Углеводы: {carbs} г")
                    print()
    else:
        print("Не найдено соответствие для данного ингредиента.")
    return current_list



def finder(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            food_list = fooder(query)
            return render(request, 'CalorieCounter1/home.html', {'food_list': food_list})
        else:
            return render(request, 'CalorieCounter1/home.html', {'error': 'Пожалуйста, введите запрос для поиска.'})
    else:
        return render(request, 'CalorieCounter1/home.html', {'error': 'Только GET запросы допускаются.'})
