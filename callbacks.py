from utils.data_loader import load_data
import plotly.graph_objects as go
from dash import Input, Output, html


def register_callbacks(app):
    
    @app.callback([
        Output('city-name', 'children'),
        Output('weather-icon', 'src'),
        Output('weather-condition', 'children'),
        Output('temperature', 'children'),
        Output('wind-speed', 'children'),
        Output('pm25-graph', 'figure'),
        Output('pm10-graph', 'figure'),
        Output('co-graph', 'figure'),
        Output('no2-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure')],
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        # Если город не выбран
        if not city:
            city = "Moscow"
        
        data = load_data(city)

        # Обрабатываем когда данные не загрузились
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

        # Создаем графики
        # График PM2.5
        pm25_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['pm25_hours'], mode='lines+markers')],
            layout=go.Layout(
                title="PM2.5 (Мелкие твердые частицы ≤2.5µm)",
                xaxis_title='Время',
                yaxis_title='Концентрация (µg/m³)',
                template='plotly'
            )
        )

        # График PM10
        pm10_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['pm10_hours'], mode='lines+markers')],
            layout=go.Layout(
                title="PM10 (Крупные твердые частицы ≤10µm)",
                xaxis_title='Время',
                yaxis_title='Концентрация (µg/m³)',
                template='plotly'
            )
        )

        # График CO
        co_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['co_hours'], mode='lines+markers')],
            layout=go.Layout(
                title="CO (Угарный газ)",
                xaxis_title='Время',
                yaxis_title='Концентрация (µg/m³)',
                template='plotly'
            )
        )

        # График NO2
        no2_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['no2_hours'], mode='lines+markers')],
            layout=go.Layout(
                title="NO2 (Диоксид азота)",
                xaxis_title='Время',
                yaxis_title='Концентрация (µg/m³)',
                template='plotly'
            )
        )

        # График O3
        o3_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['o3_hours'], mode='lines+markers')],
            layout=go.Layout(
                title="O3 (Озон)",
                xaxis_title='Время',
                yaxis_title='Концентрация (µg/m³)',
                template='plotly'
            )
        )

        # График SO2
        so2_fig = go.Figure(
            data=[go.Scatter(x=data['hours'], y=data['so2_hours'], mode='lines+markers')],
            layout=go.Layout(
                title="SO2 (Диоксид серы)",
                xaxis_title='Время',
                yaxis_title='Концентрация (µg/m³)',
                template='plotly'
            )
        )

        return [
            data['city_name'],
            f"https:{data['icon']}",
            data['condition'],
            data['temp'],
            data['wind_speed'],
            pm25_fig,
            pm10_fig, 
            co_fig,
            no2_fig,
            o3_fig,
            so2_fig
            
        ]
