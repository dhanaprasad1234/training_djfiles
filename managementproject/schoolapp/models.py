from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.IntegerField(primary_key=True)
    student_name=models.CharField(max_length=225)
    student_attendence=models.IntegerField()
    student_Email=models.CharField(max_length=33)
    student_contactNo=models.IntegerField(null=False)
    student_photo=models.ImageField(upload_to='images/')
    # student_assignment=models.FileField(upload_to='videos/',default='')
    student_description=models.TextField()
    def __str__(self):
        return self.student_name
    class Meta:
        db_table="Student_Table"


