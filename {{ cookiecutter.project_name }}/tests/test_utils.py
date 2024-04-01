from pathlib import Path

import numpy as np
from {{ cookiecutter.project_slug }} import utils

class TestUtils:
    # see https://stackoverflow.com/questions/62044541/change-pytest-working-directory-to-test-case-directory
    test_dir = Path(__file__).parent.absolute()
    test_data = test_dir / "resources"

    def setup_class(cls):
        print("Starting tests...")

    def teardown_class(cls):
        print("Finished tests...")

    def test_so2(self):
        """
        Test the utils.so2() function by checking rotation angles and imaginary unit properties.
        """

        # check some rotation angles are correct to 15 digits
        a = np.sqrt(1/2).round(15)
        b = np.sqrt(3/4).round(15)

        assert (utils.so2(45) == np.array([[a, -a],[a, a]])).all()
        assert (utils.so2(60) == np.array([[1/2, -b],[b, 1/2]])).all()

        # the imaginary unit is equivalent to rotation by 90 degrees
        imag_unit = utils.so2(90)
        assert imag_unit.tolist() == [[0.0, -1.0], [1.0, 0.0]]

        # check i^2 = -1 and i^4 = 1 using the matmul operator "@"
        assert (imag_unit @ imag_unit).tolist() == [[-1.0, 0.0], [0.0, -1.0]]
        assert (imag_unit @ imag_unit @ imag_unit @ imag_unit).tolist() == [[1.0, 0.0], [0.0, 1.0]]


