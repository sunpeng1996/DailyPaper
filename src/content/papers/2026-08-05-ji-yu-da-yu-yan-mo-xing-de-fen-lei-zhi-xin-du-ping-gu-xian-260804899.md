---
title: Evaluation Pitfalls and Sparsity Limitations in LLM-based Confidence Estimates
  for Classification
title_zh: 基于大语言模型的分类置信度评估陷阱与稀疏性限制
authors:
- Elena Merdjanovska
- Omar Zaidan
- Andreas Rücklé
affiliations:
- Humboldt-Universität zu Berlin
- Science of Intelligence
- Amazon
arxiv_id: '2608.04899'
url: https://arxiv.org/abs/2608.04899
pdf_url: https://arxiv.org/pdf/2608.04899
published: '2026-08-05'
collected: '2026-08-06'
category: Eval
direction: LLM分类置信度评估优化
tags:
- Confidence Estimation
- AUARC
- LLM Evaluation
- Verbalization
- Selective Prediction
one_liner: 提出AUARC阶梯插值评估标准，以及无额外推理成本的verbalization logprobs方法解决置信度稀疏问题
practical_value: '- 电商内容审核、LLM分类打标场景可直接复用verbalization logprobs方法，无额外推理成本即可提升置信度区分度

  - 做选择性预测（低置信样本转人工审核）的AUARC评估统一用阶梯插值，避免评估结果失真导致的方法选型错误

  - 遇到LLM生成置信度数值过于集中的稀疏问题，可直接采用按token概率加权生成数值的思路优化，无需重新训练模型'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM在分类任务（如内容审核、自动打标）中的置信度估计是风险控制核心，现有verbalization类方法输出极度稀疏，置信度区分度差；且AUARC评估插值标准不统一，会完全改变方法排名，无法公平对比。
### 方法关键点
1. 标准化AUARC评估采用阶梯插值，避免稀疏置信度下的评估偏差；
2. 提出verbalization logprobs方法，将LLM输出的置信度数字按每个token的生成概率加权得到最终置信度，无额外推理成本。
### 关键结果
Qwen3-32B在SST-2数据集上原生verbalization仅输出8种唯一置信值，超一半样本集中在95%；verbalization logprobs相比原生方法AUARC提升2.3个点，为当前最优方案。
