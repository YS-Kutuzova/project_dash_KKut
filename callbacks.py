from utils.data_loader import load_data
import plotly.graph_objects as go
from dash import Input, Output, html


def register_callbacks(app):
    
    @app.callback(
        Output('weather-output', 'children'),
        Output('temp-graph', 'figure'),
        Output('ap-graph', 'figure'),
        Output('wind-dir-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        # Если город не выбран, используем по умолчанию
        if not city:
            city = "Moscow"
        
        data = load_data(city)

        # Обрабатываем случай когда данные не загрузились
        if not data:
            error_fig = go.Figure()
            error_fig.add_annotation(
                text="❌ Не удалось загрузить данные о погоде",
                xref="paper", yref="paper",
                x=0.5, y=0.5, xanchor='center', yanchor='middle',
                showarrow=False,
                font=dict(size=16, color="red")
            )
            error_fig.update_layout(template='plotly')
            
            error_info = html.Div([
                html.H4("Ошибка"),
                html.P("Не удалось загрузить данные о погоде. Проверьте подключение к интернету.")
            ], style={'color': 'red', 'textAlign': 'center'})
            
            return error_info, error_fig, error_fig, error_fig

        # Создаем графики с реальными данными
        temp_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['temps'], mode='lines+markers')],
            layout=go.Layout(
                title="Температура по часам", 
                xaxis_title='Время', 
                yaxis_title='Температура (°C)',
                template='plotly'
            )
        )

        ap_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['ap'], mode='lines+markers')],
            layout=go.Layout(
                title="Атмосферное давление по часам",
                xaxis_title='Время',
                yaxis_title='АД (мм рт.ст.)',
                template='plotly'
            )
        )

        wind_dir_fig = go.Figure(
            data=[go.Scatterpolar(
                r=data['wind'],
                theta=data['wind_dirs'],
                mode='lines+markers',
            )]
        )
        
        wind_dir_fig.update_layout(
            title="Направление и скорость ветра (м/с)",
            template='plotly',
            polar=dict(
                angularaxis=dict(
                    direction="clockwise",
                    tickmode="array",
                    rotation=90,
                    tickvals=[0, 45, 90, 135, 180, 225, 270, 315],
                    ticktext=["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
                )
            )
        )

        weather_info = html.Div([
            html.H4(f"{data['city_name']}"),
            html.Img(src=f"https:{data['icon']}", style={'width': '64px', 'height': '64px'}),
            html.H5(f"{data['temp']}°C"),
            html.P(f"{data['condition']}")
        ], style={'textAlign': 'center'})
        
        return weather_info, temp_fig, ap_fig, wind_dir_fig
    

    # CALLBACK для качества воздуха
    @app.callback(
        [
            Output('pm25-value', 'children'),
            Output('pm10-value', 'children'),
            Output('co-value', 'children'),
            Output('no2-value', 'children'),
            Output('o3-value', 'children'),
            Output('so2-value', 'children'),
            Output('us-epa-index', 'children'),
            Output('gb-defra-index', 'children'),
            Output('us-epa-text', 'children'),
            Output('gb-defra-text', 'children')
        ],
        Input('city-input', 'value')
    )
    def update_air_quality(city):
        # Если город не выбран, используем по умолчанию
        if not city:
            city = "Moscow"
        
        try:
            data = load_data(city)
            
            # Проверяем, есть ли данные о качестве воздуха
            if not data or 'air_quality' not in data:
                return ["Н/Д"] * 10
            
            aq = data['air_quality']
            
            # Форматируем значения (округляем до 1 знака после запятой)
            pm25 = f"{aq.get('pm2_5', 0):.1f}"
            pm10 = f"{aq.get('pm10', 0):.1f}"
            co = f"{aq.get('co', 0):.1f}"
            no2 = f"{aq.get('no2', 0):.1f}"
            o3 = f"{aq.get('o3', 0):.1f}"
            so2 = f"{aq.get('so2', 0):.1f}"
            
            us_epa = aq.get('us-epa-index', 0)
            gb_defra = aq.get('gb-defra-index', 0)
            
            # Функция для текстового описания индекса из интеренета
            def get_quality_text(index):
                quality_map = {
                    1: "Хорошо",
                    2: "Умеренно", 
                    3: "Вредно для чувствительных групп",
                    4: "Вредно",
                    5: "Очень вредно",
                    6: "Опасно"
                }
                return quality_map.get(index, "Нет данных")
            
            return [
                pm25, pm10, co, no2, o3, so2,
                us_epa, gb_defra,
                get_quality_text(us_epa),
                get_quality_text(gb_defra)
            ]
            
        except Exception as e:
            print(f"Ошибка загрузки качества воздуха: {e}")
            return ["Ошибка"] * 10