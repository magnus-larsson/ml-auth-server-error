1. Verify that login works in swagger-ui with `springdoc-openapi` 2.8.3:

    Get the source code:

    ```
    git clone https://github.com/magnus-larsson/ml-auth-server-error.git
    cd ml-auth-server-error
    ```

    Build and start the auth server, the API, and the gateway:

    ```
    ./gradlew build
    docker compose up -d --build
    ```

    Open the Swagger UI and login:

    1. Open in a web browser: <https://localhost:8443/openapi/swagger-ui.html>
    2. Click on the Authorize button
    3. Select all available scopes
    4. Sign in using username `u` and password `p`
    5. Select all scopes and submit consent
    6. Login done

2. Update to `springdoc-openapi` 2.8.5 in `product-composite-service/build.gradle` and repeat the instruction above.

    1. After the sign in, an errorpage with the following text will now be displayed:

        ```
        Whitelabel Error Page

        This application has no explicit mapping for /error, so you are seeing this as a fallback.

        Sat Mar 08 16:01:11 UTC 2025
        There was an unexpected error (type=None, status=999).
        ```
