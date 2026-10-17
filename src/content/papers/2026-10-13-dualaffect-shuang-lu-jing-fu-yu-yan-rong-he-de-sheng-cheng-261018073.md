---
title: 'DualAffect: Dual-Path Paralinguistic Integration for Generative Audiovisual
  Emotion Understanding'
title_zh: DualAffect：双路径副语言融合的生成式音视频情感理解
authors:
- Yibo Wang
- Jisheng Dang
- Bimei Wang
- Junhong Liu
- Jiongpei Hou
- Jingwen Zhao
- Wenjun Ma
- Hong Peng
- Bin Hu
- Qi Tian
arxiv_id: '2610.18073'
url: https://arxiv.org/abs/2610.18073
pdf_url: https://arxiv.org/pdf/2610.18073
published: '2026-10-13'
collected: '2026-10-17'
category: Multimodal
direction: 多模态大模型 · 音视频情感理解
tags:
- Multimodal LLM
- Emotion Recognition
- Audiovisual QA
- Paralinguistic Modeling
- Dual-path Architecture
one_liner: 提出双路径副语言融合架构，实现鲁棒的生成式音视频情感理解与问答
practical_value: '- 多模态特征融合可借鉴双路径复用同一份底层编码的设计，降低多模态信号接入的算力开销，适合直播、短视频等电商多模态场景

  - 跨模态信号冲突场景（如直播口播语气和商品视觉情绪不一致）可单独保留一路独立时序特征通路，大幅提升识别鲁棒性

  - 混合任务适配时保留任务专属输出头的方案，可复用在单模型同时承载直播情感识别、多模态咨询QA等多个电商业务任务'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频情感理解方案难以处理语音表达与视觉外观不一致的场景，副语言（语气、语调等）线索到生成式输出的映射存在明显瓶颈。
### 方法关键点
1. 提出双路径架构DualAffect，两路复用同一份声学编码：融合路径通过visual query关联声学特征与视觉内容，直接路径通过独立投影器压缩有效声学序列为有序token，共同输入共享语言解码器，同时获取跨模态联合上下文与声学时序证据
2. 采用混合任务适配机制保留任务相关输出头，单模型可同时支持情感识别与通用音视频QA任务
### 关键结果
在CA-MER基准平均指标达67.89，EmotionTalk测试集准确率62.88%，Daily-Omni准确率49.87%；仅置零直接路径token时，EmotionTalk验证准确率下降9.75个百分点，CA-MER指标下降2.66点，音视信号冲突场景性能下降最为显著
