import os
from slackclient import SlackClient

#Enter Display Name AND tOKEN 
DISPLAY_NAME = ''
SLACK_TOKEN = ''

slack_client = SlackClient(SLACK_TOKEN)

if __name__ == "__main__":
   api_call = slack_client.api_call("users.list")
   if api_call.get('ok'):
      users = api_call.get('members')
      for user in users:
         if 'name' in user and user.get('name') == DISPLAY_NAME:
            print("Bot ID for'" + user['name'] + "' is " + user.get('id'))
         else:
            print("Could not find bot user with name " + DISPLAY_NAME)
   else:
      print("Bad return from Slack. Check Token and try again.")         