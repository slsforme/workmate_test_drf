from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    )

"""
- Получение списка пород
- Получение списка всех котят
- Получение списка котят определенной породы по фильтру.
- Получение подробной информации о котенке.
- Добавление информации о котенке
- Изменение информации о котенке
- Удаление информации о котенке
- JWT Авторизация пользователей
 
Бизнес логика:
 
Каждый котенок должен иметь – цвет, возраст (полных месяцев) и описание.
Удалять изменять или обновлять информацию пользователь может только о тех животных, которых он добавил сам.
"""

class Breed(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, blank=False, 
                             null=False,
                             verbose_name="Порода",
                             validators=[MinLengthValidator(2)]
                             )
    
    def __str__(self):
        return f"Порода {self.name}."

    class Meta:
        verbose_name="Порода"


class Kitty(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    color = models.CharField(max_length=255, blank=False, 
                             null=False,
                             verbose_name="Цвет котёнка",
                             validators=[MinLengthValidator(3)]
                             )
    age = models.IntegerField(null=False, blank=False,
                              db_index=True, 
                              validators=[MinValueValidator(1)],
                              verbose_name="Возраст котёнка",
                              help_text="Возраст котёнка (в полных месяцах)"                
                             )
    description = models.TextField(null=False, blank=False,
                                  default="Описание отсутсвует",
                                  help_text=(
                                    "Описание котёнка. "
                                    "(Желательно подробное)"
                                  ), 
                                  verbose_name="Описание котёнка",
                                  )
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT,
                              verbose_name="Порода котёнка",
                              )

    def __str__(self):
        return f"Котёнок №{self.id}. Возраст: {self.age} месяцев, порода: {self.breed__name}."

    class Meta:
        verbose_name="Котёнок"
        verbose_name_plural="Котята"
    


        verbose_name_plural="Породы"
    
    

