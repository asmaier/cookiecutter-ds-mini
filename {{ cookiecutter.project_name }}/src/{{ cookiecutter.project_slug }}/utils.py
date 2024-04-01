import numpy as np

def so2(degree):
    """
    Function to get the rotation matrix for a 2D rotation

    Parameters
    ----------
    degree : float
        The angle of rotation in degrees

    Returns
    -------
    numpy.ndarray
        The rotation matrix
    """
    # Convert the degree to radians
    rad = np.radians(degree)

    # Create the rotation matrix
    # The rows and columns represent the x and y axes respectively
    # The elements of the matrix represent the cosine and sine of the angle
    # The matrix is then rounded to 15 decimal places so sin(pi)=0.0
    rot_matrix = np.array([[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]])
    return rot_matrix.round(15)
