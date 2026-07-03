---
title: Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation
title_zh: 面向无标注LLM自蒸馏的神经元感知数据选择方法
authors:
- Zhuowei Chen
- Xiang Lorraine Li
affiliations:
- University of Pittsburgh, United States
arxiv_id: '2607.02460'
url: https://arxiv.org/abs/2607.02460
pdf_url: https://arxiv.org/pdf/2607.02460
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: LLM无标注自蒸馏 · 神经元激活信号利用
tags:
- Self-Distillation
- Neuron Activation
- Annotation-Free Training
- On-Policy Distillation
- Data Selection
one_liner: 利用LLM内部神经元激活信号指导无标注自蒸馏的数据选择与上下文构建，兼顾效果与泛化校准
practical_value: '- 垂域LLM（电商客服、商品属性打标、搜索query理解）微调时，可复用神经元激活数与答案正确率的强相关性，无需标注即可过滤高幻觉训练样本，降低标注成本

  - 基于神经元激活Jaccard相似度做few-shot样例检索，在推理多样性高的垂域效果优于随机检索，可用于RAG样例召回、Agent工具调用上下文构建场景

  - 无标注自蒸馏时采用reverse KL+EMA教师更新的on-policy蒸馏范式，比传统SFT/GRPO类方法更能避免跨域效果下降与校准误差膨胀，适合缺标注的垂域模型迭代'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
垂域LLM微调通常需要昂贵的专家标注，现有无标注自进化方法要么存在跨域性能退化，要么校准误差过高，同时传统基于表面指标（如熵、多数投票）的训练数据筛选不够可靠，无法解决自蒸馏中自我强化幻觉的问题。

### 方法关键点
- 神经元共识数据选择：统计每个样本零-shot推理时的激活神经元数量，激活数越少代表模型共识越高、hallucination概率越低，筛选底部20%低激活样本作为训练集，兼顾信号可靠性和提升空间
- 神经元重叠上下文构建：基于激活神经元集合的Jaccard距离为每个查询检索推理模式最相似的K个样例作为few-shot上下文，构建更可靠的教师模型分布
- 训练范式：采用on-policy reverse KL蒸馏，教师模型为学生模型的EMA滑动平均版本，全程无需人工标注

### 关键实验
在SciKnowEval（4个科学领域）、Edu-Feedback、MMLU-Pro三个数据集上，对比LMSI、TTRL、Intuitor等基线，域内Avg@8最高提升2.93个点，跨域Avg@8平均提升0.9个点，整体ECE降低0.008，同时避免了GRPO类方法的校准膨胀问题。

**最值得记住的一句话**：无标注自蒸馏的核心是在「样本可靠性」和「提升空间」之间找平衡，LLM内部神经元信号比表面输出指标能提供更可靠的无标注筛选依据。
