import dash_bootstrap_components as dbc
from dash import dcc, html

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="Погодный дашборд",
            brand_href="#",
            color="success",
            className="mb-3"
        ),

        dbc.Row([
            dbc.Col([
                dbc.Input(id='city-input', value='Moscow', placeholder="Введите город", type='text', debounce=True),
            ], width=12),
        ], className="mb-3"),
            

        # Так как я решила оставить данные о погодных условиях, 
        # то я меняю графики из изначального представления в карточки с основной информацией
        dbc.Row([
            # Карточка города и состояния
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4(id='city-name', children="--"),
                        html.Img(id='weather-icon', style={'width': '64px', 'height': '64px'}),
                        html.P(id='weather-condition', children="--")
                    ])
                ], color="light", className="h-100")
            ], width=4),
            
            # Карточка температуры
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Температура"),
                        html.H2(id='temperature', children="--"),
                        html.P("°C")
                    ])
                ], color="light", className="h-100")
            ], width=4),
            
            # Карточка скорости ветра
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Ветер"),
                        html.H2(id='wind-speed', children="--"),
                        html.P("м/с")
                    ])
                ], color="light", className="h-100")
            ], width=4),
        ], className="mb-4"),

        # Тепепрь отображаем качество воздуха по часам и по различным показателям

        dbc.Row([
            dbc.Col([
                html.H3("Качество воздуха", className="text-center mb-4"),
                
                # График PM2.5 - мелкие твердые частицы
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='pm25-graph')
                    ])
                ], className="mb-3"),
                
                # График PM10 - крупные твердые частицы
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='pm10-graph')
                    ])
                ], className="mb-3"),
                
                # График CO - угарный газ
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='co-graph')
                    ])
                ], className="mb-3"),
                
                # График NO2 - диоксид азота
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='no2-graph')
                    ])
                ], className="mb-3"),
                
                # График O3 - озон
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='o3-graph')
                    ])
                ], className="mb-3"),
                
                # График SO2 - диоксид серы
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='so2-graph')
                    ])
                ], className="mb-3"),
            ], width=12)
        ])
    ], fluid=True)
