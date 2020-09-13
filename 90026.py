a1=input('please enter number x:')
a2=input('please enter number y:')
a3=input('please enter number z:')

a=(float(a1))
b=(float(a2))
c=(float(a3))

x=(b*b-4*a*c)
if x<=0:
    
    print('no solution')
    
else:
    
     x1=(-b+(b*b-4*a*c)**0.5)/(2*a) 
     x2=(-b-(b*b-4*a*c)**0.5)/(2*a)  
     print(x1,x2)