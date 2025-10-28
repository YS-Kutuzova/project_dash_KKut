import dash_bootstrap_components as dbc
from dash import dcc, html

def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="🌦 Погодный дашборд 🌦",
            brand_href="#",
            color="success",
            className="mb-3"
        ),


        dbc.Row([
            dbc.Col([
                dbc.Input(id='city-input', value='Moscow', placeholder="Введите город", type='text', debounce=True),
            ], width=6, md=6, xs=12),
            dbc.Col([
                dbc.Card(id='weather-output', body=True),
            ], width=6, md=6, xs=12),
        ], className="mb-3"),
        dbc.Row([
            dbc.Col(dcc.Graph(id='temp-graph'), width=6, md=6, xs=12),
            dbc.Col(dcc.Graph(id='ap-graph'), width=6, md=6, xs=12),
        ], className="mb-3"),
        dbc.Row([
            dbc.Col(dcc.Graph(id='wind-dir-graph'), width=12, md=12),
        ], className="mb-3"),


        # Качество воздуха
        dbc.Row([
            dbc.Col([
                html.H3("Качество воздуха", className="text-center mb-4"),
                dbc.Row([
                    # PM2.5 и PM10
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("PM2.5", className="card-title"),
                                html.H2(id="pm25-value", children="--"),
                                html.P("μg/m³", className="card-text")
                            ])
                        ], color="light", className="h-100")
                    ], width=2, md=2, xs=6),
                    
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("PM10", className="card-title"),
                                html.H2(id="pm10-value", children="--"),
                                html.P("μg/m³", className="card-text")
                            ])
                        ], color="light", className="h-100")
                    ], width=2, md=2, xs=6),
                    
                    # CO и NO2
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("CO", className="card-title"),
                                html.H2(id="co-value", children="--"),
                                html.P("μg/m³", className="card-text")
                            ])
                        ], color="light", className="h-100")
                    ], width=2, md=2, xs=6),
                    
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("NO₂", className="card-title"),
                                html.H2(id="no2-value", children="--"),
                                html.P("μg/m³", className="card-text")
                            ])
                        ], color="light", className="h-100")
                    ], width=2, md=2, xs=6),
                    
                    # O3 и SO2
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("O₃", className="card-title"),
                                html.H2(id="o3-value", children="--"),
                                html.P("μg/m³", className="card-text")
                            ])
                        ], color="light", className="h-100")
                    ], width=2, md=2, xs=6),
                    
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("SO₂", className="card-title"),
                                html.H2(id="so2-value", children="--"),
                                html.P("μg/m³", className="card-text")
                            ])
                        ], color="light", className="h-100")
                    ], width=2, md=2, xs=6),
                ], className="mb-3"),
                
                # Индексы качества воздуха
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("🇺🇸 US-EPA Index", className="card-title"),
                                html.H2(id="us-epa-index", children="--", className="mb-2"),
                                html.P(id="us-epa-text", children="--", className="mb-0")
                            ])
                        ], color="secondary", className="h-100")
                    ], width=6, md=6, xs=12),
                    
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("🇬🇧 GB-DEFRA Index", className="card-title"),
                                html.H2(id="gb-defra-index", children="--", className="mb-2"),
                                html.P(id="gb-defra-text", children="--", className="mb-0")
                            ])
                        ], color="secondary", className="h-100")
                    ], width=6, md=6, xs=12),
                ])
            ], width=12)
        ], className="mb-3")

    ], fluid=True)