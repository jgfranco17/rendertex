import pytest
from rendertex import LatexString


@pytest.fixture
def latex_string():
    return LatexString(r'\frac{1}{2} \cdot \left(\sqrt{9}\right)^3')
