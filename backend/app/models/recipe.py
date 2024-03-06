from tortoise.models import Model
from tortoise import fields

class Recipe(Model):
    id = fields.CharField(pk=True, max_length=255, autoIncrement=True)
    name = fields.CharField(max_length=255)
    type = fields.CharField(max_length=255)
    owner = fields.ManyToOneField('models.User', related_name='recipes')
    ingredients = fields.ManyToManyField('models.Ingredient', related_name='used_in')
    likes = fields.IntField(default=0)

    def __str__(self):
        return self.name