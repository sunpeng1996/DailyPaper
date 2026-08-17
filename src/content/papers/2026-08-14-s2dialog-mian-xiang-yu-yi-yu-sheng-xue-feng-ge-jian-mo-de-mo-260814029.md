---
title: 'S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling'
title_zh: S2Dialog：面向语义与声学风格建模的多模态对话检索
authors:
- Xueqi Wang
- Zhigang Wang
- Runqing Zhang
- Zhenqi Jia
- Junfeng Zhao
affiliations:
- College of Computer Science, Inner Mongolia University
- University of Electronic Science and Technology of China, Shenzhen Campus
arxiv_id: '2608.14029'
url: https://arxiv.org/abs/2608.14029
pdf_url: https://arxiv.org/pdf/2608.14029
published: '2026-08-14'
collected: '2026-08-17'
category: Multimodal
direction: 多模态对话检索 · 跨模态对比学习
tags:
- Multimodal Retrieval
- Contrastive Learning
- Dialogue Representation
- Acoustic Modeling
- Cross-modal Alignment
one_liner: 提出融合对话级双模态检索器与跨模态对比学习的多模态对话语义风格检索框架S2Dialog
practical_value: '- 搭建电商多模态客服Agent的对话案例库时，可参考该框架分别建模对话级文本语义、语音风格特征，提升相似历史对话召回的精准度

  - 跨模态特征对齐场景可复用对话级文本-声学对比学习策略，降低不同模态表征的分布差异，提升多模态匹配效果

  - 智能音箱等语音交互类推荐场景中，可借鉴该思路同时匹配用户历史对话的语义与说话风格，提升交互自然度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多模态对话检索方法大多局限于单模态匹配或 utterance 级匹配，无法捕获整段对话的全局语义连贯性、声学风格一致性，无法满足对话系统、情感识别、对话合成等任务对相似参考对话的需求。
### 方法关键点
1. 设计S2Dialog统一检索框架，包含对话级文本检索器、对话级声学检索器两个模块，分别将对话的文本、声学模态编码为全局级表征
2. 引入对话级文本-声学对比学习策略，对齐语义、风格相似的对话的跨模态表征，同时拉大不相关对话的表征距离，提升检索区分度
### 关键结果
在多模态对话数据集DailyTalk上，相比现有主流基线检索效果实现显著提升。
