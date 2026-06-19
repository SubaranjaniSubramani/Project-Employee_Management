from django import forms
from .models import Employee_Details,Attendance,Salary

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee_Details
        fields = "__all__"

class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = "__all__"

        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

class SalaryForm(forms.ModelForm):

    class Meta:

        model = Salary

        fields = '__all__'

from django import forms
from .models import Leave_Request

class LeaveForm(forms.ModelForm):

    class Meta:

        model = Leave_Request

        fields = '__all__'