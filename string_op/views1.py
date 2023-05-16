from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    return render(request,"string_op/home_page.html")

def rev_string(request):
    if request.method=="POST":
        input1=request.POST.get("string")
        s=input1
        s1=s[::-1]

        context={"input_string":s,"output_string":s1}
        return render(request,"string_op/rev_str_output.html",context)
    else:
        return render(request,"string_op/rev_str_input.html")
    
def pallindrome(request):
    if request.method=="POST":
        input1=request.POST.get("string")
        s=input1
        s1=s[::-1]
        context={"input_string":s,"output_string":s1}
        if s==s1:
            return render(request,"string_op/pallindrom/pallindrome_output.html",context)
        else:
            return HttpResponse(f"<h3> {s} is not a pallindrome string </h3>")
        
    else:
        return render(request,"string_op/pallindrom/pallindrome_input.html")
    
def word_count(request):
    if request.method=="POST":
        input1=request.POST.get("string")
        s=input1
        s=s.split(" ")
        context={}
        for i in s:
            if i in context.keys():
                context[i]+=1
            else:
                context[i]=1
        return HttpResponse(f'the word count of your string {context}')
    else:
        return render(request,"string_op/word_count/word_count_input.html")