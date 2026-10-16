import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    from collections import Counter

    import marimo as mo
    import matplotlib.pyplot as plt

    from fizzbuzz_kata import fizzbuzz

    return Counter, fizzbuzz, mo, plt
