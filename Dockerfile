FROM openjdk:8u312-jre-slim-buster
COPY wait-for-it.sh wait-for-it.sh
COPY ./transaction-microservice/target/transaction-microservice-0.1.0.jar app.jar
ENV APP_PORT 8073
ENTRYPOINT ["java", "-jar", "/app.jar"]