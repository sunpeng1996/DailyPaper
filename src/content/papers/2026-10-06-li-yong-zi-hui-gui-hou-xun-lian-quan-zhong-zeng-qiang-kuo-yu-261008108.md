---
title: Enhancing Diffusion Language Models with Autoregressive Post-Training Weights
title_zh: 利用自回归后训练权重增强扩散语言模型的无训练A2D框架
authors:
- Yiming Qin
- Ke Wang
- Amel Abdelraheem
- Adam Hazimeh
- Pascal Frossard
affiliations:
- EPFL, Lausanne, Switzerland
arxiv_id: '2610.08108'
url: https://arxiv.org/abs/2610.08108
pdf_url: https://arxiv.org/pdf/2610.08108
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: 大模型权重融合 · AR到扩散跨范式迁移
tags:
- Diffusion LLM
- Model Merging
- Task Vector
- Cross Paradigm Transfer
- Autoregressive Model
one_liner: 提出无需训练的A2D框架，复用AR后训练权重直接增强扩散大语言模型性能
practical_value: '- 业务中若使用扩散大语言模型做商品文案、营销话术生成，可直接复用同基座AR模型的SFT/RL后训练task vector做增强，无需额外训练扩散模型，大幅降低适配成本

  - 已完成专属业务场景后训练的扩散模型，可通过A2D Merge做AR与扩散task vector插值，平均可提3-4个点的下游任务效果，且无推理耗时增加

  - 跨范式任务向量迁移思路可复用至生成式推荐场景：将AR基座的用户偏好对齐权重迁移至同底座的扩散生成推荐模型，快速适配个性化生成需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前扩散大语言模型（dLLM）大多从预训练自回归（AR）模型初始化后转换得到，但转换后完全丢弃了AR生态成熟的后训练权重资源，dLLM单独做后训练优化难度高、成本大，如何复用已有AR后训练能力增强dLLM是高价值问题。

### 方法关键点
- 提出A2D无训练框架，分为两种模式：1）A2D Transfer：直接将AR模型的后训练task向量（后训练权重减基座权重）按系数α加到dLLM基座权重上，快速赋予dLLM对应能力；2）A2D Merge：当已有dLLM后训练权重时，将AR task向量与dLLM自身task向量做插值融合，进一步提升效果
- 核心发现：AR与dLLM的后训练task向量在参数空间几乎正交，但在表征空间的变化高度对齐，二者能力互补，插值可同时保留两方增益

### 关键结果
在Dream、DiffuCoder、DiffusionGemma等6类主流dLLM上验证，覆盖指令跟随、数学推理、代码生成、医疗VQA等场景：A2D Transfer可直接将dLLM基座在MATH-500上提19.4个点，AIME24上提15.4个点，VQA-RAD上提16.7个点，效果接近直接做dLLM后训练；A2D Merge可在已后训练的dLLM基础上进一步提升，AIME25提10.4个点，HumanEval+提6.7个点，所有9个测试基准全量提升，无推理开销。

最值得记住的一句话：同基座来源的AR后训练权重可直接跨范式迁移到扩散模型复用，无需额外训练即可获得显著性能增益。
