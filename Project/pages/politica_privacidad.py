from dash_labs.plugins import register_page
from dash import html 
import dash_bootstrap_components as dbc

register_page(__name__, path="/politica_privacidad")

layout= dbc.Container([
    html.Div([
        html.H2("POLÍTICA DE PRIVACIDAD", className="tcenter"),
        html.Br(),
        html.P("El presente Política de Privacidad establece los términos en que Saby usa y protege la información que es proporcionada por sus usuarios al momento de utilizar su sitio web. Esta compañía está comprometida con la seguridad de los datos de sus usuarios. Cuando le pedimos llenar los campos de información personal con la cual usted pueda ser identificado, lo hacemos asegurando que sólo se empleará de acuerdo con los términos de este documento. Sin embargo esta Política de Privacidad puede cambiar con el tiempo o ser actualizada por lo que le recomendamos y enfatizamos revisar continuamente esta página para asegurarse que está de acuerdo con dichos cambios.", className="justi"),
        html.Br(),
        html.H3("Información que es recogida"),
        html.P("Nuestro sitio web podrá recoger información personal por ejemplo: departamento y ciudad de residencia, área de ocupación entre otros.",className="justi"),
        html.Br(),
        html.H3("Uso de la información recogida"),
        html.P("Nuestro sitio web emplea la información con el fin de proporcionar el mejor servicio posible, particularmente para ajustar los parametros necesarios para nuestro modelo de recomendación y mejorar su precisión.",className="justi"),
        html.P("Saby está altamente comprometido para cumplir con el compromiso de mantener su información segura. Usamos los sistemas más avanzados y los actualizamos constantemente para asegurarnos que no exista ningún acceso no autorizado.",className="justi"),
        html.Br(),
        html.H3("Control de su información personal"),
        html.P("Esta compañía no venderá, cederá ni distribuirá la información personal que es recopilada sin su consentimiento, salvo que sea requerido por un juez con un orden judicial.", className="justi"),
        html.P("Saby Se reserva el derecho de cambiar los términos de la presente Política de Privacidad en cualquier momento.", className="justi")

    ],className="content politics")
    
], fluid="True")