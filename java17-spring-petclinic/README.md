# Spring PetClinic

[Spring PetClinic](https://github.com/spring-projects/spring-petclinic) is an example project that uses Spring boot to model a simple pet clinic.

To run PetClinic on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli).
Then clone this examples repository and `cd` into this directory, and invoke:

```console
kraft cloud deploy --metro fra -M 1024 -p 443:8080 .
```

After deploying, point your browser to the provided URL.

## Learn more

- [Spring Boot Reference](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
