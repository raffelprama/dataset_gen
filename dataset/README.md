<div align="center">

# 🚀 LLM Benchmark Dataset Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI API" />
  <img src="https://img.shields.io/badge/Hugging%20Face-Datasets-yellow?style=for-the-badge&logo=huggingface&logoColor=white" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License" />
</p>

<p align="center">
  <strong>🎯 Generate high-quality benchmark datasets for LLM performance testing</strong>
  <br/>
  <em>Automated dataset generation with 1K, 8K, and 16K token lengths</em>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#deployment">Deployment</a> •
  <a href="#usage">Usage</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#contributing">Contributing</a>
</p>

</div>

---

## 📊 Overview

A professional Python tool for generating high-quality benchmark datasets with different token lengths (1K, 8K, 16K) for testing Large Language Model (LLM) performance. The generated datasets are optimized for benchmarking latency, throughput, and response quality across various context lengths.

### ✨ Key Features

- 🎯 **Multi-Length Support**: Generate datasets with 1K, 8K, and 16K token lengths
- 🤖 **AI-Powered Generation**: Uses LLM to create diverse, high-quality content
- 📏 **Token Standardization**: Ensures consistent token counts across all samples
- 🚀 **Hugging Face Ready**: Optimized for seamless upload to Hugging Face Hub
- ⚙️ **Highly Configurable**: Customizable prompts, token lengths, and sample counts
- 📈 **Performance Optimized**: Designed for accurate LLM benchmarking

### 📋 Generated Datasets

| Dataset | Token Length | Content Type | Use Case |
|---------|-------------|--------------|----------|
| **1K** | ~1,000 tokens | Historical analysis & general knowledge | Basic performance testing |
| **8K** | ~8,000 tokens | Comprehensive reports & detailed analysis | Extended context testing |
| **16K** | ~16,000 tokens | Creative writing & storytelling | Maximum context testing |

### 🎯 Target Applications

- **Research**: Academic studies on LLM performance across different context lengths
- **Industry**: Production system benchmarking and optimization
- **Development**: Model comparison and evaluation during development
- **Quality Assurance**: Automated testing of LLM endpoints and services

## 🚀 Quick Start

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/fast-api.git
cd fast-api/dataset

# Install dependencies
pip install -r requirements.txt

# Install Hugging Face CLI
pip install huggingface_hub
```

### ⚙️ Environment Setup

1. **Create environment file**:
```bash
cp .env.example .env
```

2. **Configure your `.env` file**:
```env
# LLM API Configuration
OPENAI_API_URL=https://your-llm-endpoint.com/v1
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=your-model-name
```

3. **Run the generator**:
```bash
python main.py
```

### 🎯 One-Line Setup

```bash
pip install openai transformers python-dotenv huggingface_hub && python main.py
```

## 💻 Usage

### 🎯 Basic Usage

```bash
# Generate all datasets (1K, 8K, 16K) with default settings
python main.py
```

**Output**: Creates three datasets with 5 samples each in `local_datasets/` directory.

### ⚙️ Advanced Configuration

Customize the generation process by editing `main.py`:

```python
# Custom dataset configuration
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

# Generation parameters
num_samples_per_length = 100  # Generate 100 samples per dataset
base_dir = "custom_datasets"  # Custom output directory
```

### 📊 Parameters Reference

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| `target_tokens` | Desired token length for prompts | - | `1000`, `8000`, `16000` |
| `initial_prompt` | Starting prompt for content generation | - | `"Write a detailed analysis..."` |
| `num_samples_per_length` | Number of samples to generate | `5` | `100` |
| `base_dir` | Output directory name | `"local_datasets"` | `"my_datasets"` |

## 📁 Generated Dataset Structure

```
local_datasets/
├── 📁 benchmark_1k/
│   ├── 📄 train.jsonl      # 1K token prompts
│   └── 📄 README.md        # Dataset documentation
├── 📁 benchmark_8k/
│   ├── 📄 train.jsonl      # 8K token prompts
│   └── 📄 README.md        # Dataset documentation
└── 📁 benchmark_16k/
    ├── 📄 train.jsonl      # 16K token prompts
    └── 📄 README.md        # Dataset documentation
```

### 📄 JSONL Format

Each line in `train.jsonl` contains a JSON object:

```json
{
  "text": "Write a detailed history of the Roman Empire. The Roman Empire was a political entity...",
  "token_length": 1000
}
```

**Field Descriptions**:
- `text`: The generated prompt content
- `token_length`: Exact token count for the prompt

## 🚀 Deploying to Hugging Face Hub

### 🔐 Step 1: Authentication

```bash
# Login to Hugging Face
huggingface-cli login

# Enter your token when prompted
# Token: hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 🏗️ Step 2: Create Repositories

