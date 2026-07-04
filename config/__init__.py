"""
Configuration objects used throughout the framework.
"""

from .base import Config
from .experiment import ExperimentConfig

__all__ = [
    "config",
    "ExperimentConfig",
]