from scene import get_colors
import pytest

def test_get_colors():
    for val in range(0, 151):
        assert get_colors(val) == {
            "sky": [(241, 150, 56), (1, 4, 41)],
            "sun": ["sienna1", "salmon2"],
            "cloud": "darkgray",
            "ground": [(1, 4, 41), (241, 150, 56)],
            "mount": "gray50"
        }

    for val in range(151, 251):
        assert get_colors(val) == {
            "sky": [(241, 150, 56), (1, 4, 41)],
            "sun": ["yellow1", "yellow2"],
            "cloud": "gray50",
            "ground": [(72, 165, 199), (255, 255, 51)],
            "mount": "gray50",
            "trees": "black"
        }
    
    for val in range(251, 501):
        assert get_colors(val) == {
            "sky": [(72, 165, 199), (129, 214, 245)],
            "sun": ["yellow1", "yellow2"],
            "cloud": "white",
            "ground": [(72, 165, 199), (255, 255, 51)],
            "mount": "gray50",
            "trees": "black"
        }



pytest.main(['-v', '--tb=line', '-rN', __file__])