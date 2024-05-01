# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import joblib
import streamlit

model = joblib.load(r'IrisModel.pkl')


# user define function
def iris_prediction(var_1,var_2,var_3,var_4):
    
    input_data = np.array([[var_1,var_2,var_3,var_4]])
    model_prediction = model.predict(input_data)
    return model_prediction


def run():
    streamlit.title("Iris Flower Classification- Model Created By Oracle IDC ")
    html_temp="""

    """
    streamlit.markdown(html_temp)
    
    var_1 = float(streamlit.text_input("Speal Len",value="0.0"))
    var_2 = float(streamlit.text_input("Speal Width",value="0.0"))
    var_3 = float(streamlit.text_input("Petal Len",value="0.0"))
    var_4 = float(streamlit.text_input("Petal Width",value="0.0"))

    
    predition = ""
    
    if streamlit.button("Predict"):
        predition = iris_prediction(var_1,var_2,var_3,var_4)
        
    streamlit.success("The Prediction by Model: {}".format(predition))
    
if __name__=='__main__':
    run()    











