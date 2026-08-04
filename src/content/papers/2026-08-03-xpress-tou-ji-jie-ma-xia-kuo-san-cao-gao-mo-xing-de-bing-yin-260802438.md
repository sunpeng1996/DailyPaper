---
title: 'xPress: Parallel Refinement for Diffusion Drafters in Speculative Decoding'
title_zh: xPress：投机解码下扩散草稿模型的并行因果修正框架
authors:
- Zheng Wang
- Davis Wertheimer
- Yu Chin Fabian Lim
- Mudhakar Srivatsa
- Raghu K. Ganti
- Minjia Zhang
- Naigang Wang
affiliations:
- University of Illinois Urbana-Champaign
- IBM
arxiv_id: '2608.02438'
url: https://arxiv.org/abs/2608.02438
pdf_url: https://arxiv.org/pdf/2608.02438
published: '2026-08-03'
collected: '2026-08-04'
category: LLM
direction: LLM推理 · 投机解码优化
tags:
- Speculative Decoding
- Diffusion LLM
- Inference Acceleration
- Jacobi Decoding
- Causal Refinement
one_liner: 轻量并行因果修正模块提升扩散型投机解码的接受长度与端到端吞吐
practical_value: '- 部署Agent/生成式推荐场景的实时LLM服务时，可直接复用xPress+扩散草稿的投机解码方案，相比串行因果修正快1.6x，能在不损失生成质量的前提下提升吞吐、降低端到端延迟

  - 生成式推荐/批量query改写等并行生成场景，可迁移低秩空间下三角线性混合+少量Jacobi迭代的修正思路，解决并行生成的token局部合理、全局因果不一致的问题

  - 微调对齐大模型输出的小模型（如RAG query重写、推荐prompt生成）时，可复用总变差损失直接优化和大模型分布的匹配度、加一致性损失对齐训练推理分布的trick，提升下游任务的实际效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
扩散型投机解码的草稿模型（如dFlash）可单次前向生成整段token，大幅降低串行草稿的开销，但生成的token是独立采样的边际分布，缺乏上下文因果依赖，容易出现局部合理但全局不一致的问题，被目标模型提前拒绝，限制了接受长度和最终加速比；现有串行因果修正方案又会重新引入串行开销，抵消并行生成的优势。

### 方法关键点
- 轻量因果修正器：仅新增低秩空间（r=256）的小参数模块，复用扩散草稿模型的隐状态、全局特征和前序token embedding，输出logits偏置修正原草稿的输出，不重写整个分布
- 并行修正：用Jacobi迭代替代串行左到右解码，全块token并行更新，K远小于块长（B=16时K≈4-6即可收敛），达到和串行修正相当的效果
- 训练优化：采用交叉熵+总变差损失组合直接优化接受率，新增锚定损失保持原草稿模型质量，加一致性损失对齐训练（教师强制）和推理（自回归输入）的分布差异

### 关键结果
目标模型采用Qwen3-8B，基线为原dFlash、DSpark的Markov头，覆盖7个数学、代码、聊天基准：接受长度平均提升~30%（最高56%），端到端吞吐平均提升1.3x（最高1.7x）；K=4时效果超过串行Markov头，同时修正速度快1.6x；vLLM下批量部署时仍保持1.2-1.4x的吞吐优势。

**最值得记住的一句话**：并行生成的因果依赖修复不需要走全串行流程，少量并行迭代即可在极低开销下补全因果性，大幅提升最终效果。
