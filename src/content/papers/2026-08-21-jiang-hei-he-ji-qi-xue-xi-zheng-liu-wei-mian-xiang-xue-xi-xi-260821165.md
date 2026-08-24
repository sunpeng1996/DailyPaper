---
title: Distilling Black-Box Machine Learning into a Small, Self-Explaining Language
  Model for Learning Analytics
title_zh: 将黑盒机器学习蒸馏为面向学习分析的小型自解释大语言模型
authors:
- Chenguang Pan
- Airui Meng
- Youmi Suk
affiliations:
- Department of Human Development, Teachers College Columbia University
arxiv_id: '2608.21165'
url: https://arxiv.org/abs/2608.21165
pdf_url: https://arxiv.org/pdf/2608.21165
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: LLM蒸馏 · 自解释模型落地
tags:
- Knowledge Distillation
- Fine-tuning
- Model Interpretability
- Small LLM
- Explainable AI
one_liner: 提出两阶段微调蒸馏流水线，将黑盒模型及其解释蒸馏为可本地部署的小参数自解释LLM，配套忠实度评估框架
practical_value: '- 可复用两阶段蒸馏思路：将业务侧已有的黑盒推荐/排序模型及其SHAP/LIME事后解释蒸馏为小参数LLM，实现预测+自然语言解释一体化输出，降低部署门槛

  - 可借鉴忠实度优先的评估框架：针对LLM生成的推荐理由，与原模型归因结果做一致性校验，规避生成式解释的幻觉问题，适配电商场景下给运营/用户的解释生成验证

  - 小参数蒸馏后的LLM可离线部署在普通硬件上，适合对数据隐私要求高的场景（如用户本地个性化推荐），避免敏感用户行为数据外传'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
学习分析领域落地黑盒ML模型时，存在可解释性不足、部署成本高、数据隐私风险三大痛点，难以适配实际业务需求。
### 方法关键点
1. 提出 estimator 无关的两阶段微调蒸馏流水线，将任意训练完成的黑盒预测模型及其事后归因解释（导师）蒸馏为小参数开源LLM（学员），可同时输出单样本预测结果与自然语言解释
2. 配套忠实度优先的评估框架，可审计每一条生成解释与其声称的归因结果的一致性，规避解释幻觉
### 关键结果
- 20亿参数LLM基于Oracle信号蒸馏时，效果面恢复相关系数r>0.90，重要变量排序100%准确，无虚假协变量引用
- 真实数据集上98.8%的生成解释通过一致性审计，无捏造数值，蒸馏后模型可在普通消费级笔记本离线运行，数据无需出域
- 验证了LLM解释的流畅度与正确性无关，类别严重不平衡场景下决策质量会向多数类偏移
