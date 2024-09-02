# importando/chamando o flet (e cores)
import flet as ft
from flet import colors

# lista de botões
botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
]

# executando a interface
def main(page: ft.Page):

    # atribuindo informações para a aplicação
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 270
    page.window_height = 400
    page.title = 'Calculadora'
    page.window_always_on_top = True
 
    # atribuindo informações das cores
    result = ft.Text(value = '0', color = colors.WHITE, size = 20)

    # criando a função de calcular dos botões
    def calculate():
        pass

    # criando ás funções do botões
    def select(e):
        value_at = result.value if result.value != '0' else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/','*','-','+','.'):
                value_at = value_at[-1]
            
            value = value_at + value

            if value[-1] in ('=','%',"±"):
                value = calculate()

        result.value = value
        result.update()

    # atribuindo posições
    display = ft.Row(
        width = 250,
        controls = [result],
        alignment = 'end'
    )
    
    # criando os botões
    btn = [ft.Container(
            content = ft.Text(value = btn['operador'], color = btn['fonte']),
            width = 50,
            height = 50,
            bgcolor = btn['fundo'],
            border_radius = 100,
            alignment = ft.alignment.center,
            on_click = select
        ) for btn in botoes]

    keyboard = ft.Row(
        width = 250,
        wrap = True,
        controls = btn,
        alignment = 'end'
    )
    
    # salvando os atributos
    page.add(display, keyboard)






# efetuando a aplicação do projeto
ft.app(target = main)

