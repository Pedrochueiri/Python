nm = input('Digite o nome do vendedor: ')
cd = int(input('Digite o códiga da peça: '))
vu = float(input('Digite o valor unitáro da peça: '))
qt = int(input('Digite a quantidade vendida: '))

comissao = (vu*qt)*5/100

print(f"nome do funcionario: {nm} \nCodigo de peça: {cd} \nTotal vendido: {qt} \nComissão:  {comissao}")

