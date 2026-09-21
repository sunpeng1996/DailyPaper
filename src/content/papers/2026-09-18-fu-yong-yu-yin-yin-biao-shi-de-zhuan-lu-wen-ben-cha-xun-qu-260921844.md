---
title: Reusing Latent Speech Representations for Query-Conditioned Topic Localization
  in Transcripts
title_zh: 复用语音隐表示的转录文本查询驱动主题定位方法
authors:
- Steffen Freisinger
- Philipp Seeberger
- Thomas Ranzenberger
- Tobias Bocklet
- Korbinian Riedhammer
affiliations:
- Technische Hochschule Nürnberg Georg Simon Ohm
arxiv_id: '2609.21844'
url: https://arxiv.org/abs/2609.21844
pdf_url: https://arxiv.org/pdf/2609.21844
published: '2026-09-18'
collected: '2026-09-21'
category: RAG
direction: 多模态RAG · 语音转录本查询片段检索
tags:
- ASR Encoder
- Speech Representation
- Query Localization
- Multimodal Embedding
- Transcript Retrieval
one_liner: 复用ASR编码器隐状态融合文本嵌入，无需额外音频编码器提升长转录本查询主题定位效果
practical_value: '- 电商直播/客服语音转录本的用户query相关片段检索场景，可直接复用ASR隐状态+文本嵌入融合方案，无需额外部署音频编码器，降低推理成本

  - 直播/短视频口播内容的关键词/主题定位任务，可参考该方法利用ASR自带的语音特征，提升严格边界匹配下的定位准确率，优化片段截取效果

  - 结构化/半结构化语音（如电商直播讲解、客服标准应答）场景优先采用该方案，自发闲聊类语音场景增益有限无需额外投入'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
长语音转录本输入下游NLP系统计算成本高、冗余信息多，现有纯文本查询片段定位方法忽略ASR自带的语音特征，额外部署独立音频编码器又会大幅提升推理开销。
### 方法关键点
1. 直接复用ASR输出的编码器隐状态作为句子级语音表示，无需单独训练或部署额外音频编码器；
2. 将语音表示与文本嵌入融合后输入轻量级跨度定位器，预测匹配用户查询的连续句子起止边界。
### 关键结果
在两个公开数据集上效果全面优于纯文本基线，严格边界匹配指标下增益更突出；跨数据集测试显示结构化/半结构化语音场景增益最高，自发语音场景增益有限且波动较大。
