# TODOs

## Wanted before merging

- [ ] Test authenticated API
  - [x] Basic Auth
  - [ ] https://github.com/codeshelldev/secured-signal-api
- [ ] Add documentation for using the `SignalCliRestApiAuth` base class
- [ ] Add return types
- [ ] Complete missing docstrings
- [ ] Add missing endpoints
  - [ ] Merge in polls
  - [x] Register account
  - [ ] Sticker Packs
  - [ ] pin-message methods for Groups
- [ ] Fill out the contribution guidelines
- [ ] Reformat the entire README
  - [x] Explain how to use the websocket methods
  - [ ] Explain how to use multiple numbers

## Later down the line

- [ ] Create custom objects for returned items
  - [x] Envelope
- [ ] Better multi-account support?

## ALL ENDPOINTS

### General

- [x] GET: /v1/about - Lists general information about the API
  - [ ] Test
- [x] GET: /v1/health - API Health Check
  - [ ] Test
  - [ ] Docstring
- [ ] GET: /v1/configuration - List the REST API configuration.
- [ ] POST: /v1/configuration - Set the REST API configuration.
- [ ] GET: /v1/configuration/{number}/settings - List account specific settings.
- [ ] POST: /v1/configuration/{number}/settings - Set account specific settings.

### Devices

Register and link Devices.

- [x] GET: /v1/qrcodelink - Link device and generate QR code.
  - [ ] Test
- [x] GET: /v1/qrcodelink/raw - Get raw device link URI
  - [ ] Test
- [x] POST: /v1/register/{number} - Register a phone number.
  - [ ] Test
- [x] POST: /v1/register/{number}/verify/{token} - Verify a registered phone number.
  - [ ] Test
- [ ] GET: /v1/devices/{number} - List linked devices.
- [ ] POST: /v1/devices/{number} - Links another device to this device.
- [ ] DELETE: /v1/devices/{number}/local-data - Delete local account data
- [ ] DELETE: /v1/devices/{number}/{deviceId} - Remove linked device
- [ ] POST:/v1/unregister/{number} - Unregister a phone number.

### Accounts

List registered and linked accounts

- [x] GET: /v1/accounts - List all accounts
  - [ ] Test
- [x] DELETE: /v1/accounts/{number}/pin - Remove Pin
  - [ ] Test
- [x] POST: /v1/accounts/{number}/pin - Set Pin
  - [ ] Test
- [ ] POST: /v1/accounts/{number}/rate-limit-challenge - Lift rate limit restrictions by solving a captcha.
- [ ] PUT: /v1/accounts/{number}/settings - Update the account settings.
- [ ] DELETE: /v1/accounts/{number}/username - Remove a username.
- [ ] POST: /v1/accounts/{number}/username - Set a username.

### Groups

Create, List and Delete Signal Groups.

- [x] GET: /v1/groups/{number} - List all Signal Groups.
  - [ ] Test
- [x] POST: /v1/groups/{number} - Create a new Signal Group.
  - [ ] Test
- [x] DELETE: /v1/groups/{number}/{groupid} - Delete a Signal Group.
  - [ ] Test
- [x] GET: /v1/groups/{number}/{groupid} - List a Signal Group.
  - [ ] Test
- [x] PUT: /v1/groups/{number}/{groupid} - Update the state of a Signal Group.
  - [ ] Test
- [x] DELETE: /v1/groups/{number}/{groupid}/admins - Remove one or more admins from an existing Signal Group.
  - [ ] Test
- [x] POST: /v1/groups/{number}/{groupid}/admins - Add one or more admins to an existing Signal Group.
  - [ ] Test
- [x] POST: /v1/groups/{number}/{groupid}/block - Block a Signal Group.
  - [ ] Test
- [x] POST: /v1/groups/{number}/{groupid}/join - Join a Signal Group.
  - [ ] Test
- [x] DELETE: /v1/groups/{number}/{groupid}/members - Remove one or more members from an existing Signal Group.
  - [ ] Test
- [x] POST: /v1/groups/{number}/{groupid}/members - Add one or more members to an existing Signal Group.
  - [ ] Test
- [x] POST: /v1/groups/{number}/{groupid}/quit - Quit a Signal Group.
  - [ ] Test
- [ ] GET: /v1/groups/{number}/{groupid}/avatar - Returns the avatar of a Signal Group.
- [ ] DELETE: /v1/groups/{number}/{groupid}/pin-message - Unpin a message in a Signal Group.
- [ ] POST: /v1/groups/{number}/{groupid}/pin-message - Pin a message in a Signal Group.

### Messages

Send and Receive Signal Messages.

- [x] GET: /v1/receive/{number} - Receive Signal Messages.
  - [ ] Test
- [x] DELETE: /v1/remote-delete/{number} - Delete a signal message.
  - [ ] Test
- [x] POST: /v2/send - Send a signal message.
  - [ ] Test
- [ ] DELETE: /v1/typing-indicator/{number} - Hide Typing Indicator.
- [ ] PUT: /v1/typing-indicator/{number} - Show Typing Indicator.

### Attachments

List and Delete Attachments.

- [x] GET: /v1/attachments - List all attachments.
  - [ ] Test
- [x] DELETE: /v1/attachments/{attachment} - Remove attachment.
  - [ ] Test
- [x] GET: /v1/attachments/{attachment} - Serve Attachment.
  - [ ] Test

### Profiles

Update Profile.

- [x] PUT: /v1/profiles/{number} - Update Profile.
  - [ ] Test

### Identities

List and Trust Identities.

- [x] GET: /v1/identities/{number} - List Identities
  - [ ] Test
- [x] PUT: /v1/identities/{number}/trust/{numberToTrust} - Trust Identity
  - [ ] Test

### Reactions

React to messages.

- [x] DELETE: /v1/reactions/{number} - Remove a reaction.
  - [ ] Test
- [x] POST: /v1/reactions/{number} - Send a reaction.
  - [ ] Test

### Receipts

Send receipts for messages.

- [x] POST: /v1/receipts/{number} - Send a receipt.
  - [ ] Test

### Search

Search the Signal Service.

- [x] GET: /v1/search/{number} - Check if one or more phone numbers are registered with the Signal Service.
  - [ ] Test

### Sticker Packs

List and Install Sticker Packs

- [ ] GET: /v1/sticker-packs/{number} - List Installed Sticker Packs.
- [ ] POST: /v1/sticker-packs/{number} - Add Sticker Pack.

### Contacts

- [x] GET: /v1/contacts/{number} - List Contacts
  - [ ] Test
- [x] PUT: /v1/contacts/{number} - Updates the info associated to a number on the contact list. If the contact doesn’t exist yet, it will be added.
  - [ ] Test
- [**x**] POST: /v1/contacts/{number}/sync - Send a synchronization message with the local contacts list to all linked devices.
  - [ ] Test
- [ ] GET: /v1/contacts/{number}/{uuid} - List Contact
- [ ] GET: /v1/contacts/{number}/{uuid}/avatar - Returns the avatar of a contact

### Polls

- [ ] DELETE: /v1/polls/{number} - Close a poll.
- [ ] POST: /v1/polls/{number} - Create a new poll.
- [ ] POST: /v1/polls/{number}/vote - Answer a poll.
