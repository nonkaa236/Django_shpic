import os
import django
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website_project.settings')
django.setup()

from django.contrib.auth import get_user_model
from Shpic_Grumming.models import Breed, Dog

User = get_user_model()
user, created = User.objects.get_or_create(
    username='admin',
    defaults={'email': 'admin@example.com'}
)
if created:
    user.set_password('admin123')
    user.save()
print('User:', user.username, 'id=', user.id, 'created=', created)

breed_data_list = [
    {
        'name': 'Померанский шпиц',
        'origin': 'Германия',
        'description': 'Рост: 18–24 см. Вес: 1,8–3,5 кг. Самый маленький и самый популярный шпиц — энергичный, пушистый и преданный.'
    },
    {
        'name': 'Малый немецкий шпиц',
        'origin': 'Германия',
        'description': 'Рост: 23–29 см. Вес: 5–10 кг. Компактный немецкий шпиц с дружелюбным характером.'
    },
    {
        'name': 'Средний немецкий шпиц',
        'origin': 'Германия',
        'description': 'Рост: 30–38 см. Вес: 7–12 кг. Уравновешенный и послушный шпиц средних размеров.'
    },
    {
        'name': 'Большой немецкий шпиц',
        'origin': 'Германия',
        'description': 'Рост: 42–50 см. Вес: 17–20 кг. Крупный представитель немецких шпицев, спокойный и надёжный.'
    },
    {
        'name': 'Вольфшпиц (кеесхонд)',
        'origin': 'Германия',
        'description': 'Рост: 43–55 см. Вес: 25–30 кг. Самый крупный среди немецких шпицев, с густой волчьей мастью.'
    },
    {
        'name': 'Японский шпиц',
        'origin': 'Япония',
        'description': 'Рост: 30–38 см. Вес: 5–10 кг. Белая порода с живым и артистичным нравом.'
    },
    {
        'name': 'Американская эскимосская собака',
        'origin': 'США',
        'description': 'Рост: 23–48 см. Вес: 5–16 кг. Энергичная и дружелюбная собака, внешне похожая на шпицев.'
    },
    {
        'name': 'Финский шпиц',
        'origin': 'Финляндия',
        'description': 'Рост: 39–50 см. Вес: 7–13 кг. Рабочая северная порода с выраженным охотничьим инстинктом.'
    },
    {
        'name': 'Самоед',
        'origin': 'Россия (Сибирь)',
        'description': 'Рост: 48–56 см. Вес: 20–30 кг. Дружелюбный северный шпиц с характерной белой шерстью.'
    },
    {
        'name': 'Евразиер',
        'origin': 'Германия/Франция',
        'description': 'Рост: 47–62 см. Вес: 21–32 кг. Смесь шпицев и других северных пород, спокойный и уравновешенный друг семьи.'
    },
    {
        'name': 'Итальянский вольпино',
        'origin': 'Италия',
        'description': 'Рост: 25–30 см. Вес: 3–5 кг. Мелкий итальянский шпиц с элегантным и живым характером.'
    },
]
created_breeds = 0
for breed_data in breed_data_list:
    breed, created = Breed.objects.get_or_create(
        name=breed_data['name'],
        defaults={
            'origin': breed_data['origin'],
            'description': breed_data['description'],
        }
    )
    if created:
        created_breeds += 1
print('Created breeds:', created_breeds)
print('Total breeds:', Breed.objects.count())

if Dog.objects.count() == 0:
    pomeranian = Breed.objects.get(name='Померанский шпиц')
    german = Breed.objects.get(name='Немецкий шпиц')
    japanese = Breed.objects.get(name='Японский шпиц')
    dogs = [
        {
            'name': 'Буба',
            'breed': pomeranian,
            'age': 3,
            'description': 'Весёлый молодой шпиц, любит прогулки.',
        },
        {
            'name': 'Лиса',
            'breed': german,
            'age': 5,
            'description': 'Спокойная и умная собака для семьи.',
        },
        {
            'name': 'Снежинка',
            'breed': japanese,
            'age': 2,
            'description': 'Нежная и активная собака, очень любит игрушки.',
        },
    ]
    for dog_data in dogs:
        Dog.objects.create(owner=user, **dog_data)
    print('Created dogs: 3')
else:
    print('Dogs already exist:', Dog.objects.count())

print('Final counts: breeds=', Breed.objects.count(), 'dogs=', Dog.objects.count())
