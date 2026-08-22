---
title: 'ID-VTG: Image-Disambiguated Video Temporal Grounding'
title_zh: ID-VTG：结合参考图像消歧的视频时序定位方法
authors:
- Minghang Zheng
- Jingli Wei
- Hongyi Yang
- Yang Liu
affiliations:
- Wangxuan Institute of Computer Technology, Peking University
- State Key Laboratory of General Artificial Intelligence, Peking University
arxiv_id: '2608.20127'
url: https://arxiv.org/abs/2608.20127
pdf_url: https://arxiv.org/pdf/2608.20127
published: '2026-08-20'
collected: '2026-08-22'
category: Multimodal
direction: 多模态时序定位 · 跨模态消歧
tags:
- Video Temporal Grounding
- Cross-Modal Disambiguation
- Multimodal Query
- Dual-Branch Architecture
- Multimodal Retrieval
one_liner: 提出参考图像+文本的多模态查询VTG任务，构建双基准与快慢双分支VGD-Agg消歧框架
practical_value: '- 电商短视频种草/商品识别场景，可复用快慢双分支架构做粗召回+细匹配的商品片段定位，平衡效率与精度

  - 处理语义模糊的用户查询（如同款商品检索），可借鉴「参考图+文本」的多模态查询范式，降低纯文本消歧成本

  - 召回排序流程可引入Compare Token+负样本打压的设计，提升相似实体/商品的区分度，减少误召回'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有Video Temporal Grounding（VTG）依赖纯文本查询，当事件涉及多个视觉相似实体时，细粒度视觉属性难以通过文字准确描述，消歧难度极高。
### 方法关键点
1. 引入Image-Disambiguated VTG任务，采用「参考图像+文本」的多模态查询范式，精准定位特定实例执行描述动作的视频片段
2. 构建两个公开基准：针对细粒度体操动作的IDVTG-Gym、覆盖多类实体的开放世界数据集IDVTG-InternVid
3. 推出VGD-Agg快慢双分支框架：快分支高效生成初步候选事件，慢分支做视频帧与参考图的细粒度帧级匹配；新增Compare Token探测目标实例是否存在，用Depress Value打压无目标的候选，提升区分度
### 关键结果
方法在两个自建基准上均达到SOTA性能
