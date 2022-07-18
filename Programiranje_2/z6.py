#Napisati rekurzivnu funkciju koja kao parametar prima string, a kao
#rezultat taj string ispisuje sa zada.

unesena_rijec = input("Unesite rijec:")
def obratna_rekurzija(unesena_rijec):
        if len(unesena_rijec)==1:
            return unesena_rijec
        return obratna_rekurzija(unesena_rijec[1::]) + unesena_rijec[0]

print(obratna_rekurzija(unesena_rijec))
