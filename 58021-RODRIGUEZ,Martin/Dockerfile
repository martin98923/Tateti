FROM python:3
RUN git clone https://github.com/martin98923/Parcial3_2019
WORKDIR /Parcial3_2019
RUN pip freeze > requirements.txt
RUN pip install requests
RUN pip install -r requirements.txt
CMD ["python", "./.py"]