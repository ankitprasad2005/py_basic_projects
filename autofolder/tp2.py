def fn1():
    n1 = 0
    if n1 <=5:
        print("a")
        n1 += 1
        fn1()
    else:
        print("b")
        n1 += 1
        fn1()
fn1()