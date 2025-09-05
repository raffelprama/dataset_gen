import os
import logging
import json
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage
from transformers import AutoTokenizer


from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# --- Configuration Section ---
HF_USERNAME = "raffel36"
TOKENIZER_NAME = "Qwen/Qwen2.5-VL-7B-Instruct" 

try:
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME)
except Exception as e:
    print(f"Error loading tokenizer: {e}")
    exit()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

print(os.getenv("OPENAI_API_URL"))
print(os.getenv("OPENAI_API_KEY"))

client = OpenAI(
    base_url=os.getenv("OPENAI_API_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)
DEFAULT_MODEL = os.getenv("OPENAI_MODEL")

def get_token_length(text: str) -> int:
    return len(tokenizer.encode(text))

def llm_chat_completion_request(
    prompt: str, 
    model: str, 
    max_tokens: int,
    temperature: float = 0.7
) -> str:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.exception(f"LLM request failed")
        return ""

def generate_and_save_dataset_locally(
    dir_path: str, 
    target_tokens: int, 
    num_samples: int, 
    initial_prompt: str
):
    """Generates a dataset and saves it to a local directory as JSONL."""
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "train.jsonl")

    logger.info(f"Generating {num_samples} samples for {target_tokens} tokens...")
    with open(file_path, "w") as f:
        for i in range(num_samples):
            current_text = initial_prompt
            current_tokens = get_token_length(current_text)

            while current_tokens < target_tokens:
                tokens_to_generate = target_tokens - current_tokens
                generated_segment = llm_chat_completion_request(
                    prompt=current_text,
                    model=DEFAULT_MODEL,
                    max_tokens=min(tokens_to_generate + 100, 4096)
                )

                if not generated_segment:
                    logger.warning(f"Generation failed for sample {i+1}. Skipping.")
                    break

                current_text += " " + generated_segment
                current_tokens = get_token_length(current_text)

            trimmed_text = tokenizer.decode(tokenizer.encode(current_text)[:target_tokens])

            data_entry = {
                "text": trimmed_text,
                "token_length": get_token_length(trimmed_text)
            }
            f.write(json.dumps(data_entry) + "\n")
            logger.info(f"Generated sample {i+1}. Final length: {get_token_length(trimmed_text)}")

    logger.info(f"Dataset for {target_tokens} tokens saved to {file_path}")

# --- Main Execution ---
if __name__ == "__main__":
    datasets_to_create = {
        "1k": {
            "target_tokens": 1000,
            "initial_prompt": "Write a detailed history of the Roman Empire."
        },
        "8k": {
            "target_tokens": 8000,
            "initial_prompt": "Compose a comprehensive report on the future of renewable energy."
        },
        "16k": {
            "target_tokens": 16000,
            "initial_prompt": "Draft a lengthy fictional story about a journey through a fantastical world."
        }
    }
    num_samples_per_length = 5
    base_dir = "local_datasets"

    for length_label, params in datasets_to_create.items():
        dir_path = os.path.join(base_dir, f"benchmark_{length_label}")
        generate_and_save_dataset_locally(
            dir_path=dir_path,
            target_tokens=params["target_tokens"],
            num_samples=num_samples_per_length,
            initial_prompt=params["initial_prompt"]
        )

        # Create a basic README.md for each directory
        readme_content = f""