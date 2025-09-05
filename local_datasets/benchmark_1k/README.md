---
language: en
license: mit
task_categories:
- text-generation
- summarization
tags:
- llm
- benchmark
- 1k-tokens
- generated
- synthetic
---

# Benchmark 1K Dataset

A curated dataset of 1,000 high-quality prompts designed for benchmarking Large Language Model (LLM) performance across various metrics including latency, throughput, and response quality.

## Dataset Overview

- **Size**: 1,000 prompts
- **Format**: JSONL (JSON Lines)
- **Average Token Length**: ~1,000 tokens per prompt
- **Purpose**: LLM benchmarking and performance testing
- **Domain**: General knowledge, historical content, and analytical writing

## Dataset Structure

Each line in the dataset contains a JSON object with the following structure:

```json
{
  "prompt": "Write a detailed history of the Roman Empire...",
  "token_length": 1000
}
```

### Fields

- **`prompt`**: The input text prompt for the LLM
- **`token_length`**: Approximate token count of the prompt (useful for token-based analysis)

## Content Characteristics

The dataset consists of prompts that:

- **Historical Analysis**: Detailed historical content requiring comprehensive knowledge
- **Long-form Content**: Prompts designed to generate substantial responses
- **Complex Topics**: Multi-faceted subjects requiring deep understanding
- **Consistent Length**: Standardized token count for fair benchmarking

### Example Topics

- Roman Empire history and legacy
- Scientific concepts and developments
- Economic analysis and trends
- Cultural and social phenomena
- Technical documentation and explanations

## Usage

### For LLM Benchmarking

This dataset is specifically designed for:

1. **Latency Testing**: Measure time-to-first-token (TTFT) and end-to-end latency
2. **Throughput Analysis**: Evaluate tokens per second and concurrent request handling
3. **Quality Assessment**: Test response coherence and factual accuracy
4. **Load Testing**: Stress test LLM endpoints under various conditions

### Integration with FastAPI Benchmark Tool

The dataset is compatible with the FastAPI LLM benchmark service:

```bash
# Example API call
curl -X POST "http://localhost:8000/run-load-test" \
  -H "Content-Type: application/json" \
  -d '{
    "user": 100,
    "spawnrate": 100,
    "model": "your-model-name",
    "url": "https://your-llm-endpoint.com",
    "duration": 60,
    "dataset": "your-username/benchmark-1k"
  }'
```

## Metrics Collected

When used with the benchmark tool, this dataset enables collection of:

- **Time to First Token (TTFT)**: Average, min, max, median
- **End-to-End Latency**: Complete response time
- **Inter-Token Latency**: Time between consecutive tokens
- **Token Speed**: Tokens generated per second
- **Throughput**: Input and output tokens per second

## Dataset Quality

- **Curated Content**: Hand-selected prompts for consistent quality
- **Token Standardization**: Uniform prompt length for fair comparison
- **Diverse Topics**: Wide range of subjects to test general knowledge
- **Real-world Scenarios**: Prompts that reflect actual usage patterns

## File Information

- **Filename**: `data.jsonl`
- **Encoding**: UTF-8
- **Line Count**: 1,000
- **Total Size**: ~1.2MB
- **Compression**: Uncompressed for easy processing

## License

This dataset is provided under the same license as the parent FastAPI LLM Benchmark project.

## Citation

If you use this dataset in your research or benchmarking, please cite:

```bibtex
@dataset{benchmark_1k_2025,
  title={Benchmark 1K Dataset for LLM Performance Testing},
  author={Raffel Prama},
  year={2025},
  url={https://huggingface.co/datasets/your-username/benchmark-1k}
}
```

## Contributing

To contribute to this dataset:

1. Fork the repository
2. Add new high-quality prompts following the same format
3. Ensure token length consistency
4. Submit a pull request with your additions

## Contact

For questions or issues related to this dataset, please open an issue in the main repository or contact the maintainer.

---

*This dataset is part of the FastAPI LLM Benchmark project - a comprehensive tool for testing and evaluating Large Language Model performance.*
