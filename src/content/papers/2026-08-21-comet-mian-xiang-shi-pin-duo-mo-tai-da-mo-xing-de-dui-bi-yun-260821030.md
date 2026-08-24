---
title: 'COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal
  Large Language Models'
title_zh: COMET：面向视频多模态大模型的对比运动增强时序推理
authors:
- Chenghua Zhu
- Zhaolu Kang
- Qifan Shi
- Siyan Wu
- Kehan Jiang
- Lei Wei
- Lianyu Hu
- Guangyuan Dong
- Mingbo Yang
- Rui Lu
affiliations:
- 北京大学
- 华南理工大学
- 华南师范大学
- 南洋理工大学
- 新加坡国立大学
arxiv_id: '2608.21030'
url: https://arxiv.org/abs/2608.21030
pdf_url: https://arxiv.org/pdf/2608.21030
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 视频多模态大模型 · 时序推理优化
tags:
- Video MLLM
- Temporal Reasoning
- Motion Representation
- Multimodal Fusion
- Contrastive Learning
one_liner: 提出融合显式运动表征与时序方向优化的视频MLLM框架COMET，显著提升动作与时序推理性能
practical_value: '- 短视频推荐/广告的内容理解场景，可复用泰勒帧差构建轻量显式运动分支，无需重训视觉编码器即可补充时序运动特征，降低建模成本

  - 涉及时序逻辑的多模态任务，可借鉴TC-GRPO正反序对比训练思路，将时序顺序作为直接监督信号，提升模型时序方向敏感度，减少逻辑错误

  - 多模态底座优化可复用「显式特征注入+专项知识蒸馏+对比对齐」的三层范式，无需大幅改动底座结构即可获得稳定的跨模型性能增益'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前Video MLLM细粒度运动-时序理解能力薄弱，核心瓶颈不仅是稀疏帧采样，更缺乏完整时序建模pipeline，无法显式表征帧间变化、实现外观-运动交互、优化时序方向敏感度。
### 方法关键点
1. 架构层面引入基于泰勒帧差的时序运动分支，通过时序注意力偏置增强的交叉注意力，将运动特征注入外观流，实现外观-运动特征交互
2. 优化层面结合时序先验蒸馏、正反序TC-GRPO训练阶段，把时序顺序作为直接学习信号，强化模型对方向运动模式的利用
### 关键结果
在Qwen3-VL-8B上，动作类任务（STAR、SSv2）平均提升4.9%，时序推理任务（NExT-QA、CLEVRER等）较BL-GRPO提升2.1%，静态感知任务性能持平；同等增益可迁移到InternVL2.5-8B，跨模型泛化性优异。
