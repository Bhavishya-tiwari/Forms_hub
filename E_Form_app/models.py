from django.db import models

# Create your models here.
class Forms(models.Model):
    fno=models.AutoField(primary_key=True)
    Form_Title=models.CharField(max_length=700)
    Disc=models.TextField( default="")
    Admin_Name=models.CharField(max_length=550)
    Admin_Email=models.CharField(max_length=550)
    Admin_Username=models.CharField(max_length=1000, default="")
    Timestamp_Created=models.CharField(max_length=505)
    st=models.CharField(max_length=505)
    sd=models.CharField(max_length=505)
    ct=models.CharField(max_length=550)
    cd=models.CharField(max_length=550)
    Qsns=models.TextField( default="")
    Correct_Ans=models.TextField( default="")
    Extras=models.TextField( default="")
    def __str__(self):
        return str(self.fno) +": "+ self.Admin_Name + " by " +self.Admin_Email
        



        








