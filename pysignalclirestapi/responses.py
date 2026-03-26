# BUILT-IN
from dataclasses import dataclass, field
from copy import deepcopy

# EXTERNAL

# INTERNAL

# DATACLASSES
# OTHER #
@dataclass
class About:
    versions: list
    build: int
    mode: str #TODO make a Literal for this
    version: float
    capabilities: dict[str:list]
    
    def __post_init__(self):
        if not isinstance(self.version, float):
            self.version = float(self.version)

@dataclass
class Reaction:
    emoji: str
    targetAuthor: str
    targetAuthorNumber: str
    targetAuthorUuid: str
    targetSentTimestamp: int
    isRemove: bool

# MESSAGE TYPES #
@dataclass
class GroupInfo:
    groupId: str
    groupName: str
    revision: int
    type: str # DELIVER
    
@dataclass
class DataMessage:
    timestamp: int
    message: str | None
    expiresInSeconds: int
    isExpirationUpdate: bool
    viewOnce: bool
    groupInfo:  GroupInfo | None = field(default=None)
    reaction: Reaction | None = field(default=None)
    
    #TODO I wonder if I can make a generic post init for this
    def __post_init__(self):
        if isinstance(self.reaction, dict):
            self.reaction = Reaction(**self.reaction)
            
    def __post_init__(self):
        if isinstance(self.groupInfo, dict):
            self.groupInfo = GroupInfo(**self.groupInfo)

@dataclass
class ReceiptMessage:
    when: int #Timestamp
    isDelivery: bool
    isRead: bool
    isViewed: bool
    timestamps: list[int] #IDK why it's in a list
    
## SYNC MESSAGES ##
#TODO bad name?
#TODO IDK why it's sender here but source elsewhere
@dataclass
class SyncMessageRead:
    sender: str
    senderNumber: str
    senderUuid: str
    timestamp:int 


@dataclass 
class SyncMessageSent:
    """Message sent by a Synced/Linked device"""
    destination: str
    destinationNumber: str 
    destinationUuid: str 
    timestamp:int
    message: str | None
    expiresInSeconds: int
    isExpirationUpdate: bool
    viewOnce: bool
    reaction: Reaction | None = field(default=None)
    
    def __post_init__(self):
        if isinstance(self.reaction, dict):
            self.reaction = Reaction(**self.reaction)
        

#TODO maybe this could be elimated and just send readMessages instead?
@dataclass
class SyncMessage:
    type: str | None = field(default=None) # CONTACTS_SYNC, #TODO make string literal. 
    readMessages: list[SyncMessageRead] | None = field(default=None)
    sentMessage: list[SyncMessageSent] | None = field(default=None)

    def __post_init__(self):
        if isinstance(self.sentMessage, list) and len(self.sentMessage) > 0:
            temp = []
            for msg in self.sentMessage:
                temp.append(SyncMessageSent(**msg))
            
            self.sentMessage = deepcopy(temp)
            
        if isinstance(self.readMessages, list) and len(self.readMessages) > 0:
            temp = []
            for msg in self.readMessages:
                temp.append(SyncMessageRead(**msg))
            
            self.readMessages = deepcopy(temp)
            
    

#TODO consider renaming
#TODO an "account" field is sent along with "Envelope". Should that be included somewere?
@dataclass
class Envelope:
    source: str
    sourceNumber: str
    sourceUuid: str #TODO what is this?
    sourceName: str
    sourceDevice: int
    timestamp: int #TODO should this be datetime?
    serverReceivedTimestamp: int
    serverDeliveredTimestamp: int
    
    #TODO usually only one of these is returned
    dataMessage: DataMessage | None = field(default=None)
    receiptMessage: ReceiptMessage | None = field(default=None)
    syncMessage: SyncMessage | None = field(default=None)
    
    def __post_init__(self):
        if isinstance(self.dataMessage, dict):
            self.dataMessage = DataMessage(**self.dataMessage)
            
        if isinstance(self.receiptMessage, dict):
            self.receiptMessage = ReceiptMessage(**self.receiptMessage)
        
        if isinstance(self.syncMessage, dict):
            self.syncMessage = SyncMessage(**self.syncMessage)