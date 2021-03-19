#!/usr/bin/python3
import json
import os
import requests


def main():
    """ The main method executed. """

    # Input variables
    input_message = os.environ.get('INPUT_MESSAGE')
    input_gchat_webhook_url = os.environ.get('INPUT_GCHAT_WEBHOOK_URL')

    # Post message to GoogleChat
    post_request_data = {'text': input_message}
    post_request_details = requests.post(
        input_gchat_webhook_url,
        json=post_request_data)

    if post_request_details.ok:
        print('::debug::Message posted successfully.')
    else:
        try:
            json_response = post_request_details.json()
            error_message = json_response['error']['message'] if 'error' in json_response and 'message' in json_response['error'] else ''
        except json.decoder.JSONDecodeError:
            error_message = ''

        print('::debug::Fail to post message to GChat.')
        print(f'::debug::Got [{post_request_details.status_code}]: {error_message}')


if __name__ == "__main__":
    main()
