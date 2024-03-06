from tortoise.models import Model
from tortoise import fields

class User(Model):
  id = fields.CharField(pk=True, max_length=255)
  name = fields.CharField(max_length=255)
  email = fields.EmailField(max_length=255, null=True)
  discord_id = fields.CharField(max_length=255, null=True)
  password = fields.CharField(max_length=255, null=True)
  recipes = fields.ForeignKeyField('models.Recipe', related_name='owner', null=True)

  def __str__(self):
    return self.name
