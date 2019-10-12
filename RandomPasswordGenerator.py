import string

def randomString_typeA(stringLength=16):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", randomString() )
print ("Random String is ", randomString() )
print ("Random String is ", randomString() )

def randomString_typeB(stringLength=16):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomString_typeC(stringLength=16):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomString_typeD(stringLength=16):
    letters = string.ascii_letters + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomString_typeE(stringLength=16):
    letters = string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomString_typeF(stringLength=16):
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomString_typeG(stringLength=16):
    letters = string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))


print ("Random String is ", randomString_typeA() )
print ("Random String is ", randomString_typeB() )
print ("Random String is ", randomString_typeC() )
print ("Random String is ", randomString_typeD() )
print ("Random String is ", randomString_typeE() )
print ("Random String is ", randomString_typeF() )
print ("Random String is ", randomString_typeG() )
