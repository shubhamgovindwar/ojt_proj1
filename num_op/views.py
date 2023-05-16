from django.shortcuts import render,HttpResponse
from num_op.rough import *

# Create your views here.
def num_home(request):
    return render(request,"num_op/num_home.html")
def num_rev(request):
    if request.method=="POST":
        s=int(request.POST.get("num"))
        s1=s
        s2=0
        while s1 >=1:
            rem=s1%10
            s2=s2*10+rem
            s1=s1//10
        context={"input_number":s,"output_number":s2}
        return render(request,"num_op/rev_num/rev_num_output.html",context)
    
    else:
        return render(request,"num_op/rev_num/rev_num_input.html")
def len_number(n):
    s1=n
    count=0
    while s1>=1:
        s1=s1//10
        count+=1
    return count

def amstrong_num(request):
    if request.method=="POST":
        s=request.POST.get("num")
        pow=len(str(s))
        s1=int(s)
        sum=0
        while s1>=1:
            rem=s1%10
            sum=sum+rem**pow
            s1=s1//10

        context={"input_number":s,"output_number":sum}

        if int(s)==sum:
            return render(request,"num_op/amstrong/amstrong_output.html",context)
        else:
            return HttpResponse(f"{s} is not equals to the prevoious {sum} tahts why its NOT amstrong number")
        
    else:
        return render(request,"num_op/amstrong/amstrong_input.html")


def num_pallindrome(request):
    if request.method=="POST":
        s=request.POST.get("num")
        s1=int(s)
        sum=0
        while s1>=1:
            rem=s1%10
            s1=s1//10
            sum=sum*10+rem
        
        context={"input_number":int(s),"output_number":sum}

        return render(request,"num_op/pallindrome/pal_output.html",context)
    else:
        return render(request,"num_op/pallindrome/pal_input.html")
    

    # def rev_numa(request):
    #     if request.method=="POST":
    #         s=request.POST.get("num")
    #         rev_no=reverse_number(s)
    #         dict1={"s":s,"r":rev_no}
    #         return HttpResponse(f"dict1")
    #     else:
    #         return HttpResponse(f'<input type="integer" name="num"> enter the number')

        