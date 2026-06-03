from pathlib import Path
base = Path('website_project/Shpic_Grumming/templates')
files = {
    'home.html': """{% extends 'base.html' %}
{% load static %}

{% block title %}Главная{% endblock %}

{% block content %}
<h2>Породы шпицев</h2>
<div class="card-grid">
{% for breed in breeds %}
<div class="breed card">
    <h3><a href="{% url 'breed_detail' breed.id %}">{{ breed.name }}</a></h3>
    <img src="{% if breed.image %}{{ breed.image.url }}{% else %}{% static 'placeholder.svg' %}{% endif %}" alt="{{ breed.name }}">
    <p>{{ breed.description|truncatechars:120 }}</p>
</div>
{% endfor %}
</div>
{% endblock %}
""",
    'breed_detail.html': """{% extends 'base.html' %}
{% load static %}

{% block title %}{{ breed.name }}{% endblock %}

{% block content %}
<h2>{{ breed.name }}</h2>
<img src="{% if breed.image %}{{ breed.image.url }}{% else %}{% static 'placeholder.svg' %}{% endif %}" alt="{{ breed.name }}">
<p><strong>Происхождение:</strong> {{ breed.origin }}</p>
<p>{{ breed.description }}</p>
<h3>Собаки этой породы</h3>
<div class="card-grid">
{% for dog in dogs %}
<div class="breed card">
    <h4><a href="{% url 'dog_detail' dog.id %}">{{ dog.name }}</a></h4>
    <img src="{% if dog.image %}{{ dog.image.url }}{% else %}{% static 'placeholder.svg' %}{% endif %}" alt="{{ dog.name }}">
    <p><strong>Возраст:</strong> {{ dog.age }} лет</p>
    <p>{{ dog.description|truncatechars:100 }}</p>
</div>
{% endfor %}
</div>
{% endblock %}
""",
    'dog_detail.html': """{% extends 'base.html' %}
{% load static %}

{% block title %}{{ dog.name }}{% endblock %}

{% block content %}
<h2>{{ dog.name }}</h2>
<img src="{% if dog.image %}{{ dog.image.url }}{% else %}{% static 'placeholder.svg' %}{% endif %}" alt="{{ dog.name }}">
<p><strong>Порода:</strong> {{ dog.breed.name }}</p>
<p><strong>Возраст:</strong> {{ dog.age }} лет</p>
<p>{{ dog.description }}</p>
<a href="{% url 'breed_detail' dog.breed.id %}">Вернуться к породе</a>
{% endblock %}
"""
}
for name, content in files.items():
    (base/name).write_text(content, encoding='utf-8')
placeholder = Path('website_project/Shpic_Grumming/static/placeholder.svg')
placeholder.write_text('''<?xml version="1.0" encoding="UTF-8"?>
<svg width="640" height="480" viewBox="0 0 640 480" xmlns="http://www.w3.org/2000/svg">
  <rect width="640" height="480" fill="#f5f5f5"/>
  <rect x="40" y="40" width="560" height="400" rx="24" ry="24" fill="#ffffff" stroke="#d1d5db" stroke-width="4"/>
  <text x="320" y="240" text-anchor="middle" fill="#9ca3af" font-family="Arial, sans-serif" font-size="36">Фото отсутствует</text>
  <text x="320" y="290" text-anchor="middle" fill="#d1d5db" font-family="Arial, sans-serif" font-size="18">Добавьте изображение через админку</text>
</svg>
''', encoding='utf-8')
print('Templates and placeholder updated.')
