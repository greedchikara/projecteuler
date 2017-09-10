# https://projecteuler.net/problem=2
ppe = 0
pe  = 2
sum = ppe + pe;
while(sum < 4000000):
    ne = 4 * pe + ppe;
    ppe = pe;
    pe = ne;
    sum = sum + ne;

print sum

# 4613732
