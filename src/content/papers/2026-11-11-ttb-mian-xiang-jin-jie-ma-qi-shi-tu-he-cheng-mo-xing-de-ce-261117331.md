---
title: 'TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis
  Models'
title_zh: TTB：面向仅解码器视图合成模型的测试时烘焙高效渲染方法
authors:
- Chin-Yang Lin
- Ryo Hachiuma
- Jaesung Choe
- Min-Hung Chen
- Yu-Chiang Frank Wang
- Yen-Yu Lin
- Wei-Chen Chiu
- Yu-Lun Liu
- Cheng Sun
affiliations:
- NVIDIA
- 国立阳明交通大学计算机科学系
arxiv_id: '2611.17331'
url: https://arxiv.org/abs/2611.17331
pdf_url: https://arxiv.org/pdf/2611.17331
published: '2026-11-11'
collected: '2026-11-14'
category: Other
direction: 仅解码器视图合成 · 测试时推理优化
tags:
- KV-cache
- Test-Time Optimization
- Decoder-only
- Efficient Inference
- MLP
one_liner: 提出测试时烘焙TTB策略，将跨视图注意力信息烘焙进轻量MLP，实现23倍渲染提速
practical_value: '- 测试时将高开销注意力映射预烘焙进轻量MLP的思路，可迁移至LLM4Rec/多模态搜索的KV cache冗余计算优化

  - 上下文输入输出解耦消除模态错位的方案，可复用在多模态推荐的跨模态泛化能力提升场景

  - 不替换原有核心模块、仅额外学习映射关系的轻量化适配思路，可降低业务模型迭代的改造成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
仅解码器大视图合成模型（LVSM）借助KV cache实现SOTA生成质量，但现有测试时训练（TTT）加速方案会显著损失生成效果，同时存在上下文预填充与新视图渲染的模态错位问题，限制落地效率。
### 方法关键点
1. 复用TTT的快速权重MLP，显式学习跨视图注意力的输入输出映射而非完全替换注意力模块，兼顾推理效率与生成质量；
2. 解耦上下文token为仅含相机参数的渲染token（作为TTB输入）和带图像内容的真值token（作为映射目标），消除模态泛化负担。
### 关键结果
在多个公开基准上实现最高23倍渲染提速，生成质量与当前SOTA模型持平，推理效率与效果的权衡达到帕累托最优。
