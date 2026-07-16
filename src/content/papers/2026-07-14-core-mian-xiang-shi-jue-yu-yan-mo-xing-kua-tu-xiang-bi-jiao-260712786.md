---
title: 'CoRe: A Comprehensive Framework for Cross-Image Comparative Reasoning in Vision-Language
  Models'
title_zh: CoRe：面向视觉语言模型跨图像比较推理的通用框架
authors:
- Lin Peng
- Cong Wan
- Zeyu Guo
- SongLin Dong
- Yihong Gong
affiliations:
- Xi'an Jiaotong University
arxiv_id: '2607.12786'
url: https://arxiv.org/abs/2607.12786
pdf_url: https://arxiv.org/pdf/2607.12786
published: '2026-07-14'
collected: '2026-07-16'
category: Multimodal
direction: 多模态大模型 · 跨图像比较推理
tags:
- VLM
- Cross-image Reasoning
- GRPO
- Multimodal Training
- Evaluation Benchmark
one_liner: 提出跨图像比较推理框架CoRe，含专用训练集、结构化奖励与评测基准，较最优基线精度提升28.2个点
practical_value: '- 可复用TriSR结构化奖励框架，优化电商多模态Agent的商品属性对比、同款差异判别能力，提升导购准确率

  - 可借鉴多专家协作自动构建训练集的思路，低成本生成电商商品跨图比对、属性校验的专用训练数据

  - CoRe-Bench的评测维度可迁移到多模态商品搜索推荐的效果评测，补充细粒度属性比对的评测指标'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前VLM在跨图像比较推理场景表现薄弱，无法满足细粒度attribute grounding、全局一致性推理的要求，同时缺少专用训练数据集与标准化评测基准。
### 方法关键点
1. 自动构建CoRe-20K大规模三元组训练集，通过多专家协作管道从结构化视觉元数据生成，覆盖计数、深度、距离、空间关系4类核心任务；
2. 提出TriSR结构化奖励框架，基于GRPO优化，联合监督属性对齐、判断对齐、三元组一致性三个维度的效果；
3. 发布首个细粒度跨图像比较推理专用评测基准CoRe-Bench。
### 关键结果
在CoRe-Bench上较最强基线实现28.2个百分点的部分精度提升，同时在标准多模态基准上保持竞争力。
