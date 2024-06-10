FROM python:3.10
RUN mkdir /app && pip install --upgrade pip
WORKDIR /app
COPY src/* /app/
RUN pip install -r requirements.txt
CMD ["/bin/bash"]