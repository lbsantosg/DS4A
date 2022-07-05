from dash import html 
import dash_bootstrap_components as dbc
import dash_trich_components as dtc

class person_card:

    def __init__(self,name,job,img,link):
        self.name=name
        self.job=job
        self.img=img
        self.link=link

    def display(self):
        layout= dtc.Card(
            link=self.link,
            image=self.img,
            title= self.name,
            description=self.job,
            dark=True
        )

        return layout