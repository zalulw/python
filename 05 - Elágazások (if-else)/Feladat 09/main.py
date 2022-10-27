from os import system

x:int = None
y:int = None

print("kérem az x értéket:", end='')
x=int(input())

print("kérem az y értéket", end='')
y=int(input())

if (x % y == 0):
    print("y osztója az x értéknek")
else: 
    print("y nem osztója az x értéknek")