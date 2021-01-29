from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        FIRST_YEAR = int(request.POST['first'])
        SECOND_YEAR = int(request.POST['second'])
        THIRD_YEAR = int(request.POST['third'])
        FOURTH_YEAR = int(request.POST['fourth'])
        f1 = FIRST_YEAR/4
        f2 = SECOND_YEAR/2
        f3 = (THIRD_YEAR/4)*3
        f4 = FOURTH_YEAR
        TOTAL_MARKS = f1 + f2 + f3 + f4
        TOTAL_PERCENTAGE = ((TOTAL_MARKS/4950)*100)
        tax = round(TOTAL_PERCENTAGE, 2)
        return render(request, 'index.html',{'TOTAL_PERCENTAGE':tax})
    else:
        return render(request,'index.html')
