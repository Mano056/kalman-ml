"""
Result container returned by indicators.
"""

from __future__ import annotations

from dataclasses import dataclass

from core import PriceSeries

@dataclass(frozen=True, slots=True)
class IndicatorResult:
    """
    Represents the output of an indicator.
    
    Attributes
    ----------
    name
        Name of the indicator.
    
    outputs
        Mapping of output names to numerical series.
    
    price_series
        Original market data used to compute the indicator.
    """

    name: str
    outputs: dict[str, list[float]]
    price_series: PriceSeries

    def __post_init__(self) -> None:
        """
        Validate that every output series has the same length 
        as the input PriceSeries.
        """
        expected = len(self.price_series)

        if not self.outputs:
            raise ValueError("IndicatorResult must contain at least one output.")
        
        for output_name, values in self.outputs.items():
            if len(values) != expected:
                raise ValueError(
                    f"Output '{output_name}' has length "
                    f"{len(values)} but expected {expected}."
                )
    
    def output(self, name: str) -> list[float]:
        """
        Return a named output series.
        
        Parameters
        ----------
        name
            Output name.
        
        Returns
        -------
        list[float]
            Numerical series.
        
        Raises
        ------
        KeyError
            If the output does not exist.
        """
        return self.outputs[name]
    
    @property
    def output_names(self) -> list[str]:
        """
        Return the available output names.
        """
        return list(self.outputs.keys())