---
title: 'LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers'
title_zh: LoopFill：面向循环Transformer的流水线多Token投机解码
authors:
- Siqi Zhu
- Suozhi Huang
- Yi Zhao
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
- Princeton University
arxiv_id: '2611.19649'
url: https://arxiv.org/abs/2611.19649
pdf_url: https://arxiv.org/pdf/2611.19649
published: '2026-11-14'
collected: '2026-11-17'
category: LLM
direction: LLM推理 · 循环Transformer解码优化
tags:
- LoopedTransformer
- SpeculativeDecoding
- InferenceOptimization
- LLM
- DecodingAcceleration
one_liner: 无需训练的双草稿源投机解码算法，将循环LLM解码速度最高提升5.85倍
practical_value: '- 业务中使用Looped LLM做Agent交互、生成式推荐文案时，可直接复用LoopFill无训练解码方案，相比最优基线最高提40%速度，无需额外训练草稿模型，节省落地成本

  - 多源草稿树融合思路可迁移到生成式推荐Token生成：将用户历史行为n-gram后缀检索与轻量模型浅输出结合，提升生成速度同时不改变原模型输出分布

  - 可根据业务并发度动态调整单请求草稿节点预算N：低并发实时场景（如用户侧Agent调用）用N=32~64降延迟，高并发批量场景（如全量商品文案生成）用N=16提吞吐量

  - 后缀频率与模型概率加权的路径得分剪枝策略，可直接复用到RAG+生成链路，减少无效候选的计算开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Looped Transformer通过权重共享循环计算大幅提升参数效率，小参数模型即可匹配大模型的推理效果，是端侧/低资源场景部署LLM的主流架构，但自回归解码时每个Token需多次遍历循环层，延迟是普通Transformer的数倍；现有流水线投机解码方法仅能生成单Token草稿，流水线空泡率高，多Token方案又需要额外训练专用草稿模型，落地成本高。

### 方法关键点
- 无训练双草稿源：同时基于历史序列构建本地+全局后缀树，检索生成多Token连续草稿，同时提取浅循环层（d<T）的输出生成单Token草稿，两类草稿共享同一棵草稿树，避免重复计算
- 路径得分剪枝：每个候选节点的得分为路径上后缀出现频率和模型预测概率的乘积，每步仅保留Top-N个高得分节点进入流水线计算，控制显存与计算开销
- 无损验证：仅用全循环深度的输出确定最终Token，完全保留原模型的输出分布，验证通过的分支可直接复用已完成的循环计算，无需重跑

### 关键实验
在GSM8K、MATH、BBH、HumanEval+等7个基准测试集上，针对Ouro-2.6B、Huginn-3.5B两款主流Looped LLM测试，对比AR、LoopSpec、LoopAhead等基线：
- 贪婪解码下平均提速5.85×（Ouro-2.6B）、5.13×（Huginn-3.5B），比最优基线LoopAhead分别高40%、25%
- 并发度为16时，端到端吞吐量是AR解码的2.81×（Ouro-2.6B）、2.67×（Huginn-3.5B）

**最值得记住的一句话**：针对循环架构的解码优化，无需额外训练的多源草稿融合方案，加速效果已经超过需要训练的专用草稿模型。
