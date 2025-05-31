FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r app/requirements.txt
RUN python model/model.py
EXPOSE 5000
CMD ["python", "app/app.py"]