# Discord Bot

This is a simple Discord bot built using Python's `discord.py` library. It provides various commands for interacting with members, sending images, and displaying custom messages.

## Features

- **Ping**: Check the bot's latency.
- **Image Commands**: Send random or specific images.
- **Welcome and Farewell Messages**: Automatically greets new members and bids farewell to those who leave.
- **Experience Information**: Display experience-related information in chat.

## Setup

1. **Install Requirements**: Ensure you have `discord.py` installed.
    ```bash
    pip install discord.py
    ```

2. **Settings File**: Create a `setting.json` file in the root directory with the following structure:
    ```json
    {
        "TOKEN": "YOUR_DISCORD_BOT_TOKEN",
        "pic": ["path/to/your/image1.jpg", "path/to/your/image2.jpg"],
        "dong": ["message1", "message2"]
    }
    ```
    - Replace `YOUR_DISCORD_BOT_TOKEN` with your bot's actual token.
    - Add paths to your images and random messages in the `"pic"` and `"dong"` arrays.

3. **Run the Bot**: Start the bot using:
    ```bash
    python your_bot_script.py
    ```

## Commands

- **Ping**: `!ping` - Displays the bot's current latency.
- **Images**: 
  - `!圖片` - Sends a specific image.
  - `!隨圖` - Sends a random image from the list.
- **Random Message Commands**:
  - `!咚神`,  `!叮咚` - Sends a random message from the list.
- **Experience Info**: `!exp` - Displays experience-related information.

## Events

- **on_member_join**: Welcomes new members in the designated channel.
- **on_member_remove**: Sends a farewell message when a member leaves.

## License

This project is open-source and can be modified as needed.
