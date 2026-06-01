import seaborn as sns
from faicons import icon_svg

# Import data from shared.py
from shared import app_dir, df

from shiny import reactive
from shiny.express import input, render, ui

ui.page_opts(title="HealthCare Dashboard", fillable=True)


with ui.sidebar(title="Filter controls"):
    ui.input_slider("age", "age", 10, 100, 100)
    ui.input_checkbox_group(
        "chestpain",
        "chestpain",
        ["asymptomatic", "nonanginal", "nontypical", "typical"],
        selected=["asymptomatic", "nonanginal", "nontypical", "typical"],
    )


with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of people"

        @render.text
        def count():
            return filtered_df().shape[0]

    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "restbp"

        @render.text
        def bill_length():
            return f"{filtered_df()['restbp'].mean():.1f} "

    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "chol"

        @render.text
        def bill_depth():
            return f"{filtered_df()['chol'].mean():.1f} "


with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Overall")

        @render.plot
        def length_depth():
            return sns.scatterplot(
                data=filtered_df(),
                x="maxhr",
                y="restbp",
                hue="sex",
            )

    with ui.card(full_screen=True):
        ui.card_header("Heart Data")

        @render.data_frame
        def summary_statistics():
            cols = [
                "chestpain",
                "restbp",
                "chol",
                "maxhr",
                "ahd",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)


ui.include_css(app_dir / "styles.css")


@reactive.calc
def filtered_df():
    filt_df = df[df["chestpain"].isin(input.chestpain())]
    filt_df = filt_df.loc[filt_df["age"] < input.age()]
    return filt_df
