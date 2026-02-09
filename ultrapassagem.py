velocidade = float(input('Opa! O computador de bordo te pergunta, qual a velocidade atual desse carro?'))
kmPermitido = 80
# Valor de R$:7 para cada km acima do limite

if velocidade > 80:
    print(f'A velocidade está acima do limite permitido de {kmPermitido}km/h e por isso você foi multado! Reduza a velocidade imediatamente!')
    multa = (velocidade - kmPermitido) * 7
    print(f'Pela infração de trânsito, você deve pagar uma multa de R$ {multa:.2f}!')

elif velocidade == 80:
    print(f'Por favor, redobre sua atenção! O limite de velocidade é de {kmPermitido}km/h, e você está NO LIMITE! Reduza a velocidade imediatamente!')

else:
    print(f'Obrigado por responder, foi apenas um teste para a sua segurança e integridade. O carro está andando atualmente a {velocidade} km/h. Tenha uma Boa Viagem!')
