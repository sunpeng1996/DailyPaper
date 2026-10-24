---
title: Cost-Aware Abstention for LLM-Based IT Ticket Classification
title_zh: 面向LLM驱动IT工单分类的成本感知拒识评估方案
authors:
- Sachin Gupta
affiliations:
- Independent Researcher, United States
arxiv_id: '2610.31657'
url: https://arxiv.org/abs/2610.31657
pdf_url: https://arxiv.org/pdf/2610.31657
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: LLM文本分类 · 成本感知评估
tags:
- cost-aware abstention
- selective prediction
- LLM calibration
- text classification
- model evaluation
one_liner: 搭建成本感知拒识离线评估框架，对比LLM与传统分类器在IT工单分类的成本表现
practical_value: '- 电商客服/售后工单自动分类场景可直接复用该成本感知拒识框架，定义正确分类/人工审核/错分三类成本，在校准集优选阈值降低整体运营成本

  - LLM落地分类任务前可先对比传统分类器、微调小模型的成本收益，多数场景下微调小模型性价比远高于LLM少样本分类

  - 模型置信度校准不能仅看ECE指标，需同步验证AUROC、风险覆盖面积等区分度指标，避免校准后分类能力下降'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
IT工单自动分类错分成本远高于人工审核成本，现有方案缺乏成本导向的离线评估机制，无法平衡自动路由与人工审核的收益。
### 方法关键点
采用离线成本条件就绪评估框架，在校准集基于明确的错分/人工/正确分类成本选择路由阈值，冻结后直接在测试集验证；对比4种传统非LLM分类器、4种LLM零/少样本prompt方案的效果，除ECE外新增AUROC、风险覆盖面积等评估指标。
### 关键结果
在(0,1,5)成本模型下，TF-IDF+LR选择0.6阈值可降低38.1%测试成本，错分率从15.3%降至3.5%；16组成本参数实验中14组优于全路由/全人工策略；少样本prompt最强配置准确率0.477，远低于微调DistilBERT的0.879。
