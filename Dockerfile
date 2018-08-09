FROM python

WORKDIR /citest

ADD . /citest

CMD python checkworks.py

CMD ["python", "checkworks.py", "parametre1", "parametre2"]
CMD ["python", "pingpage.py"]

