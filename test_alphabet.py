import pytest

from main import validate_alphabet, clean_string

# Tests that the function returns True for a lowercase string with all characters in the alphabet. 
def test_path_lowercase():
    # Arrange
    string = "the quick brown fox jumps over the lazy dog"
    # Act
    result = validate_alphabet(string)
    # Assert
    assert result == False

def test_all_alphabet():
    # Arrange
    string = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja."
    #Act
    result = validate_alphabet(string)
    # Assert
    assert result == True


# Tests that the function returns True for a string with all characters in the alphabet but with special characters. 
def test_case_special_characters():
    # Arrange
    string = "qwe!rty@uio#pas$dfgh^jkl&ñzxc*vbnm"
    # Act
    result = validate_alphabet(string)
    # Assert
    assert result == True

# Tests that the function returns False for an empty string. 
def test_case_empty_string():
    # Arrange
    string = ""
    # Act
    result = validate_alphabet(string)
    # Assert
    assert result == False

# Test that the function returns an error for a List
def test_error_type_list():
    # Arrange
    string = ["a", "b", "c"]
    # Act
    with pytest.raises(TypeError) as e:
        validate_alphabet(string)
        # Assert
        assert str(e.value) == "Input must be a string"

# Test that the function returns an error for a List
def test_error_type_set():
    # Arrange
    string = set(["a", "b", "c"])
    # Act
    with pytest.raises(TypeError) as e:
        validate_alphabet(string)
        # Assert
        assert str(e.value) == "Input must be a string"

# Test that the function returns an error for a dict
def test_error_type_dict():
    # Arrange
    string = {"a":13 , "b": 25, "c":21}
    # Act
    with pytest.raises(TypeError) as e:
        validate_alphabet(string)
        # Assert
        assert str(e.value) == "Input must be a string"

# Test that the function returns an error for numbers
def test_error_type_number():
    # Arrange
    string = 232345
    # Act
    with pytest.raises(TypeError) as e:
        validate_alphabet(string)
        # Assert
        assert str(e.value) == "Input must be a string"


# Tests that an input string containing no letters of the alphabet returns an empty set. 
def test_no_alphabet():
    # Arrange
    input_string = "1234567890!@#$%^&*()"
    expected_output = set()

    # Act
    output = clean_string(input_string)

    # Assert
    assert output == expected_output

# Tests that an input string containing no letters of the alphabet returns an empty set. 
def test_no_alphabet_vocals():
    # Arrange
    input_string = "áéíóú"
    expected_output = set()

    # Act
    output = clean_string(input_string)

    # Assert
    assert output == expected_output