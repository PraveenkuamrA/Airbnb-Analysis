import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide")
st.subheader('Airbnb Analysis')
hii=pd.read_csv(r'C:\Users\user\OneDrive\Desktop\praveen\airbnb.csv')

option = st.selectbox(":orange[SELECT COUNTRY]",('United States', 'Turkey', 'Hong Kong', 'Australia', 'Portugal','Brazil', 'Canada', 'Spain', 'China'),index=0)

a=hii[hii["country"] == option]
custom_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2', '#c2f0f0', '#ffb3b3']

# Create a Seaborn line plot
co1,co2=st.columns(2)
with co1:

    st.markdown(':blue[COUNTS OF BATHROOMS TYPE]')
    bathroom_type_counts = a['bathrooms'].value_counts()
    # Create a new DataFrame with 'bed_type' and 'count' columns
    bathroom_type_df = bathroom_type_counts.reset_index()
    bathroom_type_df.columns = ['bathrooms', 'count']
    # Print the new DataFrame
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(bathroom_type_df['bathrooms'], bathroom_type_df['count'],color=custom_colors)
    ax.set_xlabel('bathrooms')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    st.markdown(':blue[COUNTS OF BED TYPES]')
    bed_type_counts = a['bed_type'].value_counts()
    # Create a new DataFrame with 'bed_type' and 'count' columns
    bed_type_df = bed_type_counts.reset_index()
    bed_type_df.columns = ['bed_type', 'count']
    # Print the new DataFrame
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(bed_type_df['bed_type'], bed_type_df['count'],color=custom_colors)
    ax.set_xlabel('bed_type')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    option1=st.selectbox(":orange[SELECT BED TYPE]",('Real Bed', 'Futon', 'Pull-out Sofa', 'Airbed', 'Couch'),index=0)
    df=hii[hii['bed_type']==option1]
    b=df.groupby('country').size().reset_index(name='Count')
    st.markdown(":blue[COUNTS OF BED TYPE DISTRIBUTED BY COUNTRY WISE]")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(b['country'], b['Count'],color=custom_colors)
    ax.set_xlabel('Country')
    ax.set_ylabel('Bed tpye Count')
    st.pyplot(fig)  

    bed_type_df = hii.groupby(by=["bed_type"], as_index=False)["price"].sum()

with co1: 
    with st.expander("bed_type wise price"):
        st.write(bed_type_df.style.background_gradient(cmap="Blues"))
        csv = bed_type_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="bed_type.csv", mime="text/csv",
                                help='Click here to download the data as a CSV file') 

    st.markdown(':blue[COUNTS OF CANCELLATION POLICY]')
    policy_type_counts = a['cancellation_policy'].value_counts()
    # Create a new DataFrame with 'bed_type' and 'count' columns
    policy_type_df = policy_type_counts.reset_index()
    policy_type_df.columns = ['cancellation_policy', 'count']
    # Print the new DataFrame
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(policy_type_df['cancellation_policy'], policy_type_df['count'],color=custom_colors)
    ax.set_xlabel('cancellation_policy')
    ax.set_ylabel('Count')
    st.pyplot(fig)
    
    st.markdown(':blue[Selected country of Price vs Bedrooms by Bed Type]')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="bedrooms", y="price", hue="bed_type", data=a)
    plt.title("Price vs Bedrooms by Bed Type")
    st.pyplot(plt)

    with st.expander("Detailed Room Availability and Price View Data"):
        df=hii[['host_name','host_id','host_loc','country','market','amenities','property_type','price']].iloc[:500]
        st.write(df.style.background_gradient(cmap="Oranges"))
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Detailed Room Availability.csv", mime="text/csv",
                                help='Click here to download the data as a CSV file')


with co2: 

    st.markdown(':blue[COUNTS OF BEDROOMS TYPE]')
    bed_type_counts = a['bedrooms'].value_counts()
    # Create a new DataFrame with 'bed_type' and 'count' columns
    bed_type_df = bed_type_counts.reset_index()
    bed_type_df.columns = ['bedrooms', 'count']
    # Print the new DataFrame
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(bed_type_df['bedrooms'], bed_type_df['count'],color=custom_colors)
    ax.set_xlabel('bedrooms')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    st.markdown(':blue[NUMBER OF BEDS]')
    beds_type_counts = a['beds'].value_counts()
    # Create a new DataFrame with 'bed_type' and 'count' columns
    beds_type_df = beds_type_counts.reset_index()
    beds_type_df.columns = ['beds', 'count']
    # Print the new DataFrame
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(beds_type_df['beds'], beds_type_df['count'],color=custom_colors)
    ax.set_xlabel('Number of beds')
    ax.set_ylabel('Count')
    st.pyplot(fig)  

    option2=st.selectbox(":orange[SELECT ROOM TYPE]",('Private room', 'Entire home/apt', 'Shared room'),index=0)
    df=hii[hii['room_type']==option2]
    b=df.groupby('country').size().reset_index(name='Count')
    st.markdown(":blue[COUNTS OF ROOM TYPE DISTRIBUTED BY COUNTRY WISE]")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(b['country'], b['Count'],color=custom_colors)
    ax.set_xlabel('Country')
    ax.set_ylabel('Room type Count')
    st.pyplot(fig)

    room_type_df = hii.groupby(by=["room_type"], as_index=False)["price"].sum()

with co2: 
    with st.expander("room_type wise price"):
        st.write(room_type_df.style.background_gradient(cmap="Blues"))
        csv = room_type_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="room_type.csv", mime="text/csv",
                                help='Click here to download the data as a CSV file')

    st.markdown(':blue[NUMBER OF AMENITIES]')
    am_type_counts = a['amenities_count'].value_counts()
    # Create a new DataFrame with 'bed_type' and 'count' columns
    am_type_df = am_type_counts.reset_index()
    am_type_df.columns = ['amenities_count', 'count']
    # Print the new DataFrame
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(am_type_df['amenities_count'], am_type_df['count'],color=custom_colors)
    ax.set_xlabel('Number of amenities')
    ax.set_ylabel('Count')
    st.pyplot(fig) 

    st.markdown(':blue[Overall Price vs Bedrooms by Bed Type]')
    plt.figure(figsize=(10,6)) 
    sns.lineplot(x="bedrooms", y="price",hue="bed_type",data=hii)
    plt.title("Price vs Bedrooms by Bed Type")
    st.pyplot(plt)

    st.markdown(':blue[Overall Price vs Bedrooms by country]')
    plt.figure(figsize=(10,6)) 
    sns.lineplot(x="bedrooms", y="price",hue="country",data=hii)
    plt.title("Price vs Bedrooms by country wise")
    st.pyplot(plt)  

data1 = px.scatter(hii, x="country", y="property_type", color="room_type")
data1['layout'].update(title="Room_type in the country and property_type wise data using Scatter Plot.",
                    titlefont=dict(size=20), xaxis=dict(title=" COUNTRY", titlefont=dict(size=20)),
                    yaxis=dict(title="PROPERTY_TYPE", titlefont=dict(size=20)))
st.plotly_chart(data1, use_container_width=True)
