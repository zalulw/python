from computer import *
cpu: CPU() = CPU()
cpu.cores = 8

gpu: GPU() = GPU()
gpu.clockSpeed = 4500

ram: RAM() = RAM()
ram.capacity = 36

storage: Storage() = Storage()
storage.type = "SSD"

motherboard: Motherboard() = Motherboard()
motherboard.manufacturer = "Asus"

gep: computer = computer(cpu, gpu, ram, storage, motherboard)

print(gep)