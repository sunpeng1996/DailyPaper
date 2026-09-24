---
title: Enriching Speech Emotion Representations with Conversational Context
title_zh: 利用对话上下文增强语音情感表征能力
authors:
- Arthur Peuvot
- Romaric Besançon
- Gaël de Chalendar
- Bianca Vieru
- Ioana Vasilescu
affiliations:
- Université Paris-Saclay, CEA, List, France
- LISN, CNRS, Université Paris-Saclay, France
arxiv_id: '2609.26422'
url: https://arxiv.org/abs/2609.26422
pdf_url: https://arxiv.org/pdf/2609.26422
published: '2026-09-22'
collected: '2026-09-24'
category: Other
direction: 对话语音情感识别 · 上下文建模
tags:
- Speech Emotion Recognition
- Conversational Context
- ACERT
- Context Modeling
- SER
one_liner: 提出融合可变长度对话上下文的ACERT模块，显著提升多数据集语音情感识别效果
practical_value: '- 电商智能语音客服Agent可复用ACERT的可变上下文窗口设计，捕捉用户情绪变化轨迹，优化客服响应策略

  - 直播/短视频语音内容理解场景可引入对话连续建模逻辑，替代单句情绪判定，提升内容推荐精准度

  - 开发对话类Agent情绪感知模块时，可参考其消融结论，优先建模情绪/对话连续性特征，降低冗余计算'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前Speech Emotion Recognition（SER）方案多基于单句粒度预测情绪，忽略对话上下文承载的情绪流动、交互关系，难以适配真实口语交互场景的情绪判定需求。
### 方法关键点
1. 提出ACERT模块，支持灵活长度的对话上下文窗口建模，通过时序平均计算上下文情感表征，精准捕捉口语交互中的情绪演化规律
2. 跨多种情绪表达风格、场景的数据集验证方法鲁棒性，通过消融实验定位效果增益的核心来源
### 关键结果
在IEMOCAP数据集上性能超越现有SOTA；在SAFE数据集上建立首个上下文感知SER基准；在MELD数据集的无加权类平衡指标上取得优异表现；消融实验证实效果增益来自情绪与对话连续性，与说话人身份、声学条件无关。
