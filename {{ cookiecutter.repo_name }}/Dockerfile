FROM python:{{ cookiecutter.python_version }}-slim-buster
WORKDIR /var/app
COPY requirements.txt requirements.txt
COPY dist/*.whl /var/app
RUN pip install -r requirements.txt
RUN pip install *.whl
RUN rm requirements.txt *.whl
ENTRYPOINT ["{{ cookiecutter.repo_name }}"]
