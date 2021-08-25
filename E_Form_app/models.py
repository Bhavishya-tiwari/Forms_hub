from django.db import models

# Create your models here.
class Forms(models.Model):
    fno=models.AutoField(primary_key=True)
    Form_Title=models.CharField(max_length=700)
    Admin_Name=models.CharField(max_length=50)
    Admin_Username=models.CharField(max_length=1000, default="")
    Timestamp_Created=models.CharField(max_length=50)
    Timestamp_Sheduled=models.CharField(max_length=50)
    Timestamp_End=models.CharField(max_length=50)
    Qsns=models.TextField( default="")
    Correct_Ans=models.TextField( default="")
    ResponseJson=models.TextField( default="")
    Extras=models.TextField( default="")
    Extras=models.TextField( default="")
    def __str__(self):
        return self.fno +": "+ self.Name + " by " +self.Form_Title

    



