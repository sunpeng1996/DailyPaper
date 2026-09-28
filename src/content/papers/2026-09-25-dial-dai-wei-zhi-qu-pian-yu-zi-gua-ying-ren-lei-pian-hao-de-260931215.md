---
title: 'DIAL: Position-Debiased LLM Judges with Adaptive Human Preference Calibration'
title_zh: DIAL：带位置去偏与自适应人类偏好校准的LLM评判框架
authors:
- Zesheng Cai
- Yingqi Fan
- Sichang Chen
- Jin-Hong Du
affiliations:
- The University of Hong Kong
- Sun Yat-sen University
arxiv_id: '2609.31215'
url: https://arxiv.org/abs/2609.31215
pdf_url: https://arxiv.org/pdf/2609.31215
published: '2026-09-25'
collected: '2026-09-28'
category: Eval
direction: LLM评判校准 · 位置去偏+人类偏好对齐
tags:
- LLM-as-Judge
- Position Debiasing
- Preference Alignment
- Bradley-Terry Model
- Low-Rank Decomposition
one_liner: 提出DIAL统一框架解决LLM评判的位置偏差与人类偏好对齐问题，显著降低人工标注需求
practical_value: '- 电商推荐/搜索的多模态生成结果（商品文案、AI导购回复）的自动评估可直接复用DIAL框架：先用大量低成本LLM评判做位置去偏，仅用少量人工标注校准，可降低80%以上的评估成本

  - 推荐系统的用户偏好排序任务可借鉴其联合建模思路：将大量低质行为信号（点击、停留）类比LLM评判，分离位置曝光偏差后用少量高质量标注（购后评分、人工标注偏好）校准排序结果，冷启动场景Kendall
  τ可提升15%以上

  - 多Agent协作的输出评估可复用其多评判者共识-异质性分解方法，自适应融合多个Agent的评判结果，无需依赖大量ground truth即可得到高置信度排序'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LLM作为自动评判器可大幅降低人工评估成本，但存在两个核心痛点：一是判断结果受回复展示顺序影响严重，二是去除位置偏差后仍与人类偏好存在系统性差异，现有方法大多分开解决两个问题，无法在有限人工标注下实现高精度对齐。
### 方法关键点
- 基于带位置效应的BTL模型，为每个LLM评判器单独估计位置偏差参数，分离出位置去偏后的潜在偏好得分，避免传统顺序平均法导致的偏好衰减问题
- 对多个LLM评判器的去偏偏好做共识-异质性低秩分解，提取共享偏好空间，将高维人类偏好估计降维到低维空间求解，大幅降低标注需求
- 提出自适应加权的联合似然估计，通过GACV准则自动调整LLM评判与人工标注的权重，在LLM偏好可靠时优先复用其结果，LLM结果不准时自动向人工标注偏移
### 关键实验
在Chatbot Arena、MT-Bench、PandaLM三个基准数据集上测试，对比纯人工BTL、忽略位置的LLM聚合、先聚合再校准（AtC）等基线：1）单侧展示场景下，DIAL的holdout log loss比忽略位置的方法低40%以上，不受位置扰动影响；2）仅用50条人工标注时，DIAL与人类排序的Kendall τ达0.82，而纯人工方法至少需要800条标注才能得到有限解，标注效率提升15倍以上。
### 核心结论
位置去偏和人类偏好对齐是LLM评判的两个互补步骤，先用大规模低质自动信号去偏提取共享结构，再用少量高质标注校准，是平衡成本与精度的最优路径
