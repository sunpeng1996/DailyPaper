---
title: 'Propose-Filter-Release: Scaling Noise to Typical Sensitivity via Private Filtering'
title_zh: Propose-Filter-Release：通过隐私过滤将噪声适配到典型敏感度
authors:
- Moshe Shenfeld
- Eliad Tsfadia
- Katrina Ligett
affiliations:
- The Hebrew University of Jerusalem
- Bar-Ilan University
arxiv_id: '2610.40654'
url: https://arxiv.org/abs/2610.40654
pdf_url: https://arxiv.org/pdf/2610.40654
published: '2026-10-29'
collected: '2026-10-31'
category: Other
direction: 差分隐私·低噪声通用计算原语
tags:
- Differential Privacy
- Privacy Preserving
- Data Filtering
- Statistical Estimation
- DP Primitive
one_liner: 提出通用差分隐私原语PFR，通过隐私过滤异常记录降低隐私机制所需噪声规模
practical_value: '- 做用户行为统计、画像建模时，可引入PFR框架过滤极端异常样本，在满足差分隐私合规的前提下降低注入噪声量，提升统计结果/画像准确性

  - 设计用户隐私保护的推荐模型训练流程时，可复用concave friendliness score设计思路衡量样本适配性，避免异常样本主导隐私噪声量级

  - 跨域数据联合统计场景，可将PFR作为通用隐私原语替代传统PTR机制，在同等隐私预算下获得更高的统计指标精度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统差分隐私（DP）机制按最坏情况单记录影响确定噪声规模，少量异常记录会导致整体噪声过大，大幅降低输出结果可用性，直接剔除异常又会引入隐私泄露风险。
### 方法关键点
1. 提出通用隐私原语Propose-Filter-Release（PFR），通过隐私过滤步骤先移除与数据集适配度低的异常记录
2. 仅需两个输入：衡量单记录与数据集适配度的凹友好度得分、仅对典型记录满足DP的友好-DP发布机制
3. 无需修改原有发布机制逻辑，即可将其升级为满足标准DP定义的通用机制，FriendlyCore可视为其特例实现
### 关键结果
可直接适配标量统计、主成分子空间估计、用户直方图KL散度计算、图有效电阻计算、处理规则选择五类场景，同等隐私预算下噪声规模远低于传统最坏-case DP机制
