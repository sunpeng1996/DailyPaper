---
title: 'When More Evidence Hurts: Publication-Bias Drift and Principled Stopping for
  Biomedical Causal Search'
title_zh: 生物医学因果搜索中的发表偏倚漂移与检索停止策略优化
authors:
- Fred Sun
- Shangqi Guo
affiliations:
- 清华大学类脑计算研究中心
- 清华大学精密仪器系
arxiv_id: '2609.24101'
url: https://arxiv.org/abs/2609.24101
pdf_url: https://arxiv.org/pdf/2609.24101
published: '2026-09-21'
collected: '2026-09-23'
category: Agent
direction: Agent 检索停止策略优化
tags:
- Agent
- Publication Bias
- Retrieval Stopping
- Causal Knowledge Graph
- Reward Model
one_liner: 提出漂移感知因果图Agent DACG-agent，通过双层停止策略降低检索偏倚，提升推断准确率同时减少检索步数
practical_value: '- 检索系统遇到数据源存在系统性偏倚（如电商好评率偏倚、广告正向效果数据占比过高）时，可复用「检索深度增加→偏差放大」的结论，避免盲目拉长召回链路

  - Agent 检索停止策略可复用双层设计：上层用KL散度判断后验收敛保证准确率，下层用PRM检测证据质量峰值保证效率，平衡效果与算力成本

  - 当待决策的负样本/零效果样本占比较高时，可加入偏倚漂移检测模块，避免过量召回正向偏倚数据导致的假阳性判断错误'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
生物医学文献普遍存在发表偏倚，正向结果占比远高于零/负向结果，检索深度越深，越容易对零效果问题产生假阳性推断（即证据漂移现象），无限制拉长检索会大幅降低推断准确率。
### 方法关键点
1. 形式化定义证据漂移，证明标准发表偏倚模型下，零效果查询的假阳率随检索深度严格递增，极限趋近于1
2. 提出DACG-agent，增量从PubMed摘要构建因果知识图，采用双层停止策略：KL散度监控检测后验收敛（准确率层），Bradley-Terry过程奖励模型在线检测证据质量峰值触发停止（效率层）
### 关键结果数字
在140条Cochrane查询测试集上，对比全预算检索，DACG-agent将证据漂移从15.7%降至6.4%，零效果准确率提升21个百分点（40.0%→61.4%），检索步数减少67%，整体准确率从61.4%升至69.3%
