---
title: 'ReliableNet: A Chance-Constrained Approach to Trustworthy Classification in
  Deep Learning'
title_zh: ReliableNet：深度学习可信分类的机会约束方法
authors:
- Ange-Clément Akazan
- Ineza Remy Mugenga
- Abebe Geletu
- Jean Medard Ngnotchouye
- Issa Karambal
affiliations:
- University of KwaZulu-Natal
- AIMS Research and Innovation Centre, African Institute for Mathematical Sciences
- African Institute for Mathematical Sciences, Kigali
arxiv_id: '2608.09768'
url: https://arxiv.org/abs/2608.09768
pdf_url: https://arxiv.org/pdf/2608.09768
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 可信分类 · 机会约束训练优化
tags:
- Trustworthy AI
- Chance Constrained Optimization
- Risk Control
- Classification
- Deep Learning
one_liner: 提出联合置信错误概率约束的可信分类框架ReliableNet，实现训练阶段风险可控
practical_value: '- 电商推荐排序/内容审核分类模块可引入JCW概率约束，将「高置信错误排序/审核」概率控制在预设风险阈值内，减少违规内容推送等致命badcase

  - 大促、新类目上线、新用户涌入等分布漂移场景下，可复用ReliableNet的机会约束训练框架，在精度下降可接受的前提下大幅降低置信错误率

  - 可迁移到GenRec/LLM4Rec的训练环节，约束LLM高置信错误生成推荐结果的概率，提升生成式推荐的输出可靠性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有深度学习基于ERM仅控制平均损失，无法直接约束「高置信同时预测错误」的JCW风险，这类错误会绕过拒识/人工审核机制，是高风险场景的致命故障；后验校准、共形风险控制等方案均无法在训练阶段直接约束该联合事件的概率上限。
### 方法关键点
将JCW概率低于用户指定风险阈值α作为硬约束，转化为机会约束ERM问题，采用保守平滑内近似求解，确保群体级可行性满足原始JCW约束，训练过程直接实现风险可控。
### 关键结果
分布内测试时是唯一在6个数据集、所有随机种子下均满足JCW风险预算的方法；在人口漂移、伪相关、分布偏移等5类OOD场景下，JCW经验值为所有对比方法最低，精度、覆盖率、校准效果均保持竞争力，多数数据集上风险-覆盖率表现优于基准
