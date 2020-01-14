def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False       
    

print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
print(monkey_trouble(True, True))
print(monkey_trouble(False, False)) 
    
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


print(sum_double(2, 5))
print(sum_double(3, 3)) 

def diff21(n):
    if n > 21:
        return 2 * (n - 21)
    else:
        return 21 - n

print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(23)) 

def parrot_trouble(talking, hour):
    if talking:
        if hour < 7 or hour > 20:
            return True
        else:
            return False
    else:
        return False    

print(parrot_trouble(True, 5))
print(parrot_trouble(True, 7))
print(parrot_trouble(True, 21))
print(parrot_trouble(False, 6)) 

def makes10(a, b):
    if (a + b == 10) or (a == 10) or (b == 10):
        return True
    else:
        return False


print(makes10(6, 4))
print(makes10(6, 10))
print(makes10(6, 3))
print(makes10(6, 5))
print(makes10(10, 4)) 

def near_hundred(n):
    if n < 100:
        if 100 - n <= 10:
            return True
        else: 
            return False
    else:
        if n - 100 <= 10:
            return True
        else:
            if n < 200:
                if 200 - n <= 10:
                    return True
                else:
                    return False
            else:
               if n - 200 <= 10:
                   return True
               else:
                   return False         


print(near_hundred(103))
print(near_hundred(111))
print(near_hundred(89)) 

def pos_neg(a, b, negative):
    if negative:
        if a < 0 and b < 0:
            return True
        else:
            return False    
    else:
        if (a < 0 and b >= 0) or (a >= 0 and b < 0):
            return True
        else:
            return False    

print(pos_neg(1, -1, False))                   
print(pos_neg(-1, -1, False))
print(pos_neg(-11, 1, False))
print(pos_neg(1, -1, True))
print(pos_neg(-1, -1, True)) 

def not_string(str):
    if str.startswith("not"):
        return str
    else:
        return "not " + str

print(not_string("Ahmed")) 
print(not_string("not good"))         

def missing_char(str, n):
    if len(str) > 0 and n < len(str):
        result = ""
        i = 0
        while i < len(str):
            if i != n:
                result += str[i]
            i += 1
        return result    

print(missing_char("ABC", 1))
print(missing_char("", 1))        



def front_back(str):
     if len(str) <= 1:
         return str
     else:
         i = 0
         f = str[0]
         l = str[len(str) - 1]    
         body = ""
         while i < len(str):
             if i != 0 and i != len(str) - 1:
                 body += str[i]
             i += 1   
         return l + body + f

print(front_back("code"))      


def front3(str):
    if len(str) < 3:
        return str * 3
    else:
        return str[0:3] * 3


print(front3("ax"))            
