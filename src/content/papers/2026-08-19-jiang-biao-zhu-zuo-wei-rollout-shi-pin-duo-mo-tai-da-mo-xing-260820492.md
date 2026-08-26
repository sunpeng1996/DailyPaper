---
title: 'Annotations as Rollouts: Efficient and Scalable Reinforcement Learning for
  Video MLLMs'
title_zh: 将标注作为Rollout：视频多模态大模型的高效可扩展强化学习方法
authors:
- Yunheng Li
- Guohong Mu
- Hao Li
- Shengsheng Qian
- Dingwen Zhang
- Qibin Hou
- Ming-Ming Cheng
affiliations:
- 南开大学
- 西北工业大学
- 中国科学院自动化研究所
- NKIARI 深圳
arxiv_id: '2608.20492'
url: https://arxiv.org/abs/2608.20492
pdf_url: https://arxiv.org/pdf/2608.20492
published: '2026-08-19'
collected: '2026-08-26'
category: Multimodal
direction: 多模态大模型 · 强化学习训练优化
tags:
- Multimodal LLM
- Reinforcement Learning
- Video Understanding
- GRPO
- Training Optimization
one_liner: 提出OraRL强化学习框架，将标注作为Oracle Rollout，解决视频MLLM训练优势反转问题，兼顾效率与性能
practical_value: '- RL训练时可直接将人工标注转化为Oracle Rollout加入训练组，无需依赖CoT生成高质量正样本，降低标注到训练的转化成本，适配生成式推荐、多模态Agent等场景的LLM对齐任务

  - 遇到高奖励样本拉高组基线导致的优势反转问题，可复用OraRL的解耦优势估计方案：基线仅用策略生成样本计算，Oracle单独作为detached优化目标，避免抑制优质探索样本

  - 大模型RL训练加速可采用符号平衡剪枝策略：保留Oracle和正负优势的Top样本，配合选择后矩校正，仅损失不到1%精度即可获得1.48x训练提速，降低训练成本

  - 结构化输出任务（如推荐理由生成、商品属性标注）的RL训练无需引入CoT，直接用答案标注做Oracle即可同时提升精度和推理速度，比带CoT的GRPO推理速度快36倍'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有视频MLLM的RL后训练（如GRPO）依赖策略生成的On-policy Rollout，很少能产出接近标注精度的高质量正样本，引入CoT又会大幅增加训练和推理成本；直接把标注加入Rollout组会拉高组奖励基线，导致原本的正优势样本被判定为负（优势反转问题），反而抑制模型探索，性能下降。

### 方法关键点
- Annotation-as-rollout机制：将任务标注序列化为模型输出格式的Oracle Rollout，加入On-policy组作为可靠正优化目标，无需依赖CoT
- 解耦优势估计：基线仅用On-policy样本的奖励均值计算，避免Oracle拉高基线导致优势反转；Oracle与策略的奖励gap拆分为定向增益（放大高于均值的On-policy样本优势）和独立的Oracle优势（随gap缩小自适应衰减权重）
- 符号平衡剪枝：保留Oracle+正负优势的Top样本，配合剪枝后矩校正，保证优势分布无偏，获得1.48x训练提速

### 关键结果
- 训练效率：仅需SFT 2.2倍step时间，比带CoT的GRPO快1倍以上；推理无需CoT，单步解码130ms，比带CoT基线快36倍
- 性能：Video-ORA-9B在7类视频任务上SOTA，时序mIoU从62.5提至66.0，跟踪AO从73.0提至78.2，分割指标从64.3提至70.4；VSI-Bench得分73.1，远超GPT-5的55.0和Gemini-3-Pro的55.1
- 扩展性：0.8B到9B参数规模、100k以内数据量下均稳定优于GRPO和SFT

### 核心结论
标注不只是奖励打分的参考，更可以直接作为RL训练的正样本Rollout，通过解耦优势估计即可避免副作用，大幅提升RL训练的效率和上限
