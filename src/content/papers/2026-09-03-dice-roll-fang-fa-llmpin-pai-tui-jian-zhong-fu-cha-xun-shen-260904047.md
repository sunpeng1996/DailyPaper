---
title: 'The Dice Roll Method: A Standardized Protocol for Repeated-Query Auditing
  of Large Language Model Brand Recommendations'
title_zh: Dice Roll 方法：LLM品牌推荐重复查询审计的标准化协议
authors:
- Dmitrij Żatuchin
affiliations:
- Estonian Entrepreneurship University of Applied Sciences
- Rankfor.AI
arxiv_id: '2609.04047'
url: https://arxiv.org/abs/2609.04047
pdf_url: https://arxiv.org/pdf/2609.04047
published: '2026-09-03'
collected: '2026-09-04'
category: Eval
direction: LLM推荐审计 · 标准化评估协议
tags:
- LLM Auditing
- Brand Recommendation
- Measurement Reliability
- Generalizability Theory
- Statistical Power
one_liner: 提出适配LLM生成特性的品牌推荐重复查询审计标准化协议，给出迭代次数与度量选型指南
practical_value: '- 做LLM品牌/商品推荐的效果审计、bias检测时，可直接复用三档迭代次数设置：探索性n=5（G=0.58）、验证性n=10（G=0.74）、严谨性n=15（G=0.81），平衡成本和可靠性

  - 度量选型上，计数类（CV/Gini）、集合类（Jaccard）、语义类（embedding cosine）、公平性类（PASOR）四类指标互补，不要单靠某一种指标下结论，其中PASOR可直接复用到品牌曝光公平性计算场景

  - 处理LLM重复查询的非独立、非高斯、非平稳问题时，可直接复用其统计方法栈：负二项GLMM做效应检验、Cliff''s δ做无分布效应量、block bootstrap保留序列依赖、KS/PSI做漂移检测

  - 做LLM调用成本预估时，可参考其成本效率拐点：迭代n=7时达到精度边际收益拐点，再往上加迭代单位成本换的精度大幅下降，预算有限选n=7足够用'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前业界/学界采用重复相同prompt审计LLM品牌推荐的随机波动时，缺乏标准化协议：迭代次数从5到40全凭经验选择，稳定性度量选型混乱，传统高斯统计方法不符合自回归生成的条件依赖、非高斯、非平稳特性，导致审计结果不可靠、无法复现，尤其是品牌公平性、bias检测类结论可信度不足。

### 方法关键点
- 方差拆解：将LLM响应总方差拆分为token采样、prompt表述、模型间、版本/时间漂移、交互项5个分量，针对性设计统计方案
- 分析栈：采用负二项GLMM处理过离散计数，Cliff's δ做无分布效应量，moving block bootstrap保留序列依赖，基于Generalizability Theory做可靠性分解，KS/PSI做模型漂移检测
- 度量体系：覆盖计数类、集合类、语义类、公平性类四类互补指标，新增PASOR公平性调整指标消除prompt表述偏差

### 关键结果
- 基于5个已有的品牌推荐审计数据集（约19万观测、3-5个LLM、270+品牌、6种语言）重分析，得到三档迭代指导：探索性n=5（G=0.58）、验证性n=10（G=0.74）、严谨性n=15（G=0.81）
- 外部验证在39个测试单元中37个符合可靠性预测，n=5迭代的统计功效预测准确到小数点后两位
- 成本效率拐点出现在n=7，此时边际精度收益最高，继续增加迭代的单位成本换取的精度大幅下降

> 最值得记住的结论：LLM重复查询审计的可靠性核心是平衡迭代成本与统计效力，不要凭直觉选迭代次数，也不要用不满足LLM生成特性的高斯统计方法
