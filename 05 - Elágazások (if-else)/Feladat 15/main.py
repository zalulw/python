from os import system
#eloetel
zoldsegleves : bool = False
husleves : bool = False
gyumolcsleves: bool = False
#foetel
csirkecomb: bool = False
csirkemell:bool = False
rakottzoldseg: bool = False
spagetti: bool = False
pizza: bool = False
#koret
rizs: bool = False
paroltzoldseg: bool = False
gyumolcs: bool = False
sultkrumpli: bool = False
salata: bool = False
kola: bool = False
#valasztas
eloetel: int = None
foetel: int = None
koret: int = None


print("a mai menü: \n Előételek: \n Zoldsegleves [1] \n Husleves [2] \n Gyumolcsleves [3]")
eloetel=int(input())
if (eloetel == 1):
    zoldsegleves:bool = True

elif(eloetel == 2):
    husleves:bool=True

elif(eloetel == 3):
    gyumolcsleves:bool=True

print("Főételek: \n Csirkecomb [1] \n Csirkemell [2] \n Rakottzoldseg [3] \n spagetti [4] \n pizza [5]")
foetel=int(input())
if (foetel == 1):
    csirkecomb:bool=True

elif (foetel == 2):
    csirkemell:bool=True

elif (foetel == 3):
    rakottzoldseg:bool=True

elif (foetel == 4):
    spagetti:bool=True

elif (foetel == 5):
    pizza:bool=True

print("Köretek: \n Rizs [1]\n Paroltzoldseg [2]\n Gyumolcs [3]\n Sultkrumpli [4]\n Salata [5]\n Kola [6]")
koret=int(input())
if (koret == 1):
    Rizs:bool=True

elif (koret == 2):
    paroltzoldseg:bool = True

elif (koret == 3):
    gyumolcs:bool=True

elif (koret == 4):
    sultkrumpli:bool=True

elif (koret == 5):
    salata:bool=True

elif (koret == 6):
    kola:bool = True


if (zoldsegleves and spagetti and (gyumolcs or salata) and (pizza != True and rakottzoldseg != True)):
    print("kivalo ertekelesu menu")

elif (zoldsegleves and csirkemell and rizs and sultkrumpli != True):
    print("fitnessz menu")

elif (husleves and csirkecomb and (sultkrumpli and salata) and (pizza != True and rakottzoldseg != True)):
    print("vasarnapi menu")

elif ((pizza or spagetti) and (gyumolcs or kola) and (rakottzoldseg != True and paroltzoldseg != True)):
    print("napi menu") 