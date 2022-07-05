from dash_labs.plugins import register_page
from dash import html 
import dash_bootstrap_components as dbc

register_page(__name__, path="/sobre_nosotros")


from components.person_card.person_card import person_card
import dash_trich_components as dtc

layout=dbc.Container([
    dtc.Carousel([
         person_card("Carlos Bejarano", "Inegeniero Sistemas e Informática", "./assets/images/carlos.jpg","https://www.linkedin.com/in/carlos-bejarano-3b04b21b3/").display(),
         person_card("Dorges Higgins","Ingeniero de petroleos","./assets/images/dorges.jpg","https://www.linkedin.com/in/dorges-higgins").display(),
         person_card("Daniel Peñaranda","Ingeniero Agroindutrial","./assets/images/daniel.jpg","https://www.linkedin.com/in/depenarandap/").display(),
         person_card("Laura Santos","Ingeniera Sistemas e Informática","./assets/images/laura.jpg","https://www.linkedin.com/in/laura-santos-guerrero-b3ba82170/").display(),
         person_card("Carlos Vergara","Magister en Economía","./assets/images/andres.jpg","https://www.linkedin.com/in/carlosandresvergara/").display()
    ],autoplay=True)  
],class_name="content",
fluid=True)
        

    
    
