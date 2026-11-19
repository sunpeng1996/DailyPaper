---
title: 'AVTR: Adaptive Multimodal Reasoning with Visual Imagination'
title_zh: AVTR：引入视觉想象的自适应多模态推理框架
authors:
- Xiaoqian Shen
- Yunyang Xiong
- Changsheng Zhao
- Saksham Suri
- Chong Zhou
- Zechun Liu
- Zhipeng Cai
- Zhuang Liu
- Qi Qian
- Wei Wen
affiliations:
- Meta AI
- King Abdullah University of Science and Technology
- Princeton University
arxiv_id: '2611.24161'
url: https://arxiv.org/abs/2611.24161
pdf_url: https://arxiv.org/pdf/2611.24161
published: '2026-11-18'
collected: '2026-11-19'
category: Reasoning
direction: 多模态推理 · 自适应路由
tags:
- Multimodal-Reasoning
- Vision-Language-Model
- Adaptive-Routing
- Visual-Imagination
- Latent-Reasoning
one_liner: 引入训练时监督的视觉想象模态，通过自适应路由实现多模态推理精度与效率双提升
practical_value: '- 电商多模态搜索/商品理解场景可复用「训练时生成监督、推理时移除生成器」的设计，既强化视觉感知能力又不增加推理开销，适配高吞吐量线上场景

  - 自适应路由思路可迁移到推荐系统多通路排序架构，按query/用户特征动态选择召回/排序通路，平衡精度与延迟：简单请求走短通路，复杂请求走长通路

  - 视觉想象的任务相关特征蒸馏方法可用于商品图细粒度理解、短视频内容分析，自动定位任务相关的视觉区域/视频帧，提升识别准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Vision-Language Model (VLM)仅依赖文本模态推理，在视觉感知密集任务（如空间推理、视频帧定位）上性能瓶颈显著，且全局统一使用长文本推理会产生大量冗余计算，延迟高，无法兼顾推理精度与效率。

### 方法关键点
- 提出视觉想象模块，训练时通过视觉重放（重建输入图像）、视觉反射（生成问题相关的视觉目标）两步对齐VLM特征与视觉生成空间，推理时移除生成器组件，直接用学习到的视觉隐状态做推理，无像素生成额外开销
- 设计自适应路由机制，将推理模态选择建模为带成本约束的路由问题，动态选择「直接回答、视觉想象、文本推理、视觉+文本组合」4种通路，同时用路由损失优化通路选择、GRPO优化各通路内的推理效果
- 视觉查询采用并行处理设计，无需逐token生成隐状态，大幅降低视觉推理的额外延迟

### 关键实验
在16个多模态基准（覆盖高分辨率图像理解、空间推理、视频理解、时序定位4类任务）上测试，对比Qwen3.5基线，平均得分提升4.5个点，推理延迟降低33%；在2B小参数量基线上平均得分提升6.3个点，性能优于同规模所有开源基线。

### 核心结论
视觉想象与文本推理存在明确互补性：视觉模态擅长感知类任务，文本模态擅长逻辑关系推理，自适应选择而非固定使用某一种模态才能同时实现精度与效率最优
