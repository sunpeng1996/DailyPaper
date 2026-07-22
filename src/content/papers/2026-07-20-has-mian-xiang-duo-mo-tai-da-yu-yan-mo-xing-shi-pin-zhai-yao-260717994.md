---
title: 'HAS: Highlight-guided Attention Steering for Multimodal LLM Video Summarization'
title_zh: HAS：面向多模态大语言模型视频摘要的高亮引导注意力调控方法
authors:
- Rui Chu
- Yingjie Lao
affiliations:
- Tufts University
arxiv_id: '2607.17994'
url: https://arxiv.org/abs/2607.17994
pdf_url: https://arxiv.org/pdf/2607.17994
published: '2026-07-20'
collected: '2026-07-22'
category: Multimodal
direction: 多模态LLM · 视频摘要优化
tags:
- Multimodal-LLM
- Video-Summarization
- Attention-Steering
- Highlight-Distribution
- Inference-Optimization
one_liner: 提出高亮引导的注意力调控方法HAS，优化多模态LLM连续视频输入的摘要效果
practical_value: '- 电商商品短视频/直播切片摘要场景可复用HAS思路：全局计算连续帧重要性分布，替代硬剪关键帧，保留完整信息连贯性

  - 多模态LLM推理优化可借鉴注意力调控trick：高价值输入片段加权提权，低价值片段降权而非丢弃，平衡效果与计算效率

  - 短视频卖点自动提取、商品内容理解场景可直接适配连续帧高亮分布计算模块，替换传统离散关键帧选择逻辑'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态LLM（M-LLM）视频摘要方案普遍依赖离散关键帧选择策略，易破坏内容理解连贯性、丢失边缘信息，也浪费了M-LLM的原生长序列理解能力。
### 方法关键点
高亮引导的注意力调控方法HAS核心分为两模块：
1. 全局建模生成视频的连续帧级高亮分布，无需提前筛选离散关键帧；
2. 将高亮分布作为注意力调控向量输入M-LLM，推理阶段给高亮点帧分配更高注意力权重，非高亮帧仅降低注意力权重而非完全丢弃，保留全局信息完整性。
### 关键结果
在多个公开视频摘要基准数据集上显著优于现有离散选帧方案，验证了连续注意力调控的有效性。
