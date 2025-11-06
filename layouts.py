import dash_bootstrap_components as dbc
from dash import dcc, html

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="Погодный дашборд",
            brand_href="#",
            color="primary",
            dark=True, 
            className="mb-3"
        ),

        dbc.Row([
            #Карточка города с текущими показателями
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                    html.H4(id='city-name', children="--", className="mb-2", style={'fontSize': '26px', 'textAlign': 'center'}),
                                    html.P(id='weather-condition', children="--", className="mb-2", style={'fontSize': '18px', 'textAlign': 'center'}),
                                    html.Div([
                                        html.Img(id='weather-icon', style={'width': '60px', 'height': '60px'}),
                                    ], className="d-flex justify-content-center"),
                                ]),
                            ], width=6),
                            dbc.Col([
                                html.Div([
                                    html.H5("Температура", className="mb-0"),
                                    html.H4([
                                        html.Span(id='temperature', children="--", style={'fontWeight': 'normal', 'fontSize': '20px'}),
                                        html.Span("°C", style={'fontSize': '18px', 'marginLeft': '5px', 'fontWeight': 'normal'})
                                    ], className="mb-1"),
                                ], className="text-center"),
                                
                                #Пустая строка между температурой и ветром, чтобы все не сливалось в кучу
                                html.Div(style={'height': '30px'}),
                                
                                html.Div([
                                    html.H5("Ветер", className="mb-0"),
                                    html.H4([
                                        html.Span(id='wind-speed', children="--", style={'fontWeight': 'normal', 'fontSize': '20px'}),
                                        html.Span("м/с", style={'fontSize': '18px', 'marginLeft': '5px', 'fontWeight': 'normal'})
                                    ], className="mb-1"),
                                ], className="text-center"),
                            ], width=6),
                        ])
                    ])
                ], color="light", className="h-100")
            ], width=6, md=6, xs=12),
            #Поле для ввода названия города
            dbc.Col([
                html.Div([
                    html.H5("Выберите город", className="mb-3"),
                    dbc.Input(
                        id='city-input', 
                        value='Moscow', 
                        placeholder="Введите город", 
                        type='text', 
                        debounce=True,
                        className="mb-0"
                    ),
                ], className="p-3 bg-light rounded h-100")
            ], width=6, md=6, xs=12),
            ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H5("Настройки отображения", className="mb-3"),
                    
                    # Простой выбор периода времени
                    html.Div([
                        html.Label("Временной интервал:", className="fw-bold mb-2"),
                        dbc.RadioItems(
                            id='time-period',
                            options=[
                                {'label': 'Весь день (00:00-23:59)', 'value': 'full_day'},
                                {'label': 'Ночь (00:00-06:00)', 'value': 6},
                                {'label': 'Утро (06:00-12:00)', 'value': 12},
                                {'label': 'День (12:00-18:00)', 'value': 18},
                                {'label': 'Вечер (18:00-00:00)', 'value': 24}
                            ],
                            value=24,
                            inline=True,
                            className="mb-3"
                        ),
                    ]),
                    
                    # Переключатель для сглаживания данных
                    dbc.Checklist(
                        options=[
                            {"label": " Сглаживать линии графиков", "value": 1}
                        ],
                        value=[],
                        id="smooth-data",
                        switch=True,
                    ),
                ], className="p-3 bg-light rounded")
            ], width=12, className="mb-4"),
        ], className="mb-4"),
            
        # Теперь отображаем качество воздуха по часам и по различным показателям
        dbc.Row([
            dbc.Col([
                html.H3("Качество воздуха", className="text-center mb-4")])]),

        # График CO - угарный газ        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='co-graph', style={'height': '400px'})
                    ])
                ], className="h-100", style={'height': '450px'})
            ], width=4, md=4, xs=12),

            # График NO2 - диоксид азота
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='no2-graph', style={'height': '400px'})
                    ])
                ], className="h-100", style={'height': '450px'})
            ], width=4, md=4, xs=12),

            # График O3 - озон   
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='o3-graph', style={'height': '400px'})
                    ])
                ], className="h-100", style={'height': '450px'})
            ], width=4, md=4, xs=12),
        ], className="mb-4"),
        
        # График SO2 - диоксид серы
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='so2-graph', style={'height': '400px'})
                    ])
                ], className="h-100", style={'height': '450px'})
            ], width=4, md=4, xs=12),

            # График PM2.5 - мелкие твердые частицы    
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='pm25-graph', style={'height': '400px'})
                    ])
                ], className="h-100", style={'height': '450px'})
            ], width=4, md=4, xs=12),

            #График PM10 - крупные твердые частицы   
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(id='pm10-graph', style={'height': '400px'})
                    ])
                ], className="h-100", style={'height': '450px'})
            ], width=4, md=4, xs=12),
        ], className="mb-4")
    ], fluid=True)
