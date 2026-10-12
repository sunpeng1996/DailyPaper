---
title: Contextual Correction of Parallel Draftsfor Speculative Decoding
title_zh: 面向投机解码的并行草稿上下文校正方法DCOCO
authors:
- Roy Eisenstadt
- Harel Lidar
- Tal Gonen
- Omer Luxembourg
- Itamar Zimerman
- Lior Wolf
- Eli David
- Ilan Naiman
affiliations:
- Stealth Startup (Tel Aviv)
- Tel Aviv University
- Ben-Gurion University
arxiv_id: '2610.12570'
url: https://arxiv.org/abs/2610.12570
pdf_url: https://arxiv.org/pdf/2610.12570
published: '2026-10-07'
collected: '2026-10-12'
category: LLM
direction: LLM 投机解码推理加速
tags:
- Speculative Decoding
- LLM Inference
- Parallel Draft
- Throughput Optimization
- DCOCO
one_liner: 提出轻量并行校正机制DCOCO，解决并行草稿块内依赖缺失问题，大幅提升LLM解码吞吐量
practical_value: '- 优化Agent服务延迟：在电商智能客服、商品文案生成等大流量LLM服务中引入DCOCO，可在不改变输出分布的前提下提升解码吞吐量最高6.6倍，降低推理成本

  - 高并发场景适配：大促时段的推荐理由生成、搜索query改写等高并发场景下，优先选用并行校正而非串行校正方案，避免串行模块的延迟累积导致吞吐量下降

  - 轻量改造可落地：DCOCO仅基于并行草稿器输出的top-K候选和已有隐状态做校正，无需修改原大模型结构，可作为现有投机解码框架的插件式优化快速集成'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
并行扩散类投机解码（如DFlash）可通过单次前向生成多token草稿，大幅降低解码延迟，但块内各位置token未依赖前置草稿的实际输出，导致连贯性差、接受率低；现有串行校正方案会在高并发下引入额外延迟瓶颈，抵消接受率提升的收益。

### 方法关键点
- 候选保留：每个草稿位置保留top-K候选而非直接取top1，利用“59%的错误位置的正确token存在于top16候选中”的观察，将校正转化为重选任务
- 并行打分：仅基于DFlash单次前向输出的隐状态、logits和候选token，用轻量共享两层MLP并行计算所有相邻候选对的上下文兼容性得分，无额外前向开销
- 前缀优先选择：对齐投机解码“最长前缀匹配后停止”的验证逻辑，从左到右贪心选择每个位置的最优后继，优先保证前缀正确性，避免全局最优带来的后续token无效问题

### 关键实验
在4个主流LLM backbone（Qwen3-4B/8B/30B、Llama3.1-8B）、10个涵盖数学、代码、通用生成的benchmark上测试，对比DFlash、DSpark、Domino等基线：单并发下吞吐量比最优基线高8~19%，最高比原生解码快6.6倍；4~32并发下吞吐量比最优基线高6~23%，串行校正方案吞吐量在高并发下甚至低于未校正的DFlash，DCOCO优势随并发升高保持稳定。

### 核心结论
并行校正的开销远低于串行校正，对齐投机解码的前缀验证逻辑做候选选择，能同时兼顾接受率提升和低延迟，在高并发场景下收益尤其明显
