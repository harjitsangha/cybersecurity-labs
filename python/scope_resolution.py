# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) local -> enclosed -> global -> built-in

def fun1():
    a = 1
    print(a)

def fun2():
    b = 2
    print(b)

fun1()
fun2()