#Napraviti generator funkcije za ispis svih parnih i svih neparnih
#brojeva manjih od prosljeđenog parametra.

def parni_brojevi(n):
    for i in range(n):
        if i%2==0:
            yield i
            
def neparni_brojevi(n):
    for i in range(n):
        if i%2==1:
            yield i

brojevi = int(input("Unesite brojeve: "))
generator_parnih = parni_brojevi(brojevi)
generator_neparnih = neparni_brojevi(brojevi)


for i in generator_parnih:
    print("Parni brojevi su:")
    print(next(generator_parnih))

for i in generator_neparnih:
    print("Neparni brojevi su:")
    print(next(generator_neparnih))
