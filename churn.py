import streamlit as st
import pandas as pd
import numpy as np
import pickle

# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier

# loading in the model to predict on the data
pickle_in = open('rf.pkl', 'rb')
rf = pickle.load(pickle_in)

def welcome():
    return 'Welcome All!'

# Churn Prediction

def prediction(voice_mail_plan, voice_mail_messages, day_mins, evening_mins, customer_service_calls, international_plan, day_charge,
       evening_charge, total_charge):  
   
    prediction = rf.predict( 
        [[voice_mail_plan, voice_mail_messages, day_mins, evening_mins, customer_service_calls, international_plan, day_charge,
       evening_charge, total_charge]])
    print(prediction)
    return prediction


def main():
    service_call = [0,1,2,3,4,5,6,7,8,9]

    st.write("""

    # TELECOM CHURN PREDICTOR MODEL

    """)



    st.sidebar.header('User Input Values')



#    def user_input_features():

    voice_mail_plan = st.sidebar.selectbox('Voice Mail Plan:', (0, 1))

    voice_mail_messages = st.sidebar.slider('Voice Mail Messages', min_value=0, max_value=51, value=8)

    day_mins = st.sidebar.slider('Day Minutes',min_value=34 ,max_value=326, value=179)

    evening_mins = st.sidebar.slider('Evening Minutes',min_value=63, max_value=339,value=201)
    
    customer_service_calls = st.sidebar.selectbox('Customer Service Calls', service_call, 0)
    
    international_plan = st.sidebar.selectbox('International Plan', (0, 1))
    
    day_charge = st.sidebar.slider('Day Charges',min_value=5, max_value=55,value=30)
    
    evening_charge = st.sidebar.slider('Evening Charges',min_value=5, max_value=29,value=17)
    
    total_charge = st.sidebar.slider('Total Charges',min_value=31, max_value=88,value=59)
    
    

    
#     data = {'voice_mail_plan': voice_mail_plan, 
#             'voice_mail_messages': voice_mail_messages, 
#             'day_mins': day_mins,
#             'evening_mins': evening_mins, 
#             'customer_service_calls': customer_service_calls,
#             'international_plan': international_plan, 
#             'day_charge': day_charge,
#             'evening_charge': evening_charge, 
#             'total_charge': total_charge}
#     features = pd.DataFrame(data, index=[0])
#     return features

#     #df1 = user_input_features()

#     st.subheader('User Entered parameters:')

#     st.write(features)


    if st.button('Predict'):
        result = prediction(voice_mail_plan, voice_mail_messages, day_mins, evening_mins, customer_service_calls, international_plan, day_charge, evening_charge, total_charge)
    
        if result == 1:
            st.warning('Yes, the customer will terminate the service.')
        else:
            st.success('No, the customer is happy with Telco Services.')


if __name__=='__main__':
    main()



