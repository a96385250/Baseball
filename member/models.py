from django.db import models

# Create your models here.
class team(models.Model):
    teamID = models.IntegerField(primary_key=True)
    teamName = models.CharField(max_length=10,null=False)
    teamEng = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.teamName

    class Meta:
        db_table = "teams"
class member(models.Model):
    name = models.CharField(max_length=10,null=False)
    account = models.CharField(max_length=10,null=False)
    password = models.CharField(max_length=10,null=False)
    team = models.ForeignKey(team ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table="member"




