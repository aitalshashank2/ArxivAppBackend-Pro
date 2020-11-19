FROM nginx:alpine

LABEL maintainers="Shashank Aital, Shreyas Dodamani"

RUN rm /etc/nginx/conf.d/default.conf

COPY ./configuration/ /etc/nginx/conf.d/
