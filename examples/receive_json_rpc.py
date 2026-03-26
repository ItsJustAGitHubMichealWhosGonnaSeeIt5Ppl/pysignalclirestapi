# Example script showing ways to receive messages when using JSON-RPC.

from pysignalclirestapi import SignalCliRestApi
import os
import asyncio

SIGNAL_API_URL:str = os.getenv("API_URL", "")
SIGNAL_NUMBER: str = os.getenv("NUMBER", "")

client = SignalCliRestApi(
    base_url=SIGNAL_API_URL,
    number=SIGNAL_NUMBER
)

# EXAMPLE 1: Wait for messages to do actions
# 
async def example_1():
    """In this example, the script waits for a message, then performs an action. This could be used for a bot
    
    The action will be converting the original message to uppercase, sending it back to the user, and then reacting to their original message with a thumbs up emoji
    
    """
    # This for loop will wait until something is received. 
    
    async for received_item in client.stream_messages():
        # This is purely for debugging
        print("==== SOMETHING RECEIVED ====")
        
        # Envelopes are Python Dictionary objects. Envelopes usually contain messages, but they can also contain sync confirmations, and things of that nature
        envelope: str = received_item.get("envelope")
        
        # This is the source of the message. When sending a response message, this is what we'll use as the recipient
        source = envelope.get("source")
        
        # Since not every envelope will be a message, we want to check what we've received. This is a very basic way to do that
        data: dict | None = envelope.get("dataMessage")
        
        # This if statement checks that 'data' isn't None
        if data:
            # Timestamps are used like message IDs. It's used for things like quote-replying and reacting
            timestamp = data.get("timestamp")
            
            # Not every data object will have a 'message', so we need to verify that the one we're looking at does. Below are two ways that can be done
            #### GETTING 'message' VALUE ####
            # OPTION 1
            if "message" in data:
                message: str = data["message"]
            else:
                message = None
            
            # OPTION 2
            message: str | None = data.get("message")
            #### GOT 'message' VALUE ####
            # Now that we have set 'message' to either a message string or None, we can perform our 
            if message:
                # This is what we'll respond with
                response_string: str = message.upper()

                # When we send the response, it will return the timestamp for the message.
                response_message = client.send_message(message=response_string, recipients=[source])
                
                # Now we react to the original message with a thumbs up
                client.add_reaction(reaction="👍", recipient=source, timestamp=timestamp)
            
            # If there wasn't a message, then we'll print this
            else:
                print(f"dataMessage object doesn't have a message\n{data}")
        
        # This will print out the received item only if it's NOT a message
        else:
            print(message)
asyncio.run(example_1())