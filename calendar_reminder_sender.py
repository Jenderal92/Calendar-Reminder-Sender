#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
import json
import requests
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow

# Token dan Chat ID Telegram
bot_token = "your_telegram_bot_token"
bot_chatid = "your_telegram_chat_id"

def print_banner():
    banner = """
     ============================================
     |       CALENDAR REMINDER SENDER         |
     |      Stay Organized, Stay Productive      |
     ============================================
    """
    print(banner)

def get_calendar_service():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    CLIENT_SECRET_FILE = 'credentials.json'

    store = Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        creds = run_flow(flow, store)
    return build('calendar', 'v3', http=creds.authorize(httplib2.Http()))

def get_upcoming_events(service, hours=24):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    later = (datetime.datetime.utcnow() + datetime.timedelta(hours=hours)).isoformat() + 'Z'

    events_result = service.events().list(
        calendarId='primary', timeMin=now, timeMax=later,
        singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    return events

def format_date_time(date_string):
    try:
        parsed_date = datetime.datetime.strptime(date_string[:19], "%Y-%m-%dT%H:%M:%S")
        offset = date_string[19:]

        formatted_date = parsed_date.strftime("%d %B %Y, %H:%M")
        return "{} (GMT{})".format(formatted_date, offset)
    except Exception as e:
        return date_string 

def send_telegram_message(chat_id, message):
    api_url = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            print("Message sent to Telegram chat {}".format(chat_id))
        else:
            print("Failed to send message: {}".format(response.text))
    except Exception as e:
        print("Error sending message: {}".format(e))

def main():
    print_banner()
    print("Fetching events from Google Calendar...")

    service = get_calendar_service()
    events = get_upcoming_events(service, hours=24)

    if not events:
        print("No upcoming events found.")
        return

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        summary = event.get('summary', 'No Title')
        readable_date = format_date_time(start)
        details = "📅 Event: {}\n🕒 Date & Time: {}".format(summary, readable_date)

        print(details)
        send_telegram_message(bot_chatid, details)

    print("All reminders sent successfully!")

if __name__ == '__main__':
    main()
