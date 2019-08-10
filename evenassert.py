def assertioneven(list1):
    for i in list1:
        assert (i%2==0),"not even"
    print("all are even")
list1=[2,4,6,8]
assertioneven(list1)
