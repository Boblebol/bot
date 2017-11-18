import os

import requetes
import time
import requests
from slackclient import SlackClient


# currentiesvalue's ID as an environment variable
BOT_ID = "U7YRU0ADP"

# constants
AT_BOT = "<@" + BOT_ID + ">"
LISTE_COMMAND = "liste"
INFO_COMMAND = "cours5"
RECHERCHE = "recherche"
SPECIFIC_COMMAND = "cours"
MYSTERY = "mystere"

# instantiate Slack & Twilio clients
slack_client = SlackClient("xoxb-270878010465-2VHJPGIPS9cxR17A7pHlIk3a")

"""
def handle_command(command, channel):

    response = "Je ne comprends pas votre demande.\n" \
               "Liste des demandes : \n " \
               "    -" + LISTE_COMMAND +" : liste les différentes cryptomonnaies\n" \
               "    -" + INFO_COMMAND +" : obtient toutes les information ssur les 5 premieres monnaies\n"\
               "    -" + SPECIFIC_COMMAND +" : donne les information de la monnaie desiré (3 lettes obtenues via liste)\n"\
               "    -"+ MYSTERY + " : commande mystere"
    if command.startswith(LISTE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    if command.startswith(LISTECOMMAND):
        response = "Sure...write some more code then I can do that!"
    if command.startswith(INFO_COMMAND):
        response = "Sure...write some more code then I can do that!"
    if command.startswith(SPECIFIC_COMMAND):
        response = "Sure...write some more code then I can do that!"
    if command.startswith(MYSTERY):
        response = "Sure...write some more code then I can do that!"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
"""

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")