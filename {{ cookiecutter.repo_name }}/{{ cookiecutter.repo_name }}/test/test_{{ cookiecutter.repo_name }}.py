{{ cookiecutter.shebang_python }}
{{ cookiecutter.shebang_coding }}

import pytest
from unittest import TestCase


from {{ cookiecutter.repo_name }} import *


class {{ cookiecutter.class_name }}Test(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_{{ cookiecutter.repo_name }}(self):
        self.assertTrue(1)


if __name__ == '__main__':
    pytest.main()
