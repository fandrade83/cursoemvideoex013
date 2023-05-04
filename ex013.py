salario = float(input('Qual é o salario do funcionario? R$ '))
novo = salario + (salario * 15 / 100)
print("Um funcionario que ganhava {:.2f},\ncom aumento de 15% vai receber R${:.2f}.".format(salario, novo))

