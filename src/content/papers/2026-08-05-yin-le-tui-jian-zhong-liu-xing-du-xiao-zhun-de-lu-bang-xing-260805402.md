---
title: 'Robustness and User-Perceived Value of Popularity Calibration in Music Recommendation:
  A User Study'
title_zh: 音乐推荐中流行度校准的鲁棒性与用户感知价值：用户研究
authors:
- Oleg Lesota
- Gustavo Escobedo
- Bruce Ferwerda
- Simone Kopeinik
- Dominik Kowald
- Elisabeth Lex
- Markus Schedl
affiliations:
- Johannes Kepler University Linz, Austria
- Jönköping University, Sweden
- Know-Center GmbH, Austria
- University of Graz, Austria
- Graz University of Technology, Austria
arxiv_id: '2608.05402'
url: https://arxiv.org/abs/2608.05402
pdf_url: https://arxiv.org/pdf/2608.05402
published: '2026-08-05'
collected: '2026-08-07'
category: RecSys
direction: 推荐系统 · 流行度校准用户研究
tags:
- Recommender System
- Popularity Bias
- Calibration
- User Study
- Music Recommendation
one_liner: 通过受控用户研究验证音乐推荐中流行度校准的用户感知价值与JSD度量的鲁棒性
practical_value: '- 不要盲目将流行度校准（如JSD指标）作为核心优化目标，校准列表不一定提升用户满意度，优先对齐实际业务的用户反馈数据

  - 计算流行度标签时需结合用户对物品的熟悉度、用户历史数据完备度加权调整，避免纯统计流行度与用户感知偏差过大

  - 公平性、偏差修正类优化上线前建议做小流量AB测验证用户侧真实感知，不要仅依赖离线指标提升就全量上线'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有流行度校准研究多依赖离线指标，默认用户偏好与自身历史消费流行度分布匹配的推荐列表，但相关用户侧实证十分有限，校准度量在物品熟悉度不同、用户历史数据不全场景下的鲁棒性也不明确。

### 方法关键点
基于用户近期听歌历史生成三类不同流行度构成的推荐列表：高流行占比、低流行占比、与历史分布对齐的校准列表，通过受控用户研究，对比用户感知差异、偏好，验证JSD流行度校准度量的鲁棒性，以及计算侧流行度标签与用户主观判断的对齐度。

### 关键结果
用户可感知推荐列表的流行度差异，但无明确的校准列表偏好；JSD与用户感知流行度的关联受物品熟悉度、列表构成、可用用户历史的显著影响；计算生成的流行度标签与用户主观判断仅弱对齐。
