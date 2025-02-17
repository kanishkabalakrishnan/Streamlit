import streamlit as st


#set title


from PIL import Image


#Set title

st.title('Total Data Science')

image = Image.open('stream.png')
st.image(image,use_column_width=True)



st.title("Our streamlit App")

st.header("This is a header")

st.subheader("This is a subheader")

st.text("writing a text in streamlit")

st.markdown("this is a markdown just like we do in Jupyter notebook")


#message to the user

st.success("success")

st.info(" you can use this to show information")

st.warning("this is a warning")

st.error("this an error")

#Display and style data

import numpy as np 
import pandas as pd

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)


#just printint a line
st.text("----"*100)


#Display a line chart.

chart_data = pd.DataFrame(
		 	 np.random.randn(20, 3),
		    columns=['a', 'b', 'c'])
	
st.line_chart(chart_data)

st.text("----"*100)

#Display a area chart.

chart_data = pd.DataFrame(
		     np.random.randn(20, 3),
  			 columns=['a', 'b', 'c'])

st.area_chart(chart_data)


st.text("----"*100)

#creatining a bar chart

chart_data = pd.DataFrame(
  	 		 np.random.randn(50, 3),
   			 columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.text("----"*100)

#creating a histogram

import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)

st.pyplot()


st.text("----"*100)

# creating distplot


import pandas as pd
import plotly.express as px

# Create a DataFrame with hardcoded data
data = {
    'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'y': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    'category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
}

df = pd.DataFrame(data)

# Create a scatter plot
fig = px.scatter(df, x='x', y='y', color='category', 
                 title='Scatter Plot with Hardcoded Data',
                 labels={'x': 'X Axis', 'y': 'Y Axis'},
                 color_discrete_map={'A': 'red', 'B': 'blue'})

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.text("----"*100)


#creating map

import pandas as pd
import numpy as np

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)


st.text("----"*100)

#Creating a button

if st.button('Say hello'):
   st.write('Why hello there')
else:
	st.write('Goodbye')


st.text("----"*100)


#Creating a radio button

genre = st.radio(
        "What's your favorite movie genre",
       ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
      st.write('You selected comedy.')
else:
      st.write("You didn't select comedy.")



st.text("----"*100)
  

  #SelectText


option = st.selectbox(
	     'How would you like to be contacted?',
	     ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)    


#Multiselect

st.text("----"*100)

options = st.multiselect(
	     'What are your favorite colors',
	     ['Green', 'Yellow', 'Red', 'Blue'],
	     ['Yellow', 'Red'])

st.write('You selected:', options)


st.text("----"*100)

#Slider

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


#slider example 2, selecting range of values

values = st.slider(
 	     'Select a range of values',
	     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


st.text("----"*100)

#Accepting User Input


#TEXT

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


#NUMBER

number = st.number_input('Insert a number')
st.write('The current number is ',number)



st.text("----"*100)

#File Uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
   data = pd.read_csv(uploaded_file)
   st.write(data)
   st.success("success")
else:
	st.warning("this is a warning: Upload a csv file")
    


st.text("----"*100)
#Color Picker

color = color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


st.text("----"*100)

#Adding Widget to side bar

add_selectbox = st.sidebar.selectbox(
    "What is your favorite course?",
    ("A course from Total Data Science", "Others", "Am not sure")
)


st.text("----"*100)

#Add comments in your App


with st.echo():
 	 st.write('This code will be printed')


#Display progress and status


st.text("----"*100)


import time

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)


#Temporarily displays a message while executing a block of code.

with st.spinner('Wait for it...'):
     time.sleep(9)
st.success('Done!')


st.text("----"*100)

#Draw celebratory balloons.
st.balloons()
















