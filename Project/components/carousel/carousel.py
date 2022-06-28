import dash_trich_components as dtc
import dash_html_components as html

carousel = dtc.Carousel([
           	html.Div('slide 1'),
 			html.Div('slide 2'),
  			html.Div('slide 3'),
  			
		],
            slides_to_scroll=1,
            swipe_to_slide=True,
            autoplay=True,
            speed=2000,
            variable_width=True,
            center_mode=True,
            responsive=[
            {
                'breakpoint': 991,
                'settings': {
                    'arrows': True
                }
            }]
		)

layout= dbc.Container(
    [
        carousel,
    ],
    className="content",
    fluid=True,
)