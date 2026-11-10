---
title: 'From User Behaviors to Satisfaction Judgments: Reasoning about User Satisfaction
  with AI Overviews'
title_zh: 结合用户行为的AI搜索摘要用户满意度预测方法STaRS
authors:
- Xingzhu Wang
- Yitong Xu
- Yue Li
- Daiting Shi
- Jingzhou He
- Jiaxin Mao
affiliations:
- Renmin University of China
- Baidu Inc.
arxiv_id: '2611.10715'
url: https://arxiv.org/abs/2611.10715
pdf_url: https://arxiv.org/pdf/2611.10715
published: '2026-11-07'
collected: '2026-11-10'
category: Eval
direction: 生成式搜索 · 用户满意度评估
tags:
- User Satisfaction Prediction
- AI Overview
- LLM Reasoning
- Reward Shaping
- Search Evaluation
one_liner: 提出STaRS框架，融合结构化推理与奖励塑造RL，基于用户行为精准预测AI搜索摘要满意度
practical_value: '- 电商/生成式推荐场景中，判断AI生成的导购摘要、推荐理由的用户满意度时，不要直接套用传统推荐的行为规则（如长停留=满意），需结合内容上下文做细粒度推理，避免误判

  - 可复用STaRS的结构化推理范式：先对单个用户行为信号做极性判断，再综合输出结果，零样本下即可获得不错效果，适合小样本业务场景快速落地

  - RL训练时的奖励塑造方法可迁移：离线通过高能力大模型投票+反事实筛选获得核心中间过程监督信号，能有效解决推理类任务的奖励稀疏问题，提升模型效果

  - 业务侧做生成式内容体验优化时，仅依赖内容质量指标（如相关性、忠实度）的评估结果和真实用户满意度相关性低，必须引入用户行为信号提升评估准确性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
AI Overview已成为搜索引擎标配，现有评估要么仅关注系统侧内容质量，要么沿用传统IR的行为信号规则，但传统规则不适配新场景：比如传统IR中长文档停留是满意信号，在AI Overview场景下可能是摘要未满足需求用户跳转文档，也可能是摘要优质引发用户进一步探索，规则完全失效，无法准确衡量真实用户满意度。

### 方法关键点
1. 核心采用结构化推理策略：先对每类用户行为信号（AI摘要停留、文档点击、Query改写等）单独做语义解释和满意度极性（正/负/中性）判断，再综合所有信号的推理结果输出最终满意度评分
2. 设计RL奖励塑造机制解决奖励稀疏问题：离线先用大模型生成多份候选推理轨迹，筛选预测结果和ground truth一致的轨迹做多数投票得到行为信号参考极性，再通过反事实删除实验筛选出对最终评分影响大的核心信号作为中间监督，训练时同时对最终预测和中间极性判断做联合奖励
3. 构建两个标注数据集：实验室用户研究数据集（554条记录）、工业搜索日志数据集SearchLog26（6589条记录），均包含Query、AI摘要、用户行为和用户显式满意度打分

### 关键实验
在两个数据集上和三类基线对比：系统侧内容质量评估方法（RAGAs、TruLens等）、无行为输入的用户侧评估方法、传统IR行为驱动满意度预测方法（GBDT、LSTM、G-CoS等）。结果：SearchLog26数据集上STaRS的Spearman相关性达0.4652，比次优基线高14%，MAE低11.8%；零样本（无RL）在小数据集上也优于所有基线。

生成式搜索场景的用户满意度评估，仅靠内容质量指标和传统行为规则远不够，结合上下文的细粒度行为信号推理能大幅提升预测准确性。
