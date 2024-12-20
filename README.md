# Calendar Reminder Sender

![calendar-reminder-sender Jenderal92](https://github.com/user-attachments/assets/73481b21-a47d-4892-8c0b-5963e4491edc)


**Calendar Reminder Sender** is a Python-based tool that automatically fetches upcoming events from Google Calendar and sends reminders to users via Telegram. This tool ensures you never miss important meetings, tasks, or personal appointments by automating the reminder process.

## Features

- **Event Retrieval:** Fetches upcoming events from Google Calendar for a specified time range (default: 24 hours).  
- **Date/Time Formatting:** Displays event date and time in an easy-to-read format, including time zone information.  
- **Telegram Notifications:** Automatically sends reminders to a Telegram group or user via a bot.  
- **Customizable Time Range:** Defaults to 24 hours but can be adjusted as per user preference.  

## Requirements

1. **Python 2.7** or higher.  
2. **Google Calendar API** enabled and configured in the Google Cloud Console.  
3. A valid Telegram bot token and chat ID for sending notifications.  
4. Required Python libraries:
   - `requests`
   - `httplib2`
   - `apiclient`
   - `oauth2client`

## Installation

1. **Install Dependencies**  
   Run the following command to install the required Python libraries:  
   ```bash
   pip install requests httplib2 apiclient oauth2client
   ```

2. **Set Up Google Calendar API**  
   - Visit [Google Cloud Console](https://console.cloud.google.com/).  
   - Create a new project and enable **Google Calendar API**.  
   - Download the `credentials.json` file and place it in the same directory as the script.

3. **Configure Telegram Bot**  
   - Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather).  
   - Copy the **API Token** provided by BotFather.  
   - Find your **Chat ID** using Telegram API's `getUpdates` method.

4. **Edit the Script**  
   Add your Telegram bot token and chat ID in the following section of the script:  
   ```python
   bot_token = "your_telegram_bot_token"
   bot_chatid = "your_telegram_chat_id"
   ```

## How to Use

1. Run the script with the following command:  
   ```bash
   python calendar_reminder_sender.py
   ```

2. The script will:  
   - Authenticate with Google Calendar using OAuth 2.0.  
   - Retrieve events scheduled for the next 24 hours.  
   - Display the event details in the terminal.  
   - Send reminders via Telegram.

3. Example output in the terminal:  
   ```bash
   ============================================
   |       CALENDAR REMINDER SENDER         |
   |      Stay Organized, Stay Productive      |
   ============================================

   Fetching events from Google Calendar...
   📅 Event: Team Meeting  
   🕒 Date & Time: 20 December 2024, 14:00 (GMT+07:00)
   All reminders sent successfully!
   ```

4. Telegram notifications will be sent in a similar format.


## Tags/Keywords

- **Google Calendar API**  
- **Telegram Bot**  
- **Event Reminder**  
- **Task Automation**  
- **Python Automation**  
- **Date Formatter**  
- **Google API Integration**  
- **Notification System**

## Notes

- **Telegram Token and Chat ID:** Ensure you enter the correct bot token and chat ID to enable notifications.  
- **Credentials File:** The `credentials.json` file must be in the same directory as the script for Google API authentication.  
- **Time Zone Handling:** Ensure your Google Calendar time zone settings match your local time zone to avoid scheduling discrepancies.
