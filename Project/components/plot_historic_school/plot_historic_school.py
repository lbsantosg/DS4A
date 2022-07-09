import pandas as pd
import plotly as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import numpy as np #only needed for test



class PlotHistoric:

    def __init__(self, dataframe):
        #Input is a school from cleaned schools CSV, that one done by Laura

        #colums and index for a temp DataFrame
        columns = ['Lectura Crítica', 'Matemáticas', 'Ciencias Naturales', 'Ciencias Sociales', 'Inglés']
        index = ['2017','2018','2019','2020','2021']
        #picks mean Data by year
        data_plot = pd.DataFrame(columns=columns, index=index)
        for x in range(len(data_plot)):
            y = x*6
            data_plot.iloc[x]=dataframe.iloc[y+20:y+25]

        #rounds float 
        data_plot = data_plot.astype(float).round(2)
        #dataframe is the original one, used to pick other variables, like name
        self.dataframe = dataframe
        #this one have the actual plot data
        self.df_line = data_plot



    def plotHistoric(self):
        df_line = self.df_line
        #colours to be used
        saby_offblack = '#303030'
        saby_background = '#eddaa6'

        #creates basic line plot
        lineplot = px.line(df_line,
                line_shape='spline',
                render_mode='svg',
                markers=True,
                title=self.dataframe.COLE_NOMBRE_SEDE,
                labels = {"variable":"PUNTAJE<br>PROMEDIO"},
            )

        #format plot area
        lineplot.update_layout(plot_bgcolor = saby_background,
                xaxis_title=None,
                yaxis_title='Puntaje Promedio',
                paper_bgcolor = saby_background,
                font=dict(size=16,
                        color = saby_offblack        
                        ),
                )

        #disable panning
        lineplot.update_yaxes(fixedrange=True)
        lineplot.update_xaxes(fixedrange=True)

        #format legend, also disables interactivity
        lineplot.update_layout(legend={'x':1, 'y':0.5}, hoverlabel=dict(
                font_size=16,
                font_family='Rockwell',
                    ),
                legend_itemclick=False,
                legend_itemdoubleclick=False,
                font=dict(size=18,
                        color = saby_offblack        
                        )
                )
        #makes lines thicker
        lineplot.update_traces(line=dict(width=15), opacity=0.75)
        #next 5 lines creates point to build hexagons
        lineplot.add_trace(go.Scatter(x=df_line.index, y=df_line['Lectura Crítica'], mode='markers', name='Lectura Crítica', showlegend=False, hoverinfo='skip'))
        lineplot.add_trace(go.Scatter(x=df_line.index, y=df_line['Matemáticas'], mode='markers', name='Matemáticas', showlegend=False, hoverinfo='skip'))
        lineplot.add_trace(go.Scatter(x=df_line.index, y=df_line['Ciencias Naturales'], mode='markers', name='Ciencias Naturales', showlegend=False, hoverinfo='skip'))
        lineplot.add_trace(go.Scatter(x=df_line.index, y=df_line['Ciencias Sociales'], mode='markers', name='Ciencias Sociales', showlegend=False, hoverinfo='skip'))
        lineplot.add_trace(go.Scatter(x=df_line.index, y=df_line['Inglés'], mode='markers', name='Inglés', showlegend=False, hoverinfo='skip'))
        #format hexagons
        lineplot.update_traces(marker=dict(size=36,
                                    line=dict(width=2,
                                                color='DarkSlateGrey')),
                        selector=dict(mode='markers'),
                        opacity=0.85,
                        marker_symbol='hexagon',                  
                        )
        #finally plots it
        #pio.show(lineplot)

        return lineplot





##Here I test if its working
#load cleaned school df
#testdf = pd.read_csv('C:\DS4A project\schools_data\clean_schools_joined.csv', encoding='utf8')

##create an object (?) for custom class, takes a random school as input
##
#testF = PlotHistoric(testdf.iloc[int(np.random.random()*len(testdf))])
##plots the graph
#testF.plotHistoric()