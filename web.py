import streamlit as sl
def bro(a,b):
    return a+b
    
sl.title("this is where u have enter u r titel of site")
tab1,tab2=sl.tabs(["enter tab 1 name","tab2"])
with tab1:
    col=sl.columns(3)
    with col[0]:
        t=sl.number_input("hear where can can take number input ",value=1)
        h=sl.number_input("hea where can can take number input ",value=1)
        if sl.button("answer"):
            sl.write(bro(t,h))
            
        
    with col[1]:
        
        sl.text_area("this is somw where to wriet some thing")
        sl.write("this to write some thing buy using .write opration")
    with col[2]:
        sl.write("this is col 3")
    