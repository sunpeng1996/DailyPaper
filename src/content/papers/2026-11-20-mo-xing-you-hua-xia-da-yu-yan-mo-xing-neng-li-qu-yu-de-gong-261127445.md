---
title: 'Structurally Different, Functionally Persistent: Capability Regions Under
  Model Optimization'
title_zh: 模型优化下大语言模型能力区域的功能持久性与参数重叠特性研究
authors:
- Jiwoo Kum
- Chanwoo Kim
- Doyun Kim
- Seonghyeon Cho
- Sihyeon Lee
- Chanjun Park
affiliations:
- Soongsil University
arxiv_id: '2611.27445'
url: https://arxiv.org/abs/2611.27445
pdf_url: https://arxiv.org/pdf/2611.27445
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM能力区域 · 模型优化鲁棒性
tags:
- LLM
- Capability Localization
- Quantization
- Pruning
- LoRA
- Model Editing
one_liner: 发现LLM能力区域在量化/剪枝/LoRA优化后参数重构但仍为有效干预靶点
practical_value: '- 部署LLM时无需因量化/剪枝优化重新定位能力区域，原始定位的区域仍可直接用于能力干预，降低算力开销

  - 做领域LoRA适配（如电商导购、内容推荐领域微调）时，原模型的安全合规、特定能力抑制等干预方案可直接复用，无需重新提取区域

  - 落地模型编辑需求时无需过度关注能力区域的参数重叠率，以功能有效性为核心判断标准即可，大幅降低工程复杂度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM能力定位研究均基于原始权重模型验证，但实际部署的模型普遍会经过量化、剪枝、LoRA等优化操作，优化后原有能力区域是否仍可作为有效干预靶点尚不明确，直接影响模型编辑、能力抑制等方案的落地可行性。

### 方法关键点
- 测试对象覆盖3款主流指令微调LLM：Llama-3.1-8B-Instruct、Mistral-7B-Instruct-v0.3、Llama-3.2-3B-Instruct
- 评估7种常见优化方案：4种部署优化（RTN、AWQ、GPTQ 4bit量化；30%稀疏度的Magnitude、Wanda、SparseGPT剪枝）+ LoRA参数高效适配
- 定义两个核心评估维度：功能持久性（原区域在优化模型上消融后是否仍能消除目标能力）、参数重叠率（优化前后能力区域的参数重合比例）
- 设计量级匹配的对照组，排除消融参数数量、参数大小对结果的干扰

### 关键结果
- 实验数据集：HumanEval（编码能力）、HellaSwag（常识推理）、GSM8K（数学推理）、WikiText-2（语言建模）
- 20/21的优化场景下，消融原始能力区域可将编码性能降至0或接近0，而量级匹配对照组的编码性能保留率均超60%
- 优化后能力区域的参数重叠率中位数仅60%，最低仅22.4%，重叠率与功能持久性无相关性
- 原区域与优化后区域的共享参数子集贡献了绝大多数消融效果，20/21场景下共享子集消融对性能的影响显著高于独有子集

### 核心结论
LLM能力区域的干预有效性与参数结构是完全解耦的，功能持久性远高于结构一致性
