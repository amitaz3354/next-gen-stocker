
FROM tiangolo/uvicorn-gunicorn:python3.7


WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY . /backend

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]