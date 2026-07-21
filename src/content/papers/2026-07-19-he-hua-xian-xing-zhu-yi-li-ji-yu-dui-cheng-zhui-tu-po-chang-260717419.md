---
title: 'Kernelized Linear Attention: Breaking the Capacity Wall with Symmetric Cones'
title_zh: 核化线性注意力：基于对称锥突破长上下文容量瓶颈
authors:
- Ayoub Ghriss
- Sourav Chakraborty
affiliations:
- University of Colorado Boulder
arxiv_id: '2607.17419'
url: https://arxiv.org/abs/2607.17419
pdf_url: https://arxiv.org/pdf/2607.17419
published: '2026-07-19'
collected: '2026-07-21'
category: LLM
direction: LLM线性注意力 长上下文效率优化
tags:
- Linear Attention
- Long Context
- Kernel Method
- Triton Kernel
- KV Cache
one_liner: 基于对称锥提出KATA核化线性注意力，长上下文吞吐量最高达FlashAttention-2的11倍，KV缓存仅为软注意力的1/4
practical_value: '- 长上下文Agent/推荐场景可直接复用KATA开源Triton kernel实现，131k tokens下吞吐量达FlashAttention-2的11倍，大幅降低长序列用户行为建模、多轮对话推理时延

  - 对称锥特征几何设计可迁移到生成式推荐的Semantic ID编码阶段，通过秩一PSD特征降低地址碰撞，高熵item ID检索准确率比Gated DeltaNet提升90%+

  - 可借鉴分块PSD特征+关联扫描的工程优化思路，在保留O(T)线性复杂度的同时降低KV缓存占用，适合边缘端/低资源部署的推荐Agent场景'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有线性注意力虽然实现了常数时间循环推理，但长上下文关联召回性能暴跌，核心原因是固定大小状态下的内存碰撞问题，且过去线性注意力的特征映射几何设计缺乏理论支撑，无法在容量、效率、准确率之间实现最优权衡。

### 方法关键点
- 将注意力召回建模为球面填充问题，基于自对偶齐次对称锥（正象限、洛伦兹锥、PSD半正定锥）的Koecher–Vinberg分类提出KATA框架，特征映射天然保证注意力权重非负，分母项自带无参数凸输出门
- 采用秩一PSD特征实现最优容量-干扰权衡，通过Welch干扰下限表征关联容量，容忍度高于下限时可无参数扩增状态规模，支持投影维度下指数级数量的key球面编码
- 实现两种硬件对齐的Triton kernel：Flash风格O(T²)前向核吞吐量达FlashAttention-2的1.6倍；O(T)分块状态核通过关联扫描将块间循环深度降至O(log(T/C))

### 关键结果
- 合成MQAR任务：长上下文外推16倍时KATA-M1准确率达0.985，KV缓存仅为软注意力的1/4；重复key覆盖任务上DeltaKATA-M1准确率接近1
- 340M参数LLM预训练：1k上下文下UUID召回率达0.908，远高于Gated DeltaNet的0.004，零-shot性能与Gated DeltaNet相当
- 131k tokens场景下O(T)版KATA吞吐量达FlashAttention-2的11倍

**最值得记住的一句话：** 线性注意力的容量瓶颈本质是球面填充问题，基于对称锥的特征几何设计可在不新增参数的前提下，同时实现长上下文高吞吐量与高召回准确率
