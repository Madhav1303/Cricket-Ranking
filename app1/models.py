from django.db import models
class Player(models.Model):
    Roles =[
        ("Bat","Batsmen"),
        ("Bowl","Bowler"),
        ("Wk-Bat","Wicket Keeper and Batsmen"),
        ("All","All rounder")
    ]
    name = models.CharField(max_length = 30)
    dob = models.CharField(max_length = 10)
    nationality = models.CharField(max_length = 20)
    role = models.CharField(max_length = 20,choices = Roles)
    num_test_matches = models.IntegerField()
    num_odi_matches = models.IntegerField()
    num_t20_matches = models.IntegerField()
    totalruns_test_matches = models.IntegerField()
    totalruns_odi_matches = models.IntegerField()
    totalruns_t20_matches = models.IntegerField()
