import plotly.graph_objects as go

#настройка дизайна графиков
GRAPH_TITLE_FONT_SIZE = 16
GRAPH_FONT_FAMILY = 'Inter, Arial, sans-serif'
GRAPH_FONT_SIZE = 12

PLOT_BACKGROUND_COLOR = '#ffffff'
PAPER_BACKGROUND_COLOR = '#ffffff'

MY_PALETTE = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

#Цвета для показателей в разбивке
POLLUTANT_COLORS = {
    'pm25': MY_PALETTE[3],  #красный
    'pm10': MY_PALETTE[4],  #фиолетовый
    'co': MY_PALETTE[0],    #синий
    'no2': MY_PALETTE[1],   #оранжевый
    'o3': MY_PALETTE[2],    #зеленый
    'so2': MY_PALETTE[5]    #коричневый
}

NAVBAR_COLOR = '#2c5aa0'
NAVBAR_TEXT_COLOR = '#ffffff'
CARD_HEADER_BG = '#3498db'
CARD_HEADER_TEXT = '#ffffff'
ACCENT_COLOR = '#e74c3c'
