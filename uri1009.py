nome = str(input())
fixo = float(input())
venda = float(input())

print("TOTAL = R$ %.2f" % round((fixo+(0.15*venda)),4))
