import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("API key is missing")
    
    print("Hello from agent!\n")
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key=api_key)
    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,
        temperature=0,
    )

    for _ in range(20):
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=config,
        )

        # Step 1: add the model's reply to the conversation history so it
        # can see its own reasoning in the next iteration
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        # Step 2: if the model wants to call functions, run them and collect results
        if response.function_calls:
            function_responses = []
            for fc in response.function_calls:
                function_call_result = call_function(fc, verbose=args.verbose)
                if not function_call_result.parts:
                    raise RuntimeError("Function call returned no parts")
                if function_call_result.parts[0].function_response is None:
                    raise RuntimeError("Function call returned no function response")
                if function_call_result.parts[0].function_response.response is None:
                    raise RuntimeError("Function call returned no response")
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                function_responses.append(function_call_result.parts[0])

            # Step 3: add all tool results to the conversation so the model
            # sees what the functions returned on the next iteration
            messages.append(types.Content(role="user", parts=function_responses))

        else:
            # No function calls means the model has a final answer so we print and stop
            print(f"Final response:\n{response.text}")
            break

    else:
        # Loop exhausted without a final text response
        print("Error: Agent reached maximum iterations without producing a final response")
        exit(1)

if __name__ == "__main__":
    main()
