---
title: 'Debias-SparseGPT: Bias-Aware Pruning for Large Language Models'
title_zh: Debias-SparseGPT：面向大语言模型的偏见感知剪枝方法
authors:
- Irina Proskurina
- Guillaume Metzler
- Antoine Gourru
- Julien Velcin
affiliations:
- Laboratoire Hubert Curien, UMR CNRS 5516
- Université Claude Bernard Lyon 1
- Université Lumière Lyon 2
- École Centrale de Lyon, LIRIS CNRS UMR 5205
arxiv_id: '2609.02496'
url: https://arxiv.org/abs/2609.02496
pdf_url: https://arxiv.org/pdf/2609.02496
published: '2026-09-01'
collected: '2026-09-03'
category: LLM
direction: LLM压缩 · 剪枝偏见缓解
tags:
- LLM Pruning
- Model Compression
- Debiasing
- SparseGPT
- Inference Efficiency
one_liner: 改进SparseGPT剪枝逻辑，加入偏见感知项，降低压缩后LLM的偏见放大同时保留推理效率与性能
practical_value: '- 业务侧部署轻量LLM用于智能客服、商品文案生成、推荐理由生成时，可复用该偏见感知剪枝逻辑，避免压缩后模型输出性别/地域等刻板偏见导致客诉

  - 该方法仅修改SparseGPT的Hessian计算逻辑，不增加推理开销、不需要全量微调，可直接集成到现有LLM压缩管线，兼容Hugging Face生态

  - 高稀疏度下可补充业务场景的非偏见对比校准数据（如不同属性用户的商品咨询样例），同时保障压缩后模型的场景性能和公平性

  - 做LLM公平性评估时，可复用UnQover、BBQ、CrowS-Pairs这套偏见评测基准，替换为电商场景的刻板印象问答对即可'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM剪枝方法（如SparseGPT）可大幅降低推理开销、提升部署效率，但会放大模型原有偏见，压缩后模型对带人口属性提示的输出差异显著，严重影响生成内容公平性，尤其是电商、客服等面向C端的场景，偏见输出极易引发合规风险与用户不满，而现有剪枝方案普遍未考虑偏见缓解问题。

### 方法关键点
- 优化SparseGPT的剪枝目标，新增配对对比输入（如反刻板印象/刻板印象句子对）的表征差异约束，避免剪枝后两类输入的输出差距扩大
- 重构剪枝用Hessian矩阵，加入`2ΔXΔX⊤`项（ΔX为配对输入表征差），同时影响剪枝掩码选择和二阶权重更新，计算复杂度与原SparseGPT完全一致
- 支持半结构化（1:4、2:4）、非结构化等多种稀疏模式，兼容主流Transformer架构，可直接复用现有SparseGPT的工程管线

### 关键实验
在9个主流LLM（LLaMA3.1-8B、Qwen2.5-7B等）上测试，对比Magnitude Pruning、Wanda、SparseGPT基线：
1. 1:4半结构化稀疏下，LLaMA3.1-8B的UnQover偏见评测准确率从SparseGPT的35.60%提升至60.46%，MMLU零样本精度基本持平（59.76% vs 59.11%），推理吞吐量提升至2.65倍，CO2排放降低62%
2. 50%非结构化稀疏下，Qwen2.5-7B的UnQover准确率从78.35%提升至80.35%，DTO（公平性-性能权衡得分）降低0.009
3. 2:4高稀疏度下，补充通用对话校准数据后，Debias-SparseGPT的UnQover准确率比SparseGPT高4.8%，MMLU高0.33%

### 最值得记住的一句话
LLM剪枝时只要针对配对偏见输入调整二阶优化目标，就能在不增加推理开销、不损失通用性能的前提下，大幅降低压缩后的偏见放大问题。
