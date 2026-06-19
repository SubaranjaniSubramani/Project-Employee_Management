from django.db import models

# Create your models here.
class Employee_Details(models.Model):
    emp_username=models.CharField(max_length=100)
    emp_password=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    department=models.CharField(max_length=100)
    salary_amt=models.IntegerField(blank=True,null=True)
   

    def __str__(self):
        return self.emp_username
    
class Admin(models.Model):
    username=models.CharField(max_length=60)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.username
    
class Attendance(models.Model):

    employee = models.ForeignKey( Employee_Details,on_delete=models.CASCADE)

    date = models.DateField()

    status = models.CharField(
        max_length=20
    )
    

    def __str__(self):

        return self.status

class Leave_Request(models.Model):

    employee = models.ForeignKey(  Employee_Details, on_delete=models.CASCADE )
      
    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):

        return self.status
    

class Salary(models.Model):

    employee = models.ForeignKey(
        Employee_Details,
        on_delete=models.CASCADE
    )

    amount = models.IntegerField()

    month = models.CharField(
        max_length=20
    )

    def __str__(self):

        return self.month
