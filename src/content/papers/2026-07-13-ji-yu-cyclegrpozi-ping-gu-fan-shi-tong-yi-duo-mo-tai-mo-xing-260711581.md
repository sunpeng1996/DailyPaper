---
title: 'Actor as Its Own Critic: Unifying Region Understanding and Localization via
  CycleGRPO'
title_zh: 基于CycleGRPO自评估范式 统一多模态模型区域理解与定位
authors:
- Xin Zhang
- Haochen Wang
- Yikang Zhou
- Jason Li
- Robby T. Tan
affiliations:
- National University of Singapore
- University of Chinese Academy of Sciences
- Nanyang Technological University
- Wuhan University
arxiv_id: '2607.11581'
url: https://arxiv.org/abs/2607.11581
pdf_url: https://arxiv.org/pdf/2607.11581
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态大模型 · 自监督循环强化学习
tags:
- MLLM
- GRPO
- Cycle Consistency
- Region Understanding
- Visual Grounding
- Reinforcement Learning
one_liner: 提出无需文本标注的CycleGRPO框架，通过空间-语义循环一致性同时优化多模态模型区域理解与定位能力
practical_value: '- 电商商品多模态标注场景可复用该自监督循环范式，仅需商品图+目标区域mask/bbox即可生成高精度属性文本，无需人工标注，大幅降低标注成本

  - 多模态商品搜索语义对齐任务可借鉴「query→商品区域→query」闭环优化逻辑，提升query与商品细粒度属性的匹配精度，减少语义偏差

  - 生成式商品文案优化可新增「生成文案→回溯商品区域」一致性校验环节，用IoU类空间匹配信号作为RL奖励，显著降低文案幻觉

  - 多模态RL训练可直接复用G=K=6的GRPO组采样超参配置，平衡性能与计算成本，相比传统PPO降低显存开销'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多模态大模型的区域理解和定位任务通常分开优化，极度依赖高成本的人工标注文本-区域配对数据，外部LLM-as-judge的奖励存在reward hacking风险，难以规模化训练细粒度多模态感知能力。

### 方法关键点
- 基于区域理解和定位的对偶性，构建「区域→文本→区域」的自评估闭环，无需文本标注和外部评判模型，单个MLLM同时扮演actor（生成区域描述）和critic（将生成文本回溯定位到空间区域）两个角色
- 基于SAMTok的离散掩码统一表示，将定位任务转化为自回归token预测任务，实现两类任务在同一概率空间建模，无需任务特定头
- 设计质量感知的token级循环一致性奖励，用输入区域与回溯预测区域的IoU作为核心奖励信号，同时优化描述的语义判别性和定位的准确性
- 基于GRPO优化策略，无需参数化价值网络，显著降低训练显存开销

### 关键结果
基于SAMTok（Qwen3-VL-4B backbone）训练，无需任务特定微调，在多个基准上取得显著提升：GRES数据集平均gIoU较基线提升7.0%，GroundingSuite整体定位准确率从57.5%提升至67.6%，DLC-Bench平均得分提升5.8%，GCG基准CIDEr得分提升6.5，性能超过GPT-4o、Gemini 2.5 Pro等闭源模型，同时适用于掩码、bounding box等多种空间表示形式。

**最值得记住的一句话**：对于存在对偶关系的任务，利用任务间的闭环一致性构造自监督奖励信号，可在无人工标注的条件下同时实现两类任务的性能提升，是低成本规模化模型能力的有效路径。
