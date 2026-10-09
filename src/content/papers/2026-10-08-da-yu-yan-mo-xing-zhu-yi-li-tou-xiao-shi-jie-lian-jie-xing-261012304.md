---
title: 'Looking Inside LLMs: Small-World Connectivity as a Signature of Reasoning
  Performance'
title_zh: 大语言模型注意力头小世界连接性是推理性能的结构标志
authors:
- Zheng Huang
- Sansheng Cao
- Enpei Zhang
- Weikang Qiu
- Elynn Chen
- Xiang Zhang
- Yaoqing Yang
- Rex Ying
- Dawei Zhou
- Yujun Yan
affiliations:
- Dartmouth College
- Yale University
- New York University
- UNC Charlotte
- Virginia Tech
arxiv_id: '2610.12304'
url: https://arxiv.org/abs/2610.12304
pdf_url: https://arxiv.org/pdf/2610.12304
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: LLM推理性能结构指标与剪枝优化
tags:
- Small-World Network
- LLM Pruning
- Reasoning Performance
- Attention Head
- Model Compression
one_liner: 发现LLM注意力头功能网络小世界指数与推理性能正相关，提出SWA剪枝较基线最多降20%困惑度
practical_value: '- 电商导购Agent、推荐系统侧LLM模块轻量化部署时，可复用SWA剪枝策略，优先保留高core、低bridge分数的注意力头，70%稀疏度下仍能大幅降低推理延迟且保留核心性能

  - 评估自研/微调LLM推理能力时，可新增小世界指数（SWI）作为结构层面的辅助评估指标，无需跑全量业务benchmark即可快速筛选推理性能更优的模型checkpoint

  - 垂直领域LLM（如电商客服、文案生成LLM）微调过程中，可监控SWI变化，当SWI不再提升时提前停止训练，降低训练成本同时保证推理能力达标'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM推理能力评估仅依赖行为层面的benchmark指标，缺乏内部结构层面的可量化参考，难以解释模型推理能力差异的本质原因，也无法为模型压缩、训练优化等工程任务提供结构层面的指导。受神经科学中大脑功能网络小世界组织特性与人类智商正相关的发现启发，探索LLM内部注意力头的连接结构与推理性能的关联。
### 方法关键点
- 构建注意力头功能图：以Transformer各层注意力头为节点，基于SVCCA的Fisher z变换变体计算头之间的激活相似度作为边权重，固定边密度阈值生成无向功能图
- 量化小世界指数（SWI）：通过图的平均聚类系数、全局效率与同度随机图的对应指标比值计算SWI，衡量网络小世界特性强度
- 提出SWA分层剪枝策略：基于社区检测计算每个头的core分数（社区内连接权重占比）和bridge分数（跨社区连接分散程度），优先为高core、低bridge的头和对应层分配更低的稀疏度
### 关键实验
在6个开源LLM（Qwen3 1B/4B/8B/14B、Llama3/3.2系列）上验证：跨模型和训练checkpoint，SWI与DRE-Bench推理性能负相关（NLL越低、SWI越高）；SWA剪枝对比SparseGPT、Wanda、FARMS等基线，在50%/70%稀疏度下，WikiText困惑度最高降低20%，零样本任务准确率最高提升5pp，且使用GSM8K、ARC-C、MMLU等不同数据集构建功能图时均有稳定收益。
### 核心结论
LLM的推理性能不仅体现在外部行为指标上，也可通过内部注意力头功能网络的小世界结构特性来量化和优化。
