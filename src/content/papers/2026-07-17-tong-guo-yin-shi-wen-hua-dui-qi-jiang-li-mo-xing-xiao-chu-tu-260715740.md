---
title: Debiasing Text-to-Image Evaluation via Implicit Cultural Alignment Reward Modeling
title_zh: 通过隐式文化对齐奖励模型消除文生图评估偏差
authors:
- Bo-An Chang
- Yu-Chih Chen
affiliations:
- National Tsing Hua University
- National Yang Ming Chiao Tung University
arxiv_id: '2607.15740'
url: https://arxiv.org/abs/2607.15740
pdf_url: https://arxiv.org/pdf/2607.15740
published: '2026-07-17'
collected: '2026-07-20'
category: Eval
direction: 多模态评估 · 文化对齐奖励建模
tags:
- Reward Model
- Multimodal LLM
- Text-to-Image Evaluation
- Cultural Alignment
- Cross-Attention
one_liner: 提出基于4.2B轻量化MLLM的隐式文化对齐奖励模型，解决文生图评估的文化偏差与效率问题
practical_value: '- 电商营销素材/商品AI生成场景可复用SkipCA机制，优化文化适配性评估效率，避免生成内容出现地域/文化冒犯问题

  - 构建RLHF/DPO偏好优化的奖励模型时，可借鉴绕过自回归生成直接输出标量奖励的设计，实现10倍级推理提速，适配大规模在线评估场景

  - 针对隐式语义（如地域偏好、文化习俗）的识别任务，可复用「隐式探针+跨层注意力关联早期特征」的架构，减少细粒度特征丢失'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有文生图（T2I）评估指标与多模态评判器依赖的视觉语义表征对隐式文化规范覆盖不足，易产生偏好判断偏差、遗漏细粒度文化线索；基于VQA的评估器依赖自回归文本生成，实时奖励建模可扩展性差，难以适配大规模生产场景。
### 方法关键点
基于4.2B参数轻量化MLLM构建隐式文化对齐奖励模型，集成隐式文化探针与Skip-connection Cross-Attention（SkipCA）机制，允许后期语义特征直接关联早期视觉表征，更好保留文化相关显著性细节；绕过自回归文本生成流程，直接输出标量奖励信号。
### 关键结果
在CulturalFrames基准3323组标注难例图像对测试中，pairwise准确率达80.54%，Pearson、Kendall相关系数分别为0.546、0.377，全面优于现有视觉语言指标与MLLM评估器；本地推理单样本耗时仅0.21s，相比标准VQA评估器速度提升10倍，可直接对接RLHF、DPO等偏好优化pipeline。
