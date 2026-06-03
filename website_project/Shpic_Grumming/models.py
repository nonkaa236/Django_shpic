from django.db import models

class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название породы")
    description = models.TextField(verbose_name="Описание")
    origin = models.CharField(max_length=100, verbose_name="Происхождение")
    image = models.ImageField(upload_to='breeds/', blank=True, null=True, verbose_name="Фото породы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя собаки")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name="Порода")
    age = models.IntegerField(verbose_name="Возраст")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='dogs/', blank=True, null=True, verbose_name="Фото собаки")
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Владелец", default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
