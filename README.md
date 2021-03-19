![Build](https://github.com/julb/action-post-googlechat-message/workflows/Build/badge.svg)

# GitHub Action to Post a message on Google Chat

The GitHub Action for posting a message in a Google Chat channel.

The pre-requisite is to create a Webhook on your GChat channel.
Once it is done, you need to retrieve the URL and register it as secret in Github :

- `GCHAT_WEBHOOK_URL` : the Google Chat Webhook URL.

## Usage

### Example Workflow file

- Post a message on Google Chat:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Post Google Chat message
        uses: julb/action-post-googlechat-message@v1
        with:
          message: "Hello from Github Action!"
          gchat_webhook_url: ${{ secrets.GCHAT_WEBHOOK_URL }}
```

### Inputs

| Name                | Type   | Default   | Description                                 |
| ------------------- | ------ | --------- | ------------------------------------------- |
| `message`           | string | `Not set` | Text message to post to Gchat. **Required** |
| `gchat_webhook_url` | string | `Not Set` | The Google Chat Webhook URL. **Required**   |

**Important note**: Webhook URL contains sensitive values and should be provided using Github Action Secrets.
Don't paste your Webhook URL in clear in your Github action.

### Outputs

| Name | Type   | Description                  |
| ---- | ------ | ---------------------------- |

## Contributing

This project is totally open source and contributors are welcome.

When you submit a PR, please ensure that the python code is well formatted and linted.

```
$ make install.dependencies
$ make format
$ make lint
```
