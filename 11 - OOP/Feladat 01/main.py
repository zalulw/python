from negyzet import Negyzet

n: Negyzet = Negyzet()

n.oldal = 10

print(f"oldal = {n.oldal}")
print(f"T = {n.terulet()}")
print(f"K = {n.kerulet()}")