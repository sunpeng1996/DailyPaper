---
title: 'UniSpark: Exploring Hybrid Attention for Multimodal Understanding and Generation'
title_zh: UniSpark：面向多模态理解与生成的混合注意力架构研究
authors:
- Jiancheng Pan
- Yuzheng Liu
- Hengyuan Cao
- Qiyuan Zhang
- Yangyan Li
- Biao Gong
- Zheng Zhang
- Ka Long Cheng
- Xinyang Wang
- Yujun Shen
affiliations:
- Lucaria Academy
arxiv_id: '2611.16517'
url: https://arxiv.org/abs/2611.16517
pdf_url: https://arxiv.org/pdf/2611.16517
published: '2026-11-11'
collected: '2026-11-13'
category: Multimodal
direction: 多模态大模型 · 混合注意力架构
tags:
- Multimodal-LLM
- Hybrid Attention
- MoE
- Linear Attention
- Flow Matching
one_liner: 基于混合注意力+MoE骨干的9B统一多模态模型，兼容理解、2K图文生成与编辑多任务
practical_value: '- 混合注意力架构可迁移至多模态生成式推荐场景：用全注意力建模用户-商品显式交互、线性注意力压缩用户长行为序列，降低推理时延

  - 四阶段课程训练方法可复用至多模态推荐模型训练，平衡语义理解、内容生成两类任务的收敛效果与性能

  - 2K高精度图文生成、编辑能力可直接接入电商商品主图生成、AI搭配Agent的作图/修图链路'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态模型通常拆分理解、生成任务设计，难以同时支撑交错图文生成、指令引导编辑等复杂场景，且长上下文推理开销高。
### 方法关键点
1. 基于单分支9B参数量的MoE骨干，融合全注意力（显式token交互）+GatedDeltaNet线性注意力（紧凑上下文传播）的混合注意力架构；
2. 联合自回归文本预测与视觉流匹配，覆盖VQA、文生图、指令编辑、交错图文预测多任务；
3. 块级协议通过注意力掩码、循环状态保留规则隔离噪声视觉表征，避免错误传递；
4. 四阶段课程训练，使用159.7M生成样本、213.4M理解样本、624.8K交错序列训练。
### 关键结果
MME-S得分2470.3，GenEval得分0.83，支持2K分辨率图像合成、视频生成与编辑，多模态任务性能优于同量级基线
