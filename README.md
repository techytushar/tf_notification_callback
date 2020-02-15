# TensorFlow Notification Callback

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

A Tensorflow/Keras callback which sends information about your model training, on various messaging platforms.

## Installation

Using `pip`:

```bash
pip install tf_notification_callback
```

## Usage

Import the required module and add it to the list callbacks while training your model.

**Example:**

```python
>>> from tf_notification_callback import TelegramCallback
>>> telegram_callback = TelegramCallback('<BotToken>',
                                     '<ChatID>',
	                             'CNN Model',
	                             ['loss', 'val_loss'],
	                             ['accuracy', 'val_accuracy'],
	                             True)
>>> model.fit(x_train, y_train,
          batch_size=32,
          epochs=10,
          validation_data=(x_test, y_test),
          callbacks=[telegram_callback])
```

### Telegram

1. Create a telegram bot using BotFather
	* Search for @BotFather on telegram.
	* Send `/help` to get list of all commands.
	* Send `/newbot` to create a new bot and complete the setup.
	* Copy the **bot token** after creating the bot.
2. Get the **chat ID**
	* Search for the bot you created and send it any random message.
	* Go to this URL `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates` (replace <BOT_TOKEN> with your bot token)
	* Copy the `chat id` of the user you want to send messages to.
3. Use the `TelegramCallback()` class.

```python
TelegramCallback(bot_token=None, chat_id=None, modelName='model', loss_metrics=['loss'], acc_metrics=[], getSummary=False):
```

**Arguments:**

`bot_token` : unique token of Telegram bot `{str}`
`chat_id` : Telegram chat id you want to send message to `{str}`
`modelName` : name of your model `{str}`
`loss_metrics` : loss metrics you want in the loss graph `{list of strings}`
`acc_metrics` : accuracy metrics you want in the accuracy graphs `{list of strings}`
`getSummary` : Do you want message for each epoch (False) or a single message containing information about all epochs (True). `{bool}`

### Slack

1. Create a Slack workspace
2. Create a new channel
3. Search for the **Incoming Webhooks** in the Apps and install it.
4. Copy the **Webhook URL**
5. Import the `SlackCallback()` class. It takes in the following arguments

`webhookURL` : unique webhook URL of the app `{str}`
`channel` :  channel name or username you want to send message to `{str}`
`modelName` : name of your model `{str}`
`loss_metrics` : loss metrics you want in the loss graph `{list of strings}`
`acc_metrics` : accuracy metrics you want in the accuracy graph `{list of strings}`
`getSummary` : Do you want message for each epoch (False) or a single message containing information about all epochs (True). `{bool}`

*Sending images in Slack is not supported currently.*

## ToDo

* WhatsApp
* E-Mail
* Zulip
* Messages

## Motivation

As the Deep Learning models are getting more and more complex and computationally heavy, they take a very long time to train. During my internship, people used to start the model training and left it overnight. They could only check its progress the next day. So I thought it would be great if there was a simple way to get the training info remotely on their devices.
