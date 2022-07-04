import dash_bootstrap_components as dbc
from pandas import options


class rbutton:
        
    def __init__(self, id, options):
            self.id=id
            self.options=options
    
    def display(self):

        layout= dbc.RadioItems(
                    id=self.id,
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": item, "value": item}
                        for item in self.options
                        ],
                    
                )
        return layout
        
     


                                

