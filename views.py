from django.shortcuts import render

# Function for calculate the percentage
def index(request):
    if request.method == 'POST':
        FIRST_YEAR = int(request.POST['first'])
        SECOND_YEAR = int(request.POST['second'])
        THIRD_YEAR = int(request.POST['third'])
        FOURTH_YEAR = int(request.POST['fourth'])
        """For calculate the final percentage we take 25% of 1st year,
           50% of 2nd year,75% of 3rd year and 100% of final year
        """
        f1 = FIRST_YEAR/4 #RETURN 25% OF FIRST_YEAR
        f2 = SECOND_YEAR/2 #RETURN 50% OF SECOND_YEAR
        f3 = (THIRD_YEAR/4)*3 #RETURN 75% OF THIRD_YEAR
        f4 = FOURTH_YEAR # ITS ALSO 100% RETURN
        TOTAL_MARKS = f1 + f2 + f3 + f4
        TOTAL_PERCENTAGE = ((TOTAL_MARKS/4950)*100)
        t = round(TOTAL_PERCENTAGE, 2)            #For roundoff the decimal values upto 2 point
        return render(request, 'index.html',{'TOTAL_PERCENTAGE':t})
    return render(request,'index.html')
