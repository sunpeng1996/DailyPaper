---
title: 'BitMTP: When Multi-Token Prediction Meets Low-Bit Large Language Models'
title_zh: BitMTP：面向低比特大语言模型的多令牌预测联合优化框架
authors:
- Ning Zhang
- Shihao Wang
- Jinrui Zhang
- Chaodong Xiao
- Lei Zhang
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2610.28500'
url: https://arxiv.org/abs/2610.28500
pdf_url: https://arxiv.org/pdf/2610.28500
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: 低比特LLM推理 · 多令牌预测加速
tags:
- Low-bit-LLM
- Multi-Token-Prediction
- Inference-Optimization
- CUDA-Graph
- KV-cache
one_liner: 算法系统协同设计的低比特LLM多令牌预测框架，无需额外草稿模型最高获3.3倍推理加速
practical_value: '- 低比特LLM部署可复用联合NTP+MTP训练范式，无需额外草稿模型即可获得2倍以上推理加速，适合端侧Agent、批量商品文案生成等场景降本

  - 可直接迁移accepted-prefix对齐+共享KV的CUDA Graph复用方案到现有LLM推理服务，降低多令牌预测的KV缓存与调度开销

  - 三种解码策略可按需适配业务：生成短标题、推荐理由等短文本用置信度解码提效，生成客服话术、复杂推理内容用混合解码兼顾质量与速度

  - 代码、规则类生成场景多令牌提交率更高，加速效果更显著，可优先在电商智能客服、商品属性校验等场景落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
低比特量化（如BitNet b1.58、Bonsai的1.58bit权重）已经大幅降低了LLM的存储、内存带宽需求与线性层计算成本，但自回归解码的串行瓶颈仍限制了生成吞吐量；多令牌预测（MTP）可通过单次前向生成多个未来token减少解码步骤，但直接与低比特模型拼接会出现预测质量下降、额外计算与KV更新开销抵消提速收益的问题，现有MTP方案还需要额外部署独立的草稿与验证模型，进一步提升了部署复杂度。
### 方法关键点
1. 训练层：采用联合NTP（下一词预测）+MTP损失训练，单个模型同时具备自回归生成能力与块因果草稿预测能力，无需独立的草稿/验证双模型
2. 解码层：提供三种可切换策略：置信度解码（仅提交连续高置信度token，无验证）、投机解码（全块验证保证质量）、混合解码（置信度前缀达到阈值则直接提交，否则触发验证），覆盖不同质量-吞吐量的业务需求
3. 系统层：通过三个核心优化降低runtime开销：宽度定制的低比特算子适配不同解码路径、基于共享KV存储的有限状态CUDA Graph复用避免重复缓存、混合解码中提前预处理验证输入减少调度延迟；通过accepted-prefix对齐机制保证提交前缀、KV缓存边界、Graph重放状态的一致性，消除动态状态切换的额外开销
### 关键实验
在5类生成任务（指令遵循、数学推理、代码生成）上测试，对比原生低比特自回归模型、EAGLE-3等带草稿模型的投机解码方案：H20上混合解码在BitNet b1.58-2B获得2.2倍平均提速，1.7B-4B Bonsai模型获得2.1-2.4倍平均提速，生成质量与原SFT自回归模型相当；RTX 3090上平均提速最高2.0倍，Jetson Orin边缘设备上MBPP+代码任务最高获得3.3倍提速；相比EAGLE-3方案吞吐量提升近1倍，无额外草稿模型部署开销
### 核心结论
低比特LLM与多令牌预测的结合不能靠简单拼接，必须从训练、解码、runtime全栈协同设计才能获得无质量损失的真实吞吐量提升
