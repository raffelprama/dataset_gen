import os
import logging
import json
import random
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage
from transformers import AutoTokenizer


from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# --- Configuration Section ---
HF_USERNAME = "raffel36"
TOKENIZER_NAME = "Qwen/Qwen2.5-VL-7B-Instruct" 
OPENAI_API_KEY="sk-G1_wkZ37sEmY4eqnGdcNig"
try:
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME)
except Exception as e:
    print(f"Error loading tokenizer: {e}")
    exit()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

api_key = OPENAI_API_KEY
print(os.getenv("OPENAI_API_URL"))
print(api_key)

client = OpenAI(
    base_url=os.getenv("OPENAI_API_URL"),
    api_key=api_key
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
    initial_prompt: str,
    target_tokens_stddev: float = 0.1,
    enforce_exact_mean: bool = True
):
    """Generates a dataset and saves it to a local directory as JSONL.

    Each sample uses a per-sample target length drawn from a normal
    distribution centered at `target_tokens` with standard deviation
    `target_tokens * target_tokens_stddev`. If `enforce_exact_mean` is True,
    the last sample is adjusted so that the average per-sample target equals
    `target_tokens` exactly.
    """
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "test.jsonl")

    logger.info(f"Generating {num_samples} samples with mean target {target_tokens} tokens...")

    # Prepare per-sample token targets
    sigma = max(1, int(round(target_tokens * target_tokens_stddev)))
    min_target = max(50, int(target_tokens * 0.5))
    max_target = int(target_tokens * 1.5)

    per_sample_targets = []
    running_sum = 0
    for i in range(num_samples):
        if enforce_exact_mean and i == num_samples - 1:
            exact_remaining = target_tokens * num_samples - running_sum
            sampled_target = int(exact_remaining)
        else:
            sampled_target = int(round(random.normalvariate(target_tokens, sigma)))

        sampled_target = max(min_target, min(max_target, sampled_target))
        per_sample_targets.append(sampled_target)
        running_sum += sampled_target

    with open(file_path, "w") as f:
        for i, sample_target in enumerate(per_sample_targets):
            current_text = initial_prompt
            current_tokens = get_token_length(current_text)

            while current_tokens < sample_target:
                tokens_to_generate = sample_target - current_tokens
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

            trimmed_text = tokenizer.decode(tokenizer.encode(current_text)[:sample_target])

            data_entry = {
                "text": trimmed_text,
                "token_length": get_token_length(trimmed_text)
            }
            f.write(json.dumps(data_entry) + "\n")
            logger.info(
                f"Generated sample {i+1} with target {sample_target}. Final length: {get_token_length(trimmed_text)}"
            )

    achieved_avg = sum(per_sample_targets) / num_samples if num_samples else 0
    logger.info(f"Achieved mean target across samples: {achieved_avg:.2f} tokens")
    logger.info(f"Dataset saved to {file_path}")

# --- Main Execution ---
if __name__ == "__main__":
    datasets_to_create = {
        # "1k": {
        #     "target_tokens": 1000,
        #     "initial_prompt": "Write a detailed history in the world."
        # }
        # ,
        # "8k": {
        #     "target_tokens": 8000,
        #     "initial_prompt": "Compose a comprehensive report about economy or business or education or law."
        # }
        # ,
        "16k": {
            "target_tokens": 16000,
            "initial_prompt": "Draft a lengthy fictional story about a journey through a fantastical world about sad and deppresion thing."
        }
    }
    num_samples_per_length = 10
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