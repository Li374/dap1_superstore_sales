import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_frequency_distribution(
        df: pd.DataFrame,
        column: str,
        figsize = (8, 5),
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
            x="Count"
        )
        plt.ylabel(column)
        plt.xlabel("Number of Orders")
    else:
        sns.barplot(
            data=summary,
            x=column,
            y="Count"
        )
        plt.xlabel(column)
        plt.ylabel("Number of Orders")
    
    plt.title(f"{column} Distribution")
    plt.tight_layout()
    plt.show()

    return summary