---
title: The Weight Is Over - Interactive Diffusion on Consumer GPUs
title_zh: 消费级GPU交互式扩散模型轻量化推理优化方案
authors:
- Frieder Ganz
- Maximilian Müller
affiliations:
- Adobe
- NVIDIA
arxiv_id: '2609.21849'
url: https://arxiv.org/abs/2609.21849
pdf_url: https://arxiv.org/pdf/2609.21849
published: '2026-09-18'
collected: '2026-09-21'
category: Multimodal
direction: 端侧多模态生成 · 扩散模型推理优化
tags:
- diffusion
- on-device-inference
- quantization
- text-encoder
- weight-streaming
one_liner: 提出嵌入翻译器与多指标调优配方，实现消费级GPU扩散模型亚秒级TTFI
practical_value: '- 端侧生成式营销素材场景可复用嵌入翻译器方案，用小文本编码器+轻量翻译层替代大编码器，大幅降低显存占用与推理延迟

  - 扩散类图像生成服务落地可复用speed/quality/memory三指标sweep配方，快速匹配不同等级硬件的部署要求

  - 高吞吐生成式推荐服务可借鉴FP8/NVFP4低比特量化+显存卸载方案，在不损失生成质量前提下提升单卡并发量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前端侧推理进展主要集中在LLM领域，扩散模型流水线显存占用高、延迟敏感，组件调度缺乏标准化方案，难以在消费级硬件量产部署。
### 方法关键点
1. 后训练嵌入翻译器：用Qwen3-0.6B小文本编码器+187M参数量翻译层，映射到大编码器语义空间，冻结扩散主干与VAE，降低模型体积与延迟
2. 可复现调优配方：采用FP8/NVFP4低比特量化同时降低显存占用与计算延迟，搭配跨组件GPU显存卸载策略，平衡速度、质量、显存三者关系
3. 优化全链路调度的交互式端侧图像生成编辑器
### 关键结果
新款消费级GPU上首图生成延迟（TTFI）<1s，适配更多硬件设备，生成质量与原大模型方案无显著差异
