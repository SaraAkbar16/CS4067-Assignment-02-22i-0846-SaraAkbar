# CS4067-Assignment-02-22i-0846-SaraAkbar
# Tech Stacks
-User Service: FastAPI/PostgreSQL
-Event Service: Springboot/MongoDB
-Booking Service: Flask/PostgreSQL
-Notification Service: Flask/MongoDB
-Frontend: HTML, CSS, JS
-Communications: REST API(Sync), RabbitMQ(Async)

# Setup Guide
-Run any service using uvicorn main:app --reload
-Run run service on a specifoed port uvicorn fourth.main:app --reload --host 127.0.0.1 --port 8004
-Run event service using mvn spring-boot:run
-Start rabbitmq using net start rabbitmq
