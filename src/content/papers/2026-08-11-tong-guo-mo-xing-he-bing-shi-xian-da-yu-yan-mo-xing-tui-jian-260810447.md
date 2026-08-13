---
title: Towards Efficient Reasoning in LLM-Based Recommender Systems via Model Merging
title_zh: 《通过模型合并实现大语言模型推荐系统的高效推理》
authors:
- Linh Dieu Le
- Tong Chen
- Shazia Sadiq
- Hongzhi Yin
- Ming Jin
- Junliang Yu
affiliations:
- The University of Queensland
- Griffith University
arxiv_id: '2608.10447'
url: https://arxiv.org/abs/2608.10447
pdf_url: https://arxiv.org/pdf/2608.10447
published: '2026-08-11'
collected: '2026-08-12'
category: GenRec
direction: 生成式推荐 · 推理效率优化
tags:
- LLM4Rec
- Model Merging
- Chain-of-Thought
- Reasoning Compression
- Attention Head
one_liner: 提出推理头感知合并框架REAM，训练-free压缩LLM推荐的CoT推理长度同时维持精度
practical_value: '- 业务侧已上线带CoT推理的LLM推荐服务的，可直接用REAM框架做训练-free的推理压缩，无需重新标注数据或微调，上线周期短，推理成本最高可降24%，同时精度无损失

  - 多能力模型合并的系数设计可复用该思路：按attention head粒度分配权重，核心衡量「功能重要性」和「参数扰动敏感度」两个维度，避免破坏核心能力

  - 工程实现可直接复用两个trick：①冻结最后6层FFN不参与合并，能避免输出层扰动导致的精度下降，无需大量调参；②仅需500条历史正确推理样本作为校准集，即可计算头重要性与敏感度，数据成本极低

  - 针对大模型推理成本高的场景，合并快慢模型的思路可推广到其他Agent场景：把擅长复杂推理的大模型和擅长快速响应的小模型合并，兼顾能力和效率'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
带CoT推理的慢思考LLM推荐系统精度优于直接预测的快思考模型，但冗长的推理链会大幅提升推理延迟与计算成本，而现有推理压缩方案要么需要额外训练（适配成本高），要么推理时动态截断（效果不稳定）。通用模型合并方案采用全局或层粒度的统一系数，容易破坏推荐所需的核心推理能力，无法兼顾精度与效率。
### 方法关键点
- 提出REAM（推理头感知合并）框架，训练-free实现推理压缩：以慢思考推荐模型为基底，选择性注入快思考模型的简洁生成能力，合并粒度细至单个attention head，适配推荐推理的异质性分布
- 每个头的合并系数由三个信号联合计算：①检索关键度：衡量头从上下文召回用户/物品匹配证据的能力；②决策忠实度：衡量头在评分阶段对匹配推理段的注意力占比；③更新敏感度：衡量头参数被修改后对推荐损失的影响程度
- 采用带约束的优化分配系数，最大化快思考能力迁移的同时限制总扰动风险；冻结最后几层FFN不合并，避免破坏推理到评分的映射关系
### 关键结果
在Yelp、Amazon Book、Amazon Music三个公开推荐数据集上，对比8种主流模型合并基线：
- 推理长度最高降低24.3%，同时MAE最高降低4.7%，RMSE最高降低3.7%，在所有数据集上均维持甚至超越原慢思考模型的推荐精度
- 对比层粒度合并基线，推理长度最多短45.4token，MAE最多低0.0594，精度-效率trade-off显著更优
### 核心结论
LLM推荐的推理压缩无需重新训练，基于头功能异质性的细粒度模型合并可以同时实现精度提升与推理成本下降。
