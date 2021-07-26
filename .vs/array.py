def return_bits(a,b):
    y= a^b
    return y

def countDigitOne(n):
    countr = 0;
    for i in range(1, n + 1):
        print("value of i is"+str(i))
        str1 = str(i);
        print("value of str of i is"+ str(i))
        countr += str1.count("1");
        print("value of countr is: " + str(countr) +" and value of str1.count(1) is: "+ str(str1.count("1")) )
 
    return countr;

print(countDigitOne(return_bits(36,46)))