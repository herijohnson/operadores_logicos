# And = Para ser True todos tem que ser True
# Or = Para ser True pelo menos um deve ser True

print(True and True)
print(True and False)
print(False and False)
print(True or False)
print(True or False)
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)
