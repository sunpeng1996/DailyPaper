---
title: 'BYOD: Build Your Own DLM - Efficient Autoregressive-to-Diffusion Language
  Model Conversion'
title_zh: 《BYOD：基于LoRA的自回归到扩散语言模型高效转换方案》
authors:
- Ruurd J. A. Kuiper
- Robert A. Bagheri
affiliations:
- University Medical Center Utrecht
- Utrecht University
arxiv_id: '2610.41574'
url: https://arxiv.org/abs/2610.41574
pdf_url: https://arxiv.org/pdf/2610.41574
published: '2026-10-29'
collected: '2026-11-03'
category: Training
direction: 大模型训练 · AR转扩散LoRA适配
tags:
- LoRA
- DLM
- Autoregressive Model
- Parameter Efficient Fine-tuning
- Diffusion
one_liner: 仅用单GPU数小时LoRA微调，实现四大主流AR模型到DLM的低成本转换，性能接近全预训练LLaDA
practical_value: '- 生成式推荐可控文本生成场景，可复用仅微调Q/V投影的低成本LoRA方案，快速将业务现有AR大模型转换为支持双向上下文的DLM，避免全量预训练的高成本

  - 可借鉴「原模型权重全冻结+LoRA训练后直接合并」的范式，转换后的模型无额外推理开销，适合业务侧快速上线迭代

  - 搜索query改写、商品文案生成场景，可利用DLM并行token更新、双向上下文的特性，相比原生AR模型更好地利用全局约束提升生成一致性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散语言模型（DLM）支持并行token更新、灵活生成、双向注意力，但主流方案依赖昂贵的全量预训练或全参数微调，单8B规模DLM预训练成本可达数十万美元，普通团队难以落地，亟需低成本的自回归（AR）到DLM转换方案。

### 方法关键点
- 仅用LoRA微调：冻结原AR模型所有参数，仅为自注意力Q、V投影添加rank=1024的LoRA适配器，可训练参数仅占总参数的4.07%~5.77%
- 注意力改造：将所有层的因果注意力掩码替换为双向注意力掩码，复用原模型tokenizer的mask标记，无需扩充词表
- 训练目标：采用吸收掩码扩散目标，采样不同mask比例，仅计算answer和padding位置的重建损失，权重分别为0.9和0.1
- 推理逻辑：从全掩码的答案块开始，每步预测所有掩码位置，保留高置信度预测结果，低置信度位置重新掩码

### 关键实验
在9个通用基准（MMLU、GSM8K、HumanEval等）上测试，转换Gemma 2 9B、Llama 3.1 8B、Qwen2.5 7B、Ministral 8B四个主流AR模型，仅需单块Google Colab RTX Pro 6000 GPU训练3.1~4.0小时，训练数据量不超过102.4M tokens。其中BYOD-Gemma平均准确率达50.6%，仅比同规格全预训练DLM LLaDA 8B低1.3个百分点，保留了原模型大部分知识；生成128token时64步的perplexity为8.3~11.1，高于原AR模型的2.2~3.0和LLaDA的4.1。

### 最值得记住的一句话
仅用单GPU数小时、11美元成本的LoRA微调，就能将任意主流AR大模型转换为可用的DLM，成本仅为全预训练DLM的几万分之一
