FROM node:14.4.0-alpine3.10

LABEL maintainers="Shreyas Dodamani, Shashank Aital"

USER root

RUN  mkdir /frontend

WORKDIR /frontend

COPY ./ArxivAppFrontendWeb/ .

RUN npm install

RUN npm run build
