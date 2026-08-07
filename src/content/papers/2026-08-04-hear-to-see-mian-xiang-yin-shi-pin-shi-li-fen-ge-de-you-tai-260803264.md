---
title: 'Hear to See: Discerning Stateful Listening for Audio-Visual Instance Segmentation'
title_zh: Hear to See：面向音视频实例分割的有状态听觉感知方法
authors:
- Leiye Liu
- Miao Zhang
- Jiahong Jiang
- Jingjing Li
- Jialong Zhong
- Kai Peng
- Tingwei Liu
- Wei Ji
- Yongri Piao
- Huchuan Lu
affiliations:
- Dalian University of Technology
- Carnegie Mellon University
- Yale University
arxiv_id: '2608.03264'
url: https://arxiv.org/abs/2608.03264
pdf_url: https://arxiv.org/pdf/2608.03264
published: '2026-08-04'
collected: '2026-08-07'
category: Multimodal
direction: 多模态 · 音视频实例分割
tags:
- Audio-Visual Instance Segmentation
- Mamba
- Cross-Modal Alignment
- Multimodal Learning
- Temporal Modeling
one_liner: 提出ASP与音频调制Mamba的ADM模块，解决音视频实例分割的声源匹配与时序异步问题，超基线7.8%mAP
practical_value: '- 直播场景多模态内容审核可复用ASP跨模态语义到空间的层级对齐思路，精准匹配直播语音发声主体与画面物体

  - 处理多模态异步输入（如用户语音搜索+画面跳转不同步）时，可借鉴ADM的音频调制Mamba自适应状态转移逻辑，提升感知鲁棒性

  - 短视频内容标签生成场景可复用混合音频解耦方法，精准匹配不同发声物体对应的内容标签'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频实例分割（AVIS）存在两大核心痛点：一是重叠声学事件无法精准匹配对应视觉实例，二是音视频信号时序不对齐时跟踪鲁棒性差，难以输出像素级发声物体掩码。
### 方法关键点
1. 设计Acoustic-Semantic Projector（ASP）模块，对混合音频做解耦，建立从语义域到空间域的层级跨模态对应关系；
2. 提出Asynchronous Dynamics Modulator（ADM）模块，基于音频调制的Mamba自适应调整状态转移，动态变化阶段优先处理当前信息，稳定阶段维持时序连续性。
### 关键结果
在AVISeg数据集上达到SOTA性能，使用COCO预训练ResNet50时mAP达48.54，较之前最优方案提升7.8%。
