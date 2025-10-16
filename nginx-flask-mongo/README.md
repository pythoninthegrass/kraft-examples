# Flask with MongoDB

[Flask](https://flask.palletsprojects.com/en/stable/) is a lightweight WSGI web application framework in Python, and [MongoDB](https://www.mongodb.com/) is a NoSQL database that stores data in JSON-like documents.

**Credits**: This example is based on this [Awesome Compose example](https://github.com/docker/awesome-compose/tree/master/nginx-flask-mongo).

## Deployment

This example uses a [`compose.yaml`](compose.yaml) file to define the Nginx, Flask, and MongoDB services.

To run it on Unikraft Cloud, first [install the `kraft` CLI tool](https://unikraft.org/docs/cli). Make sure you have an active account on Unikraft Cloud (UKC) and that you have authenticated your CLI with your UKC account.

```bash
export UKC_TOKEN=<your-unikraft-cloud-access-token>
export UKC_METRO=fra
```

Then `cd` into [this](.) directory, and invoke:

```bash
kraft cloud compose up
```

The Flask server is exposed through Nginx. To get the public URL of the deployed application, run:

```bash
kraft cloud instance get nginx
```

and look for the `fqdn` field in the output.

## Learn more

- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Awesome Compose](https://github.com/docker/awesome-compose)
- [Unikraft Cloud's Documentation](https://unikraft.cloud/docs/)
- [Building `Dockerfile` Images with `Buildkit`](https://unikraft.org/guides/building-dockerfile-images-with-buildkit)
- [Deploying with Compose Files](https://unikraft.cloud/docs/guides/features/compose/)
- [Creating tunnels](https://unikraft.cloud/docs/guides/features/tunnel/)
