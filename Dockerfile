FROM continuumio/miniconda3:master-alpine

RUN apk add git

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN git clone --branch api https://github.com/chasemcdo/Tip-Adapter.git tip_adapter
RUN conda install -y --freeze-installed pytorch torchvision cudatoolkit -c pytorch -c conda-forge

COPY requirements-dev.txt .
RUN pip uninstall -r requirements-dev.txt  -y
RUN apk del git
RUN conda clean -afy

COPY app /app

EXPOSE 80

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]

# Run Notes:
# `--shm-size 8G` may be required if you run out of shared memory
# `--gpus all` may be required if you have multiple GPUs
