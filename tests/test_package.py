import os
import builtins
import cv2
import pytest
from rendertex import LatexString


def test_latex_to_image(latex_string):
    image_path = latex_string._LatexString__image
    assert os.path.exists(image_path)


def test_repr(latex_string):
    expected_repr = "<LatexString formula=\"\\frac{1}{2} \\cdot \\left(\\sqrt{9}\\right)^3\">"
    assert repr(latex_string) == expected_repr


def test_str(latex_string):
    expected_str = "$\\frac{1}{2} \\cdot \\left(\\sqrt{9}\\right)^3$"
    assert str(latex_string) == expected_str


def test_display(monkeypatch, latex_string):
    # Mocking cv2.imshow and cv2.waitKey functions
    def mock_imshow(window_name, image):
        assert window_name == "LaTeX Formula"
        assert isinstance(image, type(cv2.imread("temp.png", cv2.IMREAD_UNCHANGED)))

    def mock_waitKey(delay):
        assert delay == 0
        return ord('q')  # Simulating key press 'q' to close the window

    monkeypatch.setattr(cv2, 'imshow', mock_imshow)
    monkeypatch.setattr(cv2, 'waitKey', mock_waitKey)

    # Calling the display function
    latex_string.display()


def test_display_missing_image(capsys, monkeypatch, latex_string):
    # Mocking the print function to capture the output
    def mock_print(*args, **kwargs):
        print(*args, **kwargs)

    monkeypatch.setattr(LatexString, 'display', lambda x: None)  # Mocking the display function
    monkeypatch.setattr(LatexString, '__image', "non_existent_image.png")  # Setting a non-existent image path
    monkeypatch.setattr(builtins, 'print', mock_print)

    latex_string.display()
    captured_output = capsys.readouterr()
    assert f'No image found: {latex_string._LatexString__image}' in captured_output.out
