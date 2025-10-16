# Spring Boot

[Spring Boot](https://spring.io/projects/spring-boot) is an extension of the Spring plaform for Java that simplifies the creation of Spring applicaitons.

To run SpringBoot on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra -M 1024 -p 443:8080 .
```

The command will build and deploy the `DemoApplication.java` source code file.

After deploying, you can query the service using the provided URL.

## Learn more

- [Spring Boot Reference](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
