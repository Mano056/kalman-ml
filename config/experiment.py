"""
Experiment configuration.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .base import Config


@dataclass(frozen=True, slots=True)
class ExperimentConfig(Config):
    """
    Defines metadata for a research experiment.
    
    Parameters
    ----------
    name
        Human-readable experiment name.
        
    data_path
        Path to the input market data.
    """

    name: str
    data_path: Path

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Experiment name cannot be empty.")