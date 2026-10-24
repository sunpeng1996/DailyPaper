---
title: 'Different Tasks, Different Timesteps: Temporal Task-Aware Quantization for
  Diffusion Language Models'
title_zh: 面向扩散语言模型的任务与时序感知混合精度量化框架
authors:
- Ofek Avivi
- Eliron Rahimi
- Avi Mendelson
- Chaim Baskin
affiliations:
- Technion – Israel Institute of Technology
- INSIGHT Lab, Ben-Gurion University of the Negev
arxiv_id: '2610.31198'
url: https://arxiv.org/abs/2610.31198
pdf_url: https://arxiv.org/pdf/2610.31198
published: '2026-10-21'
collected: '2026-10-24'
category: LLM
direction: 扩散语言模型 · 混合精度量化推理优化
tags:
- Diffusion Language Model
- Quantization
- Mixed Precision
- Inference Optimization
- Temporal Awareness
one_liner: 提出无标注驱动的任务与时序感知混合精度量化框架T2Quant，同等位宽下DLM精度最高提升6.7个百分点
practical_value: '- 生成式推荐/Agent场景用DLM做商品文案、营销内容生成时，可复用T2Quant的时序敏感度分配逻辑，在固定推理成本下提升生成质量

  - 无标注敏感度信号的思路可迁移到LLM4Rec类模型的量化优化，无需额外标注即可适配不同推荐任务的精度需求

  - 迭代式生成模型（如扩散类图生文、多轮交互Agent）的推理优化，可借鉴按生成步骤动态分配精度的trick，降低显存占用与latency'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
Diffusion Language Models（DLMs）依赖迭代多步去噪生成文本，推理开销远高于自回归LLM；现有量化方法多针对自回归模型设计，未考虑DLM不同任务、不同去噪步骤的精度需求差异，量化后精度损失严重。
### 方法关键点
1. 验证DLM量化敏感度同时关联下游任务类型与去噪时序，且该敏感度模式可通过无标注信号预测，无需真值标签或任务专属评估指标
2. 提出T²Quant任务时序感知混合精度量化框架，基于无标注敏感度信号，在固定位宽预算下为不同去噪步骤最优分配激活精度
### 关键结果
在3款DLM、6个基准测试集上验证，相比现有量化方法精度稳定提升，同等位宽预算下最高可获得6.7个百分点的精度增益
