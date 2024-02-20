"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #   
    filenames = glob.glob(input_directory + "/*.txt")
    dataframes = [
        pd.read_csv(filename, sep = ";" ) for filename in filenames
    ]
    dataframe = pd.concat(dataframes).reset_index(drop=True)
    return dataframe

def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe = dataframe.copy()
    dataframe['word'] = dataframe['word'].str.lower().srt.replace(',','').str.replace('.','')
    return dataframe

def count_words(dataframe):
    """Word count"""
    dataframe = dataframe.copy()
    dataframe['word'] = dataframe['word'].str.split().explode('word').reset_index(drop=True)
    dataframe['count'] = 1
    conteo = dataframe.groupby(['word'],as_index=False).agg({'count':'sum'})
    return conteo
    


def save_output(dataframe, output_filename):
    """Save output to a file."""


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    dataframe = load_input(input_directory)
    return dataframe


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
