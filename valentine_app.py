import streamlit as st
import time

def show_flower_gif():
    st.image("https://i.gifer.com/Rgcm.gif", use_container_width=True)

def main():
    st.title("Will You Be My Valentine? 💖")
    st.write("Click the button below to answer!")
    
    if st.button("Yes, I will! ❤️"):
        st.success("Yay! Here's a dance for you! 🌸🌼🌷")
        time.sleep(1)
        show_flower_gif()
    elif st.button("No, sorry 😢"):
        st.warning("mxm, tsamo robala")

if __name__ == "__main__":
    main()