


import pandas as pd
import numpy as np

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('dataframe.csv')

mark_values = {2019:'2019',2020:'2020',2021:'2021'}

mark_values_month = {1:'Jan',2:'Feb',3:'Mar',
                    4:'Apr',5:'May',6:'Jun',
                    7:'Jul',8:'Aug',9:'Sep',
                    10:'Okt',11:'Nov',12:'Dec'}

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    
 # ----------------------HEADER-------------------------------  
html.Div([  
    html.Div([
        html.H1(children= "Sales Overview",
                className='H1')
    ],className='four columns'),
],className='header container'),
                    
html.Div([
    
# ----------------------LEFT COLUMN-------------------------------  
html.Div([  
    
    # ----------------------DROPDOWN-------------------------------  
    html.Div([ # ----------------------ROW START
        html.Div([
        
            dcc.Dropdown(id='region_code',
                options=[
                         {'label': y, 'value': y}
                         for y in df['region_code'].unique()],
                value=['DE','FR'],
                multi=True,
                clearable=False       
            ),],
        
        className='dropdown'),
        
        html.Div([
        
            dcc.Dropdown(id='product_category',
                options=[
                         {'label': y, 'value': y}
                         for y in df['product_category'].unique()],
                value=['Bikes','Accessories','Clothing'],
                multi=True,
                clearable=False       
            ),],
        
        className='dropdown'),
        
    ],className='row'), # ----------------------ROW END
    
    
    # ----------------------RANGE SLIDER YEAR-------------------------------  
    html.Div([ # ----------------------ROW START
        
        html.H4(children= "Year Slider:",style = {'color':'#fff'},
                className='H4'),
        
        html.Div([
            dcc.RangeSlider(id='the_year',
                min=2019,
                max=2021,
                value= [2019,2020],
                marks=mark_values,
                step=None)
        ],className='rangeslider'),
            
    # ----------------------RANGE SLIDER MONTH-------------------------------     
        html.Div([
            dcc.RangeSlider(id='the_month',
                min=1,
                max=12,
                value= [1,7],
                marks=mark_values_month,
                step=None)
        ],className='rangeslider'),            
    ],className='row'), # ----------------------ROW END
    
    
    
    html.Div([ # ----------------------ROW START
                 
    ],className='row'), # ----------------------ROW END
    
    
   html.Div([ # ----------------------ROW START
        
        html.H1(children= "Summary:",style = {'color':'#fff'},
                className='H1'),
        
        html.Summary(id='graph_summary',
                     className='summary'),
        ],
    className='row'),  # ----------------------ROW END  
    
    html.Div([ # ----------------------ROW START
        
        # ----------------------GRAPHIC 3-------------------------------    
        html.Div([
            
            dcc.Graph(id='graph_bar_product'),
        ],className='graphic_1'),
        
        ],
    className='row_bar'),  # ----------------------ROW END  
      

],className='left column'),
    

# ----------------------RIGHT COLUMN-------------------------------  
html.Div([
    
    # ----------------------GRAPHIC 1-------------------------------  
    html.Div([ # ----------------------ROW START
        
        html.Div([
            dcc.Graph(id='graph_pie'),
        ],className='graphic_1'),
        
    # ----------------------GRAPHIC 2-------------------------------    
        html.Div([
            dcc.Graph(id='graph_bar'),
        ],className='graphic_1'),
        
    ],className='row'), # ----------------------ROW END
    
    
],className='right column'),
                    

                    
# ----------------------ENDING-------------------------------   
],className = 'app container')    
            ],className = 'full body')

@app.callback(
    [Output('graph_pie', 'figure'),
    Output('graph_bar', 'figure'),
    Output('graph_summary', 'children'),
    Output('graph_bar_product', 'figure')],
    [Input('region_code', 'value'),
    Input('product_category', 'value'),
     Input('the_year','value'),
     Input('the_month','value')],
)

def cb(region_code, product_category,the_year,the_month):
    
    # ----------------------DATA-------------------------------   
    dff=df[(df['year']>=the_year[0])&(df['year']<=the_year[1])]
    dff=dff[(dff['month_nr']>=the_month[0])&(dff['month_nr']<=the_month[1])]
    dff = dff.query("region_code == @region_code and product_category == @product_category")
    
    # ----------------------GRAPHIC 1-------------------------------  
    graph_pie= px.pie(data_frame = dff, 
                        values="product_key",
                        names="product_category",
                        title='Product Category',
                      color_discrete_sequence=["#2CBFFE","#fe2cf8","#2cfec1"],
                        height=600)
    graph_pie.update_layout(paper_bgcolor='#171b26',title_font_color='white',legend_font_color='white')
    
    # ----------------------DATA------------------------------- 
    dff2 = dff.groupby(['full_name'], as_index = False)['sales_amount'].sum().sort_values('sales_amount', ascending = False).head(10)

    # ----------------------GRAPHIC 2-------------------------------
    graph_bar = px.bar(dff2, x="sales_amount",
                      y="full_name",
                      orientation='h',
                       color_discrete_sequence=["#2CBFFE"],
                     labels=dict(sales_amount="Sales Amount", full_name="Client Name"))
    
    graph_bar.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'},
                            paper_bgcolor='#171b26',font_color='white',plot_bgcolor='#171b26')

    # ----------------------SUMMARY-------------------------------
    graph_summary = dff.groupby(dff['year'])['full_name'].value_counts().count()
    
    
    # ----------------------DATA------------------------------- 
    dff3 = dff.groupby(['product_name'], as_index = False)['sales_amount'].sum().sort_values('sales_amount', ascending = False).head(10)
    # ----------------------GRAPHIC 3-------------------------------
    graph_bar_product = px.bar(dff3, x="sales_amount",
                      y="product_name",
                      orientation='h',
                       color_discrete_sequence=["#2CBFFE"],
                     labels=dict(sales_amount="Sales Amount", product_name="Product Name"))
    
    graph_bar_product.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'},
                            paper_bgcolor='#171b26',font_color='white',plot_bgcolor='#171b26')

    return (graph_pie,graph_bar,graph_summary,graph_bar_product)



if __name__ == '__main__':
    app.run_server(debug=True)