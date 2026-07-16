---
title: Let RGB Be the Language of Vision
title_zh: 让RGB成为视觉的通用语言
authors:
- Timing Yang
- Jinrui Yang
- Xinlong Li
- Yuhan Wang
- Haoran Li
- Yanqing Liu
- Guoyizhe Wei
- Jixuan Ying
- Chen Wei
- Rama Chellappa
affiliations:
- Johns Hopkins University
- UC Santa Cruz
- Carnegie Mellon University
- Rice University
arxiv_id: '2607.12450'
url: https://arxiv.org/abs/2607.12450
pdf_url: https://arxiv.org/pdf/2607.12450
published: '2026-07-13'
collected: '2026-07-16'
category: Multimodal
direction: 多模态视觉统一表征范式
tags:
- Unified Vision Model
- RGB Representation
- Zero-shot Learning
- Cross-task Transfer
- Image Editing
one_liner: 提出RGB输入输出的统一视觉范式RINO，无需任务微调即可跨多视觉任务取得有竞争力的零样本性能
practical_value: '- 多模态内容处理可参考RINO的统一接口思路，将图像、掩膜、深度图等不同视觉输入统一转为RGB格式，减少定制化编码器开发成本

  - 电商商品生成/属性识别等多任务视觉场景，可复用RGB-to-RGB统一范式，用单模型支撑分割、深度估计、姿态生成等多任务，降低部署复杂度

  - 多模态Agent的视觉交互模块可借鉴该统一表征方案，减少不同视觉任务间的格式适配开销，提升交互灵活性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉领域不同类型视觉信息（自然图像、分割掩膜、深度图等）表征不统一，各任务需单独设计专属编码器、解码器及适配组件，无法像LLM基于文本统一接口实现跨任务灵活复用，阻碍通用视觉系统落地。

### 方法关键点
提出RGB In and RGB Out（RINO）统一范式：将所有结构化视觉信号统一表示为RGB图像，把各类视觉任务转化为通用RGB-to-RGB图像编辑问题，不同视觉任务共享同一套通用图像编辑骨干的编解码架构与参数，无需任务特定微调。

### 关键结果
在分割、深度估计等密集视觉理解任务，以及姿态到图像生成等条件生成任务上，RINO的零样本性能达到行业可比水平，可实现单模型跨任务自由迁移。
