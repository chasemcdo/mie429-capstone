FROM continuumio/miniconda3

RUN apt update
RUN apt install -y git

RUN git clone --branch api https://github.com/chasemcdo/Tip-Adapter.git tip_adapter
RUN pip install -r tip_adapter/requirements.txt
RUN conda install -y pytorch torchvision cudatoolkit -c pytorch -c conda-forge

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app /app

EXPOSE 80

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]

# Run Notes:
# `--shm-size 8G` may be required if you run out of shared memory
# `--gpus all` may be required if you have multiple GPUs
