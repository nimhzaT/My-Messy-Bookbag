const tmi = require('tmi.js');

const client = new tmi.Client({
  options: { debug: true },
  connection: {
    secure: true,
    reconnect: true
  },
  identity: {
    username: 'inv0hk3',
    password: process.env.oauth:xnvrzqmvw7f0qjln0p58ye7oteldmk
  },
  channels: ['Chompdown']
});

client.connect();

client.on('message', (channel, tags, message, self) => {
  // Ignore echoed messages.
  if(self) return;

  if(message.toLowerCase() === '!hello') {
    client.say(channel, `@${tags.username}, Yo what's up`);
  }
});