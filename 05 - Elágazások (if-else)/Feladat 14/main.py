from os import system

x: int = None
y: int = None
z: int = None

print("kérem az x értéket:", end='')
x=int(input())

print("kérem az y értéket:", end='')
y=int(input())

print("kérem az z értéket:", end='')
z=int(input())

if (x % y == 0 and x % z == 0):
    print("az x érték az y és a z értékkel is osztható")
elif (x % y == 0 and x % z != 0):
    print("az x érték csak az y értékkel osztható")
elif (x % y != 0 and x % z == 0):
    print("az x érték csak a z értékkel osztható")
else: 
    print("az x érték nem osztható")