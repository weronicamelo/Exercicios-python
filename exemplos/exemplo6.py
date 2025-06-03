idade = int(input("Digite sua idade: "))
assinatura = int(input("Você tem assinatura premium:\n0.Não \n1.Sim\n"))

if idade >= 18 and assinatura == 1:
    print("Acesso ilimitado a todo conteúdo premium.")
elif idade >= 18:
    print("Acesso limitado. Considere assinar o plano premium para mais benefícios.")
else:
    print("Acesso restrito ao conteúdo (18+).")