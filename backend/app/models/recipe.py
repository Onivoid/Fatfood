from tortoise.models import Model
from tortoise import fields

class Recipe(Model):
    id = fields.IntField(pk=True, autoIncrement=True)
    name = fields.CharField(max_length=255, null=False, description='Name of the recipe')
    type = fields.CharField(max_length=255, null=False, description='Type of the recipe')
    likes = fields.IntField(default=0)

    def __str__(self):
        return self.name