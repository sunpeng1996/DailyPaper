---
title: 'Quantization Effects on Bangla Language Understanding in Large Language Models:
  A Systematic Evaluation'
title_zh: 大模型训练后量化对孟加拉语自然语言理解的影响系统评估
authors:
- Ismail Hossain
- Nafi Ullah Shafin
- Mohammad Abdullah Al Mumin
affiliations:
- Shahjalal University of Science and Technology (SUST), Bangladesh
arxiv_id: '2608.24615'
url: https://arxiv.org/abs/2608.24615
pdf_url: https://arxiv.org/pdf/2608.24615
published: '2026-08-25'
collected: '2026-08-26'
category: LLM
direction: 大模型量化 · 低资源语言性能评估
tags:
- Quantization
- Low-resource NLP
- LLM Evaluation
- Bangla NLU
- Post-training Quantization
one_liner: 首次系统评估多系列大模型不同量化格式在孟加拉语NLU任务上的表现及选型规律
practical_value: '- 8bit量化选型优先选GPTQ格式，Qwen/LLaMA系列的GPTQ-Int8精度损失<1.5%，内存占用降一半，适合端侧/边缘部署的Agent、推荐文案生成等场景

  - 推理类/常识类任务对量化敏感度远高于阅读理解类，涉及多步推理的电商导购Agent、query意图识别场景不要用未针对目标语言校准的GGUF-W8A16量化格式

  - 针对小语种本地化业务（如东南亚跨境电商），量化前必须用目标语言的任务benchmark验证，不能直接复用英文场景的量化选型结论

  - 部分量化版本精度略高于全精度的现象可归因于正则效应，业务部署时可优先验证对应量化版本的实际效果，不必默认全精度最优'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大模型训练后量化（PTQ）的效果评估几乎全部基于英文基准，对于孟加拉语这类形态复杂、资源匮乏的低资源语言，量化是否会放大精度损失、不同量化格式的适配性差异尚不明确。而低资源地区的端侧LLM部署需求迫切，缺乏针对性的选型指导。
### 方法关键点
- 控制变量实验：覆盖3个主流LLM系列（Qwen-2.5-7B、LLaMA-3.1-8B、GPT-OSS-20B），每个系列分别测试全精度版本和1种8bit量化版本（GPTQ-Int8、GPTQ-Q8、GGUF-W8A16），仅量化策略为变量
- 任务覆盖5类孟加拉语公开NLU基准：百科推理、常识推理、科学推理、物理常识、阅读理解
- 采用lm-evaluation-harness做零-shot评估，指标为准确率和相对精度衰减
### 关键实验结果
- 全精度基准：Qwen-2.5-7B在百科推理任务准确率0.44最优，LLaMA-3.1-8B在阅读理解任务准确率0.914最优
- 量化表现：GPTQ量化的Qwen、LLaMA系列精度损失均<1.5%，部分任务精度略高于全精度；GGUF-W8A16量化的GPT-OSS在推理类任务上精度衰减最高达57.4%，仅阅读理解任务衰减<6%
- 任务敏感度：推理/常识类任务的量化衰减幅度是阅读理解类的10倍以上
### 核心结论
大模型量化的精度损失主要由模型架构、量化格式和任务类型决定，而非单纯由位宽决定，低资源语言部署必须做针对性验证。
