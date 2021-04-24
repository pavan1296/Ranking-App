from django.db import models
from .enums import GenderEnum, PlayerFieldType, MatchType

# Create your models here.
GENDER_ENUMS = [(gender.name, gender.value) for gender in GenderEnum]
class Player(models.Model):

    country_choices = (
        ('INDIA', 'INDIA'),
        ('SRI LANKA', 'SRI LANKA'),
        ('AFGANISTHAN', 'AFGANISTHAN')
    )

    player_name = models.CharField(max_length=25, default='player')
    player_country = models.CharField(max_length=15, choices=country_choices)
    gender = models.CharField(max_length=7, choices=GENDER_ENUMS)


PLAYER_FIELD_TYPE = [(field.name, field.value) for field in PlayerFieldType]
MATCH_TYPE = [(match_type.name, match_type.value) for match_type in MatchType]

class PlayerStats(models.Model):

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    player_field_type = models.CharField(max_length=11, choices=PLAYER_FIELD_TYPE)
    match_type = models.CharField(max_length=5, choices=MATCH_TYPE)
    rating = models.IntegerField(default=0)