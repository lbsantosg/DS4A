from dash import html, dcc 
import dash_bootstrap_components as dbc


class slider:
    def __init__(self, id, min, max, step, value=3):
        self.id=id
        self.min= min
        self.max= max
        self.step= step
        self.value= value
        
    def display(self):
        layout= html.Div(
            [        
                dcc.Slider(id=self.id, min=self.min, max=self.max, step=self.step, value=self.value),
            ],
            className="mb-3 slider",
        )
        return layout
