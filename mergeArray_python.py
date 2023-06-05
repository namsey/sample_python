import asyncio
import json
import aiohttp


async def main():
    api_key = "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"
    input_file = r"C:\Users\176381\openai\input.txt"  # Replace with the path to your TXT file
    output_file = input_file.replace(".txt", "_output.txt")  # Create output file path by replacing file extension
    prmpt = input("Enter user prompt: ")
    with open(input_file) as f:
        lines = f.readlines()
        formatted_str = ''.join(lines).replace('\r\n', '\\n').replace('\r', '').replace('\n', '\\\\n ')
        input_str = prmpt + r"\n" + r"\n" + formatted_str
        await process_input(input_str, api_key, output_file)


async def process_input(input_str, api_key, output_file):
    async with aiohttp.ClientSession() as session:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "prompt": input_str,
            "max_tokens": 1000,
            "temperature": 0.7,
        }
        async with session.post(
                "https://api.openai.com/v1/engines/text-davinci-003/completions",
                headers=headers,
                data=json.dumps(data),
        ) as response:
            json_data = await response.json()
            print(json_data)
            output_text = json_data["choices"][0]["text"] + "\n"
            print(output_text)
            output_text = output_text.replace('\\n', '\n')
            with open(output_file, 'w') as f:  # Save output to file
                f.write(output_text)


if __name__ == "__main__":
    asyncio.run(main())
