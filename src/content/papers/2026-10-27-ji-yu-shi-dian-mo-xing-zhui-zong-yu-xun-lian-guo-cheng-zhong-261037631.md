---
title: What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time
  Models
title_zh: 基于时点模型追踪预训练过程中不同类型知识的获取规律
authors:
- Chang Su
- Bin Wu
- Emine Yilmaz
- Yao Lu
affiliations:
- University of Pennsylvania
- University College London
arxiv_id: '2610.37631'
url: https://arxiv.org/abs/2610.37631
pdf_url: https://arxiv.org/pdf/2610.37631
published: '2026-10-27'
collected: '2026-10-29'
category: LLM
direction: LLM预训练 · 知识获取动态分析
tags:
- Pre-training
- Knowledge Acquisition
- Point-in-Time Model
- Temporal Variability Score
- LLM Probing
one_liner: 提出时间变异性得分TVS，揭示预训练不同阶段不同知识的学习节奏差异
practical_value: '- 垂直领域LLM预训练（如电商商品/用户知识预训练）可参考TVS思路，对跨时间波动大的知识（新品、热点营销话术）分配更高的后期训练权重，提升这类知识的记忆效果

  - 推荐/Agent的知识召回评估中，可通过时间分片模型计算不同query/知识的TVS，区分稳定知识（商品属性）和动态知识（促销信息），分别设计召回逻辑和更新频率

  - 预训练数据筛选时，可复用TVS的变异系数归一化思路，避免用原始标准差统计混淆知识难度和出现频率波动的问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有预训练效果评估多依赖聚合指标，无法区分不同类型知识的学习节奏差异；直接统计知识在语料中的出现频率受措辞影响大，难以准确刻画知识跨时间的分布稳定性，不同知识的预训练获取规律长期不明确。
### 方法关键点
- 基于8个架构、训练流程完全一致、仅训练数据对应网页爬取年份不同的PIT-4B时点模型，定义**TVS**为问答对在不同年份模型上NLL的变异系数（标准差/均值），消除知识难度干扰，区分时间稳定知识和时间可变知识。
- 控制问答对token长度分层划分低/中/高TVS组，在6个不同规模的开源LLM全预训练checkpoint上跟踪不同组知识的准确率变化轨迹。
### 关键实验结果
覆盖HellaSwag、PIQA、ARC、MMLU等6个基准共16239条样本：
- 预训练早期低/高TVS知识准确率无显著差异，后期高TVS知识准确率增速比低TVS组高2.0个点/每10倍训练token增长。
- 预训练结束后高TVS知识在34/36的模型-基准组合中准确率超过低TVS组，平均chance-normalized准确率高7.3个点；知识密集型任务（ARC、MMLU）控制知识难度后仍有6.9个点的优势。
### 核心结论
语料中跨时间出现越不稳定的知识，在预训练后期的提升速度越快，无需访问全量预训练语料即可通过时点模型的似然差异刻画知识的学习特性。
