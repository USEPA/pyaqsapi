 Dockerfile

FROM mambaorg/micromamba:latest

COPY environment.yaml .

RUN micromamba create -n myenv --file environment.yaml && \
    micromamba clean --all --yes

ENV ENV_NAME=pyaqsapi