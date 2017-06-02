{{ cookiecutter.shebang_python }}
{{ cookiecutter.shebang_coding }}

import pytest
from unittest import TestCase

from {{ cookiecutter.repo_name }} import *
from {{ cookiecutter.repo_name }}.test.test_{{ cookiecutter.repo_name }} import *


class Test{{ cookiecutter.class_name }}(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_{{ cookiecutter.repo_name }}(self):
        assert True


if __name__ == '__main__':
    pytest.main()
