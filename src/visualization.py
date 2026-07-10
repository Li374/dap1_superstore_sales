import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


DEFAULT_FIGSIZE = (8, 5)
DEFAULT_DPI = 120

PRIMARY_COLOR = "#4C72B0"
HIGHLIGHT_COLOR = "#C44E52"
NEGATIVE_COLOR = "#A352DD"


def set_plot_style():
    """
    Apply the default plotting style used throughout the project.
    """

    sns.set_theme(
        style="whitegrid",
        context="notebook",
        palette="Blues"
    )

    plt.rcParams.update({
        "figure.figsize": DEFAULT_FIGSIZE,
        "figure.dpi": DEFAULT_DPI,

        "axes.titlesize": 14,
        "axes.titleweight": "bold",

        "axes.labelsize": 11,

        "xtick.labelsize": 10,
        "ytick.labelsize": 10,

        "legend.fontsize": 10,

        "axes.spines.top": False,
        "axes.spines.right": False
    })


def plot_bar(
        df: pd.DataFrame,
        column: str,
        figsize = DEFAULT_FIGSIZE,
        horizontal = False
) -> pd.DataFrame:
    """
    Plot the frequency distribution of a categorical variable.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    column : str
        Name of the categorical column.

    Returns
    -------
    pandas.DataFrame
        Frequency summary table.
    """

    summary = (
        df[column]
        .value_counts()
        .rename_axis(column)
        .reset_index(name="Count")
    )

    summary["Percentage"] = (
        summary["Count"]
        / summary["Count"].sum()
        * 100
    ).round(2)

    plt.figure(figsize=figsize)

    if horizontal:
        sns.barplot(
            data=summary,
            y=column,
            x="Count",
            color=PRIMARY_COLOR
        )
        plt.ylabel(column)
        plt.xlabel("Number of Orders")
    else:
        sns.barplot(
            data=summary,
            x=column,
            y="Count",
            color=PRIMARY_COLOR
        )
        plt.xlabel(column)
        plt.ylabel("Number of Orders")
    
    plt.title(
        f"Distribution of {column}",
        pad=12
    )
    plt.tight_layout()
    plt.show()

    return summary


def plot_histogram(
    df,
    column,
    bins=30
):

    plt.figure()

    sns.histplot(
        data=df,
        x=column,
        bins=bins,
        kde=True,
        color=PRIMARY_COLOR
    )

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    sns.despine()

    plt.tight_layout()
    plt.show()






