import streamlit as sl
from multiapp import MultiApp
import home
import about
app =MultiApp()
sl.title('Multi-page')

app.add_app('Home',home.app)
app.add_app('About',about.app)

app.run()