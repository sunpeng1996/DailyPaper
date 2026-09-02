---
title: 'DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution'
title_zh: DreamX-Creator 1.0：面向普适场景的2K分辨率原生音视频联合生成系统
authors:
- Jiashu Zhu
- Yanhao Zheng
- Ruitian Tian
- Rujing Dang
- Shen Zhang
- Bingze Song
- Jiachen Lei
- Ruimin Lin
- Jiahong Wu
- Xiangxiang Chu
affiliations:
- DreamX Team, Alibaba Group
arxiv_id: '2608.31106'
url: https://arxiv.org/abs/2608.31106
pdf_url: https://arxiv.org/pdf/2608.31106
published: '2026-08-30'
collected: '2026-09-02'
category: Multimodal
direction: 多模态生成 · 音视频联合生成
tags:
- Multimodal Generation
- Audio-Video Generation
- Diffusion Model
- Knowledge Distillation
- Reinforcement Learning
one_liner: 基于7B参数模型实现原生同步音视频生成，搭配1步2K精修管线性能比肩开源SOTA
practical_value: '- 门控跨模态注意力设计可直接复用至多模态推荐的特征融合环节，平衡单模态特征独立性与跨模态关联信息

  - 分阶段渐进式联合训练+模态感知反馈RL的策略，可迁移至多模态商品素材生成模型的训练优化，降低训练不稳定性

  - 多步教师蒸馏为单步学生的超分管线，可复用在电商短视频/商品图的高清化推理环节，大幅降低推理耗时

  - 按能力分层组织多模态训练数据集的思路，可借鉴至多模态推荐模型的训练集构建，针对性提升不同场景性能'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频生成方案大多省略音频或分阶段独立合成音视频，无法建模视觉动态与声学事件的双向关联，且高分辨率生成推理成本高、落地门槛高。
### 方法关键点
1. 基于7B参数生成基座，前半段网络独立处理音视频单模态流，后半段通过门控跨模态注意力实现模态耦合，支持首帧+文本prompt输入的联合去噪；
2. 构建统一音视频数据系统，过滤时序连贯片段、生成结构化多模态标注，按能力维度划分数据池；
3. 采用渐进式联合训练+模态感知多模态反馈RL优化，2K精修阶段将多步双向教师模型蒸馏为单步自回归学生，每时间块仅需1次去噪计算。
### 关键结果
原生同步音视频生成性能比肩开源SOTA，开源7B生成器与2K精修模型大幅降低音视频生成落地门槛
