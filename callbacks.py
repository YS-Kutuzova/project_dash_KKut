from utils.data_loader import load_data
import design as ds
import plotly.graph_objects as go
import plotly.io as pio
from dash import Input, Output, html
import dash_bootstrap_components as dbc

# устанавливаем наш Plotly с нашей палитрой
pio.templates['custom'] = pio.templates['plotly'].update(
    layout=dict(colorway=ds.MY_PALETTE)
)
pio.templates.default = 'custom'

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
        [Input('city-input', 'value'),
         Input('time-period', 'value'),
         Input('smooth-data', 'value')]
    )
    def update_dashboard(city, time_period, smooth_data):
        #Если город не выбран
        if not city:
            city = "Moscow"
        
        data = load_data(city)

        # Обрабатываем когда данные не загрузились
        if not data:
            error_fig = create_error_figure("Не удалось загрузить данные о погоде")
            
            error_info = "Ошибка"
            return [error_info, "", "Нет данных", "--", "--", 
                   error_fig, error_fig, error_fig, error_fig, error_fig, error_fig]

        # Применяем реальные фильтры к данным
        filtered_data = apply_time_filter(data, time_period, smooth_data)

        # Создаем графики с учетом фильтров
        pm25_fig = create_pollutant_chart(filtered_data, 'pm25', "PM2.5", "Мелкие твердые частицы ≤2.5µm", smooth_data)
        pm10_fig = create_pollutant_chart(filtered_data, 'pm10', "PM10", "Крупные твердые частицы ≤10µm", smooth_data)
        co_fig = create_pollutant_chart(filtered_data, 'co', "CO", "Угарный газ", smooth_data)
        no2_fig = create_pollutant_chart(filtered_data, 'no2', "NO2", "Диоксид азота", smooth_data)
        o3_fig = create_pollutant_chart(filtered_data, 'o3', "O3", "Озон", smooth_data)
        so2_fig = create_pollutant_chart(filtered_data, 'so2', "SO2", "Диоксид серы", smooth_data)

        # Возвращаем оригинальные данные для погодной информации
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

def apply_time_filter(data, time_period, smooth_data):
    #Фильтрация данных по времени суток
    filtered_data = data.copy()
    
    # без фильтов по времени 
    if time_period == 'full_day':
        return filtered_data
    
    if 'hours' in data and data['hours']:
        # Получаем все часы и находим соответствующие индексы
        all_hours = data['hours']
        filtered_indices = []
        
        for i, hour_str in enumerate(all_hours):
            try:
                # Парсим час из строки
                hour = int(hour_str.split(':')[0])
                
                # Фильтруем по выбранному интервалу, выделила по часам, без мину 
                if time_period == 6 and 0 <= hour < 7:  
                    filtered_indices.append(i)
                elif time_period == 12 and 6 <= hour < 13: 
                    filtered_indices.append(i)
                elif time_period == 18 and 12 <= hour < 19: 
                    filtered_indices.append(i)
                elif time_period == 24 and 18 <=hour <= 24:
                    filtered_indices.append(i)
            except (ValueError, IndexError):
                continue
        
        # Применяем фильтр только к часовым данным
        if filtered_indices:
            filtered_data['hours'] = [all_hours[i] for i in filtered_indices]
            
            pollutants = ['pm25', 'pm10', 'co', 'no2', 'o3', 'so2']
            for poll in pollutants:
                key = f'{poll}_hours'
                if key in data:
                    filtered_data[key] = [data[key][i] for i in filtered_indices]
    
    return filtered_data

def create_error_figure(message):
    #Создает график с сообщением об ошибке
    error_fig = go.Figure()
    error_fig.add_annotation(
        text=message,
        xref="paper", yref="paper",
        x=0.5, y=0.5, xanchor='center', yanchor='middle',
        showarrow=False,
        font=dict(size=16, color="red")
    )
    error_fig.update_layout(
        template='plotly',
        plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
        paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
        height=400,
        margin=dict(l=50, r=50, t=60, b=50)
    )
    return error_fig

def create_pollutant_chart(data, pollutant, short_name, description, smooth_data):
    #Создает график для конкретного загрязнителя
    fig = go.Figure()
    
    hours = data['hours']
    values = data.get(f'{pollutant}_hours', [])
    
    if not values:
        fig.add_annotation(
            text="Нет данных",
            xref="paper", yref="paper",
            x=0.5, y=0.5, xanchor='center', yanchor='middle',
            showarrow=False,
            font=dict(size=16, color="gray")
        )
    else:
        # Сглаживание данных (проба)
        if smooth_data and len(values) > 1:
            smoothed_values = []
            for i in range(len(values)):
                if i == 0:
                    smoothed_values.append((values[i] + values[i+1]) / 2)
                elif i == len(values) - 1:
                    smoothed_values.append((values[i-1] + values[i]) / 2)
                else:
                    smoothed_values.append((values[i-1] + values[i] + values[i+1]) / 3)
            
            display_values = smoothed_values
            line_style = dict(color=ds.POLLUTANT_COLORS[pollutant], width=3)
        else:
            display_values = values
            line_style = dict(color=ds.POLLUTANT_COLORS[pollutant], width=2)
        
        fig.add_trace(go.Scatter(
            x=hours, 
            y=display_values, 
            mode='lines+markers',
            line=line_style,
            marker=dict(color=ds.POLLUTANT_COLORS[pollutant], size=4),
            name=short_name
        ))
    
    # Формируем заголовок с переносом на две строки, так как длина привышает ширину окошка/карточки 
    smooth_text = " (сглажено)" if smooth_data and values else ""
    
    title = f"<b>{short_name}</b><br>{description}{smooth_text}"
    
    fig.update_layout(
        title=title,
        xaxis_title='Время',
        yaxis_title='Концентрация (µg/m³)',
        font=dict(family=ds.GRAPH_FONT_FAMILY, size=ds.GRAPH_FONT_SIZE),
        title_font=dict(size=14, family=ds.GRAPH_FONT_FAMILY),
        plot_bgcolor=ds.PLOT_BACKGROUND_COLOR,
        paper_bgcolor=ds.PAPER_BACKGROUND_COLOR,
        height=400,
        margin=dict(l=50, r=50, t=80, b=50),
        title_x=0.5 
    )
    
    return fig
