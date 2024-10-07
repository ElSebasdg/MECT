FROM grafana/grafana-enterprise:latest

ARG INFLUX_TOKEN
ENV INFLUX_TOKEN=$INFLUX_TOKEN

ADD ./provisioning /etc/grafana/provisioning
ADD ./dashboards /var/lib/grafana/dashboards