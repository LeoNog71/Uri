cod1,un1,valor1 = input().split(" ")

un1 = int(un1)
valor1 = float(valor1)

cod2,un2,valor2 = input().split(" ")

un2 = int(un2)
valor2 = float(valor2)

print("VALOR A PAGAR: R$ %.2f" % ((un1*valor1)+(un2*valor2)))


