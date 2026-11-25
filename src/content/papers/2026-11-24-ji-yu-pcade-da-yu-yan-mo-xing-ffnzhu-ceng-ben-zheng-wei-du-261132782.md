---
title: Measuring Layer-wise Intrinsic Dimensionality of FFNs in LLMs via PCA
title_zh: 基于PCA的大语言模型FFN逐层本征维度测量与优化
authors:
- Daehee Kim
affiliations:
- NAVER Cloud
arxiv_id: '2611.32782'
url: https://arxiv.org/abs/2611.32782
pdf_url: https://arxiv.org/pdf/2611.32782
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: 大语言模型压缩 · 结构剪枝优化
tags:
- LLM
- FFN
- PCA
- model pruning
- knowledge distillation
- intrinsic dimensionality
one_liner: 通过PCA测量LLM各层FFN本征维度，提出非均匀宽度分配策略，性能显著优于传统均匀分配
practical_value: '- 做电商垂直域LLM（商品文案生成、搜索query改写、客服Agent）蒸馏剪枝时，可先用PCA测量目标模型各层FFN的本征维度，按维度分配宽度，相同参数量下最高可提2.5pp，σ99越高的模型（如Qwen系列）收益越明显

  - 端侧部署的电商小模型（如商品详情页个性化文案生成）可采用该策略压缩，在效果损失可接受的前提下降低参数量，需注意非均匀宽度会带来约5%的推理延迟，可和量化等优化手段搭配抵消损耗

  - 训练自定义电商LLM时，预训练阶段即可参考「中间层FFN本征维度更高」的规律，给中间层分配更大宽度、边缘层压缩，可能用更少总参数达到相同效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM沿袭Transformer的统一FFN宽度设计，隐含各层复杂度相同的假设，但机制研究已证实不同深度层功能差异显著，统一宽度易造成参数浪费，缺乏可落地的非均匀宽度分配量化指导。

### 方法关键点
- 测量位置选择FFN下投影层的输入激活值，定义本征维度dθ为重构激活与原值余弦相似度≥阈值θ所需的最少PCA主成分数
- 提出σ99指标：各层dθ与原FFN宽度比值的标准差，量化维度分布的不均匀程度，可跨架构比较
- 宽度分配策略直接按各层dθ设置FFN宽度，与均匀分配、倒序镜像分配做对照，通过知识蒸馏训练等参学生模型

### 关键结果
扫描14个模型家族共58个开源LLM（参数量70M~72B），76%的模型符合中间层dθ更高的「中间重」分布，该分布跨中英文语料的皮尔逊相关系数≥0.94，SFT后σ99变化不超过10%；在4个不同系列teacher上做蒸馏实验，等参数预算下，PCA指导的分配比均匀分配在5个通用任务平均最高提分+2.5pp，比倒序分配最高提分+5.5pp，收益与σ99正相关，优势在下游SFT后依然保留，Qwen3-8B上SFT后ARC-C任务领先均匀分配+11pp。

### 核心结论
LLM各层FFN容量需求呈稳定的中间高、边缘低分布，按实测本征维度分配宽度是性价比极高的压缩优化手段
