''' Script with visualisation functions for exploratory data analysis
Author : Joshua Yeo
Updated : 29 Mar 2020
'''

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap


def annotate_plot(ax, dec_places=1, annot_size=14):
    '''Function that annotates plots with their value labels.
    Arguments:
        ax : Plot Axis.
        dec_places : int
            Number of decimal places for annotations.
        annot_size : int
            Font size of annotations.
    '''
    for p in ax.patches:
        ax.annotate(
            format(p.get_height(), '.{}f'.format(dec_places)),
            (p.get_x() + p.get_width() / 2., p.get_height(),),
            ha='center', va='center',
            xytext=(0,10), textcoords='offset points', size=annot_size
        )
    
    
def count_pie_plots(df, var, figsize=(8,4), palette='pastel', remove_yticks=True, dec_places=0, annot_size=14, tight_layout=True):
    '''Function that plots both the value counts and percentage distribution of the variable's categories.
    Arguments:
        df : Pandas DataFrame
            Dataframe from which the variable to plot is extracted.
        var : str
            Variable header name in the dataframe.  
        figsize : tuple
            Figure size of the plot.
        palette : str
            Seaborn palette styles.
        remove_yticks : bool
            Option to remove y-tick labels to make the figure cleaner.
        dec_places : int
            Number of decimal places for annotations.
        annot_size : int
            Sets the font size of label value annotations.
        tight_layout = bool
            Ensure subplots fit nicely in the figure.    
    '''

    fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2, figsize=figsize)

    category_distributions = df[var].value_counts().sort_values(ascending=False)
    sorted_order = category_distributions.index.to_list()
    sorted_values = category_distributions.values
    n_categories = category_distributions.size
    
    # Count Plot
    ax1.set_title(f'{var.capitalize()} Categories Count', size=16, pad=20)
    sns.countplot(x=var, data=df, palette=palette, order=sorted_order, ax=ax1)
    ax1.set_ylabel('Frequency', size=14)
    ax1.set_xlabel(f'{var.capitalize()}', size=14)
    if remove_yticks:
        ax1.set_yticklabels([])

    annotate_plot(ax1, dec_places=dec_places, annot_size=annot_size) # Annotating plot with count labels

    # Pie Plot
    pie_cmap = ListedColormap(sns.color_palette(palette, n_categories)).colors

    ax2.set_title(f'{var.capitalize()} Category Distributions', size=16, pad=20)
    ax2 = plt.pie(
        x=sorted_values,
        labels=sorted_order,
        colors=pie_cmap,
        pctdistance=0.5,
        labeldistance=1.15,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize' : annot_size}
    )

    plt.axis('equal')

    if tight_layout:
        fig.tight_layout()

    sns.despine() 
    plt.show();


def barplot_with_hue(df, var, target, y_label='Percentage', figsize=(6,4), palette='pastel', remove_yticks=True, dec_places=1, annot_size=14):
    '''Function to plot the distribution of categorical variables with the target as the hue.
    Arguments:
        df : Pandas DataFrame
            Dataframe from which the variable to plot is extracted.
        var : str
            Variable name.
        target: str
            Target variable name.
        y_label : str
            y-axis label.
        figsize : tuple
            Figure size of the plot.
        palette : str
            Seaborn palette styles.
        remove_yticks : bool
            Option to remove y-tick labels to make the figure cleaner.
        dec_places : int
            Number of decimal places for annotations.
        annot_size : int
            Sets the font size of label value annotations.
        tight_layout = bool
            Ensure subplots fit nicely in the figure.  
    '''
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    
    groupby_df = df.groupby(var)[target].value_counts(normalize=True).rename(y_label).reset_index()
    groupby_df[y_label] = groupby_df[y_label] * 100
    ax = sns.barplot(
        x=var,
        y=y_label,
        hue=target,
        data=groupby_df,
        palette=palette
    )

    ax.set_title(f'{var.capitalize()} Churn Rate Per Category', fontsize=16, pad=20)
    ax.set_ylabel(y_label, fontsize=14)
    ax.set_xlabel(f'{var.capitalize()}', fontsize=14)
    ax.legend(
        loc='center left',
        bbox_to_anchor=(1.02,0.5),
        ncol=1,
        fontsize=14
    )

    annotate_plot(ax, dec_places=dec_places, annot_size=annot_size)

    sns.despine()
    plt.show();