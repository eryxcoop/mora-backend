FROM python:3.7

WORKDIR /mora

COPY requirements requirements

RUN pip install -r requirements/requirements.txt

COPY . /mora

CMD ["python", "app.py"]