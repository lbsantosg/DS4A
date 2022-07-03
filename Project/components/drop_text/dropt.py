import dash_bootstrap_components as dbc

class dropt:
    def __init__(self,input_id,output_id,label,options):
        self.input_id=input_id
        self.output_id=output_id
        self.label=label
        self.options=options

    def display(self):
        layout= dbc.InputGroup(
                    [
                        dbc.DropdownMenu(  
                        [        
                            dbc.DropdownMenuItem(option)
                            for option in self.options
                        ],
                        label = self.label,
                        menu_variant="dark",
                        id=self.input_id,
                        direction="end"
                        ),
                        dbc.Input(id=self.output_id),
                    ], className="drop-text"
                        )
        return layout