```bash
# Create dataset repositories
huggingface-cli repo create "benchmark_1k" --type dataset
huggingface-cli repo create "benchmark_8k" --type dataset
huggingface-cli repo create "benchmark_16k" --type dataset
```

### 📤 Step 3: Upload Datasets

```bash
# Upload 1K dataset
cd local_datasets/benchmark_1k
huggingface-cli upload username/benchmark_1k . --repo-type=dataset

# Upload 8K dataset
cd ../benchmark_8k
huggingface-cli upload username/benchmark_8k . --repo-type=dataset

# Upload 16K dataset
cd ../benchmark_16k
huggingface-cli upload username/benchmark_16k . --repo-type=dataset
```

### ✅ Step 4: Verify Deployment

Check your published datasets:

| Dataset | Hugging Face URL | Status |
|---------|------------------|--------|
| **1K** | [username/benchmark_1k](https://huggingface.co/datasets/username/benchmark_1k) | 🟢 Live |
| **8K** | [username/benchmark_8k](https://huggingface.co/datasets/username/benchmark_8k) | 🟢 Live |
| **16K** | [username/benchmark_16k](https://huggingface.co/datasets/username/benchmark_16k) | 🟢 Live |

### 🎯 One-Command Deployment

```bash
# Deploy all datasets at once
for dataset in benchmark_1k benchmark_8k benchmark_16k; do
  cd local_datasets/$dataset
  huggingface-cli upload username/$dataset . --repo-type=dataset
  cd ../..
done
```

## Using Generated Datasets

### With FastAPI Benchmark Tool

```bash
# Test with 1K dataset
curl -X POST "http://localhost:8000/run-load-test" \
  -H "Content-Type: application/json" \
  -d '{
    "user": 100,
    "spawnrate": 100,
    "model": "your-model-name",
    "url": "https://your-llm-endpoint.com",
    "duration": 60,
    "dataset": "username/benchmark_1k"
  }'

# Test with 8K dataset
curl -X POST "http://localhost:8000/run-load-test" \
  -H "Content-Type: application/json" \
  -d '{
    "user": 50,
    "spawnrate": 50,
    "model": "your-model-name", 
    "url": "https://your-llm-endpoint.com",
    "duration": 60,
    "dataset": "username/benchmark_8k"
  }'

# Test with 16K dataset
curl -X POST "http://localhost:8000/run-load-test" \
  -H "Content-Type: application/json" \
  -d '{
    "user": 25,
    "spawnrate": 25,
    "model": "your-model-name",
    "url": "https://your-llm-endpoint.com", 
    "duration": 60,
    "dataset": "username/benchmark_16k"
  }'
```

### With Python

```python
from datasets import load_dataset

# Load datasets
dataset_1k = load_dataset("username/benchmark_1k")
dataset_8k = load_dataset("username/benchmark_8k")
dataset_16k = load_dataset("username/benchmark_16k")

# Access data
for sample in dataset_1k["train"]:
    print(f"Text: {sample['text'][:100]}...")
    print(f"Token Length: {sample['token_length']}")
```

## Customization

### Adding New Token Lengths

1. Add new configuration to `datasets_to_create`:
```python
"32k": {
    "target_tokens": 32000,
    "initial_prompt": "Write an extensive technical manual for advanced machine learning systems."
}
```

2. Run the generator:
```bash
python main.py
```

### Modifying Initial Prompts

Edit the `initial_prompt` field for each dataset to change the content focus:

```python
"1k": {
    "target_tokens": 1000,
    "initial_prompt": "Explain quantum computing principles in detail."
}
```

### Adjusting Sample Count

Change `num_samples_per_length` in the main execution section:

```python
num_samples_per_length = 100  # Generate 100 samples per dataset
```

## Troubleshooting

### Common Issues

1. **API Rate Limits**: Reduce `num_samples_per_length` or add delays between requests
2. **Memory Issues**: Process datasets individually for large sample counts
3. **Token Length Mismatch**: Verify tokenizer compatibility with your model
4. **Upload Failures**: Check Hugging Face token permissions and repository access

### Debug Mode

Enable detailed logging:

```python
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
```

## File Structure

```
dataset/
├── main.py              # Main dataset generator script
├── README.md            # This file
├── .env                 # Environment variables (create this)
├── requirements.txt     # Python dependencies
└── local_datasets/      # Generated datasets
    ├── benchmark_1k/
    ├── benchmark_8k/
    └── benchmark_16k/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with different configurations
5. Submit a pull request

## License

This project is licensed under the MIT License. See the main project LICENSE file for details.

## Support

For issues and questions:
- Open an issue in the main repository
- Check the Hugging Face dataset pages for usage examples
- Review the FastAPI benchmark tool documentation

---

*This dataset generator is part of the FastAPI LLM Benchmark project - a comprehensive tool for testing and evaluating Large Language Model performance.*
