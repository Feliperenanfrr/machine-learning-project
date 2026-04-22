"""Funcoes compartilhadas do projeto."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"

RAW_DATA_PATH = DATA_DIR / "Final_Augmented_dataset_Diseases_and_Symptoms.csv"
CLEAN_DATA_PATH = DATA_DIR / "dataset_tratado.csv"
FILTERED_DATA_PATH = DATA_DIR / "dataset_3_doencas.csv"
TARGET_COLUMN = "diseases"
RANDOM_STATE = 42

CLASSES_ALVO: tuple[str, ...] = ("pneumonia", "gout", "anxiety")


def _read_csv(path: Path | str) -> pd.DataFrame:
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {csv_path}")
    return pd.read_csv(csv_path)


def load_data(path: Path | str = RAW_DATA_PATH) -> pd.DataFrame:
    """Carrega o dataset bruto do projeto."""
    return _read_csv(path)


def load_clean_data(path: Path | str = CLEAN_DATA_PATH) -> pd.DataFrame:
    """Carrega o dataset tratado."""
    return _read_csv(path)


def resolve_target_classes(classes: Iterable[str] | None = None) -> tuple[str, ...]:
    """Retorna as 3 classes alvo configuradas para o projeto."""
    selected = tuple(dict.fromkeys(classes or CLASSES_ALVO))
    if len(selected) != 3:
        raise ValueError(
            "Defina exatamente 3 classes alvo em CLASSES_ALVO ou passe a lista no parametro classes."
        )
    return selected


def filter_diseases(
    df: pd.DataFrame,
    classes: Iterable[str],
    target_column: str = TARGET_COLUMN,
    drop_zero_only: bool = True,
) -> pd.DataFrame:
    """Filtra o dataset para as doencas alvo e remove colunas zeradas, se desejado."""
    selected = resolve_target_classes(classes)

    if target_column not in df.columns:
        raise KeyError(f"Coluna alvo ausente: {target_column}")

    filtered = df[df[target_column].isin(selected)].copy()
    if filtered.empty:
        raise ValueError("O filtro resultou em um DataFrame vazio.")

    if drop_zero_only:
        feature_columns = [column for column in filtered.columns if column != target_column]
        usable_columns = [
            column
            for column in feature_columns
            if pd.to_numeric(filtered[column], errors="coerce").fillna(0).sum() > 0
        ]
        filtered = filtered[[target_column, *usable_columns]]

    return filtered.reset_index(drop=True)


def save_dataset(df: pd.DataFrame, path: Path | str = FILTERED_DATA_PATH) -> Path:
    """Salva um DataFrame como CSV no caminho informado."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return output_path


def split_data(
    df: pd.DataFrame,
    target_column: str = TARGET_COLUMN,
    test_size: float = 0.2,
    val_size: float = 0.1,
    random_state: int = RANDOM_STATE,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    """Executa split estratificado em treino, validacao e teste."""
    if target_column not in df.columns:
        raise KeyError(f"Coluna alvo ausente: {target_column}")

    if not 0 < test_size < 1:
        raise ValueError("test_size deve estar entre 0 e 1.")
    if not 0 < val_size < 1:
        raise ValueError("val_size deve estar entre 0 e 1.")
    if test_size + val_size >= 1:
        raise ValueError("A soma de test_size e val_size deve ser menor que 1.")

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state,
    )

    adjusted_val_size = val_size / (1 - test_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val,
        y_train_val,
        test_size=adjusted_val_size,
        stratify=y_train_val,
        random_state=random_state,
    )

    return X_train, X_val, X_test, y_train, y_val, y_test


def evaluate_model(
    y_true: Iterable[str],
    y_pred: Iterable[str],
    labels: Iterable[str] | None = None,
) -> dict[str, object]:
    """Calcula metricas e retorna matriz de confusao e classification report."""
    y_true_series = pd.Series(list(y_true))
    y_pred_series = pd.Series(list(y_pred))

    if labels is None:
        label_list = sorted(pd.concat([y_true_series, y_pred_series]).dropna().unique().tolist())
    else:
        label_list = list(labels)

    matrix = confusion_matrix(y_true_series, y_pred_series, labels=label_list)
    report = classification_report(
        y_true_series,
        y_pred_series,
        labels=label_list,
        output_dict=True,
        zero_division=0,
    )

    return {
        "accuracy": float(accuracy_score(y_true_series, y_pred_series)),
        "precision_macro": float(
            precision_score(y_true_series, y_pred_series, labels=label_list, average="macro", zero_division=0)
        ),
        "recall_macro": float(
            recall_score(y_true_series, y_pred_series, labels=label_list, average="macro", zero_division=0)
        ),
        "f1_macro": float(
            f1_score(y_true_series, y_pred_series, labels=label_list, average="macro", zero_division=0)
        ),
        "confusion_matrix": pd.DataFrame(
            matrix,
            index=label_list,
            columns=label_list,
        ),
        "classification_report": pd.DataFrame(report).transpose(),
    }


def plot_confusion_matrix(
    y_true: Iterable[str],
    y_pred: Iterable[str],
    labels: Iterable[str],
    normalize: str | None = None,
    ax: plt.Axes | None = None,
    cmap: str = "Blues",
) -> plt.Axes:
    """Plota a matriz de confusao com rotulos legiveis."""
    label_list = list(labels)
    matrix = confusion_matrix(y_true, y_pred, labels=label_list, normalize=normalize)

    if ax is None:
        _, ax = plt.subplots(figsize=(8, 6))

    fmt = ".2f" if normalize else "d"
    sns.heatmap(
        matrix,
        annot=True,
        fmt=fmt,
        cmap=cmap,
        xticklabels=label_list,
        yticklabels=label_list,
        ax=ax,
    )
    ax.set_xlabel("Predito")
    ax.set_ylabel("Real")
    ax.set_title("Matriz de confusao")
    return ax


__all__ = [
    "CLASSES_ALVO",
    "CLEAN_DATA_PATH",
    "DATA_DIR",
    "FILTERED_DATA_PATH",
    "MODELS_DIR",
    "PROJECT_ROOT",
    "RAW_DATA_PATH",
    "RANDOM_STATE",
    "TARGET_COLUMN",
    "evaluate_model",
    "filter_diseases",
    "load_clean_data",
    "load_data",
    "plot_confusion_matrix",
    "resolve_target_classes",
    "save_dataset",
    "split_data",
]
