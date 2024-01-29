import streamlit as st
from multiapp import MultiApp   
from plotting_map import *
from dataframe import *

app = MultiApp()

# Add all your application here
app.add_app("Mapping Demo",plotting_demo)
app.add_app("Dataframe", dataframe_demo)
#app.add_app("Data Stats", data_stats.app)

# The main app
app.run()