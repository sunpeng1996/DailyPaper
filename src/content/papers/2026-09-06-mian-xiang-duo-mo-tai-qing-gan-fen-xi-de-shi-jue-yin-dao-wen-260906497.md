---
title: Vision-Guided Text Prompt Tuning for Multimodal Sentiment Analysis
title_zh: 面向多模态情感分析的视觉引导文本提示调优方法
authors:
- Xiaoran Kou
- Jingyi Wu
- Peng Sun
- Yang Liu
- Hong Chen
affiliations:
- 同济大学电子与信息工程学院
- 复旦大学智能机器人与先进制造学院
- 杜克昆山大学自然与应用科学部
arxiv_id: '2609.06497'
url: https://arxiv.org/abs/2609.06497
pdf_url: https://arxiv.org/pdf/2609.06497
published: '2026-09-06'
collected: '2026-09-11'
category: Multimodal
direction: 多模态情感分析 · 轻量提示调优
tags:
- Multimodal Sentiment Analysis
- Prompt Tuning
- Parameter-Efficient Tuning
- Cross-modal Fusion
- BERT
one_liner: 仅更新2.4M参数的分层自适应视觉引导提示调优方法，实现低成本高性能多模态情感分析
practical_value: '- 做电商直播/短视频的多模态情感识别时，可复用「冻结文本大模型+跨模态分层prompt注入」的轻量微调架构，避免全量微调的高成本和小样本过拟合问题

  - 多模态特征融合场景可参考co-guided router机制，根据当前文本语义状态动态匹配视觉辅助信息，减少无关视觉噪声对主模态语义的干扰

  - 做Agent多模态用户意图理解时，可借鉴「主模态为锚+辅助模态自适应校准」的思路，在低资源场景下快速适配业务需求'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态情感分析存在两大核心痛点：一是无差别跨模态融合易引入视觉噪声、扭曲作为语义锚的文本语义；二是全量微调大尺寸视觉/文本编码器算力成本高，在场景受限的小数据集上易过拟合，亟需可控、自适应、参数高效的建模方案。

### 方法关键点
提出VG-TPT框架，固定BERT等文本编码器权重，通过分层自适应prompt将视觉情感cue注入文本编码过程，替代传统后期特征融合或全backbone微调；设计co-guided router，根据当前层文本状态和视觉引导特征从可训练prompt bank中动态组合样本/层专属prompt，实现视觉信息的可控校准。

### 关键结果
在CMU-MOSEI、CMU-MOSI数据集上效果显著优于纯文本基线，性能比肩甚至超过全模态微调方法，仅需更新2.4M可训练参数。
