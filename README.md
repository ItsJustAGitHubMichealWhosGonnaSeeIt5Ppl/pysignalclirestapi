# pysignalclirestapi

`pysignalclirestapi` is a small library for the [Signal CLI REST API](https://github.com/bbernhard/signal-cli-rest-api) that allows you to send, receive, and interact with Signal.

API reference: https://bbernhard.github.io/signal-cli-rest-api/#/

## Getting Started

To use this library, you'll need the [Signal CLI REST API](https://github.com/bbernhard/signal-cli-rest-api)

### Installation

```python
pip install pysignalclirestapi
```

### Usage

Set up the client

```python
from pysignalclirestapi import SignalCliRestApi

API_URL = "http://localhost:8080" # Your server address and port
NUMBER ="+123456789" # The phone number you registered with the API

signal = SignalCliRestApi(
    base_url = API_URL,
    number = NUMBER
)
```

Send a message

```python
myMessage = "Hello World" # Your message
myFriendSteve = +987654321 # The number you want to message (must be registered with Signal)

sendMe = signal.send_message(message=myMessage,recipients=myFriendSteve)

```

#### Receiving messages

Receiving messages in 'normal' or 'native' mode
> In 'normal' and 'native' mode, messages remain on the Signal server until `receive()` is called

```python
myMessages = signal.receive()
```

Receiving messages in 'json-rpc' mode
> In 'json-rpc' mode, messages are instantly sent via websocket, regardless of whether anything is connected/listening. That means you can miss messages if your script crashes, or isn't listening at the moment the message is sent! The example below will catch ALL messages sent while the script is running.

```python
async def main():
    while True:
        async for message in signal.stream_messages():
            print(message)

asyncio.run(main())
```

## Authentication

This library provides limited built-in support for authenticated APIs, along with an Abstract Base Class `SignalCliRestApiAuth` which can be used to implement other authentication types. For more details, see [Custom Auth](#custom-auth)

### Basic Auth

Connecting to an API instance behind basic HTTP authentication

```python
from pysignalclirestapi import SignalCliRestApi, SignalCliRestApiHTTPBasicAuth

API_URL = "http://localhost:8080"
NUMBER = "+123456789" 

# Create an authentication object
auth = SignalCliRestApiHTTPBasicAuth(
    basic_auth_user="admin",
    basic_auth_pwd="hunter2"
    )

# Pass the auth object to the client
signal = SignalCliRestApi(
    base_url = API_URL,
    number = NUMBER,
    auth = auth
)
```

### Custom Auth

TBD

## Contributing

Want to contribute? Check the guidelines (which aren't yet added)