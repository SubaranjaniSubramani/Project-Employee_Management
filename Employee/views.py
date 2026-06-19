from django.shortcuts import render,redirect
from .models import Employee_Details,Admin,Attendance,Leave_Request,Salary
from .forms import EmployeeForm,AttendanceForm,SalaryForm,LeaveForm
# Create your views here.

def Home(request):

    return render(
        request,
        'home.html'
    )
#Admin login

def Admin_login(request):

    

    if request.method == "POST":

        print("POST request received")

        username = request.POST.get('username')
        password = request.POST.get('password')

     

        admin = Admin.objects.filter(
            username=username,
            password=password
        ).first()

        print(admin)

        if admin:
            
            return redirect('Admin_dashboard')

    return render(request, 'admin_login.html')

def Admin_dashboard(request):
    return render(request,"admin_dashboard.html")

def Add_employee(request):
    Employee=EmployeeForm()
    if request.method=="POST":
        Employee=EmployeeForm(request.POST)
        if Employee.is_valid():
            Employee.save()
            return redirect('Employee_list')
    return render(request,'add_employee.html',{"forms":Employee})

def Employee_list(request):
    emp_list=Employee_Details.objects.all()
    return render(request,'employee_list.html',{'emp_list':emp_list})



def Update_employee(request, id):

    employee = Employee_Details.objects.get(id=id)

    form = EmployeeForm(instance=employee)

    if request.method == 'POST':

        form = EmployeeForm(
            request.POST,
            instance=employee
        )

        if form.is_valid():

            form.save()

            return redirect('Employee_list')

    return render(
        request,
        'update_employee.html',
        {'form': form}
    )

def Delete_employee(request,id):
    delete=Employee_Details.objects.get(id=id)
    delete.delete()
    return redirect('Employee_list')


def Employee_login(request):

    if request.method == 'POST':

        username = request.POST.get('emp_username')
        password = request.POST.get('emp_password')

        employee = Employee_Details.objects.filter(
            emp_username=username,
            emp_password=password
        ).first()

        if employee:

            request.session['employee_id'] = employee.id

            return redirect(
                'Employee_profile',
                employee.id
            )

    return render(
        request,
        'employee_login.html'
    )

def Employee_profile(request, id):

    employee = Employee_Details.objects.get(id=id)

    salary = Salary.objects.filter(employee=employee)

    attendance = Attendance.objects.filter(employee=employee)

    leave = Leave_Request.objects.filter(employee=employee)

    return render(
        request,
        'employee_profile.html',
        {
            'employee': employee,
            'salary': salary,
            'attendance': attendance,
            'leave': leave
        }
    )
def Add_attendance(request):

    form = AttendanceForm()

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            employee = form.cleaned_data['employee']
            date = form.cleaned_data['date']

            attendance_exists = Attendance.objects.filter(
                employee=employee,
                date=date
            ).exists()

            if attendance_exists:

                return render(
                    request,
                    'attendance.html',
                    {
                        'form': form,
                        'error': 'Attendance already marked for this employee on this date'
                    }
                )

            form.save()

            return redirect('Attendance_list')

    return render(
        request,
        'attendance.html',
        {'form': form}
    )

def Attendance_list(request):

    attendance = Attendance.objects.all().order_by('-date')

    dates = Attendance.objects.values_list(
        'date',
        flat=True
    ).distinct().order_by('-date')

    return render(
        request,
        'attendance_list.html',
        {
            'attendance': attendance,
            'dates': dates
        }
    )

def Leave_request(request):

    form = LeaveForm()

    if request.method == 'POST':

        form = LeaveForm(request.POST)

        if form.is_valid():

            leave = form.save()

            return redirect(
                'Employee_profile',
                leave.employee.id
            )

    return render(
        request,
        'leave_request.html',
        {'form': form}
    )

def Approve_leave(request,id):

    leave = Leave_Request.objects.get(id=id)

    leave.status = "Approved"

    leave.save()

    return redirect('Leave_list')

def Reject_leave(request,id):

    leave = Leave_Request.objects.get(id=id)

    leave.status = "Rejected"

    leave.save()

    return redirect('Leave_list')

def Logout(request):

    request.session.flush()

    return redirect('Employee_login')


def Add_salary(request):

    form = SalaryForm()

    if request.method == 'POST':

        form = SalaryForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'Salary_list'
            )

    return render(
        request,
        'salary.html',
        {'form':form}
    )

def Salary_list(request):

    salary = Salary.objects.all()

    return render(
        request,
        'salary_list.html',
        {'salary':salary}
    )

def Leave_list(request):

    leave = Leave_Request.objects.all()

    return render(
        request,
        'leave_list.html',
        {'leave':leave}
    )