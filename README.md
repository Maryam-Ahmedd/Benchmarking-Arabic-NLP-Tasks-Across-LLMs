
# Arabic LLM Benchmarking Framework

A framework for benchmarking and comparing multiple Arabic-capable Large Language Models (LLMs) across a variety of Arabic NLP tasks.

## Overview

This project was built to evaluate the performance of different LLMs on Arabic language tasks while providing a unified pipeline for prompt execution, response collection, scoring, and comparative analysis.

The benchmark covers Modern Standard Arabic (MSA), Classical Arabic, and Arabic dialects to assess how each model handles linguistic diversity and Arabic-specific challenges.

## Models

* ChatGPT
* Gemini
* ALLaM
* Jais
* Fanar

## System Architecture

To support large-scale evaluation, different integration approaches were implemented depending on model accessibility.

### ALLaM Deployment

* Deployed ALLaM locally.
* Configured the local inference environment.
* Integrated the model into the benchmarking pipeline.
* Automated prompt execution and output collection.

### API Integrations

For models that provide API access:

* Integrated Gemini through its API.
* Integrated Fanar through its API.
* Implemented automated request handling.
* Parsed and stored model responses for evaluation.

### Browser Automation

For models without direct API access:

* Developed browser automation scripts for ChatGPT.
* Developed browser automation scripts for Jais.
* Automated prompt submission.
* Monitored response generation.
* Extracted model outputs automatically.
* Logged responses into structured datasets.

## Evaluation Pipeline

The framework automatically:

1. Loads benchmark prompts.
2. Sends identical prompts to all models.
3. Collects generated responses.
4. Stores outputs in a unified format.
5. Organizes results for analysis.
6. Generates comparison reports and visualizations.

## Response Evaluation

Responses were manually reviewed and rated using predefined evaluation criteria:

* Correctness
* Relevance
* Completeness
* Clarity
* Fluency
* Consistency
* Arabic language understanding

The collected ratings were used to compare model performance and identify strengths and weaknesses across different Arabic language varieties.

## Technologies

* Python
* LLM Deployment
* API Integration
* Browser Automation
* Prompt Engineering
* Data Processing
* Data Analysis
* Visualization

## Key Contributions

* Local deployment and integration of ALLaM.
* API-based integration of Gemini and Fanar.
* Browser automation for ChatGPT and Jais.
* Automated response collection and logging.
* Manual evaluation and comparative analysis of model outputs.
* Benchmarking across multiple Arabic language varieties.
