"""Basic project sanity tests."""

def test_project_imports() -> None:
    """Ensure the package structure imports successfully."""

    import core
    import data
    import indicators
    import ml
    import strategies

    assert core is not None
    assert data is not None
    assert indicators is not None
    assert ml is not None
    assert strategies is not None