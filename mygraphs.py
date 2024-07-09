import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings


def create_boxplots(df, num_columns):
    warnings.filterwarnings('ignore', module='matplotlib.*')
    graph_df = df.select_dtypes(exclude=['object']).copy()
    num_plots = len(graph_df.columns)
    num_rows = int(np.ceil(num_plots / num_columns))

    fig, axs = plt.subplots(num_rows, num_columns, figsize=(15, num_rows*5))

    # Reshape axs to 2D if num_rows or num_columns is 1
    if num_rows == 1 or num_columns == 1:
        axs = np.reshape(axs, (num_rows, num_columns))

    for i, column in enumerate(graph_df.columns):
        if graph_df[column].dtype != 'object':
            row = i // num_columns
            col = i % num_columns
            axs[row, col].boxplot(graph_df[column])
            axs[row, col].set_title(f'Boxplot of {column}')

    plt.tight_layout()
    plt.show()


def create_histograms(df, num_columns):
    warnings.filterwarnings('ignore', module='matplotlib.*')
    graph_df = df.select_dtypes(exclude=['object']).copy()
    num_plots = len(graph_df.columns)
    num_rows = int(np.ceil(num_plots / num_columns))

    fig, axs = plt.subplots(num_rows, num_columns, figsize=(15, num_rows*5))

    # Reshape axs to 2D if num_rows or num_columns is 1
    if num_rows == 1 or num_columns == 1:
        axs = np.reshape(axs, (num_rows, num_columns))

    for i, column in enumerate(graph_df.columns):
        if True: #graph_df[column].dtype != 'object':
            row = i // num_columns
            col = i % num_columns
            axs[row, col].hist(graph_df[column], bins=30, color='skyblue', edgecolor='black')
            axs[row, col].set_title(f'Histogram of {column}')

    plt.tight_layout()
    plt.show()


def create_graphs(df, num_columns):
    warnings.filterwarnings('ignore', module='matplotlib.*')
    graph_df = df.copy()
    num_plots = len(graph_df.columns)
    num_rows = int(np.ceil(num_plots / num_columns))

    fig, axs = plt.subplots(num_rows, num_columns, figsize=(15, num_rows*5))

    # Reshape axs to 2D if num_rows or num_columns is 1
    if num_rows == 1 or num_columns == 1:
        axs = np.reshape(axs, (num_rows, num_columns))

    for i, column in enumerate(graph_df.columns):
        row = i // num_columns
        col = i % num_columns
        if np.issubdtype(graph_df[column].dtype, np.number):
            # If the column is numeric, create a histogram
            axs[row, col].hist(graph_df[column], bins=30, color='skyblue', edgecolor='black')
            axs[row, col].set_title(f'Histogram of {column}')
        else:
            # If the column is not numeric (i.e., it's an object), create a bar graph
            graph_df[column].value_counts().plot(kind='bar', ax=axs[row, col])
            axs[row, col].set_title(f'Bar Graph of {column}')

    plt.tight_layout()
    plt.show()

def create_boxplots2(df, num_columns):
    warnings.filterwarnings('ignore', module='matplotlib.*')
    numeric_df = df.select_dtypes(include=[np.number])
    object_df = df.select_dtypes(include=['object'])
    
    num_plots = len(numeric_df.columns) * len(object_df.columns)
    num_rows = int(np.ceil(num_plots / num_columns))

    fig, axs = plt.subplots(num_rows, num_columns, figsize=(15, num_rows*5))

    # Reshape axs to 2D if num_rows or num_columns is 1
    if num_rows == 1 or num_columns == 1:
        axs = np.reshape(axs, (num_rows, num_columns))

    plot_index = 0
    for num_column in numeric_df.columns:
        for obj_column in object_df.columns:
            row = plot_index // num_columns
            col = plot_index % num_columns
            sns.boxplot(x=obj_column, y=num_column, data=df, ax=axs[row, col])
            axs[row, col].set_title(f'Boxplot of {num_column} by {obj_column}')
            plot_index += 1

    plt.tight_layout()
    plt.show()