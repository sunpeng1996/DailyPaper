---
title: 'eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings
  and Large Archives via e-means'
title_zh: eDIAR：基于e-means的免训练开放说话人流式分割方法，适配长会议与大型语料库
authors:
- Kyudan Jung
- Jihwan Kim
- Minwoo Lee
- Eunji Shin
- Jaegul Choo
affiliations:
- KAIST AI
- Ewha W. University
arxiv_id: '2611.18529'
url: https://arxiv.org/abs/2611.18529
pdf_url: https://arxiv.org/pdf/2611.18529
published: '2026-11-12'
collected: '2026-11-16'
category: Other
direction: 说话人分割 · 免训练流式聚类算法
tags:
- SpeakerDiarization
- TrainingFree
- Streaming
- Clustering
- e-means
one_liner: 免训练突破固定槽位说话人分割模型人数上限，长会议精度高、聚类速度比k-means快数倍
practical_value: '- 电商智能客服/会议Agent的说话人分割模块可复用免训练改造思路，无需重训固定槽位模型即可适配多说话人场景

  - 大规模会话语料标注时可替换k-means用e-means做说话人embedding聚类，速度提升数倍且质量持平

  - 流式处理场景可复用「限定窗口重聚类+槽位锚定」设计，控制单步更新开销不随会话时长增长'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有固定槽位流式说话人分割模型精度高、支持在线推理，但无法支持超出槽位数量的说话人，长会议场景误差累积严重，大规模语料的说话人聚类效率低。
### 方法关键点
1. 免训练改造：原有模型槽位全部占满后，调用e-means对单个槽位内的说话人embedding聚类，突破人数上限；
2. 流式优化：重聚类限定在固定窗口内，仅修正数秒内的标签，说话人身份锚定到模型输出槽位，控制更新开销；
3. e-means默认参数即可适配数百到百万级embedding的聚类任务，无需额外调参。
### 关键结果
长会议场景精度远高于Streaming Sortformer，单步更新开销不随会议时长增长；可直接将4槽位Streaming Sortformer改造为开放说话人系统；e-means聚类质量与Lloyd's k-means持平，速度快数倍
