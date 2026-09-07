---
title: 'Don''t Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training
  and Inference'
title_zh: 别弃用Dropout：优化层稀疏性实现高效LLM训练与推理
authors:
- Mostafa Elhoushi
- Alex Pretko
- Nolan Dey
- Bin Claire Zhang
- Gavia Gray
- Gurpreet Gosal
- Abdulrahman Mahmoud
- Shane Bergsma
- Joel Hestness
affiliations:
- Cerebras Systems
- MBZUAI
arxiv_id: '2609.05275'
url: https://arxiv.org/abs/2609.05275
pdf_url: https://arxiv.org/pdf/2609.05275
published: '2026-09-03'
collected: '2026-09-07'
category: Training
direction: 大语言模型 · 训练推理效率优化
tags:
- Layer Dropout
- LLM Efficiency
- Training Optimization
- Inference Acceleration
- Stochastic Depth
one_liner: 通过最优层dropout配置实现LLM训练FLOPs减25%、推理提速1.5倍且精度损失可忽略
practical_value: '- 训练电商垂域LLM（商品理解、用户意图识别、Agent决策模型）时，直接复用论文的层dropout最优配置，无需修改模型架构即可节省25%训练FLOPs，降低预训练/微调成本

  - 部署LLM驱动的推荐/Agent服务时，基于层dropout预训练的模型可动态调整推理深度：大促流量高峰时开启早停/层跳过，最高提速1.5倍，精度损失可忽略

  - 需多规格LLM部署时，无需单独训练不同参数量的模型，单个大模型通过剪层即可得到适配不同算力场景的小模型，精度优于同规模独立训练的基线，降低多模型维护成本

  - 微调垂域小模型时，直接套用论文超参规则：缩放因子rtrain=1/ρ、逐层递增dropout率+随步递减调度、序列粒度dropout，无需大量ablation即可获得训练加速效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM预训练算力成本极高，层dropout（随机深度）可带来结构化稀疏算力节省、天然赋予模型推理深度弹性，但长期被认为会损伤精度，被主流大模型训练流程弃用，且缺乏大规模场景下的系统性最优配置验证。

### 方法关键点
- 超参配置：确定缩放因子rtrain=1/ρ、reval=1，实现超参在不同dropout率下的可迁移，无需逐率调参
- 粒度选择：优先按完整Transformer层做dropout、按序列粒度生成掩码，精度优于子层/按批次dropout
- 分布与调度：采用逐层递增的dropout分布（底层率为0，顶层到pmax），搭配随训练步从pmax线性降到0的递减调度，相同FLOPs下精度最优
- 推理适配：训练后的模型无需修改主干权重，天然支持零样本早停、中间层跳过、自投机解码等加速方案

### 关键结果
实验覆盖271M~8.2B参数模型，最高160B tokens训练数据，共2400+组对照实验，对比无dropout的标准预训练基线：相同训练步数下最高节省25%训练FLOPs，验证集损失持平甚至更优；推理侧自投机解码最高提速1.5×，精度损失可忽略；动态剪层后精度衰减远优于基线。

最值得记住的一句话：配置得当的层dropout可同时实现LLM训练降本、推理提效，完全可纳入现代大模型预训练标准流程
