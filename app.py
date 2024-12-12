import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pickle
def flat_type_mapping(flt_type):
 
    if flt_type == '3 ROOM':

        flat_type_1= int(2)

    elif flt_type == '4 ROOM':

        flat_type_1= int(3)

    elif flt_type == '5 ROOM':

        flat_type_1= int(4)

    elif flt_type == '2 ROOM':

        flat_type_1= int(1)

    elif flt_type == 'EXECUTIVE':

        flat_type_1= int(5)

    elif flt_type == '1 ROOM':

        flat_type_1= int(0)

    elif flt_type == 'MULTI-GENERATION':

        flat_type_1= int(6)
 
    return flat_type_1
 
def flat_model_mapping(fl_m):
 
    if fl_m == 'Improved':
        flat_model_1= int(5)
    elif fl_m == 'New Generation':
        flat_model_1= int(12)
    elif fl_m == 'Model A':
        flat_model_1= int(8)
    elif fl_m == 'Standard':
        flat_model_1= int(17)
    elif fl_m == 'Simplified':
        flat_model_1= int(16)
    elif fl_m == 'Premium Apartment':
        flat_model_1= int(13)
    elif fl_m == 'Maisonette':
        flat_model_1= int(7)
 
    elif fl_m == 'Apartment':
        flat_model_1= int(3)
    elif fl_m == 'Model A2':
        flat_model_1= int(10)
    elif fl_m == 'Type S1':
        flat_model_1= int(19)
    elif fl_m == 'Type S2':
        flat_model_1= int(20)
    elif fl_m == 'Adjoined flat':
        flat_model_1= int(2)
 
    elif fl_m == 'Terrace':
        flat_model_1= int(18)
    elif fl_m == 'DBSS':
        flat_model_1= int(4)
    elif fl_m == 'Model A-Maisonette':
        flat_model_1= int(9)
    elif fl_m == 'Premium Maisonette':
        flat_model_1= int(15)
    elif fl_m == 'Multi Generation':
        flat_model_1= int(11)
 
    elif fl_m == 'Premium Apartment Loft':
        flat_model_1= int(14)
    elif fl_m == 'Improved-Maisonette':
        flat_model_1= int(6)
    elif fl_m == '2-room':
        flat_model_1= int(0)
    elif fl_m == '3Gen':
        flat_model_1= int(1)
 
    return flat_model_1

def town_mapping(town_map):
    if town_map == 'ANG MO KIO':
        town_1 = int(0)
    elif town_map == 'BEDOK':
        town_1 = int(1)
    elif town_map == 'BISHAN':
        town_1= int(2)
    elif town_map == 'BUKIT BATOK':
        town_1= int(3)
    elif town_map == 'BUKIT MERAH':
        town_1= int(4)
    elif town_map == 'BUKIT PANJANG':
        town_1= int(5)
 
    elif town_map == 'BUKIT TIMAH':
        town_1= int(6)
    elif town_map == 'CENTRAL AREA':
        town_1= int(7)
    elif town_map == 'CHOA CHU KANG':
        town_1= int(8)
    elif town_map == 'CLEMENTI':
        town_1= int(9)
    elif town_map == 'GEYLANG':
        town_1= int(10)
    elif town_map == 'HOUGANG':
        town_1 = int(11)
    elif town_map == 'JURONG EAST':
        town_1= int(12)
    elif town_map == 'JURONG WEST':
        town_1= int(13)
    elif town_map == 'KALLANG/WHAMPOA':
        town_1= int(14)
    elif town_map == 'MARINE PARADE':
        town_1= int(15)
 
    elif town == 'PASIR RIS':
        town_1= int(16)
    elif town == 'PUNGGOL':
        town_1= int(17)
    elif town == 'QUEENSTOWN':
        town_1= int(18)
    elif town == 'SEMBAWANG':
        town_1= int(19)
    elif town == 'SENGKANG':
        town_1= int(20)
 
    elif town == 'SERANGOON':
        town_1= int(21)
    elif town == 'TAMPINES':
        town_1= int(22)
    elif town == 'TOA PAYOH':
        town_1= int(23)
    elif town == 'WOODLANDS':
        town_1= int(24)        
    elif town == 'YISHUN':
        town_1= int(25)      
 
    return town_1

def predicting_the_price(year,flat_type,flr_area_sqm,flat_model,town,lease_commence_date,storey_srt,storey_end,
                                           remain_lease_yr,reamin_lease_mn):
    
    flat_type_integer = flat_type_mapping(flat_type)
    flat_model_integer = flat_model_mapping(flat_model)
    town_integer = town_mapping(town)
    storey_srt_log = np.log(storey_srt)
    storey_end_log = np.log(storey_end)

    with open(r"C:\Users\praba\Desktop\streamlit\Random_forest_model.pkl","rb") as f:
        model = pickle.load(f)

    user_data = np.array([[year,flat_type_integer,flr_area_sqm,flat_model_integer,town_integer,lease_commence_date,
                           storey_srt_log,storey_end_log,remain_lease_yr,reamin_lease_mn]])
    y_predict = model.predict(user_data)
    st.write("## :green[**the predicted price is:**]",int(np.exp(y_predict[0])))
#streamlit part
st.set_page_config(layout = "wide")

st.title("Singapore Flat Price Prediction")

with st.sidebar:
    select = option_menu("main_menu",["home","price_prediction","about"])

if select == "home":
    pass
elif select == "price_prediction":
    st.title("predict the house price")
    col1,col2 = st.columns(2)
    with col1:
        year = st.selectbox("select the year",[i for i in range(1950,2051)])

        flat_type= st.selectbox("Select the Flat Type", ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM',
                                                        'MULTI-GENERATION'])
        
        flr_area_sqm = st.number_input("enter the floor area sqm:")

        flat_model= st.selectbox("Select the Flat Model", ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                        'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2',
                                                        'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS',
                                                        'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation',
                                                        'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen'])
        
        town= st.selectbox("Select the Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                                            'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                                            'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                                            'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        
    with col2:
        lease_commence_date = st.selectbox("select lease_commence_date",[i for i in range(1900,2025)])

        storey_srt = st.selectbox("select the storey_start",[i for i in range(0,61)])
        storey_end = st.selectbox("select the storey_end",[i for i in range(0,61)])

        remain_lease_yr = st.selectbox("select the remaining_lease_year",[i for i in range(101)])

        reamin_lease_mn = st.selectbox("select the remaining_lease_month",[i for i in range(13)])

button = st.button("predict the price",use_container_width=True)
if button:
    predicted_price = predicting_the_price(year,flat_type,flr_area_sqm,flat_model,town,lease_commence_date,storey_srt,storey_end,
                                           remain_lease_yr,reamin_lease_mn)