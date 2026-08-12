---
title: 'StreamFlow: Dynamic Memory Flows for Streaming Video Understanding'
title_zh: StreamFlow：面向流式视频理解的动态内存流框架
authors:
- Muxin Fu
- Yifan Zhang
- Wentao Zhang
- Fangming Guo
- Qian Chen
- Guibin Zhang
- Shuicheng Yan
- Bo An
affiliations:
- Tongji University
- Nanyang Technological University
- University of Michigan
- The Hong Kong University of Science and Technology
- National University of Singapore
arxiv_id: '2608.10949'
url: https://arxiv.org/abs/2608.10949
pdf_url: https://arxiv.org/pdf/2608.10949
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 多模态大模型 · 流式视频高效理解
tags:
- Multimodal LLM
- Streaming Video
- Dynamic Memory
- Efficient Inference
- Video Understanding
one_liner: 提出分层动态视觉内存框架StreamFlow，低延迟低内存下实现SOTA流式视频理解
practical_value: '- 电商直播实时理解场景可复用分层内存设计：先对冗余直播帧过滤再编码，大幅降低推理延迟与算力成本

  - 多模态Agent流式感知模块可借鉴注意力引导的历史潜向量检索机制，提升视觉信息利用效率的同时控制内存占用

  - 长视频内容理解召回场景可复用潜向量长期内存压缩方案，无需微调大模型backbone即可适配长时序输入'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：流式视频理解要求MLLM在严格因果性、有限内存约束下留存连续流中的有效信息，现有方案要么需要侵入式更新backbone，要么冗余视觉编码算力开销大、历史视觉信息访问逻辑僵化，无法适配实时场景需求。
**方法关键点**：StreamFlow设计三层核心机制：1）轻量动态感知中期内存，在视觉编码前过滤时序冗余帧；2）潜向量长期内存，将历史视频内容压缩为可访问的视觉潜向量；3）注意力引导检索机制，生成阶段当模型视觉证据依赖度下降时自动注入相关历史潜向量，无需修改模型主干。
**关键结果**：StreamingBench上整体准确率达67.73%，为当前SOTA；相比基线方案，视觉注意力得分提升59.1%，端到端延迟降低50.4%，峰值内存占用降低21.1%，同时在离线长视频基准上也有优异表现。
