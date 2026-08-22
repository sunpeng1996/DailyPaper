---
title: Explainable Transformer Models for Clinical Prediction Tasks on Structured
  Electronic Health Records
title_zh: 面向结构化电子健康记录临床预测任务的可解释Transformer模型
authors:
- Jun Ni Du
- Lukas Adamek
- Maxim Kryukov
- Flavio Dormont
- Ziv Bar-Joseph
- Sven Jager
- Brandon Rufino
affiliations:
- Sanofi
- Carnegie Mellon University
arxiv_id: '2608.20315'
url: https://arxiv.org/abs/2608.20315
pdf_url: https://arxiv.org/pdf/2608.20315
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 医疗EHR建模 · 可解释Transformer
tags:
- Transformer
- Interpretability
- EHR Modeling
- Clinical Prediction
- BERT Fine-tuning
one_liner: 提出融合百分位分箱数值表征与积分梯度可解释性的BERT-LER，EHR临床预测性能优于公开基准
practical_value: '- 结构化连续特征离散化可借鉴百分位分箱方案，将用户行为、商品价格等连续特征转离散token喂入LLM/Transformer类推荐模型，保留梯度信息

  - 对生成式推荐/搜索排序的可解释性需求，可复用Integrated Gradients做token级归因，定位影响预测结果的核心用户行为/Item特征

  - 多场景迁移验证思路可复用，新模型上线前除标准任务benchmark，额外加垂直业务场景（如大促、下沉市场）验证泛化性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有结构化电子健康记录（EHR）预测模型极少同时兼顾实验室定量信息保留与输入医疗事件的可解释性，EHR基础建模存在实验室数值表征和可解释性未统一的方法缺口。
### 方法关键点
提出BERT-LER预训练微调框架，基于7500万去标识化患者EHR数据训练：通过百分位分箱将实验室检测结果编码为离散token的同时保留分级信息，搭配Integrated Gradients实现输入EHR序列的token级归因。
### 关键结果
在公开EHRShot基准套件与真实哮喘严重程度进展任务上，预测性能与公开基准相当，实验室相关任务性能普遍超出基准，归因结果与临床已知风险因子高度对齐。
