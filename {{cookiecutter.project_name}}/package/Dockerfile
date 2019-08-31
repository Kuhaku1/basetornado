FROM python:{{cookiecutter.version_python}}
COPY requirements.txt /app/requirements.txt
ADD main.py /app/
ADD pip.conf /root/.pip/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY {{cookiecutter.package_name}}.tar.gz /app/
RUN pip install /app/{{cookiecutter.package_name}}.tar.gz
# CMD ["gunicorn", "-w", "2", "-b","0.0.0.0:8000","--access-logfile","-","--error-logfile","-","--log-file","-","{{cookiecutter.package_name}}:app"]
CMD ["python","main.py"]
