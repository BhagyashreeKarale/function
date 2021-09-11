def greet(*names):#this is arbitrary argument. it is used when we aren't sure about number of arguments
    for name in names:
               print("Hello", name)
greet("sonu", "kartik", "umesh", "bijender")#it will print "hello" with each name separately
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<output>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# Hello sonu
# Hello kartik
# Hello umesh
# Hello bijender