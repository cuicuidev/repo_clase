import streamlit as st
import seaborn as sns
import plotly.express as px
import pickle as pkl

def main():
    st.set_page_config(layout= "wide")

    df = sns.load_dataset("iris")
    st.write("# Iris")
    with st.expander("Dataframe"):
        st.dataframe(df)

    col1, col2 = st.columns(2)

    x1 = col1.slider(df.columns[0], min_value=df.min().iloc[0], max_value=df.max().iloc[0], step=0.01)
    x2 = col1.slider(df.columns[1], min_value=df.min().iloc[1], max_value=df.max().iloc[1], step=0.01)

    x3 = col2.slider(df.columns[2], min_value=df.min().iloc[2], max_value=df.max().iloc[2], step=0.01)
    x4 = col2.slider(df.columns[3], min_value=df.min().iloc[3], max_value=df.max().iloc[3], step=0.01)

    df.loc[df.shape[0]] = [x1,x2,x3,x4, "nueva_flor"]
    col1.plotly_chart(px.scatter(data_frame=df, x="sepal_length", y="sepal_width", color="species", color_discrete_sequence=px.colors.qualitative.Dark2))
    col2.plotly_chart(px.scatter(data_frame=df, x="petal_length", y="petal_width", color="species", color_discrete_sequence=px.colors.qualitative.Dark2))

    with open("model.pkl", "br") as file:
        model = pkl.load(file)

    if st.button("Predict"):
        st.success(model.predict([[x1,x2,x3,x4]])[0])

if __name__ == "__main__":
    main()