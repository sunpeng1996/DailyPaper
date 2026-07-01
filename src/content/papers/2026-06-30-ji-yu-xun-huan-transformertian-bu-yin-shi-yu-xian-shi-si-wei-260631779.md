---
title: Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers
title_zh: 基于循环Transformer填补隐式与显式思维链的性能差距
authors:
- Ying Fan
- Anej Svete
- Kangwook Lee
affiliations:
- UW-Madison
- Microsoft Research
- ETH Zürich
- KRAFTON
- Ludo Robotics
arxiv_id: '2606.31779'
url: https://arxiv.org/abs/2606.31779
pdf_url: https://arxiv.org/pdf/2606.31779
published: '2026-06-30'
collected: '2026-07-01'
category: Reasoning
direction: 大模型推理 · 隐式思维链优化
tags:
- Looped-Transformer
- Chain-of-Thought
- Latent-Reasoning
- Inference-Optimization
- LLM
one_liner: 提出LOTUS隐式思维链框架，3B规模下匹配显式CoT精度，推理延迟最高降6.9倍
practical_value: '- 电商/推荐Agent做复杂推理（多轮需求拆解、优惠券计算、商品搭配）时，可复用LOTUS思路将长CoT压缩为并行隐式迭代，3B级小模型部署场景下既保精度又降用户侧响应延迟

  - 训练trick：隐式推理模块无需复杂蒸馏，直接用基础模型LM头对隐式块做gold CoT对齐的并行交叉熵监督，跨模型大小的鲁棒性优于额外加辅助decoder的方案

  - 延迟优化可复用结论：隐式推理延迟仅和循环迭代次数R正相关，和并行隐式token数几乎无关，可根据业务精度需求动态调整R无需重训，复杂推理加R、简单意图理解降R即可

  - 搜索推荐的多步路径召回、用户意图拆解的中间状态可采用该方案的可解释隐式CoT存储，既能加速推理，又能通过LM头读回中间步骤做可解释性排查'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
显式CoT推理精度高，但逐token生成延迟高，无法满足低延迟业务需求；现有隐式CoT方案虽延迟低，但在1B参数以上规模下性能和显式CoT的差距随模型增大持续拉大，核心痛点在于要么存在自回归生成瓶颈，要么缺乏和显式CoT直接对齐的监督信号，大模型下训练极易漂移。

### 方法关键点
- 架构设计：在输入问题和答案之间插入K个可学习隐式块，每个块对应一个CoT步骤，用Looped Transformer对隐式块迭代R次优化，无需新增参数即可提升推理深度
- 监督方案：用基础模型LM头直接对迭代后的隐式块做并行交叉熵损失，对齐每个隐式位置对应的gold CoT token，再配合答案预测交叉熵损失联合训练，两类损失分别负责CoT步骤覆盖和全局推理一致性
- 推理流程：预计算问题的KV cache，迭代R次得到优化后隐式状态，直接基于隐式状态解码答案，无需生成中间CoT token

### 关键结果
在GSM8K数学推理数据集测试，对比Explicit CoT、SIM-CoT、CODI等基线：3B参数规模下LOTUS的GSM8K精度达70%，仅比显式CoT低1.5个百分点，域外平均精度超过显式CoT；数学表达式CoT场景推理延迟降低2.5倍，自然语言长CoT场景延迟降低6.9倍；隐式空间可解释性强，通过LM头读回隐式状态能还原70.9%的gold CoT token，还能生成未见过的有效推理步骤。

最值得记住的结论：Looped Transformer加并行gold CoT对齐监督的简单组合，就能在大参数规模下同时实现隐式CoT的低延迟和显式CoT的高精度，打破了以往隐式推理随规模增大性能掉队的规律。
