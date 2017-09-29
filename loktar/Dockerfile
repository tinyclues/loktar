FROM quay.io/loktar/base:master

COPY src /src

WORKDIR /src

COPY pip.conf /root/.pip/pip.conf

RUN pip install -r requirements.txt -r test_requirements.txt "ipython<6"
