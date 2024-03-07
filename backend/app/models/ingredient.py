from tortoise.models import Model
from tortoise import fields

class Ingredient(Model):
    id = fields.IntField(pk=True, auto_increment=True)
    name = fields.CharField(max_length=255)
    image_url = fields.CharField(max_length=255)
    price = fields.DecimalField(max_digits=5, decimal_places=2)
    portion_size = fields.DecimalField(max_digits=5, decimal_places=2)
    kcal = fields.DecimalField(max_digits=5, decimal_places=2)
    proteins = fields.DecimalField(max_digits=5, decimal_places=2)
    carbohydrate = fields.DecimalField(max_digits=5, decimal_places=2)
    fats = fields.DecimalField(max_digits=5, decimal_places=2)
    used_in = fields.ManyToManyField('models.Recipe', related_name='ingredients')

    def __str__(self):
        return self.name