---
title: 'CADER: Confidence-Aware Dynamic Evidence Reasoning for Long-Video Understanding'
title_zh: CADER：面向长视频理解的置信度感知动态证据推理框架
authors:
- Jinlong Yang
- Wenhao Zhang
- Kuanwei Lin
- Sijie Cheng
affiliations:
- 西北工业大学计算机学院
- 北京大学电子与计算机工程学院
- 清华大学计算机科学与技术系
arxiv_id: '2607.24582'
url: https://arxiv.org/abs/2607.24582
pdf_url: https://arxiv.org/pdf/2607.24582
published: '2026-07-27'
collected: '2026-07-28'
category: Multimodal
direction: 多模态长视频推理 · 自适应工具调用
tags:
- VideoQA
- Multimodal Reasoning
- Adaptive Inference
- Tool Augmented LLM
- Confidence Estimation
one_liner: 免训练的置信度感知自适应长视频推理框架，按样本难度动态调用工具，性能媲美专用增强方案
practical_value: '- 可复用置信度感知早停架构：在电商商品短视频质检、用户视频评论理解等场景，先做全局轻量推理，高置信样本直接输出，大幅降低推理成本

  - 样本级动态工具调用逻辑可迁移到Agent系统：简单query直接返回结果，复杂query才调用搜索、知识库等工具，平衡性能与开销

  - logit-margin置信度估计方法无需额外训练，可快速集成到现有多模态大模型推理链路，降低落地成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前长视频理解系统对所有样本采用统一推理流程，简单样本不必要调用工具浪费算力，复杂样本又缺乏细粒度时序证据支撑，无法平衡推理效率与效果。
### 方法关键点
提出免训练的CADER自适应推理框架：① 第一阶段对均匀采样帧做全局推理，通过logit-margin信号计算答案置信度，高置信样本直接早停输出；② 低置信样本进入第二阶段工具增强循环，结合时序裁剪、轻量语义验证、相关性引导重采样逐步定位问题相关证据，仅对难样本调用额外处理能力。
### 关键结果
在多个VideoQA基准上实现长视频推理性能提升，高置信样本可跳过第二阶段；基于仅用无工具思维链监督训练的backbone，即可达到专用工具增强框架的同等竞争力，推理成本显著降低。
