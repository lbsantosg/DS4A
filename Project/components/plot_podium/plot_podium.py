import pandas as pd
import plotly as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go



class PlotPodium:

    def __init__(self, dataframe):
        #Input is a sorted DataFrame by="Punt_global_mean_2021", descenging order, of selected schools.
        self.df_bar = dataframe #I dont understand too well this part, I think the warning comes from this

    def plot_podium(self):
        #Here renames columns and change its index, so first place is on the middle, just like a podium
        df_bar = self.df_bar
        df_bar = df_bar.rename(columns={'Punt_lectura_critica_mean_2021':'LECTURA CRÍTICA', 'Punt_matematicas_mean_2021':'MATEMÁTICAS',\
        'Punt_c_naturales_mean_2021':'CIENCIAS NATURALES', 'Punt_sociales_ciudadanas_mean_2021':'CIENCIAS SOCIALES',\
        'Punt_ingles_mean_2021':'INGLÉS'})
        """         df_bar['LECTURA CRÍTICA'] = df_bar['LECTURA CRÍTICA']*df_bar['calculated_score']/500
        df_bar['MATEMÁTICAS'] = df_bar['MATEMÁTICAS']*df_bar['calculated_score']/500
        df_bar['CIENCIAS NATURALES'] = df_bar['CIENCIAS NATURALES']*df_bar['calculated_score']/500
        df_bar['CIENCIAS SOCIALES'] = df_bar['CIENCIAS SOCIALES']*df_bar['calculated_score']/500
        df_bar['INGLÉS'] = df_bar['INGLÉS']*df_bar['calculated_score']/500 """
        df_bar= df_bar.head(3).sort_values(by="Punt_global_mean_2021",ascending=False)
        df_bar = df_bar.reset_index(drop=True).reindex([1,0,2])
        print(df_bar)
        #colours used
        color1 = '#ef476f'
        saby_yellow = '#f2ab2c'
        color3 = '#06d6a0'
        color4 = '#118ab2'
        color5 = '#073b4c'
        saby_background = '#eddaa6'
        saby_offblack = '#303030'
        saby_boulder = '#747474'
        saby_armadillo = '#37342c'
    #########################################################
    #########################################################
        #this is the main plot, width and height are baked but I dont know how to do it relative to screen size
        barchart = px.bar(
            data_frame = df_bar,
            x = 'COLE_NOMBRE_SEDE',
            y = ["LECTURA CRÍTICA","MATEMÁTICAS","CIENCIAS NATURALES","CIENCIAS SOCIALES","INGLÉS"],
            opacity = 0.95,
            barmode = 'relative',
            color_discrete_map = {"LECTURA CRÍTICA":color1, "MATEMÁTICAS":saby_yellow, "CIENCIAS NATURALES":color3, "CIENCIAS SOCIALES":color4, "INGLÉS":color5},
            width = 900,
            height = 600,
            labels = {"value":"Puntaje promedio pruebas Saber 11", "COLE_NOMBRE_ESTABLECIMIENTO":"Podio 3 primeros lugares en afinidad y puntaje",\
                "variable":"PUNTAJE PROMEDIO"},
    
            hover_name='COLE_NOMBRE_SEDE',

            hover_data={'COLE_NOMBRE_SEDE':False,
                        'variable':False,
                        },
        )

        ##This changes legend position, format it and disable ability to turn on/off some data
        barchart.update_layout(legend={'x':1, 'y':0.5, 'bgcolor':saby_background, 'traceorder':'reversed'}, hoverlabel=dict(
                font_size=16,
                font_family='Rockwell',
                    ), 
                legend_itemclick=False,
                legend_itemdoubleclick=False
                )
        ##disables title and format schools names
        barchart.update_layout(plot_bgcolor = saby_background,
                xaxis_title=None,
                paper_bgcolor = saby_background,
                font=dict(size=16,
                        color = saby_offblack        
                        )
                )
        #this change width for columns on a barchart, so middle one looks bigger, in front of the other two
        barchart.update_traces(width=[0.88,1.1,0.88],
                        marker_line_color=saby_background,
                        marker_line_width=1.5)
    
        #cannt remember what this is supposed to do, disabled it and nothing happened
        #barchart.add_trace(go.Bar(name="first"))

        #this uses x axis to simulate a floor, also disables panning
        barchart.update_xaxes(showline=True, linewidth=5, linecolor='black', fixedrange=True, tickangle=0,
                        tickwidth=200
                                )
        #disable y axis and disables panning
        barchart.update_yaxes(fixedrange=True, visible=False)

        #this 'sorts' schools names, and put breaklines on 2dn and 3rd place so they arent draw on top of each other
        barchart.update_layout(xaxis=dict(tickmode='array', tickvals=[1,0,2], ticktext=[df_bar['COLE_NOMBRE_SEDE'][0],'<br>' + df_bar['COLE_NOMBRE_SEDE'][1], '<br><br>' + df_bar['COLE_NOMBRE_SEDE'][2]]))


        #### this code draws I, II, and III markers, first 3 draws circles
        #rest draws lines for numbers
        gx = 0
        gy = -100
        barchart.add_shape(type="circle",
            xref="x", yref="y",
            fillcolor=saby_boulder,
            x0=0.75 + gx, y0=240.75 + gy, x1=1.25 + gx, y1=315 + gy,
            opacity=0.75,
                line=dict(
                color=saby_armadillo,
                width=5
            )
        )

        barchart.add_shape(type="circle",
            xref="x", yref="y",
            fillcolor=saby_boulder,
            x0=-0.25 + gx, y0=200.75 + gy, x1=0.25 + gx, y1=275 + gy,
            opacity=0.75,
            line=dict(
                color=saby_armadillo,
                width=5
            )
        )

        barchart.add_shape(type="circle",
            xref="x", yref="y",
            fillcolor=saby_boulder,
            x0=1.75 + gx, y0=175.75 + gy, x1=2.25 + gx, y1=250 + gy,
            opacity=0.75,
                line=dict(
                color=saby_armadillo,
                width=5
            )
        )

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=1 + gx, y0=260 + gy, x1=1 + gx, y1=300 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))
        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=0.975 + gx, y0=300 + gy, x1=1.025 + gx, y1=300 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))
        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=0.975 + gx, y0=260 + gy, x1=1.025 + gx, y1=260 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=0.04 + gx, y0=220 + gy, x1=0.04 + gx, y1=260 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))
        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=-0.04 + gx, y0=220 + gy, x1=-0.04 + gx, y1=260 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=-0.08 + gx, y0=260 + gy, x1=0.08 + gx, y1=260 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=-0.08 + gx, y0=220 + gy, x1=0.08 + gx, y1=220 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=1.95 + gx, y0=195 + gy, x1=1.95 + gx, y1=235 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=2 + gx, y0=195 + gy, x1=2 + gx, y1=235 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))
            
        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=2.05 + gx, y0=195 + gy, x1=2.05 + gx, y1=235 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=1.90 + gx, y0=235 + gy, x1=2.1 + gx, y1=235 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=1.9 + gx, y0=235 + gy, x1=2.1 + gx, y1=235 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        barchart.add_shape(type="line",
            xref="x", yref="y",
            x0=1.9 + gx, y0=195 + gy, x1=2.1 + gx, y1=195 + gy,
            line=dict(
                color=saby_offblack,
                width=5,
            ))

        return barchart



##Here I test if it worked
#load cleaned school df
#testdf = pd.read_csv('C:\DS4A project\schools_data\clean_schools_joined.csv', encoding='utf8')

##create an object (?) for custom class, takes a random sample and sort it by mean global score
##so it simulates matching algorithm
#testF = PlotPodium(testdf.sample(10).sort_values(by="Punt_global_mean_2021", ascending=False))
##here plots the graph
#testF.plot_podium()