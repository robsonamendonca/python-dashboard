import math

from rich import print
from rich.prompt import Prompt
from rich.progress import track
from rich.console import Console
from time import sleep
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel

console = Console()
prompt = Prompt()
continuar = True 
numero_de_latas_f  = 0
numero_de_galoes_f  = 0
numero_de_galoes  = 0
valor_com_apenas_latas  = 0
valor_com_apenas_galoes  = 0
valor_de_latas = 0
numero_de_latas  = 0
valor_com_galoes  = 0
valor_total = 0
console.clear()
console.log('')
console.log('### Calcular quanta tinta comprar para pintar uma certa metragem  ###')
console.log('')

while continuar == True:
    preco_lata_18l = int(prompt.ask('[green]Digite o Valor (R$) da Lata de Tinta de [bold]18L[/]: [/]'))
    resposta = prompt.ask(
        f'Você digitou [red]{preco_lata_18l}[/], este preço está correto?')
    if resposta.lower() in ('s', 'sim'):
        print('ótimo')
        continuar = False
    elif resposta.lower() in ('n', 'não'):
        print('reiniciando...')
    else:
        print('Digite apenas [red]"s"[/] ou [red]"n"[/]')
    preco_galao_3l = int(prompt.ask('[green]Digite o Valor (R$) da Galão de Tinta de [bold]3.6L[/]: [/]'))
    resposta = prompt.ask(
        f'Você digitou [red]{preco_galao_3l}[/], este preço está correto?')
    if resposta.lower() in ('s', 'sim'):
        print('ótimo')
        continuar = False
    elif resposta.lower() in ('n', 'não'):
        print('reiniciando...')
    else:
        print('Digite apenas [red]"s"[/] ou [red]"n"[/]')

area_a_ser_pintada = int(prompt.ask('[green]Digite a área, a ser realizada a pintura em metros quadrados (m2)[/]'))

def calculando_preco():
    global numero_de_latas_f 
    global numero_de_galoes_f 
    global numero_de_galoes 
    global valor_com_apenas_latas 
    global valor_com_apenas_galoes 
    global valor_de_latas
    global numero_de_latas 
    global valor_com_galoes 
    global valor_total     
    console.log('Calculando... área a ser pintada com folga.')
    area_com_folga = area_a_ser_pintada * 1.1
    litros_por_metro = 6
    sleep(1)
    console.log('Calculando... litros a serem usados.')
    litros_a_serem_usados = area_com_folga / litros_por_metro
    litros_por_lata = 18
    sleep(1)
    console.log('Calculando... valor usando latas de 18 litros.')
    numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_lata)
    valor_com_apenas_latas = numero_de_latas * preco_lata_18l 
    numero_de_latas_f = numero_de_latas 
    sleep(1)
    console.log('Calculando... valor usando galões de 3.6 litros.')
    litros_por_galao = 3.6
    numero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
    valor_com_apenas_galoes = numero_de_galoes * preco_galao_3l
    numero_de_galoes_f = numero_de_galoes
    sleep(1)
    console.log('Calculando... compra de tinta otimizada por valor.')
    numero_de_latas = math.floor(litros_a_serem_usados / litros_por_lata)
    valor_de_latas = numero_de_latas * preco_lata_18l
    litros_faltantes = litros_a_serem_usados % litros_por_lata
    numero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)
    valor_com_galoes = numero_de_galoes * preco_galao_3l
    valor_total = valor_de_latas + valor_com_galoes
    sleep(2)
    console.log('calculos realizados com sucesso')

with console.status('[green]Realizando os devidos calculos[/]') as status:
    calculando_preco()

#print(f'Você deverá usar {numero_de_latas} latas de 18 litros mais {numero_de_galoes} galões de 3.6 litros, no valor de R$ {valor_total}')

print('[green]O Calculo está pronto para sua analise![/]')

table = Table(title='Opções Disponíveis')
table.add_column("Qtd. Latas(18L)")
table.add_column("Valor R$ ", justify="right")
table.add_column("Qtd. Galões(3.6L)")
table.add_column("Valor R$", justify="right")
table.add_column("Total R$", justify="right")

table.add_row(str(numero_de_latas_f),str(valor_com_apenas_latas), str(0), str(0),str(valor_com_apenas_latas))
table.add_row(str(0),str(0), str(numero_de_galoes_f), str(valor_com_apenas_galoes),str(valor_com_apenas_galoes))
table.add_row(str(numero_de_latas),str(valor_de_latas), str(numero_de_galoes), str(valor_com_galoes),str(valor_de_latas+valor_com_galoes))


print(table)

nome = input('Digite seu nome para finalizar: ')

print(
    f'[on blue][yellow]Parabéns [white]{nome}[/], você deverá usar {numero_de_latas} latas de 18 litros mais {numero_de_galoes} galões de 3.6 litros, no valor de R$  [green]{valor_total}[/][/][/]')

console.log('')
console.log('')    