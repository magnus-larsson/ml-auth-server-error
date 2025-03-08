
```
git clone ...
cd ...

./gradlew clean && docker compose down

clear; time ./gradlew build && \
docker compose up -d --build && \
./test-em-all.bash && \
openapi-ui-test/runTests.bash
```


```
./gradlew microservices:product-composite-service:build && docker compose build product-composite &&  docker compose up -d
```
