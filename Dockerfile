FROM continuumio/anaconda3
COPY . /usr/src/Prefocus

WORKDIR "/usr/src/Prefocus"
RUN conda env create -f /usr/src/Prefocus/env.yml

ENV PATH /opt/conda/envs/prefocus/bin:$PATH
RUN /bin/bash -c "source activate prefocus"

WORKDIR "/usr/src/Prefocus/src/prefocus/backend"

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "1112"]
EXPOSE 5000
