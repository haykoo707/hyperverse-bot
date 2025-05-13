// index.js

require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');
const fs = require('fs');
const path = require('path');
const { main } = require('./keyboards');

// Բեռնել Token-ը միջավայրից
const bot = new TelegramBot(process.env.BOT_TOKEN, { polling: true });

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  const username = msg.from.username || "friend";

  const photoPath = path.join(__dirname, 'Flux.jpg'); // պատկերիդ անունը
  const caption = `Hey👋 @${username} Welcome to the HyperVerse`;

  bot.sendPhoto(chatId, fs.createReadStream(photoPath), {
    caption,
    ...main
  });
});
