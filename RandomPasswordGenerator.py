import random
import string

def randomString_typeA(stringLength=16):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
    
print ("Random String is ", randomString() )
print ("Random String is ", randomString() )
print ("Random String is ", randomString() )
