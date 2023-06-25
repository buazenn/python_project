from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
import matplotlib.pyplot as plt
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import WorkedList, PersonalData, WorkedTime, Statistic, NewsModel, Contribution, RetirementValue
# Create your views here.
#E:\project_venv\Scripts\activate
### LOGOWANIE SIE ###
def loginPage(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            messages.error(request, 'Username or password does not exist')


    context = {'page':page}
    return render(request, "html/login_register.html", context)

@login_required(login_url='login/')
## WYLOGOWANIE SIE ###
def logoutUser(request):
    logout(request)
    return redirect('login')

### REGISTER ###
def registerPage(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('register')
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('register')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Udało się zarejestrować!")
        return redirect('login')
    
    return render(request, 'html/login_register.html')

def home(request):
    return render(request, 'html/index.html')

@login_required
def index(request):
    personal_data = PersonalData.objects.get(user=request.user)
    worked_times = WorkedTime.objects.filter(user=request.user)
    worked_list = WorkedList.objects.filter(user=request.user)
    statistics = Statistic.objects.filter(user=request.user)
    news = NewsModel.objects.all()
    contributions = Contribution.objects.filter(user=request.user)

    # Obliczanie prognozy emerytury
    initial_capital_sum = sum(contribution.initial_capital for contribution in contributions)
    indexed_contributions_sum = sum(contribution.indexed_contributions for contribution in contributions)
    current_payment_sum = sum(contribution.current_payment for contribution in contributions)
    gross_salary_sum = sum(worked_time.gross_salary * worked_time.employment_period_months for worked_time in worked_times)
    contribution_amount_sum = sum(worked_time.contribution_amount * worked_time.employment_period_months for worked_time in worked_times)

    re_value = (
        initial_capital_sum + indexed_contributions_sum + current_payment_sum +
        (Decimal('0.5') * gross_salary_sum) + contribution_amount_sum
    )

    # Sprawdzanie wieku emerytalnego
    birth_year = personal_data.birth_date.year
    current_year = date.today().year
    age = current_year - birth_year

    # Obsługa wyjątku
    if age < 65:
        monthly_pension = "Nie przekroczono wieku emerytalnego"
    else:
        remaining_years = 109 - age  # Maksymalny wiek dożywotni (109 lat)
        remaining_months = remaining_years * 12  # Obliczanie pozostałych miesięcy życia
        monthly_pension = re_value / remaining_months  # Obliczanie miesięcznej emerytury
        monthly_pension = round(monthly_pension, 2)


    salaries = [worked_time.gross_salary for worked_time in worked_times]
    months = [worked_time.employment_period_months for worked_time in worked_times]
    labels = [f"{salary} ({month} months)" for salary, month in zip(salaries, months)]

    fig, ax = plt.subplots()
    ax.bar(labels, salaries)

    plt.xlabel('Salary (Months Worked)')
    plt.ylabel('Salary')
    plt.title('Salary per Months Worked')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/images/salary_chart.png')

    return render(request, 'html/home.html', {
        'personal_data': personal_data,
        'worked_list': worked_list,
        'worked_times': worked_times,
        'statistics': statistics,
        'news': news,
        'contributions': contributions,
        're_value': re_value,
        'monthly_pension': monthly_pension,
        "status_lables": ["new", "assigned", "in-progress", "waiting", "resolved", "waiting", "closed"],
        "status_count": [1, 2, 2, 1, 1, 2, 0]
    })

