from dash import Dash # pyright: ignore[reportMissingImports]
from layouts import create_layout # pyright: ignore[reportMissingImports]
from callbacks import register_callbacks # pyright: ignore[reportMissingImports]
import dash_bootstrap_components as dbc # pyright: ignore[reportMissingImports]


app = Dash(external_stylesheets=[dbc.themes.MATERIA])
app.layout = create_layout()

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)