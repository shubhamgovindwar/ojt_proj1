def reverse_number(n):
    n1=n
    rev_no=0
    while n1>=1:
        rem=n1%10
        n1=n1//10
        rev_no=rev_no*10+rem
    
    return rev_no