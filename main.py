import streamlit as st
import seaborn as sns

def main():
    st.write("Hola mundo!")
    with st.expander("Dataframe"):
        st.dataframe(sns.load_dataset("iris"))
    st.write("Adiós mundo...")

if __name__ == "__main__":
    main()