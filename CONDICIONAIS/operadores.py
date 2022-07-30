import random

nome = input()
idade = input()
idade = int(idade)
sexo = input()
tem_militar = bool(input())
quer_titulo_ou_tem_que_fazer = False

if(idade<16):
    print('Você não emitir o título')
elif(idade>=16 and idade<18):
    if(sexo == 'M' and tem_militar == 'False'):
        print('É preciso que você faça seu titulo militar')
    else:
        print('Você pode emitir o título caso queira')
        condicao = input('Você deseja emitir o titulo? SIM OU NÃO')
        if(condicao == 'SIM'):
            quer_titulo_ou_tem_que_fazer = True
elif idade>18:
    if(sexo == 'M' and tem_militar == 'Não'):
        print('É preciso que você faça seu titulo militar')
    else:
        print('Você tem a obrigação da emissão do título')
        quer_titulo_ou_tem_que_fazer = True
    
if quer_titulo_ou_tem_que_fazer:
    numero_titulo = random.random()
    print(f'SEU TÍTULO É: {numero_titulo}\nPARA: {nome}')
    