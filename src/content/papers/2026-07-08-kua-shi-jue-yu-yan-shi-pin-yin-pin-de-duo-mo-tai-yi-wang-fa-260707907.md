---
title: 'Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of
  Methods, Datasets, and Benchmarks'
title_zh: 跨视觉/语言/视频/音频的多模态遗忘方法、数据集与基准综述
authors:
- Nobin Sarwar
- Shubhashis Roy Dipta
- Zheyuan Liu
- Vaidehi Patil
affiliations:
- University of Maryland, Baltimore County
- University of Notre Dame
- UNC Chapel Hill
arxiv_id: '2607.07907'
url: https://arxiv.org/abs/2607.07907
pdf_url: https://arxiv.org/pdf/2607.07907
published: '2026-07-08'
collected: '2026-07-11'
category: Multimodal
direction: 多模态基础模型 · 遗忘技术综述
tags:
- Multimodal Unlearning
- VLM
- Foundation Model
- Model Safety
- Survey
one_liner: 系统梳理多模态遗忘技术体系，给出统一分类框架、权衡分析及配套开源资源库
practical_value: '- 电商多模态推荐/生成系统迭代中，可参考本文的4类干预点分类，快速定位版权/敏感内容遗忘的技术选型，避免全量重训成本

  - 多模态Agent合规优化时，可参考本文给出的5维度权衡框架，匹配不同业务场景的合规要求与性能约束

  - 可复用论文配套的开源资源库，直接获取成熟的多模态unlearning baseline方法，降低自研门槛'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态基础模型（VLM、DM、LLM、AFM等）训练过程中会从数据中编码敏感、版权、偏见、不安全的跨模态关联，收到删除请求或政策更新时全量重训成本极高，且分布式表征下定向遗忘难度大。
### 方法关键点
从系统视角梳理了跨视觉、语言、音频、视频的多模态unlearning技术体系，构建统一分类框架，覆盖数据侧、训练时、架构约束、解码时4类干预点，支持不同架构、模态下方法的系统性对比。
### 关键结果
明确了不同方法在删除强度、效用保留、效率、可逆性、鲁棒性五个维度的权衡关系，配套开源了精选多模态unlearning资源库，梳理了落地实践要点与开放问题。
