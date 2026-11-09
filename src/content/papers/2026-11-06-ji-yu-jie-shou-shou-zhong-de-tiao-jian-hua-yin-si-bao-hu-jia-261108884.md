---
title: Who's Asking? Audience-Conditioned Privatization
title_zh: 基于接收受众的条件化隐私保护框架
authors:
- Daniil Filienko
- Anusha Bagalkotkar
- Xan Vongsathorn
- Sikha Pentyala
affiliations:
- University of Washington Tacoma
- Zillow
arxiv_id: '2611.08884'
url: https://arxiv.org/abs/2611.08884
pdf_url: https://arxiv.org/pdf/2611.08884
published: '2026-11-06'
collected: '2026-11-09'
category: Other
direction: 文本隐私脱敏 · 受众条件化处理
tags:
- Differential Privacy
- Synthetic Text Generation
- Anonymization
- Contextual Integrity
- Data Privacy
one_liner: 提出Ext-Classify-Priv受众条件化隐私框架，仅保护指定受众敏感属性，提升脱敏文本保真度
practical_value: '- 电商UGC（评论、客服会话、用户搜索query）脱敏可复用该框架，针对内部运营、第三方分析、公开发布等不同受众仅保护对应敏感属性，避免过度脱敏丢失业务特征

  - 用户生成内容用于RAG知识库构建、推荐模型训练前的隐私处理，可优先采用仅保护目标敏感特征的Feature-DP方案，比通用DP方案文本保真度提升3倍以上

  - 多权限Agent的数据访问管控可借鉴该思路，不同权限等级的Agent仅可访问对应脱敏等级的数据，在降低隐私泄露风险的同时最大化数据业务价值'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有差分隐私合成文本生成（DP-SDG）、匿名化方法不区分数据下游接收受众，无差别保护所有属性导致过度脱敏，损失大量业务需要的有效信息，且未考虑同一属性对不同受众的敏感度差异。
### 方法关键点
提出Ext-Classify-Priv三段式框架：1）自动提取语料中包含的所有信息类型；2）基于上下文完整性规则，分类识别对指定受众敏感的属性集合；3）仅对敏感属性执行保护，兼容匿名化、Feature-DP驱动的SDG两种实现路径。
### 关键结果
- Reddit数据集3类受众测试中，受众专属脱敏方案的保真度全面优于无差别脱敏方案
- bioRxiv数据集ε=1时，SDG实现路径的MAUVE从基线的0.097提升至0.420
- 私有房产数据集上，匿名化实现路径的MAUVE比最优基线的0.698提升至0.959
