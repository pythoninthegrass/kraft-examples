# GitHub Webhook receiver

This example shows how to build a simple GitHub Webhook receiver using Node.js with [Express](https://expressjs.com/) and run it on Unikraft Cloud.
A webhook, also called a reverse API, is a way for a server to send real-time data to other applications when a specific event occurs.
In this case, the webhook receiver listens for GitHub events, such as push events or pull request events, and logs them to the console.
To run this it, follow these steps:

1. Install the [`kraft` CLI tool](https://unikraft.org/docs/cli/install) and a container runtime engine, for example [Docker](https://docs.docker.com/engine/install/).

1. Clone the [`examples` repository](https://github.com/unikraft-cloud/examples) and `cd` into the `examples/webhook-github-node/` directory:

```bash
git clone https://github.com/unikraft-cloud/examples
cd examples/webhook-github-node/
```

Make sure to log into Unikraft Cloud by setting your token and a [metro](https://unikraft.com/docs/platform/metros) close to you.
This guide uses `fra` (Frankfurt, 🇩🇪):

```bash
export UKC_TOKEN=token
# Set metro to Frankfurt, DE
export UKC_METRO=fra
```

When done, invoke the following command to deploy this app on Unikraft Cloud:

```bash
kraft cloud deploy -p 443:3000 -M 1Gi -e GITHUB_WEBHOOK_SECRET=your_secret_here .
```

`GITHUB_WEBHOOK_SECRET` is the secret used to validate incoming webhook requests from GitHub. Set it to a string with high entropy.
The output shows the instance address and other details:

```ansi
[●] Deployed successfully!
 │
 ├─────── name: webhook-github-node-bzq7u                                                                         
 ├─────── uuid: 8a8634f1-fc78-4cc0-aa36-8f082d8a59f5                                                              
 ├────── metro: https://api.fra.unikraft.cloud/v1                                                                 
 ├────── state: starting                                                                                 
 ├───── domain: https://dry-cloud-uuw0qlb6.fra.unikraft.app                                                       
 ├────── image: acioc/webhook-github-node@sha256:10974aac67ce6355148e21d91f918960bf0af29ad840fffeeb2fd01f8c905f66 
 ├───── memory: 1024 MiB                                                                                          
 ├──── service: dry-cloud-uuw0qlb6                                                                                
 ├─ private ip: 10.0.1.205                                                                                        
 └─────── args: node /app/server.js
```

In this case, the instance name is `webhook-github-node-bzq7u` and the address is `https://dry-cloud-uuw0qlb6.fra.unikraft.app`.
They're different for each run.

Use `curl` to query the Unikraft Cloud instance of the Node.js webhook server's health endpoint:

```bash
curl https://dry-cloud-uuw0qlb6.fra.unikraft.app/health
```
```text
{"status":"healthy","timestamp":"2025-12-17T14:55:20.953Z","uptime":0.063799807}
```

The `uptime` field is so small because the instance is scaled to zero when no connections are active.
When a request comes in, Unikraft Cloud automatically starts the instance.

To see the incoming webhook events (you set up the [webhook in GitHub](#test-github-webhooks)), you can retrieve the logs of the instance by running:

```bash
kraft cloud instance logs webhook-github-node-bzq7u --follow
```
```console
[2025-12-17T15:20:54.524Z] Webhook received: ping
{
  "timestamp": "2025-12-17T15:20:54.524Z",
  "event": "ping",
  "data": {
    "zen": "Accessible for all.",
    ...
  },
  "receivedAt": 1765984854525
}
...
```

The `ping` event is sent by GitHub when you set up the webhook.
You can list information about the instance by running:

```bash
kraft cloud instance list
```
```ansi
NAME                       FQDN                                 STATE    STATUS   IMAGE                                               MEMORY   VCPUS  ARGS                 BOOT TIME
webhook-github-node-bzq7u  dry-cloud-uuw0qlb6.fra.unikraft.app  standby  standby  webhook-github-node@sha256:10974aac67ce6355148e...  1.0 GiB  1      node /app/server.js  197.47 ms
```

When done, you can remove the instance:

```bash
kraft cloud instance remove webhook-github-node-bzq7u
```

## Test GitHub webhooks

To test the GitHub webhook receiver, you must set up a [webhook in a GitHub repository](https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks).
Make sure to set the payload URL to the Unikraft Cloud instance webhook, in this case `https://dry-cloud-uuw0qlb6.fra.unikraft.app/webhook/github`.
You should also set the content type to `application/json` and select the events you want to receive.
Lastly, you should set the secret to validate that the requests come from GitHub and were not tampered with.
Now, once you make changes in the repository (that you are listening to), you should see the webhook events logged in the instance logs:

```bash
kraft cloud instance logs webhook-github-node-bzq7u --follow
```
```console
[2025-12-17T17:28:51.136Z] Webhook received: push
{
  "timestamp": "2025-12-17T17:28:51.136Z",
  "event": "push",
  "data": {
    "ref": "refs/heads/main",
    "before": "3312f99896b85e896f730d246180979553748f9d",
    "after": "12b2962bbc70f92fa33e4b30c0e1a3ed5f35f9d4",
    "repository": {
      "id": 123456789,
      "name": "your-repo",
      ...
    },
    ...
  },
  "receivedAt": 1765992531136
}
```

## Customize your app

To customize the app, update the files in the repository, listed below:

* `server.js`: The Node.js Express web server that handles GitHub webhook events
* `Kraftfile`: the Unikraft Cloud specification
* `Dockerfile`: the Docker-specified app filesystem

## Learn more

Use the `--help` option for detailed information on using Unikraft Cloud:

```bash
kraft cloud --help
```

Or visit the [CLI Reference](https://unikraft.com/docs/cli/overview).
