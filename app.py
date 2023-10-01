import streamlit as st
st.title("title -> geeksforgeeks")
st.header("header -> geeksforgeeks")
st.subheader("subheader -> geeksforgeeks")
st.text("text -> geeksforgeeks")

st.markdown("# Hi")
st.markdown("#### Hi")


st.success("success")
st.info("information")
st.warning("warning")
st.error("error")
st.exception(ZeroDivisionError('Division not possible'))

st.help(ZeroDivisionError)
st.write("range(1,9)")
st.write(range(1,9))
st.write(1+4+3)
st.write("1*4*3")

st.code('x=10\n'
         'for i in range(x) :\n'
         'print(i)')

st.subheader('checkbox')
st.checkbox('male')
if (st.checkbox('adult')):
    st.write('you are an adult!')

st.subheader('radiobutton')
radiobutton = st.radio('select :',('male','female','others'))
if (radiobutton=='male'):
    st.write('you are a male')
elif (radiobutton=='female'):
    st.write('you are a female')
elif (radiobutton=='others'):
    st.write('you are an other gender')

st.subheader('Select box')                             #selectbox
selectbox =  st.selectbox('Data Science:',['Deeplearning','Computer Vision',
                                           'Natural language Processing',      'Image processing','webscrapping','Machine learning'])
st.write("You have selected :",selectbox)

st.subheader('Multiselectbox')                          #multiselect
Multiselectbox = st.multiselect('Data Science:',['Deeplearning','Computer Vision',
                                           'Natural language Processing',      'Image processing','webscrapping','Machine learning'])
st.write("you have selected",len(Multiselectbox),"courses")

st.subheader("button")
if(st.button('click me')):
    st.write('Thanks for clicking me')

st.subheader('slider')
vol = st.slider('Adjust the Volume ',1,100,step = 1)
st.write('Volume is ',vol)

st.subheader("Text input")
Username = st.text_input("UserName :")
Password = st.text_input("Password :",type = 'password')

st.subheader("Text Area")
st.text_area('Write Something Interesting about yourself')

st.subheader("Input Number")
st.number_input('Enter your age',18,110)

st.subheader("Input Date")
st.date_input('Date')

st.subheader("Input Time")
st.time_input('Time')




