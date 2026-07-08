---
title: 'Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive,
  Diffusion, and Self-Speculation Decoding'
title_zh: Nemotron-Labs-Diffusion：统一自回归、扩散与自投机解码的三模式语言模型
authors:
- Yonggan Fu
- Lexington Whalen
- Abhinav Garg
- Chengyue Wu
- Maksim Khadkevich
- Nicolai Oswald
- Enze Xie
- Daniel Egert
- Sharath Turuvekere Sreenivas
- Shizhe Diao
affiliations:
- NVIDIA
- Georgia Tech
- HKU
- University of Chicago
- MIT
arxiv_id: '2607.05722'
url: https://arxiv.org/abs/2607.05722
pdf_url: https://arxiv.org/pdf/2607.05722
published: '2026-07-06'
collected: '2026-07-08'
category: LLM
direction: 大模型推理加速 · 三模式统一解码
tags:
- Diffusion LM
- Autoregressive Decoding
- Speculative Decoding
- Inference Acceleration
- Tri-Mode LM
one_liner: 单架构融合AR与扩散训练，支持三模式解码，兼顾精度与全场景推理吞吐量
practical_value: '- 推理侧可参考三模式适配不同并发场景：高并发服务用AR模式复用现有KV cache链路，低并发场景（如端侧Agent、个性化对话推荐）用自投机模式提升吞吐量，平衡服务成本与响应速度

  - 做生成式推荐（如商品文案、营销内容生成）时，可复用双阶段训练策略：先训纯AR目标对齐语言先验，再加扩散损失解锁并行生成能力，无需完全重训现有AR模型

  - 自投机模式的LoRA对齐trick可直接复用：仅训练attention的o_proj层LoRA（占参数~0.4%），即可提升30%左右的推理TPF，无需改动模型主干

  - 扩散训练的全局token级loss平均策略可迁移到扩散类生成任务，解决可变mask带来的梯度不稳定问题，稳定训练过程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
自回归(AR)大模型逐token解码的串行特性限制了推理并行度，低批量场景下资源利用率低、吞吐量差；扩散LM虽支持并行生成，但精度和训练效率弱于AR模型，现有并行解码方案（如MTP）的精度-效率trade-off仍有较大优化空间，同时适配不同并发场景的统一架构长期缺失。
### 方法关键点
- 训练：采用联合AR+扩散损失优化，α=0.3平衡两者权重；双阶段训练，先纯AR训练对齐左到右语言先验，再加入扩散损失；全局token级loss平均，解决可变mask带来的梯度波动
- 注意力设计：clean流严格因果掩码支持AR目标计算，noisy流块内双向、块间因果，同时支持扩散并行去噪
- 三模式推理：AR模式适配高并发场景；扩散模式块级并行去噪，可搭配轻量采样器提升接受率；自投机模式用扩散分支生成多token草稿、AR分支验证，可加LoRA微调提升草稿匹配度
### 关键结果
- 8B版本自投机模式在GB200上SPEED-Bench吞吐量是Qwen3-8B的4倍，单forward token数(TPF)是后者6倍，平均精度领先0.86%
- 自投机模式加LoRA微调可提升32.5%的TPF，精度几乎无损失；最优采样器下扩散模式TPF比自投机模式高76.5%，长期潜力大
- 3B/8B/14B全规模、文本/多模态全场景均一致领先SOTA AR和扩散LM的精度-效率trade-off
### 核心结论
AR和扩散范式不是竞争关系，融合两者的统一架构可在几乎不损失AR精度的前提下，大幅提升推理效率并适配全场景部署需求
