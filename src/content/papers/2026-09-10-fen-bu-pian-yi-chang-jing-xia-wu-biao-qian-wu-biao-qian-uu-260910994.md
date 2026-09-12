---
title: Importance Weighting for Unlabeled-unlabeled Learning under Distribution Shift
title_zh: 分布偏移场景下无标签-无标签（UU）学习的重要性加权方法
authors:
- Atsutoshi Kumagai
- Tomoharu Iwata
- Hiroshi Takahashi
- Taishi Nishiyama
- Kazuki Adachi
- Yasuhiro Fujiwara
affiliations:
- NTT, Inc.
arxiv_id: '2609.10994'
url: https://arxiv.org/abs/2609.10994
pdf_url: https://arxiv.org/pdf/2609.10994
published: '2026-09-10'
collected: '2026-09-12'
category: Training
direction: 弱监督训练 · 分布偏移适配
tags:
- Unlabeled-Unlabeled Learning
- Distribution Shift
- Importance Weighting
- Weak Supervision
- Positive-Unlabeled Learning
one_liner: 提出无需偏移类型假设的UU学习重要性加权框架，兼容PU、噪声标签等多类弱监督场景
practical_value: '- 电商推荐跨域/季节分布偏移场景下，可复用该重要性加权思路做弱监督分类器域适配，无需标注大量目标域样本

  - PU学习（如仅用点击正样本+无标签样本做CTR预估）遇到分布偏移时，可直接套用该通用框架适配，无需单独开发定制化方案

  - 噪声标签训练场景下（如用户反馈标签含大量噪声），可基于该方法统一处理分布偏移+噪声标签问题，降低多问题叠加的适配成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有UU学习可覆盖PU、噪声标签等多类弱监督学习范式，默认训练与测试分布的类条件密度一致，但实际业务中分布偏移普遍存在，现有重要性加权方法无法直接适配UU数据场景，且多数偏移适配方案仅针对特定问题设计，通用性差。

### 方法关键点
基于重要性加权的UU学习分布偏移适配方法，仅需训练域UU数据+少量测试域UU数据即可完成适配，无需假设分布偏移类型（如协变量偏移），通过为训练数据估计并赋予对应重要性权重最小化测试风险，在统一框架下支持分布偏移场景下的PU、噪声标签等多类弱监督学习任务。

### 关键结果
多个真实世界数据集实验验证了方法有效性，分布偏移场景下的分类精度优于现有针对特定任务的定制化偏移适配方案。
