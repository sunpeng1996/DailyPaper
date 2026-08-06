---
title: 'CAPEval: A Decoupled Caption Evaluation across Understanding and Generation'
title_zh: CAPEval：面向理解与生成任务的解耦式图像描述评估框架
authors:
- Zhipeng Liu
- Haochen Wang
- Zhaoxiang Zhang
affiliations:
- University of Chinese Academy of Sciences
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2608.02589'
url: https://arxiv.org/abs/2608.02589
pdf_url: https://arxiv.org/pdf/2608.02589
published: '2026-08-02'
collected: '2026-08-06'
category: Eval
direction: 多模态评估 · 图像描述质量解耦评估
tags:
- Multimodal
- Caption Evaluation
- Benchmark
- Coverage
- Precision
one_liner: 提出将图像描述质量拆解为覆盖率与准确率的解耦评估基准CAPEval，为下游任务选型提供指引
practical_value: '- 电商商品图文生成、多模态检索场景可复用Coverage/Precision双维度评估范式，替代单一评分，更精准对齐业务目标

  - 下游任务选型可直接复用论文结论：理解类任务（如多模态召回、商品标签抽取）优先选高Coverage的caption生成器，生成类任务（如商品文案、AI作图）优先选高Precision模型

  - 构建电商多模态训练数据集时，可参考CAPEval的原子校验项设计标注流程，降低标注误差，提升数据对齐度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像描述（caption）评估采用单一标量评分，混淆了信息覆盖度和事实准确性两个核心属性，无法适配多模态理解、文生图两类不同下游任务的差异化评估需求。
### 方法关键点
1. 提出CAPEval解耦评估基准，将caption质量拆解为两个独立维度：Coverage（覆盖真实事实内容的完整度）、Precision（所有表述的事实准确率）；
2. 配套人工撰写的ground-truth caption和人工校验的原子检查项，实现细粒度的质量诊断。
### 关键结果
在4类模型家族共10个caption生成器的受控实验中验证：Coverage与理解类任务性能相关性更强，Precision对生成类任务性能的预测度更高，两类指标的任务适配性差异稳定。
