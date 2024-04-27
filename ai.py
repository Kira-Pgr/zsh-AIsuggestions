import requests
import sys

def get_suggestion(user_input):
    url = "http://nekorevo:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    attempts = 3  # Number of attempts to get a valid suggestion

    for attempt in range(attempts):
        data = {
            "model": "llama3",
            "prompt": f"Complete the given Linux command with the most relevant and concise option(s) using plain text. If the given Linux command is already complete, predict the next possible argument or command that the user might want to use. Provide only the completion within the <cmd> tags, followed by a brief explanation after a # symbol. Do not include any additional text or formatting outside the tags. For example: If the input is l, you should output: <cmd>ls # list files</cmd>. If the input is pw, you should output: <cmd>pwd # print working directory</cmd>. If the input is ls -a, you should output: <cmd>ls -al # list all files, including hidden ones</cmd>. If the input is gcc, you should output: <cmd>gcc test.c # Compile test.c</cmd>.Now, please complete the following command: {user_input}",
            "stream": False
        }
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            # Check if the response is correctly formatted
            if '<cmd>' in result['response'] and '</cmd>' in result['response']:
                command_section = result['response'].split('<cmd>')[1].split('</cmd>')[0].strip()
                # Validate if the command starts with user input
                if command_section.startswith(user_input):
                    # Output only the command after the user's input
                    command = command_section[len(user_input):].strip().split(' #')[0]
                    return command.strip()
                else:
                    pass
                    #print(f"Command does not start with user input. Attempt {attempt + 1} failed.")
            else:
                pass
                #print(f"Response format mismatch. Attempt {attempt + 1} failed.")
        else:
            pass
            #print(f"Error: Failed to get suggestion with status code {response.status_code}")

    return ""

if __name__ == "__main__":
    input_cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    print(get_suggestion(input_cmd))
