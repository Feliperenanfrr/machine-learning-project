"""Funcoes compartilhadas do projeto."""

from pathlib import Path

import pandas as pd


DATA_PATH = Path("data") / "Final_Augmented_dataset_Diseases_and_Symptoms.csv"


def load_data(path: Path | str = DATA_PATH) -> pd.DataFrame:
    """Carrega o dataset principal do projeto."""
    return pd.read_csv(path)
