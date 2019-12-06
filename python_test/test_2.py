
# NOTE : Viết một chương trình có thể tính giai thừa của một số cho trước

num = 3

def fact (x):
    if x == 0 :
        return 1
    else:
        t = x*fact(x-1)
        return t

print (fact(num))

            
