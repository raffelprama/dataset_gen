---
language: en
license: mit
task_categories:
- text-generation
tags:
- llm
- benchmark
- 16k-tokens
- generated
- synthetic
- creative-writing
- storytelling
---

# Benchmark 16K Dataset

A curated dataset of 100 high-quality prompts designed for benchmarking Large Language Model (LLM) performance across various metrics including latency, throughput, and response quality. This dataset features very long, complex prompts ideal for testing models' capabilities with extended context, creative writing, and detailed narrative generation.

## Dataset Overview

- **Size**: 100 prompts
- **Format**: JSONL (JSON Lines)
- **Average Token Length**: Variable (very long-form; computed from actual data)
- **Purpose**: LLM benchmarking and performance testing with maximum context length
- **Domain**: Creative writing, storytelling, detailed narratives, and complex multi-scenario content

## Dataset Structure

Each line in the dataset contains a JSON object with the following structure:

```json
{
  "prompt": "Draft a lengthy fictional story about a journey through a fantastical world..."
}
```

### Fields

- **`prompt`**: The input text prompt for the LLM

## Content Characteristics

The dataset consists of prompts that:

- **Creative Writing**: Extensive fictional stories, narratives, and creative content
- **Detailed Storytelling**: Complex plots with multiple characters, settings, and scenarios
- **Extended Context**: Very long prompts designed to test maximum context window capabilities
- **Narrative Coherence**: Content requiring consistent character development and plot progression
- **Imaginative Content**: Fantasy, science fiction, and creative scenarios requiring extensive world-building

### Example Topics

- Epic fantasy adventures and quests
- Science fiction narratives and space exploration
- Historical fiction with detailed period settings
- Complex character-driven stories
- Multi-generational family sagas
- Detailed world-building and universe creation

## Usage

### For LLM Benchmarking

This dataset is specifically designed for:

1. **Maximum Context Testing**: Measure how well models handle very long prompts and extended outputs
2. **Creative Writing Assessment**: Test models' ability to generate coherent, engaging narratives
3. **Memory and Consistency**: Evaluate models' ability to maintain character consistency and plot coherence
4. **Extended Throughput Analysis**: Evaluate tokens per second with very long content generation
5. **Stress Testing**: Push LLM endpoints to their limits with maximum context length prompts
6. **Creative Quality Metrics**: Assess narrative flow, character development, and storytelling quality

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
    "dataset": "your-username/benchmark-16k"
  }'
```

## Metrics Collected

When used with the benchmark tool, this dataset enables collection of:

- **Time to First Token (TTFT)**: Average, min, max, median
- **End-to-End Latency**: Complete response time for very long content
- **Inter-Token Latency**: Time between consecutive tokens
- **Token Speed**: Tokens generated per second
- **Throughput**: Input and output tokens per second
- **Context Retention**: Coherence metrics over very extended outputs
- **Creative Quality**: Narrative consistency and storytelling metrics
- **Character Consistency**: Character development and dialogue quality
- **Plot Coherence**: Story structure and logical progression

## Dataset Quality

- **Curated Content**: Hand-selected prompts for consistent quality and creativity
- **Token Standardization**: Uniform 16k token count for fair comparison
- **Diverse Genres**: Wide range of creative writing styles and genres
- **Real-world Scenarios**: Prompts that reflect actual creative writing and storytelling needs
- **Maximum Context**: Designed to test models' capabilities with the longest possible prompts
- **Creative Excellence**: High-quality prompts that challenge models' creative and narrative abilities

## File Information

- **Filename**: `train.jsonl`
- **Encoding**: UTF-8
- **Line Count**: 100
- **Compression**: Uncompressed for easy processing

## Stats

- Prompt length is data-driven and may vary significantly across entries. Compute current averages locally by scanning `train.jsonl`.

## Use Cases

### Research Applications

- **Context Window Studies**: Research how models handle maximum context lengths
- **Creative AI Evaluation**: Assess models' creative writing and storytelling capabilities
- **Narrative Coherence Analysis**: Study how well models maintain story consistency
- **Performance Benchmarking**: Standardized testing for very long content generation

### Industry Applications

- **Creative Writing Tools**: Test models for creative writing assistance and story generation
- **Content Creation**: Evaluate models for long-form content creation
- **Entertainment Industry**: Assess models for script writing and narrative development
- **Educational Tools**: Test models for creative writing education and assistance
- **Publishing**: Evaluate models for book writing and manuscript assistance

## Special Considerations

### Context Window Limitations

- **Model Compatibility**: Ensure your target models support 16k+ context windows
- **Memory Requirements**: Higher memory usage due to extended context
- **Processing Time**: Longer processing times for very long prompts
- **Quality vs Speed**: Balance between response quality and generation speed

### Creative Writing Metrics

- **Narrative Flow**: How well the story progresses and maintains reader interest
- **Character Development**: Consistency and depth of character portrayal
- **World Building**: Coherence and detail of fictional settings
- **Dialogue Quality**: Natural and engaging character conversations
- **Plot Structure**: Logical progression and satisfying story arcs

## License

This dataset is provided under the same license as the parent FastAPI LLM Benchmark project.

## Citation

If you use this dataset in your research or benchmarking, please cite:

```bibtex
@dataset{benchmark_16k_2025,
  title={Benchmark 16K Dataset for LLM Performance Testing with Maximum Context and Creative Writing},
  author={Raffel Prama},
  year={2025},
  url={https://huggingface.co/datasets/your-username/benchmark-16k}
}
```

## Contributing

To contribute to this dataset:

1. Fork the repository
2. Add new high-quality creative writing prompts following the same format
3. Ensure 16k token length consistency
4. Focus on creative, engaging, and imaginative content
5. Submit a pull request with your additions

## Contact

For questions or issues related to this dataset, please open an issue in the main repository or contact the maintainer.

---

*This dataset is part of the FastAPI LLM Benchmark project - a comprehensive tool for testing and evaluating Large Language Model performance with maximum context length and creative writing capabilities.*
