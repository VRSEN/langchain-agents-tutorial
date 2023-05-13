<!-- @format -->

# Virtual Assistant with Langchain

This is a basic guide on how to set up and run a virtual assistant project that connects to your calendar, email, and Twitter accounts using Langchain, Tweepy, and Zapier.

[![Youtube thumbnail](thumb.png)](https://youtu.be/N4k459Zw2PU)

## Prerequisites

1. Python 3.6 or higher
2. `tweepy` library
3. `langchain` library

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

## Setting up API keys

You need to obtain API keys for the following services:

1. Twitter Developer Account (for Tweepy)
2. OpenAI API key
3. Zapier NLA API key

Replace the placeholders in the code with the respective API keys:

```python
consumer_key = "<CONSUMER_KEY>"
consumer_secret = "<CONSUMER_SECRET>"
access_token = "<ACCESS_TOKEN>"
access_token_secret = "<ACCESS_TOKEN_SECRET>"
```

```python
set_api_key("<11LABS_API_KEY>")
openai.api_key = "<OPENAI_API_KEY>"
```

```python
zapier = ZapierNLAWrapper(zapier_nla_api_key="<ZAPIER_NLA_API_KEY>")
```

## Running the program

1. Save the provided code in a file named `main.py`.
2. Open a terminal or command prompt and navigate to the folder containing `main.py`.
3. Run the program using the following command:

```bash
python main.py
```

4. The program will start an interactive session where you can type your messages to the virtual assistant. The assistant will respond to your queries based on the available tools and integrations.

## Example usage

You can interact with the virtual assistant using natural language, as it is capable of understanding and executing actions based on your input.

Examples:

- "Post a tweet saying 'Hello, World!'"
- "Schedule a meeting tomorrow at 3 PM"
- "Send an email to john@example.com with the subject 'Meeting reminder' and the message 'Don't forget our meeting tomorrow at 3 PM.'"

To exit the program, press `Ctrl+C` or close the terminal window.
