---
title: Unlocking Lossless Speedups in LLMs via Discrete Diffusion
title_zh: 基于离散扩散实现大语言模型无损推理加速
authors:
- Subham Sekhar Sahoo
- Lingjie Chen
- Khiem Pham
- Jonathan Geuter
- Chaitanya Dwivedi
- Varad Pimpalkhute
- Yash Akhauri
- Alexander Moreno
- Mikhail Yurochkin
- Zhenting Wang
affiliations:
- Institute of Foundation Models
- University of Illinois Urbana-Champaign
- Cornell Tech
- Harvard University
- Cerebras Systems
arxiv_id: '2609.04010'
url: https://arxiv.org/abs/2609.04010
pdf_url: https://arxiv.org/pdf/2609.04010
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: 大语言模型 · 无损推理加速
tags:
- LLM Inference Acceleration
- Discrete Diffusion
- LoRA
- Speculative Decoding
- Autoregressive LLM
one_liner: 为自回归LLM添加轻量扩散LoRA权重，无需单独草稿模型实现全批次无损加速
practical_value: '- 可复用「轻量LoRA扩散支路+冻结基座AR权重」架构，给业务开源LLM（如Qwen、Llama）快速加无损加速能力，无需重训基座，训练成本极低，适合中小团队落地低延迟LLM服务，适配推荐理由生成、Agent工具调用等场景。

  - 扩散蒸馏阶段的总变差（TV）损失可直接复用，相比仅用蒸馏损失，可提升多token生成接受率约7%，进一步降低推理延迟。

  - Ψ-Spec采样器的双配置可直接适配业务场景：高并发批量推理（如批量用户标签生成、批量推荐文案生成）用线性采样器最大化吞吐量，低延迟单请求（如实时搜索query改写、Agent实时调用）用树采样器最大化单请求速度。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有自回归LLM逐token生成延迟高，投机解码需单独维护草稿模型，扩散LLM存在质量损失且大批次下加速效果消失；而电商/Agent场景同时有高并发批量推理、低延迟单请求需求，亟需全批次范围的无损加速方案。

### 方法关键点
- 架构解耦：每个Transformer层保留AR权重（负责生成质量，全程冻结）+ 轻量扩散LoRA权重（负责并行生成，仅训练该部分），参数增量仅0.35B，远低于主流投机解码的草稿模型。
- 训练流程：基座AR模型完成预训练/SFT/RL后，通过扩散蒸馏训练LoRA权重，结合DCD蒸馏损失和TV总变差损失，最大化并行生成token的接受率。
- Ψ-Spec采样器：高并发场景用线性采样器最大化系统吞吐量，低延迟场景用树采样器最大化单请求速度，推理时用AR权重验证，完全保留基座模型输出分布，实现无损加速。

### 关键结果
对比EAGLE-3、DFlash等投机解码方案，Uno全批次吞吐量更高、额外参数更少、峰值内存更低；对比DiffusionGemma、Mercury 2等扩散LLM，质量全面领先，大批次吞吐量高4.6倍。相对基座AR模型，最大批次下吞吐量提升1.6倍，单请求场景提升2.5倍，最高可达3倍加速；RL训练阶段用扩散支路加速rollout，端到端训练速度提升40%；基于开源Qwen3-8B适配的Uno仅需训练14.7B token即可生效。

最值得记住的结论：无需修改基座AR模型，仅添加轻量扩散LoRA即可实现全批次无损加速，是LLM推理加速的低成本落地方案。
