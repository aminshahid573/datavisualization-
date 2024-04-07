import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import time

# Function to plot line plot


def line_plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Line Plot')
    st.pyplot(fig)

# Function to plot bar plot


def bar_plot(x, y):
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Bar Plot')
    st.pyplot(fig)

# Function to plot scatter plot


def scatter_plot(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Scatter Plot')
    st.pyplot(fig)

# Function to plot histogram


def histogram_plot(data):
    fig, ax = plt.subplots()
    ax.hist(data, bins=10)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram')
    st.pyplot(fig)

# Function to plot pie chart


def pie_chart(labels, sizes):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title('Pie Chart')
    st.pyplot(fig)

# Function to plot box plot


def box_plot(data):
    fig, ax = plt.subplots()
    ax.boxplot(data)
    ax.set_xlabel('Data')
    ax.set_ylabel('Values')
    ax.set_title('Box Plot')
    st.pyplot(fig)

# Function to plot violin plot


def violin_plot(data):
    fig, ax = plt.subplots()
    sns.violinplot(data=data, ax=ax)
    ax.set_xlabel('Data')
    ax.set_ylabel('Values')
    ax.set_title('Violin Plot')
    st.pyplot(fig)

# Function to plot heatmap


def heatmap_plot(data):
    fig, ax = plt.subplots()
    sns.heatmap(data, annot=True, cmap="YlGnBu", ax=ax)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Heatmap')
    st.pyplot(fig)

# Function to plot area plot


def area_plot(x, y):
    fig, ax = plt.subplots()
    ax.fill_between(x, y)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Area Plot')
    st.pyplot(fig)

# Function to plot horizontal bar plot


def horizontal_bar_plot(x, y):
    fig, ax = plt.subplots()
    ax.barh(x, y)
    ax.set_xlabel('Y-axis')
    ax.set_ylabel('X-axis')
    ax.set_title('Horizontal Bar Plot')
    st.pyplot(fig)


def main():
    st.title("Data Visualization App")

    # Sidebar
    st.sidebar.header("Input Parameters")
    st.sidebar.info(
        "To visualize data, select a plot type from the dropdown below and click the 'Visualize' button.")
    plot_type = st.sidebar.selectbox("Select Plot Type", ["Line Plot", "Bar Plot", "Scatter Plot", "Histogram", "Pie Chart",
                                     "Box Plot", "Violin Plot", "Heatmap", "Area Plot", "Horizontal Bar Plot"], help="Select the type of visualization.")

    # Main content
    st.write("## Input Data")

    # Option to upload file or enter data manually
    data_source = st.radio("Select data source", ("Upload file", "Enter data manually"),
                           help="Choose whether to upload a file or enter data manually.")

    if data_source == "Upload file":
        uploaded_file = st.file_uploader(
            "Upload file", type=["xlsx", "xls", "csv"], help="Upload a CSV or Excel file.")

        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)

                st.write("### Data Preview:")
                st.write(df.head())

                # Display columns with their respective data types
                columns = df.columns
                st.write("### Data Columns:")
                st.write(df.dtypes)

                x_column = st.selectbox("Select X-axis column", columns)
                y_column = st.selectbox("Select Y-axis column", columns)

                visualize_button = st.sidebar.button(
                    "Visualize", help="Click to generate the selected visualization.")

                if visualize_button:
                    with st.spinner('Visualizing...'):
                        time.sleep(2)
                        x_data = df[x_column]
                        y_data = df[y_column]

                        if plot_type == "Line Plot":
                            line_plot(x_data, y_data)
                        elif plot_type == "Bar Plot":
                            bar_plot(x_data, y_data)
                        elif plot_type == "Scatter Plot":
                            scatter_plot(x_data, y_data)
                        elif plot_type == "Histogram":
                            histogram_plot(y_data)
                        elif plot_type == "Pie Chart":
                            pie_chart(x_data, y_data)
                        elif plot_type == "Box Plot":
                            box_plot(y_data)
                        elif plot_type == "Violin Plot":
                            violin_plot(y_data)
                        elif plot_type == "Heatmap":
                            heatmap_plot(
                                df.pivot(x_column, y_column, y_column))
                        elif plot_type == "Area Plot":
                            area_plot(x_data, y_data)
                        elif plot_type == "Horizontal Bar Plot":
                            horizontal_bar_plot(x_data, y_data)
            except Exception as e:
                st.error(f"An error occurred: {e}")

    elif data_source == "Enter data manually":
        st.write("### Enter data manually:")
        num_rows = st.number_input("Number of rows", min_value=1,
                                   step=1, help="Specify the number of rows in your dataset.")
        num_cols = st.number_input("Number of columns", min_value=1,
                                   step=1, help="Specify the number of columns in your dataset.")
        data = []

        for i in range(num_cols):
            col_data = []
            col_name = st.text_input(
                f"Column {i+1} name", key=f"col_{i}", help=f"Enter a name for column {i+1}.")
            data_type = st.selectbox(f"Data type for column {col_name}", [
                                     "Numeric", "Object"], help=f"Select the data type for column {col_name}.")
            for j in range(num_rows):
                if data_type == "Numeric":
                    value = st.text_input(
                        f"Enter value for {col_name} row {j+1}", key=f"{col_name}_{j}", help=f"Enter a value for row {j+1} in column {col_name}.")
                else:
                    value = st.text_input(
                        f"Enter value for {col_name} row {j+1}", key=f"{col_name}_{j}", help=f"Enter a value for row {j+1} in column {col_name}.")
                col_data.append(value)
            data.append(col_data)

        df = pd.DataFrame(data).transpose()
        df.columns = [st.text_input(
            f"Enter name for Column {i+1}", key=f"col_name_{i}", help=f"Enter a name for column {i+1}.") for i in range(num_cols)]

        st.write("### Data Preview:")
        st.write(df.head())

        visualize_button = st.sidebar.button(
            "Visualize", help="Click to generate the selected visualization.")

        if visualize_button:
            with st.spinner('Visualizing...'):
                time.sleep(2)
                x_column = st.selectbox("Select X-axis column", df.columns)
                y_column = st.selectbox("Select Y-axis column", df.columns)

                x_data = df[x_column]
                y_data = df[y_column]

                if plot_type == "Line Plot":
                    line_plot(x_data, y_data)
                elif plot_type == "Bar Plot":
                    bar_plot(x_data, y_data)
                elif plot_type == "Scatter Plot":
                    scatter_plot(x_data, y_data)
                elif plot_type == "Histogram":
                    histogram_plot(y_data)
                elif plot_type == "Pie Chart":
                    pie_chart(x_data, y_data)
                elif plot_type == "Box Plot":
                    box_plot(y_data)
                elif plot_type == "Violin Plot":
                    violin_plot(y_data)
                elif plot_type == "Heatmap":
                    heatmap_plot(df.pivot(x_column, y_column, y_column))
                elif plot_type == "Area Plot":
                    area_plot(x_data, y_data)
                elif plot_type == "Horizontal Bar Plot":
                    horizontal_bar_plot(x_data, y_data)

    st.markdown("---")
    st.write("Powered by")
    st.markdown("[Pseudowebs](https://pseudowebs.netlify.com/)",
                unsafe_allow_html=True)
    st.write("Designed and developed by Team Pseudowebs")
    st.markdown("---")


if __name__ == "__main__":
    main()
