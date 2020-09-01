import streamlit as st

#title/text
st.title('Stream lit Tutorials')

# header/subheader
st.header('This is a header')
st.subheader('This is a sub header')


# text
st.text('hello streamlit')

# mardowm
st.markdown('## This is a markdown')

# colorful
st.success('This is success')
st.info('This is information')
st.warning('This is a warning')
st.error('this is an error')
st.exception("NameError('name three not deined)")

# Get help about python
st.help(range)

# writing text/ super function
st.write('Text with write')
st.write(range(10))

# images
from PIL import Image
img = Image.open('example.png')
st.image(img, width=300, caption='simple Image')

# videos
vid_file = open('example.mp4', 'rb').read()
st.video(vid_file)

# audio file

audio_file = open('examplemp3.mp3', 'rb').read()
st.audio(audio_file, format='audio/mp3')


# widget 
# checkbox
if st.checkbox('Show/Hide'):
    st.text('Showing or Hiding Widget')


# Radio
# status = st.radio("What is your status, ('active', 'inactive) ")

# if status == 'active':
#     st.success('you are active')
# else:
#     st.warning('inactive', 'activate')

# select box
occupation = st.selectbox("Your occupation", ["Programmer", "Developer"])
st.write('You selected this option', occupation)

# multiselect
location = st.multiselect('Where do you work', ('london', 'nairobi', 'meru'))
st.write('You selected', len(location), 'locations')


# slider
age = st.slider('What is your level?', 1,20)


# button
st.button('simple button')

if st.button('about'):
    st.text('stream is lit')




# text input
firstname = st.text_input('Enter your Name', 'Type here....')
if st.button('submit'):
    result = firstname.title()
    st.success(result)


# text area
me