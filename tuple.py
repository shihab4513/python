# Tuple
# Tuple is similar to list one difference is you cant change it
mobile=("Nokia",5,5,9,80,"sumsung","apple",5,7,8,9,6,5,2,3,1);
# You cant change tuple its like constant version of array/list in python
# mobile[0]="Samsung";
print(type(mobile),mobile);
# You can check whether a value is in tuple or not
if "Nokia" in mobile:
    print("Yes Nokia is present in mobile")

# slicing possible in tuple.It wont alter original tuple instead it will

mobile2=mobile[0:6]
print(mobile2)
