# GIVEN:
p = 11
q = 5
e = 3

n = p*q
phi = (p-1)*(q-1)


def modular_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No mod inverse exists')
    return x%m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def lcm(a, b):
   # choosing the greater number
   if a > b:
       greater = a
   else:
       greater = b
   while(True):
       if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

val = lcm((p-1),(q-1))
d = modular_inverse(e,val)
d_phi = modular_inverse(e, phi)

print('####################### PART A ##############################')
print('P = {0} \t Q = {1} \t E = {2}'.format(p,q,e))
print('N = {0} \t t=lcm(p−1,q−1) \t D = {1} '.format(n,d))
print('####################### PART B ##############################')
print('P = {0} \t Q = {1} \t E = {2}'.format(p,q,e))
print('N = {0} \t t = Φ(n) = {1} \t\t D = {2} '.format(n,phi,d_phi))
