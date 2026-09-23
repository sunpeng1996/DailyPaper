---
title: 'CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents'
title_zh: CliffCompaction：面向长周期编码Agent的低成本上下文压缩技术
authors:
- Trang Nguyen
- Eulrang Cho
- Bingqing Chen
- Tim Dettmers
affiliations:
- Carnegie Mellon University
- Bosch Center for AI
arxiv_id: '2609.26779'
url: https://arxiv.org/abs/2609.26779
pdf_url: https://arxiv.org/pdf/2609.26779
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent 长会话上下文压缩优化
tags:
- Long-horizon Agent
- Context Compaction
- KV Cache
- Cost Efficiency
- Test-time Scaling
one_liner: 提出仅截断不重写的无训练上下文压缩方案，降本50%同时保性能，支持百万token长会话
practical_value: '- 上下文压缩可优先采用「仅截断丢弃冗余内容、不做重写/摘要」的规则方案，避免递归压缩导致的上下文漂移，同时不需要额外LLM调用，落地成本极低

  - 针对电商导购Agent、客服Agent等长会话场景，可优先裁剪占比最高的工具调用返回结果、长参数等冗余内容，核心指令、最近K轮对话完整保留，平衡精度和成本

  - KV cache优化可参考其「仅在阈值触发时修改上下文、其余时间保持上下文不变」的设计，最大化cache命中率，减少重预填充开销，适合高并发Agent部署

  - 测试时缩放场景可搭配该压缩方案，用小规模模型多轮推理逼近大模型效果，成本降低40%以上，适合推荐系统多候选打分、A/B测试等场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长周期Agent会话动辄百万token，现有上下文管理方案要么滑动窗口频繁失效KV cache推高推理成本，要么递归摘要压缩导致上下文漂移、精度下降，测试时缩放成本过高难以落地，亟需兼顾性能、成本、可落地性的压缩方案。

### 方法关键点
- 仅做截断丢弃不重写：压缩时仅裁剪冗余的长工具返回结果、截断长工具调用为签名、截断长思考内容，系统指令、任务描述、最近2K轮对话完整保留，无额外LLM调用
- 不递归压缩：每次触发压缩时直接丢弃上一轮压缩结果，仅基于最新的活跃会话生成新的压缩块，完全避免上下文漂移累积
- KV cache友好：仅在上下文超过预设阈值（16K/32K等）时触发压缩，其余时间保持上下文不变，最大化cache命中率，重预填充开销极低

### 关键结果
在SWE-bench Verified、Terminal-Bench 2.0、KernelBench三个基准测试，对比滑动窗口、LLM摘要、微压缩等方案：Terminal-Bench上降本50%的同时成功率提升2.26pp；测试时缩放场景下3轮Kimi K2.6推理成本低于单轮GPT-5.3 Codex，效果匹配Opus 4.7；KernelBench百万token长会话下CUDA kernel加速比达3.58×，超过专用优化算法25%。

**最值得记住的一句话**：长会话Agent上下文压缩优先保精度而非召回，冗余内容可通过工具重新获取，上下文漂移带来的精度损失远高于部分信息丢弃的损失。
