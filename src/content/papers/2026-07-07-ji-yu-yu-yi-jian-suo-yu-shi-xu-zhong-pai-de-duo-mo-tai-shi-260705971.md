---
title: Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal
  Reranking
title_zh: 基于语义检索与时序重排的多模态视频配乐推荐框架
authors:
- Seungheon Doh
- Minhee Lee
- Sangmoon Lee
- Ben Sangbae Chon
- Juhan Nam
affiliations:
- KAIST, South Korea
- Gaudio Lab, Inc, South Korea
arxiv_id: '2607.05971'
url: https://arxiv.org/abs/2607.05971
pdf_url: https://arxiv.org/pdf/2607.05971
published: '2026-07-07'
collected: '2026-07-08'
category: RecSys
direction: 多模态内容推荐 · 两阶段检索重排架构
tags:
- Multimodal Recommendation
- Cross-modal Alignment
- Retrieval
- Reranking
- Temporal Modeling
one_liner: 提出两阶段多模态视频配乐推荐框架，结合全局语义检索与时序对齐重排提升匹配效果
practical_value: '- 跨模态匹配场景可复用「粗检索+细重排」两阶段架构：先用全局粗Embedding降本召回候选集，再做细粒度特征对齐优化排序效果，平衡效率与精度

  - 短视频/直播等带有时序属性的内容匹配场景，可引入跨模态时序注意力捕捉动态特征对应关系，比如直播背景乐匹配、短视频带货BGM推荐业务可直接落地

  - 多模态融合时可先对齐音视文三模态到联合表征空间，降低跨模态语义gap，适合电商内容的图文音跨模态检索、素材推荐等场景'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
短视频、直播等场景下的背景乐匹配需要同时满足语义兼容性（风格、情绪匹配）与时序动态对齐（画面节奏与音乐节拍匹配），现有方案难以同时兼顾效率与匹配精度。
### 方法关键点
提出VTMR两阶段框架：1）第一阶段将视频的音、视、文多模态信号与音乐信号对齐到联合表征空间，基于全局粗Embedding快速召回语义匹配的候选音乐；2）第二阶段引入时序注意力机制，同时建模视频与音乐的时序序列特征，对候选集做重排捕捉细粒度时序对应关系。
### 关键结果
对比最强基线，第一阶段检索将R@10从14.2提升至15.9，中位排名从75降至58；叠加时序重排后R@10进一步提升至18.3，中位排名降至46；人类偏好评估显示整体效果与商业基线持平，音乐质量优于生成式基线。
