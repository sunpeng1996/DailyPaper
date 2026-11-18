---
title: 'CARE: Conversational Affective Response Retrieval for Internet Memes'
title_zh: CARE：面向互联网表情包的会话式情感响应检索框架
authors:
- Jiajun Li
- Leihan Zhang
- Teng Zhang
- Le Zhang
- Qiang Yan
affiliations:
- 北京邮电大学经济管理学院
- 北京市多模态数据智能感知与治理重点实验室
- 北京信息科技大学计算机学院
arxiv_id: '2611.23005'
url: https://arxiv.org/abs/2611.23005
pdf_url: https://arxiv.org/pdf/2611.23005
published: '2026-11-17'
collected: '2026-11-18'
category: Multimodal
direction: 多模态检索 · 情感感知召回重排
tags:
- Multimodal Retrieval
- Meme Recommendation
- CLIP
- Learning to Rank
- Affective Computing
one_liner: 提出融合情感增强CLIP召回与Jina重排的CARE框架，提升会话场景表情包检索性能
practical_value: '- 两阶段多模态检索架构可直接复用：第一阶段用门控融合注入业务领域特征（如情感、营销属性）增强CLIP召回，第二阶段引入交互特征做精排，适配表情包、商品海报等多模态内容推荐场景

  - 弱监督信号利用技巧可迁移：同会话/同场景共现可作为弱相关标签，点赞、点击等隐式反馈可作为排序监督信号，解决多模态内容标注成本高的问题

  - 情感描述符门控融合方法可复用到情绪感知类场景：如电商智能客服表情包/话术推荐、社交平台内容情感化推荐等'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有会话场景表情包检索仅关注语义匹配，忽略情感表达一致性，且标注数据稀缺，微调CLIP的基线方案性能存在瓶颈。
### 方法关键点
1. 构建豆瓣、Imgflip两个跨语言数据集，包含98506条表情包记录、5583个讨论主题，采用同线程共现作为弱相关标签、点赞数作为隐式排序监督信号；
2. 两阶段CARE框架：召回层通过门控融合引入自由形式情感描述符增强CLIP，支持单Query多正例训练；重排层基于Jina融合Query-图像交互特征与情感表示，用用户engagement信号做排序监督训练。
### 关键结果
主题留出评估协议下，CARE在豆瓣数据集Hit@10达24.03%，在Imgflip数据集Hit@10达49.33%，较微调CLIP基线分别提升0.87pct、8.26pct。
