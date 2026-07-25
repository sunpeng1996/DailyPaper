---
title: Detecting LLM-Generated Tokens in Human--LLM Coauthored Text
title_zh: 人-LLM合著文本中的LLM生成token细粒度检测方法
authors:
- Yangjun Lu
- Hongyi Zhou
- Fabian Spill
- Kai Ye
- Chengchun Shi
- Jin Zhu
affiliations:
- School of Mathematics, University of Birmingham
- School of Statistics and Data Science, Shanghai University of Finance and Economics
- Department of Statistics, The London School of Economics and Political Science
arxiv_id: '2607.21458'
url: https://arxiv.org/abs/2607.21458
pdf_url: https://arxiv.org/pdf/2607.21458
published: '2026-07-23'
collected: '2026-07-25'
category: LLM
direction: LLM生成内容检测 · 细粒度token级定位
tags:
- LLM Detection
- Token-level Classification
- Kernel Smoothing
- Human-LLM Co-writing
- Unsupervised Method
one_liner: 提出无需token级标注的自适应平滑方法，实现人机合著文本中LLM生成token的精准定位
practical_value: '- 做UGC/AI生成内容合规审核时，可复用该自适应平滑方法提升LLM生成片段的细粒度定位精度，无额外标注成本

  - 搭建Agent生成内容溯源工具链时，可直接集成该无监督检测逻辑，无需token级标注数据训练，快速落地合规校验能力

  - 该自适应带宽选择的Lepski规则可迁移到序列信号降噪场景，比如用户行为序列、query意图序列的噪声平滑处理'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM生成文本检测方法以文档级分类为主，无法定位人机合著文本中LLM生成的具体片段，人-LLM协同写作场景下的细粒度检测需求迫切。

### 方法关键点
1. 基于成熟的token级检测分数底座，对相邻token的检测分数做平滑处理降低随机波动
2. 引入自适应Lepski型规则，根据局部文本的作者属性结构动态选择平滑带宽，平衡偏差与方差
3. 无需token级标注数据训练，工程实现复杂度极低

### 关键结果
- 理论上证明信号估计的均方误差表现优于现有方法
- 合成与真实数据集上检测性能显著超越各类基线
- 开源了Hugging Face在线可直接调用的检测服务
