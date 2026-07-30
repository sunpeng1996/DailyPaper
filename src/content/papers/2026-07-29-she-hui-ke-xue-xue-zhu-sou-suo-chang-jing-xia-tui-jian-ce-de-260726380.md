---
title: Continuous Online Evaluation of Recommendation Strategies in Social Science
  Academic Search
title_zh: 社会科学学术搜索场景下推荐策略的持续在线评估
authors:
- Mehmet Deniz Türkmen
- Daniel Hienert
affiliations:
- GESIS - Leibniz Institute for the Social Sciences
arxiv_id: '2607.26380'
url: https://arxiv.org/abs/2607.26380
pdf_url: https://arxiv.org/pdf/2607.26380
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 学术搜索推荐 · 持续在线评估
tags:
- Continuous Evaluation
- Academic Search
- Semantic Similarity
- Lexical Similarity
- Session-based Recommendation
one_liner: 在社会科学学术搜索场景下对比三类推荐算法，落地持续在线评估框架
practical_value: '- 多算法在线评估可复用STELLA框架思路，支持多策略并行灰度、实时回收用户反馈，无需频繁切流降低实验成本

  - 垂直搜索/垂类推荐场景可优先测试语义相似度方案，通常效果优于传统词匹配、session-based基线，可先小流量验证再全量

  - 同平台不同内容类目（如电商标品/非标品、内容类图文/短视频）需单独评估算法效果，用户行为差异会导致算法表现明显分化'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
垂直领域学术搜索的推荐面临学科差异大、信息类型复杂、用户偏好分散的痛点，现有方案缺乏持续在线评估机制，难以对齐真实用户需求。
### 方法关键点
基于STELLA评估框架，在GESIS社会科学学术搜索中并行上线三类推荐策略做实时在线评估：1）传统 lexical 词相似度匹配算法；2）基于Transformer embedding的语义相似度推荐；3）基于历史用户点击路径的session-based推荐，全量接入真实用户行为数据，无需额外切流即可多策略同步对比效果。
### 关键结果
语义相似度推荐用户偏好度最优，显著优于词匹配与session-based方案；不同信息类目（研究数据、出版物、变量等）下算法表现差异明显，对应不同信息类型的用户检索行为存在显著分化。
