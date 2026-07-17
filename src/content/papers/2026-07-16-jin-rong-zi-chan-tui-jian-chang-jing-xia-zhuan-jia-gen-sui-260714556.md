---
title: Impact of Expert-Following Strategies in Financial Asset Recommendation
title_zh: 金融资产推荐场景下专家跟随策略的效果研究
authors:
- Ryuki Unno
- Koshi Watanabe
- Keigo Sakurai
- Keisuke Maeda
- Takahiro Ogawa
- Miki Haseyama
affiliations:
- Hokkaido University, Japan
arxiv_id: '2607.14556'
url: https://arxiv.org/abs/2607.14556
pdf_url: https://arxiv.org/pdf/2607.14556
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 金融资产推荐 · 收益-偏好双目标优化
tags:
- Financial Recommendation
- Multi-Objective Optimization
- User Preference Alignment
- ROI Optimization
- Transaction Mining
one_liner: 提出基于高ROI投资者交易记录的专家跟随推荐框架，同步提升投资收益与用户偏好匹配度
practical_value: '- 双目标优化场景可复用「头部优质行为池筛选+加权排序」思路，解决收益与相关性天然trade-off问题，可落地到电商高转化达人带品推荐、广告高ROI创意推荐等场景

  - 轻量统计规则方案无需复杂深度模型，冷启动阶段可快速上线作为基线，投入产出比极高

  - 多目标业务效果评估可参考双指标同时显著性校验的实验设计，避免单指标优化导致的业务偏科'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
金融资产推荐场景长期存在收益（ROI）与用户偏好匹配度（nDCG）的天然 trade-off，传统基于收益或偏好的单目标优化策略只能兼顾一端，无法同时满足投资回报要求和用户体验目标。
### 方法关键点
1. 基于历史交易数据筛选高ROI的头部投资者构建「专家池」
2. 对专家池内用户购买过的资产，以ROI加权的购买频率作为排序得分，输出推荐列表
### 关键结果
在真实交易数据集的4组不同阈值实验中，该策略相对市场平均基线，ROI和nDCG均实现统计显著的同步提升，无单指标下降。
