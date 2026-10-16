import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    Notebook for the png2svg Function which will transform a picture in a svg of hexagons
    """)
    return


@app.cell
def _(mo):
    from png2svg import png2svg
    import os
    output_file = "output.svg"
    size=10
    Flattop=mo.ui.switch(value=True,label="Afficher l'image avec des hexagons à haut plat ou pointu")
    Flattop

    return Flattop, output_file, png2svg, size


@app.cell
def _(Flattop, output_file, png2svg, size):
    png2svg("img/screenshot.jpg",output_file,size,Flattop.value)
    return


@app.cell
def _(mo, output_file):
    mo.image(output_file)

    return


if __name__ == "__main__":
    app.run()
