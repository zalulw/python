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

eloetel: str = None
foetel: str = None
koret: str = None

valtozas: int = None


print("a mai menü: \n Előételek: \n Zoldsegleves [1] \n Husleves [2] \n Gyumolcsleves [3]")
valtozas=int(input())
if (valtozas == 1):
    zoldsegleves:bool = True

elif(valtozas == 2):
    husleves:bool=True

elif(valtozas == 3):
    gyumolcsleves:bool=True



print("Főételek: \n Csirkecomb [1] \n Csirkemell [2] \n Rakottzoldseg [3] \n spagetti [4] \n pizza [5]")
foetel=str(input())



print("Köretek: \n Rizs [1]\n Paroltzoldseg [2]\n Gyumolcs [3]\n Sultkrumpli [4]\n Salata [5]\n Kola [6]")
koret=str(input())






