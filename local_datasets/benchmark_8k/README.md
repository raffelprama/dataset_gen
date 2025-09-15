---
language: en
license: mit
task_categories:
- text-generation
- summarization
tags:
- llm
- benchmark
- 8k-tokens
- generated
- synthetic
---

# Benchmark 8K Dataset

A curated dataset of 1,000 high-quality prompts designed for benchmarking Large Language Model (LLM) performance across various metrics including latency, throughput, and response quality. This dataset features longer, more complex prompts ideal for testing models' capabilities with extended context and detailed analysis tasks.

## Dataset Overview

- **Size**: 100 prompts
- **Format**: JSONL (JSON Lines)
- **Average Token Length**: Variable (extended context; computed from actual data)
- **Purpose**: LLM benchmarking and performance testing with extended context
- **Domain**: Comprehensive reports, detailed analysis, and complex multi-topic content

## Dataset Structure

Each line in the dataset contains a JSON object with the following structure:

```json
{
  "prompt": "Compose a comprehensive report on the future of renewable energy..."
}
```

### Fields

- **`prompt`**: The input text prompt for the LLM

## Content Characteristics

The dataset consists of prompts that:

- **Comprehensive Reports**: Detailed, multi-section reports requiring extensive knowledge synthesis
- **Extended Analysis**: Long-form content designed to test models' ability to maintain coherence over extended outputs
- **Complex Multi-Topic Content**: Prompts covering multiple interconnected subjects requiring deep understanding
- **Consistent Length**: Standardized 8k token count for fair benchmarking across different models
- **Professional Writing**: Business, academic, and technical writing styles

### Example Topics

- Comprehensive renewable energy reports
- Detailed historical analysis and documentation
- Multi-faceted scientific and technical explanations
- Complex economic and policy analysis
- Extensive cultural and social phenomenon studies

## Usage

### For LLM Benchmarking

This dataset is specifically designed for:

1. **Extended Context Testing**: Measure how well models handle long-form content generation
2. **Coherence Analysis**: Test response quality and consistency over extended outputs
3. **Memory and Context Retention**: Evaluate models' ability to maintain context throughout long responses
4. **Throughput Analysis**: Evaluate tokens per second and concurrent request handling with longer prompts
5. **Load Testing**: Stress test LLM endpoints with complex, extended content generation

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
    "dataset": "your-username/benchmark-8k"
  }'
```

## Metrics Collected

When used with the benchmark tool, this dataset enables collection of:

- **Time to First Token (TTFT)**: Average, min, max, median
- **End-to-End Latency**: Complete response time for extended content
- **Inter-Token Latency**: Time between consecutive tokens
- **Token Speed**: Tokens generated per second
- **Throughput**: Input and output tokens per second
- **Context Retention**: Coherence metrics over extended outputs
- **Response Quality**: Consistency and accuracy across long-form content

## Dataset Quality

- **Curated Content**: Hand-selected prompts for consistent quality and complexity
- **Token Standardization**: Uniform 8k token count for fair comparison
- **Diverse Topics**: Wide range of subjects to test comprehensive knowledge
- **Real-world Scenarios**: Prompts that reflect actual professional and academic usage patterns
- **Extended Context**: Designed to test models' capabilities with longer, more complex inputs

## File Information

- **Filename**: `train.jsonl`
- **Encoding**: UTF-8
- **Line Count**: 100
- **Compression**: Uncompressed for easy processing

## Stats

- Prompt length is data-driven and varies across entries. Compute up-to-date averages locally by scanning `train.jsonl`.

## Use Cases

### Research Applications

- **Model Comparison**: Compare different LLMs on extended content generation
- **Context Window Testing**: Evaluate how models perform with longer prompts
- **Coherence Studies**: Analyze response quality over extended outputs
- **Performance Benchmarking**: Standardized testing for long-form content generation

### Industry Applications

- **Content Generation**: Test models for professional report writing
- **Academic Research**: Evaluate models for research paper assistance
- **Business Intelligence**: Assess models for comprehensive analysis tasks
- **Technical Documentation**: Test models for detailed technical writing

## License

This dataset is provided under the same license as the parent FastAPI LLM Benchmark project.

## Citation

If you use this dataset in your research or benchmarking, please cite:

```bibtex
@dataset{benchmark_8k_2025,
  title={Benchmark 8K Dataset for LLM Performance Testing with Extended Context},
  author={Raffel Prama},
  year={2025},
  url={https://huggingface.co/datasets/your-username/benchmark-8k}
}
```

## Contributing

To contribute to this dataset:

1. Fork the repository
2. Add new high-quality prompts following the same format
3. Ensure 8k token length consistency
4. Submit a pull request with your additions

## Contact

For questions or issues related to this dataset, please open an issue in the main repository or contact the maintainer.

---

*This dataset is part of the FastAPI LLM Benchmark project - a comprehensive tool for testing and evaluating Large Language Model performance with extended context and complex content generation.*