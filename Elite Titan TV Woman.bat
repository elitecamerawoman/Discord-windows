@echo off

set BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN

set CHANNEL_ID=YOUR_CHANNEL_ID

set MESSAGE=Your message here

curl -X POST -H "Content-Type: application/json" -H "Authorization: Bot %BOT_TOKEN%" ^
-d "{\"content\":\"%MESSAGE%\"}" ^
"https://discord.com/api/v10/channels/%CHANNEL_ID%/messages"
