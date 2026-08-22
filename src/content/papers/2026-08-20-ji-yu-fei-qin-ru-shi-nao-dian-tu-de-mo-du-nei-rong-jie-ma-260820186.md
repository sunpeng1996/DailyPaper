---
title: Decoding silent reading from non-invasive EEG
title_zh: 基于非侵入式脑电图的默读内容解码
authors:
- Ingo Marquardt
- Anthilia Alchanat
- Priyanka Jain
affiliations:
- nubrain
arxiv_id: '2608.20186'
url: https://arxiv.org/abs/2608.20186
pdf_url: https://arxiv.org/pdf/2608.20186
published: '2026-08-20'
collected: '2026-08-22'
category: Other
direction: 脑机接口 · 非侵入式EEG语义解码
tags:
- EEG
- Brain-Computer Interface
- Contrastive Learning
- CLIP
- Open-Vocabulary Decoding
one_liner: 基于CLIP风格对比学习实现从非侵入式EEG中解码开放词汇默读内容
practical_value: '- 跨模态CLIP式对比对齐异源特征的方法，可直接复用至多模态推荐/广告的跨域特征融合、多模态召回特征对齐场景

  - 用低成本可扩展代理任务替代难采集标注的思路，可用于解决推荐冷启动、广告效果归因等标注数据稀缺的业务问题

  - 随机扰动低阶特征实现核心特征解耦的实验设计思路，可迁移至多模态内容理解、用户兴趣建模的特征去噪环节'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
非侵入式内隐语音解码核心痛点是大脑活动与自发内心独白的配对语料无法采集，现有代理范式采集慢、时序对齐差、受试者合规性难验证。
### 方法关键点
1. 选取默读作为可扩展代理任务，采用快速序列视觉呈现随机字体的连续文本，消除低阶视觉特征与词身份的关联干扰
2. 架构为卷积EEG编码器+可选因果Transformer，以CLIP风格对比学习为目标，对齐短时EEG窗口与大语言模型输出的对应词隐层嵌入
3. 设计对照实验分离词级解码、叙事上下文追踪、Transformer位置嵌入引入的非神经位置先验的影响
### 关键结果
基于单被试49小时共24万词的19通道干电极EEG数据，词级top-10检索准确率显著高于随机基线，性能随训练数据量对数线性增长无饱和；移除枕叶/颞后电极仅降低约1/3词级解码增益，上下文追踪能力不受影响。
