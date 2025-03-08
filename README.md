1. Verify the expected behavior with `springdoc-openapi` 2.8.3, by running the commands:

    ```
    git clone https://github.com/magnus-larsson/ml-auth-server-error.git
    cd ml-auth-server-error

    ./gradlew clean && docker compose down

    clear; time ./gradlew build && \
    docker compose up -d --build && \
    ./test-em-all.bash && \
    openapi-ui-test/runTests.bash
    ```

2. Update to `springdoc-openapi` 2.8.4 in `product-composite-service/build.gradle` and repeat the commands above.

   The openapi-ui test will fail with an error message like the following, indicating that the login failed:

    ```
    Traceback (most recent call last):
    File "/Users/magnus/tmp/ml-auth-server-error/openapi-ui-test/test-openapi-ui.py", line 106, in <module>
        loginOAuth(interactive)
                  ^^^^^^^^^^^^^
    File "/Users/magnus/tmp/ml-auth-server-error/openapi-ui-test/test-openapi-ui.py", line 56, in loginOAuth
        driver.find_element(By.ID, "product:write").click();
                           ^^^^^^^^^^^^^^^^^^^^^^^^
    ```

 3. To verify the error manually:
    1. Open Swagger UI in a web browser: <https://localhost:8443/openapi/swagger-ui.html>
    2. Click on the Authorize button
    3. Select all scopes
    4. Login using username `u` and password `p`
    5. An errorpage with the following text will be displayed:

        ```
        Whitelabel Error Page

        This application has no explicit mapping for /error, so you are seeing this as a fallback.

        Sat Mar 08 16:01:11 UTC 2025
        There was an unexpected error (type=None, status=999).
        ```

