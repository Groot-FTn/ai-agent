import os
import argparse
import json
import sys
from prompts import system_prompt
from call_functions import available_functions, call_function
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = api_key
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt}
]

def main():

    for _ in range(20):

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions
            # temperature=0,
        )

        if response.usage == None:
            raise RuntimeError("API request failed, try again after a few seconds.")
        if response.usage != None and args.verbose == True:
            print(f"User prompt: {messages[1]["content"]}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                if not result_message.get("content"):
                    raise Exception("Error: Content not found")
                if args.verbose:
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
        else:
            print(f"Response:\n{message.content}")
            break
    else:
        print("Error: the number of iterations reached it's limit, the model cannot produce a final response")
        sys.exit(1)

if __name__ == "__main__":
    main()
