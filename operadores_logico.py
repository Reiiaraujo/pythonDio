#Na condição and para ser True, tudo tem que ser True
#Ou Apenas um tem que ser True
print(True and True)
print(True and False)
print(True and False)
print(True or True)
print(True or False)
print( False or False)

saldo = 1000;
saque = 200;
limite = 100;
conta_especial = True;



print (saldo >= saque and saque <= limite)


conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite;
conta_especiao_com_saldo_suficiente = conta_especial and saldo >= saque;

exp_3 = conta_especiao_com_saldo_suficiente or conta_normal_com_saldo_suficiente
print(f"A conta está apta para saque {exp_3}")