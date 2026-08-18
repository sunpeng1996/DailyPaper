---
title: MOSS-VL Technical Report
title_zh: MOSS-VL：支持边生成边感知的开源视觉语言模型技术报告
authors:
- Pengyu Wang
- Chenkun Tan
- Shaojun Zhou
- Qirui Zhou
- Yanxin Chen
- Xingyang He
- Huazheng Zeng
- Jijun Cheng
- Chenghao Wang
- Xiaomeng Qian
affiliations:
- OpenMOSS Team
- 复旦大学
arxiv_id: '2608.15045'
url: https://arxiv.org/abs/2608.15045
pdf_url: https://arxiv.org/pdf/2608.15045
published: '2026-08-14'
collected: '2026-08-18'
category: Multimodal
direction: 实时多模态大模型 · 边生成边感知
tags:
- Vision-Language Model
- Real-time Interaction
- Gated Cross-Attention
- Streaming Inference
- Multimodal LLM
one_liner: 跨栈协同设计的开源视觉语言模型族，支持生成时同步感知视觉输入，实时交互性能领先开源基线
practical_value: '- 实时交互场景（如直播智能助理、实时内容审核Agent）可复用其门控交叉注意力设计，仅在语言解码侧按需关联视觉token，大幅降低长视觉上下文下的首包延迟

  - 多轮交互类Agent的训练可参考其分层课程学习方案，先完成基础能力预训练，最后仅用轻量阶段微调实时交互相关的沉默/发言/修正决策逻辑，降低训练成本

  - 直播带货场景的实时卖点提取、异常行为告警等需求，可直接复用其开源的实时推理代码和预训练checkpoint，降低多模态Agent落地门槛'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有开源视觉语言模型多为离线处理逻辑，生成回复时无法同步感知新输入的视觉帧，无法满足直播、智能监控等场景下「边生成边感知」的实时交互需求。

### 方法关键点
1. 跨栈协同设计：语言解码器仅通过门控交叉注意力关联视觉信息，视觉token放在解码序列外，支持生成过程中动态读取新输入帧；
2. 构造专用交互语料，监督模型学习何时发言、沉默、修正回复的决策逻辑；
3. 采用分层课程训练：先完成离线基础能力训练，最后仅用轻量阶段微调实时交互专属能力。

### 关键结果
- 离线版本在同规模模型中性能持平竞品，时序推理视频任务表现领先；
- 实时版本在4个流处理基准中3个平均得分第一，OmniMMI主动告警任务得分66.0，远超最优基线的37.5；
- 11.3B参数量版本随视觉上下文增长，首token延迟优势从同骨干Qwen3-VL-8B的2.8倍提升至5.1倍。
