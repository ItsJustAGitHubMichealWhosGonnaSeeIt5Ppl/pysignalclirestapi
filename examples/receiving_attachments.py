# Example script showing how to receive attachments

from pysignalclirestapi import SignalCliRestApi
import os
import asyncio

SIGNAL_API_URL:str = os.getenv("API_URL", "")
SIGNAL_NUMBER: str = os.getenv("NUMBER", "")

client = SignalCliRestApi(
    base_url=SIGNAL_API_URL,
    number=SIGNAL_NUMBER
)


# This is only async because json-rpc is being used to receive messages in this example. If you are in normal or native mode and using `receive()`, then this doesn't need async
async def receive_attachment():
    """If a message contains an attachment, a filename is returned, rather than the actual attachment
    
    To get the actual attachment, you need to use the `get_attachment()` method
    """
    
    # This example uses the json-rpc `stream_messages()` method, but the core principals apply regardless of what receiving mode you use
    async for received_item in client.stream_messages():
        # For more information on the returned objects, look at 'receive_json_rpc.py' example
        envelope: str = received_item.get("envelope")
        data = envelope.get("dataMessage")
        if data:
            attachments = data.get("attachments", [])
            # Attachments are always returned in a list, even if it's just one
            for attachment in attachments:
                # Attachment types include 'image/png', (idk that's all I tested with sorry)
                attachment_type = attachment.get("contentType")
                
                # The filename can sometimes be None, especially on images
                filename = attachment.get("filename")
                
                # The attachment ID is what's used when we request it from the API. It's basically just <random string>.<filetype>
                attachment_id = attachment.get("id")
                
                # Attachments are returned as bytes
                attachment_bytes:bytes = client.get_attachment(attachment_id=attachment_id)
                
                # we'll try to use the filename, and fallback to the attachment ID if no filename was provided
                saved_filename = filename if filename else attachment_id
                
                # Now that we have our attachment as bytes, we can write it to a file
                with open(saved_filename, "wb") as wb:
                    wb.write(attachment_bytes)
                    print(f"File saved as: {saved_filename}")
                    
                # To avoid filling up the server hosting your API, it's a good idea to delete the attachment once you've received it
                client.delete_attachment(attachment_id=attachment_id)
            
            if len(attachments) == 0:
                print(f"No attachments\n{data}")
                
                
            
        else:
            print(f"No dataMessage\n{envelope}")
        
        pass
        

asyncio.run(receive_attachment())