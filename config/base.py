"""
Base configuration types.
"""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Config:
    """
    Base class for immutable configuration objects.
    
    Configuration classes intentionally contain data only.
    They should not implement business logic.
    """
    