# Solicitar ao usuário que insira as notas até que -1 seja digitado
while nota != -1:
    nota = float(input("Insira a nota (ou -1 para finalizar): "))
    if nota != -1:
        notas.append(nota)

# Remover o -1 da lista, se presente
if -1 in notas:
    notas.remove(-1)

# Calcular a média das notas
if notas:
    media = sum(notas) / len(notas)
else:
    media = 0

# Verificar se o aluno foi aprovado ou reprovado
resultado = "Aprovado" if media >= 7 else "Reprovado"

# Imprimir o resultado
print("Média das notas:", media)
print("Situação do aluno:", resultado)







