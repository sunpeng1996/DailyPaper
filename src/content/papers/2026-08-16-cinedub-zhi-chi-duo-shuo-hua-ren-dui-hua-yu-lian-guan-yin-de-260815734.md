---
title: 'CineDub: Scaling End-to-End Video Dubbing to Multi-Speaker Dialogues with
  Coherent Sound Effects'
title_zh: CineDub：支持多说话人对话与连贯音效的端到端视频配音框架
authors:
- Yusheng Dai
- Kangdi Wang
- Baolong Gao
- Yuxuan Jiang
- Weiqiang Wang
- Qiuhong Ke
- Jianfei Cai
affiliations:
- Monash University
- University of Chinese Academy of Sciences
- Tsinghua University
arxiv_id: '2608.15734'
url: https://arxiv.org/abs/2608.15734
pdf_url: https://arxiv.org/pdf/2608.15734
published: '2026-08-16'
collected: '2026-08-20'
category: Multimodal
direction: 跨模态生成 · 音视频联合生成
tags:
- Diffusion Model
- Cross-Modal Learning
- Curriculum Learning
- Multi-Speaker Generation
- Video-to-Audio
one_liner: 提出基于扩散的统一多说话人视频配音框架，无需人脸裁剪与分轨，支持语音音效联合生成
practical_value: '- 隐式跨模态耦合（ICHC）范式可迁移至多模态内容生成类业务，无需显式的多模态对齐/分轨预处理，大幅降低管线复杂度与落地成本

  - Ambient-to-Linguistic Curriculum Learning（ALC）可复用至多任务联合生成场景，有效缓解不同子任务间的性能退化问题

  - 解耦文本分支控制机制可直接应用于多prompt联合生成任务，解决不同输入prompt间的交叉干扰问题'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频配音方案存在两类核心缺陷：分层方法依赖多阶段预处理管线，鲁棒性差、数据扩展性弱、部署难度高；全局方法直接处理未裁剪视频，多说话人场景下时序对齐误差大、说话人与话语的对应歧义高。
### 方法关键点
1. 基于扩散模型构建统一配音框架，无需人脸裁剪、说话人分轨预处理，直接从原始未裁剪视频生成精准多说话人对话配音；
2. 核心采用ICHC范式：全局视觉表征、语义绑定转录文本独立编码，通过跨模态训练隐式耦合，解决多说话人歧义问题；
3. 扩展支持语音+音效联合生成，引入ALC课程学习缓解子任务性能退化，设计解耦文本分支控制机制解决多prompt交叉干扰；
4. 开源CineDub-Multi、CineDub-SA两个真实场景基准数据集。
### 关键结果
在公开单说话人配音、视频转音频基准上达到SOTA，多说话人对话配音、语音音效联合生成性能显著优于现有方案。
