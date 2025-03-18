from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import math
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout of the app
app.layout = html.Div(
    style={'textAlign': 'center', 'fontFamily': 'Arial', 'marginTop': '50px'},
    children=[
        # Red band at the top with title
        html.Div(
            style={
                'backgroundColor': '#D32F2F',  # Red background for the band
                'padding': '20px',  # Padding around the title
                'textAlign': 'center',  # Center align the text
                'fontFamily': 'Arial',  # Set the font family
            },
            children=[
                html.H1(
                    "Summit ESP: Bending Stress Calculator",  # Title text
                    style={'color': 'white', 'fontSize': '36px'}  # White text with large font size
                )
            ]
        ),
        html.Br(),  # This will create a line break for space
        html.Label("Select Casing Size:"),
        dcc.Dropdown(
            id="casing-dropdown",
            options=[
                {"label": "4 1/2", "value": "4 1/2"},
                {"label": "5", "value": "5"},
                {"label": "5 1/2", "value": "5 1/2"},
                {"label": "7", "value": "7"},
                {"label": "7 5/8", "value": "7 5/8"},
                {"label": "8 5/8", "value": "8 5/8"},
                {"label": "9 5/8", "value": "9 5/8"},
            ],
            value=["5"],  # Set a default value to trigger the callbacks
            placeholder="Select a casing size",
            style={"width": "50%", "margin": "auto", "fontSize": "16px"}
        ),
        html.Div(
            children=[
                html.Label("Select the Casing Weight:"),
                dcc.Dropdown(
                    id="casing-weight-dropdown",
                    options=[],
                    placeholder="Select a weight",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        html.Div(
            children=[
                html.Label("Select the Casing Dimension:"),
                dcc.Dropdown(
                    id="casing-dim-dropdown",
                    options=[
                        {"label": "Drift", "value": "Drift"},
                        {"label": "Nominal", "value": "Nominal"},
                    ],
                    placeholder="Select casing dimension",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        # First Motor Dropdown
        html.Div(
            children=[
                html.Label("Select Motor Series:"),
                dcc.Dropdown(
                    id="motor-series-dropdown",
                    options=[
                        {"label": "375", "value": "375"},
                        {"label": "420", "value": "420"},
                        {"label": "456", "value": "456"},
                        {"label": "562", "value": "562"},
                    ],
                    placeholder="Select motor series",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        html.Div(
            children=[
                html.Label("Select First Motor HP Rating:"),
                dcc.Dropdown(
                    id="motor-dropdown-1",
                    options=[],
                    placeholder="Select a motor",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),

        # Second Motor Dropdown
        html.Div(
            children=[
                html.Label("Select Second Motor HP Rating:"),
                dcc.Dropdown(
                    id="motor-dropdown-2",
                    options=[{"label": "None", "value": "None"}],
                    placeholder="Select the second motor or none",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
html.Div(
            children=[
                html.Label("Select Seal Series:"),
                dcc.Dropdown(
                    id="seal-series-dropdown",
                    options=[
                        {"label": "338", "value": "338"},
                        {"label": "400", "value": "400"},
                        {"label": "513", "value": "513"},
                        #{"label": "675", "value": "675"},
                        #875
                    ],
                    placeholder="Select seal series",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),

        html.Div(
            children=[
                html.Label("Select First Seal:"),
                dcc.Dropdown(
                    id="seal-dropdown-1",
                    options=[],
                    placeholder="Select a seal or none",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        html.Div(
            children=[
                html.Label("Select Second Seal:"),
                dcc.Dropdown(
                    id="seal-dropdown-2",
                    options=[{"label": "None", "value": "None"}],
                    placeholder="Select a seal or none",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        html.Div(
            children=[
                html.Label("Select Gas Separator Series:"),
                dcc.Dropdown(
                    id="gas-sep-series-dropdown",
                    options=[
                        {"label": "338", "value": "338"},
                        {"label": "400", "value": "400"},
                        {"label": "538", "value": "538"},
                    ],
                    placeholder="Select gas separator series",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        html.Div(
            children=[
                html.Label("Select First Gas Separator:"),
                dcc.Dropdown(
                    id="gas-separator-dropdown-1",
                    options=[],
                    placeholder="Select a gas separator or none",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        html.Div(
            children=[
                html.Label("Select Second Gas Separator:"),
                dcc.Dropdown(
                    id="gas-separator-dropdown-2",
                    options=[{"label": "None", "value": "none"}],
                    placeholder="Select a second gas separator or none",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        html.Div(
            children=[
                html.Label("Select Pump Series:"),
                dcc.Dropdown(
                    id="pump-series-dropdown",
                    options=[
                        {"label": "338", "value": "338"},
                        {"label": "400", "value": "400"},
                        {"label": "400 - Stiff", "value": "401"},
                        {"label": "538", "value": "538"},
                    ],
                    placeholder="Select pump series",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        # Pump Housing Dropdowns
        html.Div(
            children=[
                html.Label(f"Select Pumps:"),
                dcc.Dropdown(
                    id="pump-housing-dropdown-1",
                    options=[],
                    placeholder="Select Pump 1 Housing #",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
                *[
                    dcc.Dropdown(
                        id=f"pump-housing-dropdown-{i}",
                        options=[],
                        placeholder=f"Select Pump {i} Housing #",
                        style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                    ) for i in range(2, 7)
                ]
            ],
            style={"marginTop": "20px"}
        ),

    #html.Div(id="deviation-output", style={"textAlign": "center", "fontSize": "18px"}),
        html.Div(
            children=[
                html.Label("Select Tubing Size Effect:"),
                dcc.Dropdown(
                    id="tubing-effect-dropdown",
                    options=[
                        {"label": "2 3/8", "value": "2 3/8"},
                        {"label": "2 7/8", "value": "2 7/8"},
                        {"label": "3 1/2", "value": "3 1/2"},
                        {"label": "4 1/2", "value": "4 1/2"},
                        {"label": "None", "value": "None"},
                    ],
                    placeholder="Select tubing size",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),

        html.Div(
            children=[
                html.Label("Select Bottom Stinger Effect:"),
                dcc.Dropdown(
                    id="stinger-effect-dropdown",
                    options=[
                        {"label": "2 3/8", "value": "2 3/8"},
                        {"label": "2 7/8", "value": "2 7/8"},
                        {"label": "3 1/2", "value": "3 1/2"},
                        {"label": "4 1/2", "value": "4 1/2"},
                        {"label": "None", "value": "None"},
                    ],
                    placeholder="Select tubing size",
                    style={"width": "50%", "margin": "auto", "fontSize": "16px"}
                ),
            ],
            style={"marginTop": "20px"}
        ),
        html.Br(),  # This will create a line break for space

        html.Label("Enter DLS (deg/100ft):"),
             dcc.Input(
                id="dls-input",   # Unique ID for the input box
                type="text",  # Set to text to remove the up/down arrows
                value="",      # Default value (empty box)
                placeholder="Enter DLS here...",  # Placeholder text
        style={
            "width": "350px",  # Smaller width for the input box
            "fontSize": "16px",
            "margin": "auto",  # Centers it horizontally
            "display": "block",
            "textAlign": "center",
        },
        inputMode="numeric"  # Ensures numeric input (no arrows)
             ),
        html.Label("Enter Deviation Angle (deg):"),
             dcc.Input(
                id="deviation-input",   # Unique ID for the input box
                type="text",  # Set to text to remove the up/down arrows
                value="",      # Default value (empty box)
                placeholder="Enter deviation angle here...",  # Placeholder text
        style={
            "width": "350px",  # Smaller width for the input box
            "fontSize": "16px",
            "margin": "auto",  # Centers it horizontally
            "display": "block",
            "textAlign": "center",
        },
        inputMode="numeric"  # Ensures numeric input
             ),
        html.Label("Enter Secondary Horizontal Orientation (Max 90 deg):"),
             dcc.Input(
                id="horizontal-input",   # Unique ID for the input box
                type="text",  # Set to text to remove the up/down arrows
                value="",      # Default value (empty box)
                placeholder="Enter secondary horizontal orientation here...",  # Placeholder text
        style={
            "width": "350px",  # Smaller width for the input box
            "fontSize": "16px",
            "margin": "auto",  # Centers it horizontally
            "display": "block",
            "textAlign": "center",
        },
        inputMode="numeric"  # Ensures numeric input (no arrows)
             ),
        html.Label("Enter Secondary vs Primary Bend (%):"),
             dcc.Input(
                id="bend-input",   # Unique ID for the input box
                type="text",  # Set to text to remove the up/down arrows
                value="",      # Default value (empty box)
                placeholder="Enter secondary vs primary bend here...",  # Placeholder text
        style={
            "width": "350px",  # Smaller width for the input box
            "fontSize": "16px",
            "margin": "auto",  # Centers it horizontally
            "display": "block",
            "textAlign": "center",
        },
        inputMode="numeric"  # Ensures numeric input (no arrows)
             ),
        html.Label("Enter External Load (lbs):"),
             dcc.Input(
                id="load-input",   # Unique ID for the input box
                type="text",  # Set to text to remove the up/down arrows
                value="",      # Default value (empty box)
                placeholder="Enter external load here...",  # Placeholder text
        style={
            "width": "350px",  # Smaller width for the input box
            "fontSize": "16px",
            "margin": "auto",  # Centers it horizontally
            "display": "block",
            "textAlign": "center",
        },
        inputMode="numeric"  # Ensures numeric input (no arrows)
             ),
        html.Div(
            children=[
                html.Button('Generate Stress Plot', id='generate-plot-button', n_clicks=0, style={'fontSize': '18px', 'padding': '10px 20px'})
            ],
            style={'marginTop': '20px'}
        ),
        html.Div(
            children=[
                #html.Label("Max Stress Plot"),
                dcc.Graph(id="stress-plot", style={"height": "500px"})
            ],
            style={"marginTop": "20px"}
        ),
        html.Div(
            children=[
                html.Button('Generate Clearance Plot', id='clearance-plot-button', n_clicks=0, style={'fontSize': '18px', 'padding': '10px 20px'})
            ],
            style={'marginTop': '20px'}
        ),
        html.Div(
            children=[
                #html.Label("Clearance Plot:"),
                dcc.Graph(id="clearance-plot", style={"height": "500px"})
            ],
            style={"marginTop": "20px"}
        ),

        # Output Display
        #html.Div(id="output", style={"marginTop": "20px", "fontSize": "18px", "fontWeight": "bold"}),
       # html.Div(id="output1", style={"marginTop": "20px", "fontSize": "18px", "fontWeight": "bold"}),
        #html.Div(id="output2", style={"marginTop": "20px", "fontSize": "18px", "fontWeight": "bold"}),
    ]
)

segment = 1000  # defines graphing x axis division
modulus = 29000000  # defines Young's modulus
#tubing_4500_I = 8.08  # 4.5 inch tubing moment of inertia
#tubing_3500_I = 3.017  # 3.5 inch tubing moment of inertia
#tubing_2875_I = 1.61  # 2.875 inch tubing moment of inertia
#tubing_2375_I = 0.9654  # 2.375 inch tubing moment of inertia
cable_width = 1.12
cable_height = 0.365


pump_configurations = {
    338: {
            1: {"frame": 1, "length": 2.1, "weight": 38},
            2: {"frame": 2, "length": 3.5, "weight": 63},
            3: {"frame": 3, "length": 4.9, "weight": 78 },
            4: {"frame": 4, "length": 6.3, "weight": 107},
            5: {"frame": 5, "length": 7.7, "weight": 141},
            6: {"frame": 6, "length": 9.2, "weight": 167},
            7: {"frame": 7, "length": 10.6, "weight": 193},
            8: {"frame": 8, "length": 12, "weight": 219},
            9: {"frame": 9, "length": 13.4, "weight": 245},
            10: {"frame": 10, "length": 14.8, "weight": 271},

    },
    400: {
            1: {"frame": 1, "length": 2.1, "weight": 71},
            2: {"frame": 2, "length": 3.5, "weight": 126},
            3: {"frame": 3, "length": 4.9, "weight": 192},
            4: {"frame": 4, "length": 6.3, "weight": 247},
            5: {"frame": 5, "length": 7.7, "weight": 303},
            6: {"frame": 6, "length": 9.2, "weight": 358},
            7: {"frame": 7, "length": 10.6, "weight": 414},
            8: {"frame": 8, "length": 12, "weight": 479},
            9: {"frame": 9, "length": 13.4, "weight": 534},
            10: {"frame": 10, "length": 14.8, "weight": 590},
            11: {"frame": 11, "length": 16.2, "weight": 645},
            12: {"frame": 12, "length": 17.6, "weight": 701},
            13: {"frame": 13, "length": 19.0, "weight": 766},
            14: {"frame": 14, "length": 20.4, "weight": 821},
            15: {"frame": 15, "length": 21.8, "weight": 877}


    },
401: {
            1: {"frame": 1, "length": 2.1, "weight": 71},
            2: {"frame": 2, "length": 3.5, "weight": 126},
            3: {"frame": 3, "length": 4.9, "weight": 192},
            4: {"frame": 4, "length": 6.3, "weight": 247},
            5: {"frame": 5, "length": 7.7, "weight": 303},
            6: {"frame": 6, "length": 9.2, "weight": 358},
            7: {"frame": 7, "length": 10.6, "weight": 414},
            8: {"frame": 8, "length": 12, "weight": 479},
            9: {"frame": 9, "length": 13.4, "weight": 534},
            10: {"frame": 10, "length": 14.8, "weight": 590},
            11: {"frame": 11, "length": 16.2, "weight": 645},
            12: {"frame": 12, "length": 17.6, "weight": 701},
            13: {"frame": 13, "length": 19.0, "weight": 766},
            14: {"frame": 14, "length": 20.4, "weight": 821},
            15: {"frame": 15, "length": 21.8, "weight": 877}


    },
    538: {
            1: {"frame": 1, "length": 2.5, "weight": 93},
            2: {"frame": 2, "length": 4, "weight": 167},
            3: {"frame": 3, "length": 5.5, "weight": 220},
            4: {"frame": 4, "length": 7, "weight": 284},
            5: {"frame": 5, "length": 8.5, "weight": 347},
            6: {"frame": 6, "length": 10, "weight": 412},
            7: {"frame": 7, "length": 11.5, "weight": 473},
            8: {"frame": 8, "length": 13, "weight": 537},
            9: {"frame": 9, "length": 14.5, "weight": 602},
            10: {"frame": 10, "length": 16, "weight": 665},
            11: {"frame": 11, "length": 17.5, "weight": 729},
            12: {"frame": 12, "length": 19, "weight": 793},
            13: {"frame": 13, "length": 20.5, "weight": 867},
            14: {"frame": 14, "length": 22, "weight": 921},
            15: {"frame": 15, "length": 23.5, "weight": 985}
    },


}
seal_configurations={
338: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "LSL", "length": 5.9, "weight": 110},
            {"label": "BLS", "length": 5.9, "weight": 170},
            {"label": "BPBSL", "length": 8.9, "weight": 180},

    ],
400: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "LSL", "length": 5.9, "weight": 110},
            {"label": "BLS", "length": 5.9, "weight": 170},
            {"label": "BPBSL", "length": 8.9, "weight": 180},
],
513: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "LSL", "length": 5.9, "weight": 275},
            {"label": "BLS", "length": 5.9, "weight": 290},
            {"label": "BPBSL", "length": 8.9, "weight": 380},
        ],
}
gas_sep_LT_configurations={
338: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "BOI", "length": 1.2, "weight": 50},
            {"label": "H2X", "length": 6, "weight": 50},
            {"label": "High Flow", "length": 2.2, "weight": 50},
            {"label": "UT", "length": 2, "weight": 50},
    ],
400: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "BOI", "length": 1, "weight": 29},
            {"label": "H2X", "length": 5.1, "weight": 137},
            {"label": "High Flow", "length": 3.6, "weight": 55},
            {"label": "UT", "length": 2.3, "weight": 66},
        ],
538: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "BOI", "length": 1.2, "weight": 51},
            {"label": "LT-500x", "length": 3.9, "weight": 154},
            {"label": "LT-500", "length": 7, "weight": 304},
            {"label": "UT", "length": 3.9, "weight": 154},
],
}
gas_sep_UT_configurations={
338: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "LT-300X", "length": 6, "weight": 50},
            {"label": "High Flow", "length": 2.2, "weight": 50},
            {"label": "UT", "length": 2, "weight": 50},
        ],
400: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "H2X", "length": 5.1, "weight": 137},
            {"label": "High Flow", "length": 3.6, "weight": 55},
            {"label": "UT", "length": 2.3, "weight": 66},
        ],
538: [
            {"label": "None", "length": 0, "weight": 0},
            {"label": "LT-500x", "length": 3.9, "weight": 154},
            {"label": "LT-500", "length": 7, "weight": 304},
            {"label": "UT", "length": 3.9, "weight": 154},
        ],
}
motor_configurations={
375: {
    18: {"frame": 18, "length": 6, "weight": 242},
    36: {"frame": 36, "length": 21.1, "weight": 360},
    54: {"frame": 54, "length": 16.9, "weight": 516},
    75: {"frame": 75, "length": 22.7, "weight": 713},
    100: {"frame": 100, "length": 28.5, "weight": 909},

},
420:{
    133: {"frame": 133, "length": 23.6, "weight": 865},
    167: {"frame": 167, "length": 28.6, "weight": 1050},
    200: {"frame": 200, "length": 32.9, "weight": 1200},

},
456:{
    30: {"frame": 30, "length": 6, "weight": 313},
    45: {"frame": 45, "length": 7.5, "weight": 313},
    60: {"frame": 60, "length": 8.9, "weight": 313},
    75: {"frame": 75, "length": 10.4, "weight": 313},
    90: {"frame": 90, "length": 11.8, "weight": 313},
    105: {"frame": 105, "length": 17.6, "weight": 313},
    120: {"frame": 120, "length": 14.7, "weight": 313},
    150: {"frame": 150, "length": 17.6, "weight": 313},
    180: {"frame": 180, "length": 20.5, "weight": 313},
    240: {"frame": 240, "length": 26.2, "weight": 313},
    300: {"frame": 300, "length": 32.0, "weight": 313},

},
562: {
    60: {"frame": 60, "length": 5.9, "weight": 313},
    90: {"frame": 90, "length": 7.6, "weight": 403},
    120: {"frame": 120, "length": 9.4, "weight": 533},
    150: {"frame": 150, "length": 11.1, "weight": 663},
    180: {"frame": 180, "length": 12.9, "weight": 781},
    #210: {"frame": 210, "length": 17.2, "weight": 1190},
    240: {"frame": 240, "length": 16.4, "weight": 992},
    #270: {"frame": 270, "length": 21.4, "weight": 1570},
    300: {"frame": 300, "length": 19.9, "weight": 1198},
    330: {"frame": 330, "length": 21.7, "weight": 1500},
    360: {"frame": 360, "length": 23.4, "weight": 1500},
    #390: {"frame": 390, "length": 29.8, "weight": 2210},
    #420: {"frame": 420, "length": 31.9, "weight": 2340},
    #450: {"frame": 450, "length": 34, "weight": 2500},
    500:{"frame": 500, "length": 34, "weight": 2178},
    },
}
qmax_configurations={
338: {
            1: {"length": 6, "weight": 75, "type": "HighFlow UT"},
            2: {"length": 2.2, "weight": 41, "type": "H2X"},
            3: {"length": 2, "weight": 36.3, "type": "UT"},
            4: {"length": 1.2, "weight": 45, "type": "BOI"},
            5: {"length": 0, "weight": 0, "type": "none"}
        },
400: {
            1: {"length": 3.6, "weight": 5, "type": "Highflow UT"},
            2: {"length": 5.7, "weight": 137, "type": "H2X"},
            3: {"length": 4, "weight": 66, "type": "UT"},
            4: {"length": 1, "weight": 29, "type": "BOI"},
            5: {"length": 0, "weight": 0, "type": "none"}
        },
538: {
            1: {"length": 8, "weight": 175, "type": "LT8000"},
            2: {"length": 8, "weight": 175, "type": "LT11500"},
            3: {"length": 4.5, "weight": 110, "type": "UT"},
            4: {"length": 1.2, "weight": 100, "type": "BOI"},
            5: {"length": 0, "weight": 0, "type": "none"}
        }
}
casing_id={
    "4 1/2": [
        {"label": "9.5", "value": "9.5", "id": 3.965},
        {"label": "11.6", "value": "11.6", "id": 3.875},
        {"label": "13.5", "value": "13.5", "id": 3.795},
    ],
    "5": [
        {"label": "18", "value": "18", "id": 4.151},
        {"label": "20.3", "value": "20.3", "id": 4.059},
        {"label": "20.8", "value": "20.8", "id": 4.031},
        {"label": "21.4", "value": "21.4", "id": 4.001},
    ],
    "5 1/2": [
        {"label": "15.5", "value": "15.5", "id": 4.825},
        {"label": "17", "value": "17", "id": 4.767},
        {"label": "20", "value": "20", "id": 4.653},
        {"label": "23", "value": "23", "id": 4.545},
    ],
    "7": [
        {"label": "23", "value": "23", "id": 6.241},
        {"label": "26", "value": "26", "id": 6.151},
        {"label": "29", "value": "29", "id": 6.059},
        {"label": "32", "value": "32", "id": 5.969},
    ],
    "7 5/8": [
        {"label": "26.4", "value": "26.4", "id": 6.844},
        {"label": "29.7", "value": "29.7", "id": 6.75},
        {"label": "33.7", "value": "33.7", "id": 6.64},
        {"label": "39", "value": "39", "id": 6.5},
    ],
    "8 5/8": [
        {"label": "36", "value": "36", "id": 7.7},
        {"label": "40", "value": "40", "id": 7.6},
        {"label": "44", "value": "44", "id": 7.5},
        {"label": "49", "value": "49", "id": 7.386},
    ],
    "9 5/8": [
        {"label": "43.5", "value": "43.5", "id": 8.599},
        {"label": "47", "value": "47", "id": 8.525},
        {"label": "53.5", "value": "53.5", "id": 8.379},
        {"label": "58.4", "value": "58.4", "id": 8.279},
    ],
}

casing_nominal={
"4 1/2": [
        {"label": "9.5", "value": "9.5", "id": 4.09},
        {"label": "11.6", "value": "11.6", "id": 4},
        {"label": "13.5", "value": "13.5", "id": 3.92},
    ],
    "5": [
        {"label": "18", "value": "18", "id": 4.276},
        {"label": "20.3", "value": "20.3", "id": 4.184},
        {"label": "20.8", "value": "20.8", "id": 4.156},
        {"label": "21.4", "value": "21.4", "id": 4.126},
    ],
    "5 1/2": [
        {"label": "15.5", "value": "15.5", "id": 4.95},
        {"label": "17", "value": "17", "id": 4.892},
        {"label": "20", "value": "20", "id": 4.778},
        {"label": "23", "value": "23", "id": 4.67},
    ],
    "7": [
        {"label": "23", "value": "23", "id": 6.366},
        {"label": "26", "value": "26", "id": 6.276},
        {"label": "29", "value": "29", "id": 6.184},
        {"label": "32", "value": "32", "id": 6.094},
    ],
    "7 5/8": [
        {"label": "26.4", "value": "26.4", "id": 6.969},
        {"label": "29.7", "value": "29.7", "id": 6.875},
        {"label": "33.7", "value": "33.7", "id": 6.765},
        {"label": "39", "value": "39", "id": 6.625},
    ],
    "8 5/8": [
        {"label": "36", "value": "36", "id": 7.825},
        {"label": "40", "value": "40", "id": 7.725},
        {"label": "44", "value": "44", "id": 7.625},
        {"label": "49", "value": "49", "id": 7.511},
    ],
    "9 5/8": [
        {"label": "43.5", "value": "43.5", "id": 8.755},
        {"label": "47", "value": "47", "id": 8.681},
        {"label": "53.5", "value": "53.5", "id": 8.535},
        {"label": "58.4", "value": "58.4", "id": 8.435},
    ],
}
# Function to get motor options
#def get_motor_options(selected_equipment):
#    config = motor_configurations.get(selected_equipment, {})
#    return [{"label": str(frame), "value": str(frame)} for frame in config.keys()]

# Function to get pump options
#def get_pump_options(selected_equipment):
 #   config = pump_configurations.get(selected_equipment, {})
  #  pump_lengths = config.get("pump_lengths", {})
   # return [{"label": str(i), "value": str(i)} for i in range(1, len(pump_lengths) + 1)]



# Single callback to update both motors and gas separators based on selected equipment
@app.callback(
    [
        Output("motor-dropdown-1", "options"),
        Output("motor-dropdown-2", "options"),
        Output ("seal-dropdown-1", "options"),
        Output ("seal-dropdown-2", "options"),
        Output("gas-separator-dropdown-1", "options"),
        Output("gas-separator-dropdown-2", "options"),
    ],
    [
        Input("motor-series-dropdown", "value"),
Input("seal-series-dropdown", "value"),
Input("gas-sep-series-dropdown", "value"),
Input("pump-series-dropdown", "value"),
    ]
)
def update_dropdowns(selected_motor, selected_seal, selected_gassep, selected_pump):


    motor_options = []
    motor_options_2 = [{"label": "None", "value": "None"}]

    seal_options=[
        {"label": "None", "value": "None"},
        {"label": "LSL", "value": "LSL"},
        {"label": "BLS", "value": "BLS"},
        {"label": "BPBSL", "value": "BPBSL"},
    ]
    seal_options_2=[
        {"label": "None", "value": "None"},
        {"label": "LSL", "value": "LSL"},
        {"label": "BLS", "value": "BLS"},
        {"label": "BPBSL", "value": "BPBSL"},
    ]



    # Initialize gas separator options
    gas_separator_options = []
    gas_separator_options_2 = [{"label": "None", "value": "None"}]

    # Update motor options based on selected equipment
    if selected_motor == "375":
        motor_options = [{"label": str(i), "value": str(i)} for i in [18, 36, 54, 75, 100]]


    elif selected_motor == "420":
        motor_options = [{"label": str(i), "value": str(i)} for i in [133,167,200]]


    elif selected_motor == "456":
        motor_options = [{"label": str(i), "value": str(i)} for i in [45, 60, 75, 90, 120, 150, 180, 240, 300]]


    elif selected_motor == "562":
        motor_options = [{"label": str(i), "value": str(i)} for i in
                         [60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 500]]


    motor_options_2 = [{"label": "None", "value": "None"}] + motor_options

    # Update gas separator options based on selected equipment
    if selected_gassep == "338":
        gas_separator_options = [
            {"label": "None", "value": "None"},
            {"label": "BOI", "value": "BOI"},
            {"label": "H2X", "value": "H2X"},
            {"label": "High Flow", "value": "High Flow"},
            {"label": "UT", "value": "UT"},
        ]
        gas_separator_options_2.extend([
            #{"label": "None", "value": "None"},
            {"label": "LT-300X", "value": "LT-300X"},
            {"label": "High Flow", "value": "High Flow"},
            {"label": "UT", "value": "UT"},
        ])

    elif selected_gassep == "400":
        gas_separator_options = [
            {"label": "None", "value": "None"},
            {"label": "BOI", "value": "BOI"},
            {"label": "H2X", "value": "H2X"},
            {"label": "High Flow", "value": "High Flow"},
            {"label": "UT", "value": "UT"},
        ]
        gas_separator_options_2.extend([
            {"label": "UT", "value": "UT"},
            {"label": "H2X", "value": "H2X"},
            {"label": "High Flow", "value": "High Flow"},
            {"label": "LT", "value": "LT"},
        ])


    elif selected_gassep == "538":
        gas_separator_options = [
            {"label": "None", "value": "None"},
            {"label": "BOI", "value": "BOI"},
            {"label": "LT-500", "value": "LT-500"},
            {"label": "LT-500x", "value": "LT-500x"},
            {"label": "UT", "value": "UT"},
        ]

        gas_separator_options_2.extend([
            #{"label": "None", "value": "None"},
            {"label": "UT", "value": "UT"},
            {"label": "LT-500", "value": "LT-500"},
            {"label": "LT-500x", "value": "LT-500x"},
        ])


    # Return all dropdown options for motor and gas separator
    return motor_options, motor_options_2, seal_options, seal_options_2, gas_separator_options, gas_separator_options_2

@app.callback(
    Output("casing-weight-dropdown", "options"),
    [Input("casing-dropdown", "value")]
)


def update_casing_weight(selected_casing):
    #weight_options=[]

    if selected_casing == "4 1/2":
        weight_options = [{"label": str(i), "value": str(i)} for i in [9.5, 11.6, 13.5]]
    elif selected_casing == "5":
        weight_options = [{"label": str(i), "value": str(i)} for i in [18, 20.3, 20.8, 21.4]]
    elif selected_casing == "5 1/2":
        weight_options = [{"label": str(i), "value": str(i)} for i in [15.5, 17, 20, 23]]
    elif selected_casing == "7":
        weight_options = [{"label": str(i), "value": str(i)} for i in [23, 26, 29, 32]]
    elif selected_casing == "7 5/8":
        weight_options = [{"label": str(i), "value": str(i)} for i in [26.4, 29.7, 33.7, 39]]
    elif selected_casing == "8 5/8":
        weight_options = [{"label": str(i), "value": str(i)} for i in [36, 40, 44, 49]]
    elif selected_casing == "9 5/8":
        weight_options = [{"label": str(i), "value": str(i)} for i in [43.5, 47, 53.5, 58.4]]
    else:
        weight_options = [{"label": "No options available", "value": "No options"}]
    return weight_options


@app.callback(
    [
        Output("pump-housing-dropdown-1", "options"),
        Output("pump-housing-dropdown-2", "options"),
        Output("pump-housing-dropdown-3", "options"),
        Output("pump-housing-dropdown-4", "options"),
        Output("pump-housing-dropdown-5", "options"),
        Output("pump-housing-dropdown-6", "options"),

    ],
    [
        Input("pump-series-dropdown", "value"),
    ]
)
def update_pump_dropdowns(selected_equipment):
    # Default pump options are 1-15
    all_pump_options = [{"label": str(i), "value": str(i)} for i in range(1, 16)]

    # For "338" equipment, update pump options to 1-10
    if selected_equipment == "338":
        pump_options = [{"label": str(i), "value": str(i)} for i in range(1, 11)]
    else:
        pump_options = all_pump_options  # Default options for other equipment

    # Add "None" option as the first choice for each dropdown
    pump_options_with_none2 = [{"label": "None", "value": "None"}] + pump_options
    pump_options_with_none3 = [{"label": "None", "value": "None"}] + pump_options
    pump_options_with_none4 = [{"label": "None", "value": "None"}] + pump_options
    pump_options_with_none5 = [{"label": "None", "value": "None"}] + pump_options
    pump_options_with_none6 = [{"label": "None", "value": "None"}] + pump_options


    # Return the updated pump options for all 7 pump dropdowns
    return (
        pump_options,  # For pump dropdown 1
        pump_options_with_none2,  # For pump dropdown 2
        pump_options_with_none3,  # For pump dropdown 3
        pump_options_with_none4,  # For pump dropdown 4
        pump_options_with_none5,  # For pump dropdown 5
        pump_options_with_none6,  # For pump dropdown 6
    )



@app.callback(
    Output("stress-plot", "figure"),
    [
        Input("motor-series-dropdown", "value"),
        Input("motor-dropdown-1", "value"),
        Input("motor-dropdown-2", "value"),
        Input("seal-series-dropdown", "value"),
        Input("seal-dropdown-1", "value"),
        Input("seal-dropdown-2", "value"),
        Input("gas-sep-series-dropdown", "value"),
        Input("gas-separator-dropdown-1", "value"),
        Input("gas-separator-dropdown-2", "value"),
        Input("pump-series-dropdown", "value"),
        Input("pump-housing-dropdown-1", "value"),  # New pump housing input 1
        Input("pump-housing-dropdown-2", "value"),  # New pump housing input 2
        Input("pump-housing-dropdown-3", "value"),  # New pump housing input 3
        Input("pump-housing-dropdown-4", "value"),  # New pump housing input 4
        Input("pump-housing-dropdown-5", "value"),  # New pump housing input 5
        Input("pump-housing-dropdown-6", "value"),  # New pump housing input 6
        #Input("deviation-angle-input", "value"),
        Input("tubing-effect-dropdown", "value"),
        Input("stinger-effect-dropdown", "value"),
        Input("dls-input", "value"),
        Input("casing-dim-dropdown", "value"),
        Input("casing-dropdown", "value"),
        Input("casing-weight-dropdown", "value"),
        Input("horizontal-input", "value"),
        Input("bend-input", "value"),
        Input("deviation-input", "value"),
        Input("load-input", "value"),
        Input("generate-plot-button", "n_clicks"),



    ]
)
def handle_selections(motor_equipment, motor1, motor2, seal_equipment, seal1, seal2,gassep_equipment,gassep1, gassep2, pump_equipment, pump1, pump2, pump3, pump4, pump5, pump6, tubing_effect, stinger_effect, dls, casing_dim, casing_OD, casing_weight, orientation, t_path, t_path_seal,ext_wt, n_clicks):

    motor_equipment = int(motor_equipment) if motor_equipment is not None else None
    motor1 = int(motor1) if motor1 is not None else None
    if motor2 and motor2 != "None":  # Ensure motor2 is not None or the string 'None'
        motor2 = int(motor2)
    else:
        motor2 = None
    segment = 1000  # defines graphing x axis division
    modulus = 29000000

    bendingdeviation=None
    #dls_new=None
    pumpI = None
    pumpC = None
    pumpneckC = None
    pumpneckI = None
    pump_OD = None
    pump_OD = None
    pump_neck_area = None
    intakeI = None  # estimate
    intakeC = None
    intakeneckI = None
    intakeneckC = None
    intake_neck_area = None
    sealC = None
    sealI = None
    sealneckC = None
    sealneckI = None
    seal_hsg_od = None
    seal_hsg_id = None
    seal_neck_area = None
    # motorI = None  # moment of inertia for 300 motor and pump series is an estimate
    motorC = None
    motorneckI = None  # actual
    motorneckC = None  # actual
    motor_OD = None
    motor_neck_area = None
    stress_concentration_1 = None
    stress_concentration_2 = None


    if pump_equipment is not None:
        if pump_equipment == "338":
            pumpI = 4
            pumpC = 1.69
            pumpneckC = 1.1  # actual
            pumpneckI = 0.815  # actual
            pump_OD = 3.38
            pump_neck_area = 1.78
            stress_concentration_1 = 1.15
            stress_concentration_2 = 1.1
        elif pump_equipment == "400":
            pumpI = 6.19
            pumpC = 2
            pumpneckC = 1.325
            pumpneckI = 1.94
            pump_OD = 4
            pump_neck_area = 2.686
            stress_concentration_1 = 1.4
            stress_concentration_2 = 1.4
        elif pump_equipment == "401":
            pumpI = 6.19
            pumpC = 2
            pumpneckC = 1.95
            pumpneckI = 3.08
            pump_OD = 4
            pump_neck_area = 3.025
            stress_concentration_1 = 1.2
            stress_concentration_2 = 1.15


        elif pump_equipment == "538":
            pumpI = 17.63 #QUESTION
            pumpC = 2.69
            pumpneckC = 1.766  # actual
            pumpneckI = 4.1154756  # actual
            pump_OD = 5.38
            pump_neck_area = 3.531
            stress_concentration_1 = 1.6
            stress_concentration_2 = 1.4

    if seal_equipment is not None:
        if seal_equipment == "338":
            sealC = 1.691
            sealI = 5.3
            sealneckC = 1.1  # actual
            sealneckI = 1.541273  # actual
            seal_hsg_od = 3.38
            seal_hsg_id = 3
            seal_neck_area = 1.98

        elif seal_equipment == "400":
            sealC = 2.01
            sealI = 5.62
            sealneckC = 1.435  # actual
            sealneckI = 1.76  # actual
            seal_hsg_od = 4
            seal_hsg_id = 3.5
            seal_neck_area = 1.572
        elif seal_equipment == "513":
            sealC = 2.566
            sealI = 11.75
            sealneckC = 1.765  # actual
            sealneckI = 5.413  # actual
            seal_hsg_od = 5.13
            seal_hsg_id = 4.527
            seal_neck_area = 4.518

    motorI = None

    # Check if motor_equipment is provided and not None
    if motor_equipment is not None:
        # Set motorI based on motor_equipment
        if motor_equipment == 375:
            motor_options = [{"label": str(i), "value": str(i)} for i in [18, 36, 54, 75, 100]]
            motorI = 8  # Moment of inertia for 375 motor equipment
            motorC = 1.875
            motorneckI = 1.445
            motorneckC = 1.369
            motor_OD = 3.75
            motor_neck_area = 2.475

        elif motor_equipment == 420:
            motor_options = [{"label": str(i), "value": str(i)} for i in [133, 167, 200]]
            motorI = 12.97  # Moment of inertia for 420 motor equipment
            motorC = 2.1
            motorneckI = 1.94
            motorneckC = 1.3
            motor_OD = 4.2
            motor_neck_area = 3.35

        elif motor_equipment == 456:
            motor_options = [{"label": str(i), "value": str(i)} for i in [45, 60, 75, 90, 120, 150, 180, 240, 300]]
            motorI = 15.4  # Moment of inertia for 456 motor equipment
            motorC = 2.28
            motorneckI = 2.487
            motorneckC = 1.4375
            motor_OD = 4.56
            motor_neck_area = 1.45

        elif motor_equipment ==562:
            motorI = 25.24  # Moment of inertia for 562 motor equipment
            motorC = 2.81
            motorneckI = 5.54756
            motorneckC = 1.766
            motor_OD = 5.62
            motor_neck_area = 5.116
    if gassep_equipment is not None:
        if gassep_equipment =="338":
            intakeI = 4  # estimate
            intakeC = 1.69
            intakeneckI = 0.828  # actual
            intakeneckC = 1.1  # actual
            intake_neck_area = 1.819  # actual
        elif gassep_equipment == "400":
            intakeI = 5.72  # estimate
            intakeC = 2
            intakeneckI = 1.1  # actual
            intakeneckC = 1.125  # actual
            intake_neck_area = 2.07  # actual

        elif gassep_equipment == "538":
            intakeI = 15.75  #QUESTION
            intakeC = 2.69
            intakeneckI = 5.875  # actual
            intakeneckC = 1.75  # actual
            intake_neck_area = 5.991  # actual



    # Check if equipment is selected and convert it to integer
    if motor1 is not None and motor1 in motor_configurations.get(motor_equipment, {}):
        motor1_data = motor_configurations[motor_equipment][motor1]
        motor_LT_length = motor1_data["length"]
        motor_LT_weight = motor1_data["weight"]

    else:
        motor_LT_length = 0
        motor_LT_weight = 0



    # Similarly, for motor2
    if motor2 is not None and motor2 in motor_configurations[motor_equipment]:
        motor2_data = motor_configurations[motor_equipment][motor2]
        motor_UT_length = motor2_data["length"]
        motor_UT_weight = motor2_data["weight"]

    else:
        motor_UT_length = 0
        motor_UT_weight = 0


    seal_equipment = int(seal_equipment) if seal_equipment is not None else None
    seal1_length, seal1_weight = 0, 0
    seal2_length, seal2_weight = 0, 0

    # Check if equipment is selected and convert it to integer
    if seal1 is not None and seal1 != "None" and seal1 in [seal['label'] for seal in
                                                           seal_configurations.get(seal_equipment, [])]:
        seal1_data = next(seal for seal in seal_configurations[seal_equipment] if seal['label'] == seal1)
        seal1_length = seal1_data["length"]
        seal1_weight = seal1_data["weight"]

    else:
        seal1_length, seal1_weight = 0, 0


    # Similarly, for motor2
    if seal2 is not None and seal2 != "None" and seal2 in [seal['label'] for seal in
                                                           seal_configurations.get(seal_equipment, [])]:
        seal2_data = next(seal for seal in seal_configurations[seal_equipment] if seal['label'] == seal2)
        seal2_length = seal2_data["length"]
        seal2_weight = seal2_data["weight"]

    else:
        seal2_length, seal2_weight = 0, 0



    gassep_equipment = int(gassep_equipment) if gassep_equipment is not None else None
    gassep1_length, gassep1_weight = 0, 0
    gassep2_length, gassep2_weight = 0, 0

    # Check if equipment is selected and convert it to integer
    if gassep1 is not None and gassep1 != "None" and gassep1 in [gassep['label'] for gassep in
                                                                 gas_sep_LT_configurations.get(gassep_equipment, [])]:
        gassep1_data = next(gassep for gassep in gas_sep_LT_configurations[gassep_equipment] if gassep['label'] == gassep1)
        gassep1_length = gassep1_data["length"]
        gassep1_weight = gassep1_data["weight"]

    else:
        gassep1_length, gassep1_weight = 0, 0


    # Similarly, for motor2
    if gassep2 is not None and gassep2 != "None" and gassep2 in [gassep['label'] for gassep in
                                                                 gas_sep_UT_configurations.get(gassep_equipment, [])]:
        gassep2_data = next(gassep for gassep in gas_sep_UT_configurations[gassep_equipment] if gassep['label'] == gassep2)
        gassep2_length = gassep2_data["length"]
        gassep2_weight = gassep2_data["weight"]

    else:
        gassep2_length, gassep2_weight = 0, 0


    pump_equipment = int(pump_equipment) if pump_equipment is not None else None
    pump1_length, pump1_weight = 0, 0
    pump2_length, pump2_weight = 0, 0
    pump3_length, pump3_weight = 0, 0
    pump4_length, pump4_weight = 0, 0
    pump5_length, pump5_weight = 0, 0
    pump6_length, pump6_weight = 0, 0

    # Check if equipment is selected and convert it to integer
    if pump1 is not None and pump1 != "None" and pump1 in [str(pump) for pump in
                                                           pump_configurations.get(pump_equipment, {}).keys()]:
        pump1_data = pump_configurations[pump_equipment][int(pump1)]
        pump1_length = pump1_data["length"]
        pump1_weight = pump1_data["weight"]

    else:
        pump1_length, pump1_weight = 0, 0


    # Similarly, for motor2
    if pump2 is not None and pump2 != "None" and pump2 in [str(pump) for pump in
                                                           pump_configurations.get(pump_equipment, {}).keys()]:
        pump2_data = pump_configurations[pump_equipment][int(pump2)]
        pump2_length = pump2_data["length"]
        pump2_weight = pump2_data["weight"]

    else:
        pump2_length, pump2_weight = 0, 0


    if pump3 is not None and pump3 != "None" and pump3 in [str(pump) for pump in
                                                           pump_configurations.get(pump_equipment, {}).keys()]:
        pump3_data = pump_configurations[pump_equipment][int(pump3)]
        pump3_length = pump3_data["length"]
        pump3_weight = pump3_data["weight"]

    else:
        pump3_length, pump3_weight = 0, 0


    if pump4 is not None and pump4 != "None" and pump4 in [str(pump) for pump in
                                                           pump_configurations.get(pump_equipment, {}).keys()]:
        pump4_data = pump_configurations[pump_equipment][int(pump4)]
        pump4_length = pump4_data["length"]
        pump4_weight = pump4_data["weight"]

    else:
        pump4_length, pump4_weight = 0, 0


    # Handle Pump 5 selection
    if pump5 is not None and pump5 != "None" and pump5 in [str(pump) for pump in
                                                           pump_configurations.get(pump_equipment, {}).keys()]:
        pump5_data = pump_configurations[pump_equipment][int(pump5)]
        pump5_length = pump5_data["length"]
        pump5_weight = pump5_data["weight"]

    else:
        pump5_length, pump5_weight = 0, 0


    # Handle Pump 6 selection
    if pump6 is not None and pump6 != "None" and pump6 in [str(pump) for pump in
                                                           pump_configurations.get(pump_equipment, {}).keys()]:
        pump6_data = pump_configurations[pump_equipment][int(pump6)]
        pump6_length = pump6_data["length"]
        pump6_weight = pump6_data["weight"]

    else:
        pump6_length, pump6_weight = 0, 0

    #motor2_I= None
    #seal1_I= None
    #seal2_I= None
    #gassep1_I=None
    #gassep2_I = None
    #pump1_I = None
    #pump2_I = None
    #pump3_I = None
    #pump4_I = None
    #pump5_I = None
    #ump6_I = None

    if motor_equipment is not None:
        motor1_I=motorI
        if motor2 != "None":
            motor2_I= motorI
        else:
            motor2_I= None
    else:
        motor1_I=None

    if seal_equipment is not None:
        seal1_I = sealI  # Assign the correct moment of inertia
        #print(f'Seal I={seal1_I}')
        if seal2 != "None":  # Check if seal2 is not "None"
            seal2_I = sealI  # Assign the second seal's moment of inertia
        else:
            seal2_I = None  # If seal2 is not selected, set it to None
    else:
        seal1_I = None  # If seal_equipment is None, set seal1_I to None

    if gassep_equipment is not None:
        gassep1_I = intakeI  # Assign the correct moment of inertia for gas separator

        if gassep2 != "None":  # Check if gassep2 is not "None"
            gassep2_I = intakeI  # Assign the second gas separator's moment of inertia
        else:
            gassep2_I = None  # If gassep2 is not selected, set it to None
    else:
        gassep1_I = None  # If gassep_equipment is None, set gassep1_I to None


    # Assuming you want to check if pump equipment is valid (i.e., not "None")
    #if pump_equipment is not None:  # Check if pump equipment is selected
        #pump1_I = pumpI  # Assign inertia for pump 1


        # Check if each pump is not the "None" string (or empty string, or actual None)
        #if pump2 not in ["None", None, ""]:  # Check if pump2 is not "None", None, or empty
         #   pump2_I = pumpI  # Assign inertia for pump 2
        #else:
           # pump2_I = None  # If pump2 is not selected, set it to None

      # if pump3 not in ["None", None, ""]:  # Same check for pump3
           # pump3_I = pumpI  # Assign inertia for pump 3
       #else:
         #   pump3_I = None  # If pump3 is not selected, set it to None

       # if pump4 not in ["None", None, ""]:  # Same check for pump4
          #  pump4_I = pumpI  # Assign inertia for pump 4
        #else:
         #   pump4_I = None  # If pump4 is not selected, set it to None

        #if pump5 not in ["None", None, ""]:  # Same check for pump5
          #  pump5_I = pumpI  # Assign inertia for pump 5
       # else:
         #   pump5_I = None  # If pump5 is not selected, set it to None

        #if pump6 not in ["None", None, ""]:  # Same check for pump6
        #    pump6_I = pumpI  # Assign inertia for pump 6
        #else:
        #    pump6_I = None  # If pump6 is not selected, set it to None

    #else:
        # If no pump equipment is selected (i.e., pump_equipment is None)
       #pump1_I = pump2_I = pump3_I = pump4_I = pump5_I = pump6_I = None


    total_length=motor_UT_length+motor_LT_length+seal1_length+seal2_length+gassep1_length+gassep2_length+pump1_length+pump2_length+pump3_length+pump4_length+pump5_length+pump6_length
    #rint(total_length)
    total_weight = motor_UT_weight + motor_LT_weight + seal1_weight + seal2_weight + gassep1_weight + gassep2_weight + pump1_weight + pump2_weight + pump3_weight + pump4_weight + pump5_weight + pump6_weight
    incrementor = (total_length * 12 / segment)


    if tubing_effect == "2 1/2":
        tubing_I=0.9654
    elif tubing_effect == "2 7/8":
        tubing_I=1.61
    elif tubing_effect == "3 1/2":
        tubing_I= 3.017
    elif tubing_effect == "4 1/2":
        tubing_I=8.08
    elif tubing_effect == "None":
        tubing_I=0
    else:
        tubing_I=0

    if stinger_effect == "2 1/2":
        tubing_I2=0.9654
    elif stinger_effect == "2 7/8":
        tubing_I2=1.61
    elif stinger_effect == "3 1/2":
        tubing_I2= 3.017
    elif stinger_effect == "4 1/2":
        tubing_I2=8.08
    elif stinger_effect == "None":
        tubing_I2=0
    else:
        tubing_I2=0



    # Logic for Casing Dim handling
    casing_id_value = None  # Initializing the casing_id_value

    # Check if casing_OD is set
    if not casing_dim or not casing_OD or not casing_weight:

        return  # No need to return anything if conditions aren't met

        # Determine if the user selected "Nominal" or other option
    if casing_dim == "Nominal":
        # Access the corresponding data from casing_nominal
        casing_data = casing_nominal.get(casing_OD, [])
    else:
        # Access the corresponding data from casing_id
        casing_data = casing_id.get(casing_OD, [])

        # Check if casing_data exists and is not empty

        # Iterate through the casing_data to find the corresponding weight
    for weight in casing_data:
        if weight['value'] == casing_weight:
            casing_id_value = weight['id']  # Set the casing ID value when a match is found

            break  # Exit loop once the correct casing ID is found



    if dls:
        try:
            # Check if dls is not None or empty
            if dls.strip() != "":
                # Convert dls to float, remove extra spaces
                dls_new = float(dls.strip())
                # Now you can safely use dls_new for further calculations
                deflection = 2.6 * (total_length / 100) ** 2 * dls_new
            else:
                # Handle case where dls is empty or invalid
                dls_new = 0
                deflection = 0  # Or assign a default value, depends on your need
        except ValueError:
            # Error handling for invalid float conversion
            dls_new = 0  # Set default value
            deflection = 0  # Or assign a default value

    else:
        # If dls is None, assign default values
        dls_new = 0
        deflection = 0  # Or assign a default value

    if motor_equipment:
        try:
            motor_equipment = float(motor_equipment)
            # Now, divide by 100 to get motor_OD in meters
            motor_OD = motor_equipment / 100
            #(f"The motor OD (in meters) is: {motor_OD}")
        except ValueError:
            motor_equipment = 0

    if pump_equipment:
        try:
            pump_equipment = float(pump_equipment)
            # Now, divide by 100 to get motor_OD in meters
            pump_OD = pump_equipment / 100
        except ValueError:
            pump_equipment = 0

    #deviationcal=None
    #bendingdeviation=None
    casing_id_value = casing_id_value if casing_id_value is not None else 0
    motor_OD = motor_OD if motor_OD is not None else 0
    pump_OD = pump_OD if pump_OD is not None else 0
    #print(casing_id_value)

    if casing_id_value:
        deviationcal = ((casing_id_value - motor_OD) + (casing_id_value - pump_OD)) / 2
        bendingdeviation = (((casing_id_value - pump_OD) - deviationcal) / 2) + deviationcal

    joint_length = 30
    if 'dls_new' in locals():
        joint_length = 30
        tubing_deflection = 2.6 * (joint_length / 100) ** 2 * dls_new

    else:
        tubing_deflection = 0  # Default value or fallback


    tubing_moment = tubing_deflection * modulus * tubing_I * joint_length * 12 / (joint_length * 12 / 2) ** 3
    tubing_moment_2 = tubing_deflection * modulus * tubing_I2 * joint_length * 12 / (joint_length * 12 / 2) ** 3

    # Initialize the break variables to None
    break1 = break2 = break3 = break4 = break5 = break6 = break7 = break8 = break9 = break10 = break11 = break12 = None


    # This is the condition we're checking
    if motor1 is not None:
        break1 = round(motor_LT_length, 1)

    else:
        break1 = 0
    if motor2 is not None:
        break2 = round(motor_UT_length + break1, 1)
    else:
        break2 = 0

    if seal1 is not None:
        break3 = round(motor_UT_length + motor_LT_length + seal1_length, 1)
    else:
        break3 = 0

    if seal2 is not None:
        break4 = round(motor_UT_length + motor_LT_length + seal1_length + seal2_length, 1)
    else:
        break4 = 0

    if gassep1 is not None:
        break5 = round(motor_UT_length + motor_LT_length + seal1_length + seal2_length + gassep1_length, 1)
    else:
        break5 = 0

    if gassep2 is not None:
        break6 = round(motor_UT_length + motor_LT_length + seal1_length + seal2_length + gassep1_length + gassep2_length, 1)
    else:
        break6 = 0

    if pump1 is not None and pump2 is not None:
        break7 = round(motor_UT_length + motor_LT_length + seal1_length + seal2_length + gassep1_length + gassep2_length + pump1_length, 1)
    else:
        break7 = 0

    if pump2 is not None and pump3 is not None:
        break8 = round(motor_UT_length + motor_LT_length + seal1_length + seal2_length + gassep1_length + gassep2_length+ pump1_length + pump2_length, 1)
    else:
        break8 = 0

    if pump3 is not None and pump4 is not None:
        break9 = round(
            motor_UT_length + motor_LT_length + seal1_length + seal2_length + gassep1_length + gassep2_length + pump1_length + pump2_length + pump3_length,
            1)
    else:
        break9 = 0

    if pump4 is not None and pump5 is not None:
        break10 = round(
            motor_UT_length + motor_LT_length + seal1_length + seal2_length + gassep1_length + gassep2_length + pump1_length + pump2_length + pump3_length + pump4_length,
            1)
    else:
        break10 = 0

    if pump5 is not None and pump6 is not None:
        break11 = round(
            motor_UT_length + motor_LT_length + seal1_length + seal2_length + gassep1_length + gassep2_length + pump1_length + pump2_length + pump3_length + pump4_length + pump5_length,
            1)
    else:
        break11 = 0

    # Calculate break a, b, c, d, e for each break group
    # Break 1:
    if break1 > 0:
        break1a = break1 + 0.1
        break1b = break1a + 0.1
        break1c = break1b + 0.1
        break1d = break1c + 0.1
        break1e = break1d + 0.1
    else:
        break1a = break1b = break1c = break1d = break1e = 0

    # Break 2:
    if break2 > 0:
        break2a = break2 + 0.1
        break2b = break2a + 0.1
        break2c = break2b + 0.1
        break2d = break2c + 0.1
        break2e = break2d + 0.1
    else:
        break2a = break2b = break2c = break2d = break2e = 0

    # Break 3:
    if break3 > 0:
        break3a = break3 + 0.1
        break3b = break3a + 0.1
        break3c = break3b + 0.1
        break3d = break3c + 0.1
        break3e = break3d + 0.1
    else:
        break3a = break3b = break3c = break3d = break3e = 0

    # Break 4:
    if break4 > 0:
        break4a = break4 + 0.1
        break4b = break4a + 0.1
        break4c = break4b + 0.1
        break4d = break4c + 0.1
        break4e = break4d + 0.1
    else:
        break4a = break4b = break4c = break4d = break4e = 0

    # Break 5:
    if break5 > 0:
        break5a = break5 + 0.1
        break5b = break5a + 0.1
        break5c = break5b + 0.1
        break5d = break5c + 0.1
        break5e = break5d + 0.1
    else:
        break5a = break5b = break5c = break5d = break5e = 0

    # Break 6:
    if break6 > 0:
        break6a = break6 + 0.1
        break6b = break6a + 0.1
        break6c = break6b + 0.1
        break6d = break6c + 0.1
        break6e = break6d + 0.1
    else:
        break6a = break6b = break6c = break6d = break6e = 0

    # Break 7:
    if break7 > 0:
        break7a = break7 + 0.1
        break7b = break7a + 0.1
        break7c = break7b + 0.1
        break7d = break7c + 0.1
        break7e = break7d + 0.1
    else:
        break7a = break7b = break7c = break7d = break7e = 0

    # Break 8:
    if break8 > 0:
        break8a = break8 + 0.1
        break8b = break8a + 0.1
        break8c = break8b + 0.1
        break8d = break8c + 0.1
        break8e = break8d + 0.1
    else:
        break8a = break8b = break8c = break8d = break8e = 0

    # Break 9:
    if break9 > 0:
        break9a = break9 + 0.1
        break9b = break9a + 0.1
        break9c = break9b + 0.1
        break9d = break9c + 0.1
        break9e = break9d + 0.1
    else:
        break9a = break9b = break9c = break9d = break9e = 0

    # Break 10:
    if break10 > 0:
        break10a = break10 + 0.1
        break10b = break10a + 0.1
        break10c = break10b + 0.1
        break10d = break10c + 0.1
        break10e = break10d + 0.1
    else:
        break10a = break10b = break10c = break10d = break10e = 0

    # Break 11:
    if break11 > 0:
        break11a = break11 + 0.1
        break11b = break11a + 0.1
        break11c = break11b + 0.1
        break11d = break11c + 0.1
        break11e = break11d + 0.1
    else:
        break11a = break11b = break11c = break11d = break11e = 0

    if break11 != 0:
        temp_break1 = break11
        temp_break = break10
    elif break11 == 0 and break10 != 0:
        temp_break1 = break10
        temp_break = break9
    elif break11 == 0 and break10 == 0 and break9 != 0:
        temp_break1 = break9
        temp_break = break8
    elif break11 == 0 and break10 == 0 and break9 == 0 and break8 != 0:
        temp_break1 = break8
        temp_break = break7
    elif break11 == 0 and break10 == 0 and break9 == 0 and break8 == 0 and break7 != 0:
        temp_break1 = break7
        temp_break = break6
    elif break11 == 0 and break10 == 0 and break9 == 0 and break8 == 0 and break7 == 0 and break6 != 0:
        temp_break1 = break6
        temp_break = break5
    else:
        temp_break1 = temp_break = 0


    tubing_moment_length = 0
    tubing_moment_increment = 0

    if total_length and temp_break and tubing_moment:
        # Proceed with calculations if all variables have valid values
        tubing_moment_length = (total_length - temp_break) / (total_length / 1000)
        tubing_moment_increment = tubing_moment / tubing_moment_length


    stress_concentration_motor = 1.6
    stress_concentration_motor_A = 1.4
    seal_base_stress_modifier =0.85
    stress_reduction = 1



    # Initialize motor options
    pump_options = []

    if t_path_seal is None or sealneckC is None or motorC is None:
        seal_neck_adjuster = 0
    else:
        try:
            t_path_seal = int(t_path_seal)  # Attempt conversion to integer
            if t_path_seal > 0:
                seal_neck_adjuster = (sealneckC / motorC) ** (5 ** 0.5)
            else:
                seal_neck_adjuster = (sealneckC / motorC) ** (2.5 ** 0.5)
        except ValueError:
            seal_neck_adjuster = 0  # Handle invalid integer input, if any

    if sealneckI is None:
        seal_loadfactor=0,
    else:
        seal_loadfactor = 1 + 1 / sealneckI

    max_deflection=0,

    total_I = 0

    # Initialize arrays with values
    MyArray_in_increment = [0] * 1002  # 1002 because the indexing seems to go up to 1001
    MyArray_ft_increment = [0] * 1002
    MyArray_inertia1 = [0] * 1002
    MyArray_inertia2 = [0] * 1002  # Assuming motorI is a defined variable
    MyArray_centroid = [0] * 1002  # Assuming motorC is a defined variable
    MyArray_deflection = [0] * 1002
    MyArray_load = [0] * 1002
    MyArray_moment = [0] * 1002
    MyArray_mod_1 = [1] * 1002
    MyArray_mod_2 = [0] * 1002
    MyArray_mod_3 = [0] * 1002
    MyArray_mod_4 = [1] * 1002
    MyArray_stress = [0] * 1002
    MyArray_axis = [0] * 1002
    MyArray_stress_wtadder = [0] * 1002
    MyArray_seal_neck_stress_correction = [0] * 1002  # List of 1002 elements, all set to 0



    # Check conditions based on the range of MyArray_ft_increment[2]

    for i in range(1, 1002):
        MyArray_seal_neck_stress_correction[i] = 0
        # Perform calculations and conditional checks
    for i in range(1, 1002):
        MyArray_in_increment[i] = incrementor + MyArray_in_increment[i - 1]  # Assuming 'add' is a predefined variable
        MyArray_ft_increment[i] = round(MyArray_in_increment[i] / 12, 2)


        # Checking if MyArray_ft_increment[i] fits any of the conditions
        #if isinstance(MyArray_inertia2[i], tuple):
            #MyArray_inertia2[i] = float(MyArray_inertia2[i][0])  # Pick the first value if it's a tuple

        if MyArray_ft_increment[i] < break1:
            MyArray_inertia2[i] = float(motorI) if motorI is not None else 0
        elif break1 <= MyArray_ft_increment[i] <= break1e and break2 > 0:
            MyArray_inertia2[i] = float(motorneckI) if motorneckI is not None else 0
        elif break1 <= MyArray_ft_increment[i] <= break1e and break2 == 0:
            MyArray_inertia2[i] = float(sealneckI) if sealneckI is not None else 0
        elif break1e < MyArray_ft_increment[i] < break2:
            MyArray_inertia2[i] = float(motorI) if motorI is not None else 0
        elif break2 <= MyArray_ft_increment[i] <= break2e:
            MyArray_inertia2[i] = float(sealneckI) if sealneckI is not None else 0
        elif break2e < MyArray_ft_increment[i] < break3:
            MyArray_inertia2[i] = float(sealI) if sealI is not None else 0
        elif break3 <= MyArray_ft_increment[i] <= break3e:
            MyArray_inertia2[i] = float(sealneckI) if sealneckI is not None else 0
            MyArray_seal_neck_stress_correction[i] = float(seal_neck_adjuster) if seal_neck_adjuster is not None else 0
        elif break3e < MyArray_ft_increment[i] < break4:
            MyArray_inertia2[i] = float(sealI) if sealI is not None else 0
        elif break4 <= MyArray_ft_increment[i] <= break4e:
            MyArray_inertia2[i] = float(intakeneckI) if intakeneckI is not None else 0
        elif break4e < MyArray_ft_increment[i] < break5:
            MyArray_inertia2[i] = float(intakeI) if intakeI is not None else 0
        elif break5 <= MyArray_ft_increment[i] <= break5e:
            MyArray_inertia2[i] = float(pumpneckI) if pumpneckI is not None else 0
        elif break5e < MyArray_ft_increment[i] < break6:
            MyArray_inertia2[i] = float(intakeI) if intakeI is not None else 0
        elif break6 <= MyArray_ft_increment[i] <= break6e:
            MyArray_inertia2[i] = float(pumpneckI) if pumpneckI is not None else 0
        elif break6e < MyArray_ft_increment[i] < break7:
            MyArray_inertia2[i] = float(pumpI) if pumpI is not None else 0
        elif break7 <= MyArray_ft_increment[i] <= break7e:
            MyArray_inertia2[i] = float(pumpneckI) if pumpneckI is not None else 0
        elif break7e < MyArray_ft_increment[i] < break8:
            MyArray_inertia2[i] = float(pumpI) if pumpI is not None else 0
        elif break8 <= MyArray_ft_increment[i] <= break8e:
            MyArray_inertia2[i] = float(pumpneckI) if pumpneckI is not None else 0
        elif break8e < MyArray_ft_increment[i] < break9:
            MyArray_inertia2[i] = float(pumpI) if pumpI is not None else 0
        elif break9 <= MyArray_ft_increment[i] <= break9e:
            MyArray_inertia2[i] = float(pumpneckI) if pumpneckI is not None else 0
        elif break9e < MyArray_ft_increment[i] < break10:
            MyArray_inertia2[i] = float(pumpI) if pumpI is not None else 0
        elif break10 <= MyArray_ft_increment[i] <= break10e:
            MyArray_inertia2[i] = float(pumpneckI) if pumpneckI is not None else 0
        elif break10e < MyArray_ft_increment[i] < break11:
            MyArray_inertia2[i] = float(pumpI) if pumpI is not None else 0
        elif break11 <= MyArray_ft_increment[i] <= break11e:
            MyArray_inertia2[i] = float(pumpneckI) if pumpneckI is not None else 0
        elif MyArray_ft_increment[i] > break11e:
            MyArray_inertia2[i] = float(pumpI) if pumpI is not None else 0



        if motor_LT_weight is None or ext_wt is None or ext_wt == '':
            wt1 = 0
        else:
            # Convert motor_LT_weight to float if it's a string
            motor_LT_weight = float(motor_LT_weight) if isinstance(motor_LT_weight, str) else motor_LT_weight

            # Convert ext_wt to integer (if it's not empty or None)
            ext_wt = int(ext_wt) if ext_wt not in [None, ''] and isinstance(ext_wt, str) else ext_wt

            # Now calculate wt1
            wt1 = motor_LT_weight + ext_wt

    for i in range(len(MyArray_ft_increment)):
        # Only proceed if none of the required variables are None
        if (motor_LT_weight is not None and motor_UT_weight is not None and seal1_weight is not None and seal_neck_area is not None and intake_neck_area is not None and pump_neck_area is not None and t_path_seal is not None):
            seal_hsg_od = float(seal_hsg_od) if seal_hsg_od is not None else 0
            seal_hsg_id = float(seal_hsg_id) if seal_hsg_id is not None else 0
            ext_wt = float(ext_wt) if ext_wt not in [None, ""] else 0
            load_reduction = 1
            if isinstance(t_path_seal, str) and t_path_seal.strip() == "":
                # Optionally, you can assign a default value, e.g., 0
                angle = 0
            else:
                try:
                    # If t_path_seal is not a string, we convert it to string for safety
                    t_path_seal_str = str(t_path_seal)
                    angle = float(t_path_seal_str)
                    # Convert to radians
                    angle_radians = math.radians(angle)
                    # Calculate the load reduction
                    load_reduction = math.cos(angle_radians) ** 2.95

                except ValueError:
                    # If there's an error in conversion, set load_reduction to 0
                    load_reduction = 1

            seal_hsg_area = 3.14159 * ((seal_hsg_od) ** 2 - (seal_hsg_id) ** 2) / 4

            # Run your calculations
            ft_increment = MyArray_ft_increment[i]

            if ft_increment < break1:  # (1)
                MyArray_stress_wtadder[i] = 0

            elif break1 <= ft_increment <= break1e and break2 > 0:  # (2)
                wt1 = motor_LT_weight + ext_wt
                MyArray_stress_wtadder[i] = wt1 / motor_neck_area * load_reduction

            elif break1 <= ft_increment <= break1e and break2 == 0:  # (2)
                wt2 = motor_LT_weight + ext_wt
                MyArray_stress_wtadder[i] = wt2 / seal_neck_area * load_reduction

            elif break1e < ft_increment < break2:  # (3)
                MyArray_stress_wtadder[i] = 0

            elif break2 <= ft_increment <= break2e:  # (4)
                wt3 = motor_LT_weight + motor_UT_weight + ext_wt
                MyArray_stress_wtadder[i] = wt3 / seal_neck_area * load_reduction

            elif break2e < ft_increment < break3:
                wt3 = motor_LT_weight + motor_UT_weight + ext_wt# (5) Add loading to seal housing for external load force
                MyArray_stress_wtadder[i] = (wt3 + ext_wt) / seal_hsg_area * load_reduction

            elif break3 <= ft_increment <= break3e:  # (6)
                wt4 = motor_LT_weight + motor_UT_weight + seal1_weight + ext_wt
                MyArray_stress_wtadder[i] = wt4 / seal_neck_area * load_reduction

            elif break3e < ft_increment < break4:  # (7)
                wt4 = motor_LT_weight + motor_UT_weight + seal1_weight + ext_wt
                MyArray_stress_wtadder[i] = (wt4 + ext_wt) / seal_hsg_area * load_reduction

            elif break4 <= ft_increment <= break4e:  # (8)
                wt5 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + ext_wt
                MyArray_stress_wtadder[i] = wt5 / intake_neck_area * load_reduction

            elif break4e < ft_increment < break5:  # (9)
                wt5 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + ext_wt
                MyArray_stress_wtadder[i] = (wt5 + ext_wt) / seal_hsg_area * load_reduction

            elif break5 <= ft_increment <= break5e:  # (10)
                wt6 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + ext_wt
                MyArray_stress_wtadder[i] = wt6 / pump_neck_area * load_reduction

            elif break5e < ft_increment < break6:  # (11)
                wt6 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + ext_wt
                MyArray_stress_wtadder[i] = (wt6 + ext_wt) / seal_hsg_area * load_reduction

            elif break6 <= ft_increment <= break6e:  # (12)

                wt7 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + gassep2_weight + ext_wt
                MyArray_stress_wtadder[i] = wt7 / pump_neck_area * load_reduction

            elif break6e < ft_increment < break7:  # (13)
                MyArray_stress_wtadder[i] = 0

            elif break7 <= ft_increment <= break7e:  # (14)
                wt8 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + gassep2_weight + pump1_weight + ext_wt
                MyArray_stress_wtadder[i] = wt8 / pump_neck_area * load_reduction

            elif break7e < ft_increment < break8:  # (15)
                MyArray_stress_wtadder[i] = 0

            elif break8 <= ft_increment <= break8e:  # (16)
                wt9 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + gassep2_weight + pump1_weight + pump2_weight + ext_wt
                MyArray_stress_wtadder[i] = wt9 / pump_neck_area * load_reduction

            elif break8e < ft_increment < break9:  # (17)
                MyArray_stress_wtadder[i] = 0

            elif break9 <= ft_increment <= break9e:  # (18)
                wt10 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + gassep2_weight + pump1_weight + pump2_weight + pump3_weight + ext_wt
                MyArray_stress_wtadder[i] = wt10 / pump_neck_area * load_reduction

            elif break9e < ft_increment < break10:  # (19)
                MyArray_stress_wtadder[i] = 0

            elif break10 <= ft_increment <= break10e:  # (20)
                wt11 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + gassep2_weight + pump1_weight + pump2_weight + pump3_weight + pump4_weight + ext_wt
                MyArray_stress_wtadder[i] = wt11 / pump_neck_area * load_reduction

            elif break10 < ft_increment <= break10e:  # (20)
                wt12 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + gassep2_weight + pump1_weight + pump2_weight + pump3_weight + pump4_weight + pump5_weight + ext_wt
                MyArray_stress_wtadder[i] = wt12 / pump_neck_area * load_reduction

            elif ft_increment > break10e:  # (21)
                MyArray_stress_wtadder[i] = 0
                wt13 = motor_LT_weight + motor_UT_weight + seal1_weight + seal2_weight + gassep1_weight + gassep2_weight + pump1_weight + pump2_weight + pump3_weight + pump4_weight + pump5_weight + pump6_weight + ext_wt
                MyArray_stress_wtadder[i] = wt13 / pump_neck_area * load_reduction

    for i in range(len(MyArray_inertia2)):
        # First set of conditions for MyArray_inertia1 based on MyArray_inertia2
        if MyArray_inertia2[i] == motorI:
            MyArray_inertia1[i] = motorI
        elif MyArray_inertia2[i] == motorneckI:
            MyArray_inertia1[i] = motorI
        elif MyArray_inertia2[i] == sealneckI:
            MyArray_inertia1[i] = sealI
        elif MyArray_inertia2[i] == sealI:
            MyArray_inertia1[i] = sealI
        elif MyArray_inertia2[i] == intakeneckI:
            MyArray_inertia1[i] = pumpI
        elif MyArray_inertia2[i] == intakeI:
            MyArray_inertia1[i] = pumpI
        else:
            MyArray_inertia1[i] = pumpI

        # Second set of conditions for MyArray_centroid based on MyArray_inertia2
        if MyArray_inertia2[i] == motorI:
            MyArray_centroid[i] = motorC
        elif MyArray_inertia2[i] == motorneckI:
            MyArray_centroid[i] = motorneckC
        elif MyArray_inertia2[i] == sealI:
            MyArray_centroid[i] = sealC
        elif MyArray_inertia2[i] == sealneckI:
            MyArray_centroid[i] = sealneckC
        elif MyArray_inertia2[i] == intakeI:
            MyArray_centroid[i] = intakeC
        elif MyArray_inertia2[i] == intakeneckI:
            MyArray_centroid[i] = intakeneckC
        elif MyArray_inertia2[i] == pumpI:
            MyArray_centroid[i] = pumpC
        else:
            MyArray_centroid[i] = pumpneckC


    for i in range(len(MyArray_inertia2)):  # Adjust the loop range if needed
        total_I += MyArray_inertia2[i]


    average_I = total_I / 1000


    if t_path == "":
        t_path_new=0
    else:
        t_path_new = float(t_path)/100

    if t_path_new > 0:
        # Directly convert to float or set default values without checking for None or ""
        t_path_new = float(t_path_new) if t_path_new is not None else 0
        average_I = float(average_I) if average_I is not None else 0
        modulus = float(modulus) if modulus is not None else 0
        deflection = float(deflection) if deflection is not None else 0
        bendingdeviation = float(bendingdeviation) if bendingdeviation is not None else 0
        seal1_length = float(seal1_length) if seal1_length is not None else 0
        motor_OD = float(motor_OD) if motor_OD is not None else 0
        seal_hsg_od = float(seal_hsg_od) if seal_hsg_od is not None else 0
        seal1_weight = float(seal1_weight) if seal1_weight is not None else 0
        sealI = float(seal1_I) if sealI is not None else 0
        sealneckC = float(sealneckC) if sealneckC is not None else 0
        motorC = float(motorC) if motorC is not None else 0
        if orientation and orientation != "":
            # Convert to float
            orientation = float(orientation)
        else:
            # Set default value (0 or any other value that makes sense for your use case)
            orientation = 0

        # Proceed with the load calculation
        if total_length in [None, 0]:
            load=0
        else:
            load = (average_I * 384 * modulus * (deflection - (bendingdeviation * 2 - bendingdeviation * 2 * t_path_new))) / 5 / (total_length * 12) ** 4

        # Orientation modifier based on user input (default to 1 if not provided)
        if orientation == 0 or orientation is None:
            orientation_modifier = 1
        else:
            orientation_modifier = math.cos(2 * math.pi / 360 * orientation)

        if angle == 0 or angle is None:
            # Load modifier based on some angle (set to 0 for now, replace with real angle if necessary)
            load_modifier = math.sin(2 * math.pi / 360 * angle)
        else:
            load_modifier=1

        # DLS Deflection and related calculations
        DLS_deflection = 2.6 * (seal1_length * 2 / 100) ** 2 * dls_new
        required_seal_deflection = (motor_OD / 2 - seal_hsg_od / 2) + DLS_deflection

        if seal1_length in [None, 0]:
            uniform_load_w = 0
            load_req_for_deflect = 0
        else:
            uniform_load_w = seal1_weight / (seal1_length * 12)
            load_req_for_deflect = (required_seal_deflection * 24 * modulus * sealI / (seal1_length * 2 * 12) ** 4) * load_modifier
        Mmax = (load_req_for_deflect * (seal1_length * 2 * 12) ** 2) / 3
        #seal_neck_stress = 0
        if seal1_I not in [None, 0]:
            seal_neck_stress=0
        else:
            # Seal neck stress calculation
            seal_neck_stress = Mmax * sealneckC / sealI * orientation_modifier
        #seal_neck_stress = 0
        m_hsg = 0
        Seal_Hsg_Stress_Mod = 0
        #print(f'Length seal-{seal1_length}')

        if sealI != 0 and seal1_length !=0:  # Check if neither sealI nor seal1_length is zero
            m_hsg = uniform_load_w / 6 * ((seal1_length * 2 * 12) ** 2) / 4
            Seal_Hsg_Stress_Mod = m_hsg * seal_hsg_od / 2 / sealI
            #print(f'it worked={Seal_Hsg_Stress_Mod}')
        else:
            m_hsg = 0
            Seal_Hsg_Stress_Mod = 0  # Set to 0 or handle as needed


        # Return the results (load and seal neck stress)
        #return f"Calculated Load: {load}, Seal Neck Stress: {seal_neck_stress}"

    elif t_path_new == 0:
        #print(f'tpathnew= 0')
        # Directly convert to float or set default values without checking for None or ""
        t_path_new = float(t_path_new) if t_path_new is not None else 0
        average_I = float(average_I) if average_I is not None else 0
        modulus = float(modulus) if modulus is not None else 0
        deflection = float(deflection) if deflection is not None else 0
        bendingdeviation = float(bendingdeviation) if bendingdeviation is not None else 0
        total_length = float(total_length) if total_length is not None else 0
        seal1_length = float(seal1_length) if seal1_length is not None else 0
        motor_OD = float(motor_OD) if motor_OD is not None else 0
        seal_hsg_od = float(seal_hsg_od) if seal_hsg_od is not None else 0
        seal1_weight = float(seal1_weight) if seal1_weight is not None else 0
        if orientation and orientation != "":
            # Convert to float
            orientation = float(orientation)
        else:
            # Set default value (0 or any other value that makes sense for your use case)
            orientation = 0
        try:
            dls_new = float(dls_new)
        except NameError:
            dls_new = 0  # Handle case where dls_new is not defined
        sealI = float(sealI) if sealI is not None else 0
        sealneckC = float(sealneckC) if sealneckC is not None else 0
        motorC = float(motorC) if motorC is not None else 0

        # Proceed with the load calculation for t_path_new == 0
        if total_length in [None, 0]:
            load = 0  # Set load to 0 if total_length is invalid
        else:
            load = (average_I * 384 * modulus * (deflection - bendingdeviation * 2)) / 5 / (total_length * 12) ** 4

        orientation_modifier = 1
        load_modifier = 1

        DLS_deflection = 2.6 * (seal1_length * 2 / 100) ** 2 * dls_new
        required_seal_deflection = (motor_OD / 2 - seal_hsg_od / 2) + DLS_deflection
        if seal1_length in [None, 0]:
            uniform_load_w=0
            load_req_for_deflect=0
        else:
            uniform_load_w = seal1_weight / (seal1_length * 12)
            load_req_for_deflect = (required_seal_deflection * 24 * modulus * sealI / (seal1_length * 2 * 12) ** 4) * load_modifier
        Mmax = (load_req_for_deflect * (seal1_length * 2 * 12) ** 2) / 3
        m_hsg = 0
        Seal_Hsg_Stress_Mod = 0
        seal_neck_stress = 0





    MyArray_pipe_moment=[0]*1002
    if pump2 is None:
        for i in range(1,1002):  # In Python, ranges are exclusive at the end, so range(1, 1002) gives us the same result as 1 To 1001 in VBA
            if MyArray_ft_increment[i] >= break5:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1]
            else:
                MyArray_pipe_moment[i] = 0

    elif pump3 is None and pump2 is not None:
        for i in range(2, 1002):
            if break5 <= MyArray_ft_increment[i] < break6:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.75
            elif MyArray_ft_increment[i] >= break6:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 1

    elif pump4 is None and pump3 is not None and pump2 is not None:
        for i in range(2, 1002):
            if break5 <= MyArray_ft_increment[i] < break6:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.5
            elif break6 <= MyArray_ft_increment[i] < break7:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.75
            elif MyArray_ft_increment[i] >= break7:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 1

    elif pump5 is None and pump4 is not None and pump3 is not None and pump2 is not None:
        for i in range(2, 1002):
            if break5 <= MyArray_ft_increment[i] < break6:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.3
            elif break6 <= MyArray_ft_increment[i] < break7:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.6
            elif break7 <= MyArray_ft_increment[i] < break8:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.8
            elif MyArray_ft_increment[i] >= break8:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 1

    elif pump6 is None and pump5 is not None and pump4 is not None and pump3 is not None and pump2 is not None:
        for i in range(2, 1002):
            if break5 <= MyArray_ft_increment[i] < break6:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.3
            elif break6 <= MyArray_ft_increment[i] < break7:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.6
            elif break7 <= MyArray_ft_increment[i] < break8:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.8
            elif break8 <= MyArray_ft_increment[i] < break9:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.8
            elif MyArray_ft_increment[i] >= break9:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 1

    elif pump6 is not None:
        for i in range(2, 1002):
            if break5 <= MyArray_ft_increment[i] < break6:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.5
            elif break6 <= MyArray_ft_increment[i] < break7:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.8
            elif break7 <= MyArray_ft_increment[i] < break8:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.9
            elif break8 <= MyArray_ft_increment[i] < break9:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 0.9
            elif MyArray_ft_increment[i] >= break9:
                MyArray_pipe_moment[i] = tubing_moment_increment + MyArray_pipe_moment[i - 1] * 1

    if total_length != 0:  # Check if total_length is not 0

        if motor1 is not None and motor2 is not None:
            # Initialize MyArray_pipe_moment (assuming its size is 1001 and initialized to some default values)
            MyArray_pipe_moment = [0] * 1002
            #tubing_moment_2 = 1  # Define tubing_moment_2 within this block (replace `some_value_2` with actual value)
            MyArray_pipe_moment[0] = tubing_moment_2

            stinger_moment_length = (motor1 + motor2) / (total_length / 1000)
            stinger_moment_increment = tubing_moment_2 / stinger_moment_length

            for i in range(1, 1002):
                if MyArray_ft_increment[i] <= break2:
                    MyArray_pipe_moment[i] = MyArray_pipe_moment[i - 1] - stinger_moment_increment

        elif motor1 is not None and motor2 is None:
            # Initialize MyArray_pipe_moment (assuming its size is 1001 and initialized to some default values)
            MyArray_pipe_moment = [0] * 1002
            #tubing_moment_2 = 1  # Define tubing_moment_2 within this block (replace `some_value_2` with actual value)
            MyArray_pipe_moment[0] = tubing_moment_2

            stinger_moment_length = (motor1) / (total_length / 1000)
            stinger_moment_increment = tubing_moment_2 / stinger_moment_length

            for i in range(1, 1002):  # tubing bending moment effect on the bottom of the ESP string
                if MyArray_ft_increment[i] <= break1:  # defines the point of tubing bending moment applied to string which is to bottom motor
                    MyArray_pipe_moment[i] = MyArray_pipe_moment[i - 1] - stinger_moment_increment

    else:
        # Set values to 0 when total_length is 0
        MyArray_pipe_moment = [0] * 1002
        tubing_moment_2 = 0
        stinger_moment_length = 0
        stinger_moment_increment = 0

    max_deflection = 0  # For finding the minimum deflection
    max_stress = 0
    #stress_concentration_motor = 1
    #stress_concentration_motor_A = 1
    #seal_loadfactor = 1
    #seal_base_stress_modifier = 0.85
    #stress_reduction = 1
    #seal_neck_stress = 1
    seal_neck_stress_correction = [0] * 1002

    # Iterate through the arrays (starting at index 1 to 1001, assuming zero-based indexing in Python)
    for i in range(1, 1002):
        if total_length in [None, 0]:
            load = 0
        else:
            load = (average_I * 384 * modulus * (deflection - (bendingdeviation * 2 - bendingdeviation * 2 * t_path_new))) / 5 / (total_length * 12) ** 4
            # Deflection calculation
            MyArray_deflection[i] = load * MyArray_in_increment[i] / (24 * modulus * average_I) * ((total_length * 12) ** 3 - (2 * total_length * 12) * (MyArray_in_increment[i]) ** 2 + (MyArray_in_increment[i]) ** 3) * -1

        # Load calculation
        if pump2 is not None:
            # Iterate through the array and perform the calculations
            for i in range(1,len(MyArray_inertia1)):  # Assuming you want to start at index 1 to avoid out-of-range errors
                # Load calculation
                if MyArray_inertia1[i] == sealI and MyArray_inertia2[i] == sealneckI:
                    MyArray_load[i] = (MyArray_inertia1[i] / average_I * load) * seal_loadfactor
                else:
                    MyArray_load[i] = (MyArray_inertia1[i] / average_I) * load

                # Moment calculation
                if MyArray_inertia2[i - 1] == motorI and MyArray_inertia2[i] == motorneckI:
                    MyArray_moment[i] = ((MyArray_load[i] * MyArray_in_increment[i] / 2 * (
                                total_length * 12 - MyArray_in_increment[i]) / stress_concentration_2)) + MyArray_pipe_moment[i]
                else:
                    MyArray_moment[i] = ((MyArray_load[i] * MyArray_in_increment[i] / 2 * (total_length * 12 - MyArray_in_increment[i]))) + MyArray_pipe_moment[i]

        # Track the minimum deflection
        for i in range(1, 1002):
            if max_deflection > MyArray_deflection[i]:
                max_deflection = MyArray_deflection[i]

    # Assuming you need to store the max_deflection result somewhere
    #print(max_deflection * -1)
    MyArray_Stress_orientation_modifier=[0]*1002


    # Second loop for calculating Stress Orientation Modifier
    for i in range(1, 1002):
        # Check if sealneckC, seal_neck_stress, and Seal_Hsg_Stress_Mod are not None
        if seal1 is not None:
            if MyArray_centroid[i] == sealneckC:
                MyArray_Stress_orientation_modifier[i] = seal_neck_stress * (1 - MyArray_seal_neck_stress_correction[i])
            elif MyArray_centroid[i] == sealC:
                MyArray_Stress_orientation_modifier[i] = Seal_Hsg_Stress_Mod * (1 - MyArray_seal_neck_stress_correction[i])
        else:
            # Handle the case where the required values are None (if needed)
            MyArray_Stress_orientation_modifier[i] = 0

    # Third loop for Mod 1, Mod 2, Mod 3, and Mod 4 calculations
    # Iterate over the valid range of indices (1 to len(MyArray_centroid) - 2)
    for i in range(1, len(MyArray_centroid) - 1):
        if MyArray_centroid[i] == motorneckC and MyArray_centroid[i - 1] == motorC:
            MyArray_mod_1[i] = stress_concentration_motor
        elif MyArray_centroid[i] == motorneckC and MyArray_centroid[i + 1] == motorC:
            MyArray_mod_1[i] = stress_concentration_motor_A
        elif MyArray_centroid[i] == sealneckC and MyArray_centroid[i - 1] == motorC:
            MyArray_mod_1[i] = stress_concentration_motor
        elif MyArray_centroid[i] == sealneckC and MyArray_centroid[i + 1] == sealC:
            MyArray_mod_1[i] = stress_concentration_motor_A
        elif MyArray_centroid[i] == sealneckC and MyArray_centroid[i - 1] == sealC:
            MyArray_mod_1[i] = stress_concentration_motor
        elif MyArray_centroid[i] == intakeneckC and MyArray_centroid[i - 1] == sealC:
            MyArray_mod_1[i] = stress_concentration_1
        elif MyArray_centroid[i] == intakeneckC and MyArray_centroid[i + 1] == intakeC:
            MyArray_mod_1[i] = stress_concentration_2
        elif MyArray_centroid[i] == intakeneckC and MyArray_centroid[i - 1] == intakeC:
            MyArray_mod_1[i] = stress_concentration_1
        elif MyArray_centroid[i] == pumpneckC and MyArray_centroid[i - 1] == intakeC:
            MyArray_mod_1[i] = stress_concentration_1
        elif MyArray_centroid[i] == pumpneckC and MyArray_centroid[i + 1] == pumpC:
            MyArray_mod_1[i] = stress_concentration_2
        else:
            MyArray_mod_1[i] = 1

        if MyArray_centroid[i] == sealneckC and MyArray_centroid[i - 1] == motorC:
            MyArray_mod_2[i] = 1
        else:
            MyArray_mod_2[i] = 0

        if MyArray_inertia2[i - 1] == motorI and MyArray_inertia2[i] == motorneckI:
            MyArray_mod_3[i] = 1.5
        else:
            MyArray_mod_3[i] = 0

        if MyArray_inertia2[i - 1] == motorI and MyArray_inertia2[i] == motorneckI:
            MyArray_mod_4[i] = seal_base_stress_modifier
            #print(f'Mod4 worked {MyArray_mod_4[i]}')
        else:
            MyArray_mod_4[i] = 1

    max3_value = max(MyArray_mod_3)
    #print(f"Maximum value of MyArray_mod_3: {max3_value}")
    min4_value = min(MyArray_mod_4)
    #print(f"Maximum value of MyArray_mod_4: {min4_value}")

    # Final loop for stress calculation
    if pump2 is not None:
        for i in range(1, 1002):  # Loop over the range 1 to 1000 (inclusive)
            if MyArray_mod_2[i] == 1:
                #print("mod2")
                MyArray_stress[i] = ((MyArray_moment[i] * MyArray_centroid[i] / MyArray_inertia2[i] * MyArray_mod_1[i] * seal_base_stress_modifier) / MyArray_mod_4[i]) + MyArray_stress_wtadder[i] +  MyArray_Stress_orientation_modifier[i]
            elif MyArray_mod_3[i] == 1.5:
                #print("mod3")
                MyArray_stress[i] = ((MyArray_moment[i] * MyArray_centroid[i] / MyArray_inertia2[i] * MyArray_mod_1[i] / stress_reduction) / MyArray_mod_4[i]) + MyArray_stress_wtadder[i] + MyArray_Stress_orientation_modifier[i]
            else:
                 #print the values of the arrays for the specific index i
                MyArray_stress[i] = ((MyArray_moment[i] * MyArray_centroid[i] / MyArray_inertia2[i] * MyArray_mod_1[i]) / MyArray_mod_4[i]) + MyArray_stress_wtadder[i] + MyArray_Stress_orientation_modifier[i]

    #print(f'seal_base_stress_modifier={seal_base_stress_modifier}')
    #print(f'stress Reduction={stress_reduction}')
    # Initialize the max_stress variable
    max_stress = 0
    #print(MyArray_stress)
    # Loop to find the maximum stress in MyArray_stress
    for i in range(1, 1002):  # Adjusting for Python's zero-based index
        if MyArray_stress[i] > max_stress:
            max_stress= MyArray_stress[i]
            #print (max_stress)
    max_stress=round(max_stress)
    max_stress = "{:,}".format(max_stress)
    # Assuming you want to #print or store the max_stress
    #print(max_stress)

    # Now loop through MyArray_ft_increment in steps of 20 and store in MyArray_axis
    for i in range(0, 1002, 20):  # 0, 1001, and step 20
        MyArray_axis[i] = MyArray_ft_increment[i]

    if isinstance(n_clicks, list):
        n_clicks = n_clicks[0]  # Ensure we get the integer value

    #print(f"n_clicks: {n_clicks}")
    #print(MyArray_ft_increment)
    #print(MyArray_stress)

    if n_clicks > 0:
        print("it worked")
        print(f"Max Stress: {max_stress}")
        print(f"Dog Leg Severity: {dls}")
        print(f"Data points: {len(MyArray_ft_increment)}")

        fig = go.Figure(
            data=[
                go.Scattergl(
                    x=MyArray_ft_increment,
                    y=MyArray_stress,
                    mode="lines",
                    name="Stress",
                    line=dict(color="red")
                ),
                go.Scattergl(
                    x=MyArray_ft_increment,
                    y=MyArray_deflection,
                    mode="lines",
                    name="Deflection",
                    line=dict(color="blue"),
                    yaxis="y2"  # Specify that this trace should use the second y-axis
                )
            ],
            layout=go.Layout(
                title="Max Stress and Deflection Plot",
                xaxis=dict(title="Equipment String Length (ft)"),
                yaxis=dict(title="Bending Stress (psi)"),  # Primary y-axis
                yaxis2=dict(
                    title="Deflection (in)",  # Secondary y-axis title
                    overlaying="y",  # Overlay this axis on the primary y-axis
                    side="right"  # Place the second y-axis on the right
                ),
                annotations=[  # Add annotation for max stress above the plot
                    dict(
                        x=0.5,  # Position annotation at the center of the plot (adjust as necessary)
                        y=1.2,  # Position above the plot (y = 1.1 is above the plot)
                        xref="paper",  # Use relative coordinates for x (0 to 1 across the plot width)
                        yref="paper",  # Use relative coordinates for y (0 to 1 across the plot height)
                       text=f"Max Stress: {max_stress} psi<br>Dog Leg Severity: {dls} deg/100ft",  # Text for the annotation
                        showarrow=False,  # Don't show an arrow
                        font=dict(size=14, color="black"),  # Font settings for the annotation
                        bgcolor="rgba(255, 255, 255, 0.7)",  # Background color for the text box
                        borderpad=4  # Padding around the text box
                    )
                ]
            )
        )


        return fig  # Return two separate figures for stress/deflection and clearance (circles)
    else:
        return go.Figure() # Return empty figures when no button click has occurred
@app.callback(
    Output("clearance-plot", "figure"),
    [Input("clearance-plot-button", "n_clicks"),
     Input("motor-series-dropdown", "value"),
    Input("seal-series-dropdown", "value"),
    Input("gas-sep-series-dropdown", "value"),
    Input("pump-series-dropdown", "value"),
    Input("casing-dropdown", "value"),
    Input("casing-weight-dropdown", "value"),
    Input("casing-dim-dropdown", "value"),
     ]
)
def update_clearance_plot(n_clicks, motor_equipment, seal_equipment, gassep_equipment, pump_equipment, casing_selection, weight_selection, casing_dim):
    if n_clicks > 0:
        def convert_casing_size(casing_size):
            if isinstance(casing_size, str) and " " in casing_size:
                whole_number, fraction = casing_size.split()
                whole_number = float(whole_number)
                numerator, denominator = map(int, fraction.split("/"))
                decimal_fraction = numerator / denominator
                return whole_number + decimal_fraction
            else:
                return float(casing_size)  # Return as float if already decimal

        # Convert the casing size (e.g., '7 5/8') to decimal
        casing_selection2 = convert_casing_size(casing_selection)

        # Calculate the casing OD radius (half of casing diameter)
        casing_OD_radius = casing_selection2 / 2
        motor_equipment = float(motor_equipment)
        motor_radius = motor_equipment / 200  # Since diameter is motor_equipment / 100, radius is half of that

        # Parametric equation for the motor circle with the calculated radius
        theta = [i * 0.01 for i in range(0, 628)]  # Parametric equation for circle
        motor_x = [motor_radius * math.cos(t) for t in theta]  # X points of motor circle with updated radius
        motor_y = [motor_radius * math.sin(t) for t in theta]  # Y points of motor circle with updated radius

        casing_id_value = None

        # Check if casing_dim, casing_selection, and weight_selection are set
        if not casing_dim or not casing_selection or not weight_selection:
            return go.Figure()  # Return an empty figure if no casing info is provided

        # Determine if the user selected "Nominal" or other option for casing_dim
        if casing_dim == "Nominal":
            # Access the corresponding data from casing_nominal (assuming it's a predefined dictionary)
            casing_data = casing_nominal.get(casing_selection, [])
        else:
            # Access the corresponding data from casing_id (assuming it's a predefined dictionary)
            casing_data = casing_id.get(casing_selection, [])

        # Iterate through casing_data to find the corresponding weight
        for weight in casing_data:
            if weight['value'] == weight_selection:
                casing_id_value = weight['id']  # Set the casing ID value when a match is found
                break  # Exit the loop once the correct casing ID is found

        # If casing_id_value is set, calculate the casing circle radius
        if casing_id_value:
            casing_radius = casing_id_value / 2  # Assuming casing_id_value is in diameter, divide by 200 for radius
        else:
            casing_radius = 0  # If no valid casing_id_value, set to 0 (no casing circle)

        casing_OD_x = [casing_OD_radius * math.cos(t) for t in theta]  # X points of casing circle
        casing_OD_y = [casing_OD_radius * math.sin(t) for t in theta]  # Y points of casing circle

        # Parametric equation for the casing circle with the calculated radius
        casing_x = [casing_radius * math.cos(t) for t in theta]  # X points of casing circle
        casing_y = [casing_radius * math.sin(t) for t in theta]  # Y points of casing circle

        seal_equipment=float(seal_equipment)
        seal_radius = seal_equipment / 200  # Assuming seal_selection is in diameter, divide by 200 for radius
        seal_x = [seal_radius * math.cos(t) for t in theta]  # X points of motor circle with updated radius
        seal_y = [seal_radius * math.sin(t) for t in theta]  # Y points of motor circle with updated radius

        gassep_equipment = float(gassep_equipment)


        gassep_radius = gassep_equipment / 200# Assuming seal_selection is in diameter, divide by 200 for radius
        gassep_x = [gassep_radius * math.cos(t) for t in theta]  # X points of motor circle with updated radius
        gassep_y = [gassep_radius * math.sin(t) for t in theta]  # Y points of motor circle with updated radius

        if pump_equipment == "401":
            #print("ohno")
            pump_final = "400"
        else:
            pump_final = pump_equipment

        pump_equipment2 = float(pump_final)
        #print(f'pump={pump_equipment2}')
        pump_radius = pump_equipment2 / 200  # Assuming seal_selection is in diameter, divide by 200 for radius
        pump_x = [pump_radius * math.cos(t) for t in theta]  # X points of motor circle with updated radius
        pump_y = [pump_radius * math.sin(t) for t in theta]  # Y points of motor circle with updated radius

        # Find the maximum radius and determine which equipment to plot
        max_radius = max(seal_radius, gassep_radius, pump_radius)

        # Determine which equipment to display based on the largest radius
        if max_radius == seal_radius:
            selected_radius = seal_radius
            selected_color = 'rgba(0, 255, 0, 1)'  # Green for Seal
            equipment_name = "Seal"
        elif max_radius == pump_radius:
            selected_radius = pump_radius
            selected_color = 'rgba(0, 0, 255, 1)'  # Blue for Pump
            equipment_name = "Pump"
        elif max_radius == gassep_radius:
            selected_radius = gassep_radius
            selected_color = 'rgba(255, 0, 0, 1)'  # Red for Gassep
            equipment_name = "Gassep"

        circle_x = [selected_radius * math.cos(t) for t in theta]  # X points of selected circle
        circle_y = [selected_radius * math.sin(t) for t in theta]  # Y points of selected circle


        # Position the motor circle's center so that its edge touches the top edge of the casing circle
        motor_center_y = casing_radius - motor_radius  # Motor center is at casing_radius - motor_radius
        equipment_center_y = casing_radius - selected_radius

        motor_clearance=casing_id_value-(motor_radius*2)
        mle_equipment= casing_id_value-(selected_radius*2)-0.615
        mle_motor = casing_id_value - (motor_radius * 2) - 0.615 / 2
        #print(casing_id_value)
        #print(mle_equipment)
        #print(mle_motor)
        #print(mle_clearance)
        a = .65  # Half the width (1 wide)
        b = 0.3075  # Half the height (0.615 tall)

        mle_x = [a * math.cos(t) for t in theta]
        mle_y = [b * math.sin(t) for t in theta]

        if motor_radius > selected_radius:
            mle_center_y = motor_center_y - motor_radius
            mle_clearance = mle_motor
            equipment_center_y=motor_center_y
        else:
            mle_center_y = equipment_center_y - selected_radius - b
            motor_center_y = equipment_center_y
            mle_clearance=mle_equipment

        mle_y_adjusted = [y + mle_center_y for y in mle_y]

        # Create the clearance plot (two circles: casing and motor)
        clearance_fig = go.Figure(
            data=[
                go.Scatter(
                    x=casing_OD_x,
                    y=casing_OD_y,
                    mode='lines',  # This specifies that the shape will be a line
                    fill='toself',  # This will fill the circle with a solid color
                    fillcolor='rgba(255, 0, 0, 1)',  # Light red fill with some transparency for casing
                    name="Casing OD",
                    line=dict(width=0)  # Remove the outline by setting the line width to 0
                ),
                go.Scatter(
                    x=casing_x,
                    y=casing_y,
                    mode='lines',  # This specifies that the shape will be a line
                    fill='toself',  # This will fill the circle with a solid color
                    fillcolor='rgba(255, 255, 255, 1)',  # Light red fill with some transparency for casing
                    name="Casing ID",
                    showlegend=False,
                    line=dict(width=0)  # Remove the outline by setting the line width to 0
                ),
                go.Scatter(
                    x=[x + 0 for x in motor_x],  # Align motor circle to the center x-axis
                    y=[y + motor_center_y for y in motor_y],  # Move motor circle to the adjusted y position
                    mode='lines',  # This specifies that the shape will be a line
                    fill='toself',  # This will fill the circle with a solid color
                    fillcolor='rgba(0, 0, 255, 1)',  # Solid blue fill with no transparency
                    name="Motor",
                    line=dict(width=0)  # Remove the outline by setting the line width to 0
                ),
                go.Scatter(
                    x=circle_x,
                    y=[y + equipment_center_y for y in circle_y],
                    mode='lines',  # This specifies that the shape will be a line
                    fill='toself',  # This will fill the circle with a solid color
                    fillcolor='rgba(0, 255, 0, .75)',  # Fill the circle with the selected color
                    name=f"{equipment_name}",  # Dynamically set the name of the equipment
                    line=dict(width=0)  # Remove the outline by setting the line width to 0
                ),
                go.Scatter(
                    x=mle_x,  # X points of the oval
                    y=mle_y_adjusted,  # Y points of the oval with adjusted position
                    mode='lines',  # This specifies that the shape will be a line
                    fill='toself',  # This will fill the oval with a solid color
                    fillcolor='rgba(0, 0, 0, 1)',  # Orange fill for the oval
                    name="MLE",  # Name for the oval in the legend
                    line=dict(width=0),  # Remove the outline by setting the line width to 0
                    legendgroup="equipment"  # Grouping oval-related traces together in the legend
                ),
            ],
            layout=go.Layout(
                title="Clearance Plot",
                xaxis=dict(
                    scaleanchor="y",
                    zeroline=False,
                    showline=False,  # Hides the axis line
                    showgrid=False,  # Hides the grid
                    showticklabels=False  # Hides tick labels
                ),
                yaxis=dict(
                    scaleanchor="x",
                    zeroline=False,
                    showline=False,  # Hides the axis line
                    showgrid=False,  # Hides the grid
                    showticklabels=False  # Hides tick labels
                ),
                showlegend=True,
                legend=dict(
                    x=0.85,
                    y=0.5,
                    traceorder='normal',
                    orientation='v',
                    font=dict(
                        size=12,
                        color='black'
                    ),
                    bgcolor='rgba(255, 255, 255, 0.8)',
                    bordercolor='rgba(255, 255, 255, 0)',
                    borderwidth=0
                ),
                plot_bgcolor='white',
                margin=dict(t=100, b=0, l=0, r=0),
                annotations=[
                    # Motor Clearance Annotation
                    dict(
                        x=0.5,  # X position in plot relative to axis
                        y=1.05,  # Y position in plot relative to axis
                        xref="paper",  # Use paper coordinates for position
                        yref="paper",
                        text=f"Motor Clearance: {motor_clearance:.2f}",
                        showarrow=False,
                        font=dict(
                            size=12,
                            color='black'
                        ),
                        align='center'
                    ),
                    # MLE Clearance Annotation
                    dict(
                        x=0.5,  # X position in plot relative to axis
                        y=1.12,  # Y position in plot relative to axis
                        xref="paper",  # Use paper coordinates for position
                        yref="paper",
                        text=f"MLE Clearance: {mle_clearance:.2f}",
                        showarrow=False,
                        font=dict(
                            size=12,
                            color='black'
                        ),
                        align='center'
                    )
                ]
            ),
        )


        return clearance_fig
    else:
        # Return an empty figure if no button click has occurred
        return go.Figure()

if __name__ == "__main__":
    app.run_server(debug=True)
