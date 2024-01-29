# Import necessary libraries 
import streamlit as st


# Define the multipage class to manage the multiple apps in our program 
class MultiApp: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.apps = []
    
    def add_app(self, title, func) -> None: 
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 
            
            func: Python function to render this page in Streamlit
        """

        self.apps.append(
            {
                "title": title, 
                "function": func
            }
        )   

    def run(self):
        # Drodown to select the page to run  
        app = st.sidebar.radio(
            'Go To',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
  