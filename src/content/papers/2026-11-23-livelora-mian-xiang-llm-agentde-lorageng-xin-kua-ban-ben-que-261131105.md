---
title: 'LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents'
title_zh: LiveLoRA：面向LLM Agent的LoRA更新跨版本精确KV缓存迁移方案
authors:
- Tianyi Huang
- Samuel Xu
- Ivy Gu
- Nathan Huang
- Siqi Zhang
affiliations:
- Ryquo
- App-In Club
arxiv_id: '2611.31105'
url: https://arxiv.org/abs/2611.31105
pdf_url: https://arxiv.org/pdf/2611.31105
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: LLM Agent · LoRA KV缓存迁移优化
tags:
- LoRA
- KV Cache
- LLM Agent
- Inference Optimization
- Online Adaptation
one_liner: 通过模型-运行时协同设计，实现LoRA更新无需重放全会话历史的精确KV缓存迁移
practical_value: '- 电商导购、智能客服等在线个性化Agent可复用「冻结下层Decoder+固定K/V LoRA下投影」的设计，避免LoRA更新时重放全用户会话历史，大幅降低更新延迟

  - 可复用其原子化发布协议，同时提交LoRA权重、KV缓存、下一词logits，避免版本不一致导致的生成错误，适配高可用在线Agent服务要求

  - 针对高频动态更新的生成式推荐Agent场景，可参考其成本计算模型选择适配的LoRA更新频率，平衡更新延迟与推理开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
持久化LLM Agent在线更新LoRA适配器时，直接复用旧版本KV缓存会导致模型版本混合、生成结果出错，重放全会话历史做prefill的成本随上下文长度、活跃会话数增长急剧升高，严重影响在线服务延迟，现有方案无法兼顾迁移精度和性能。
### 方法关键点
- 结构约束：冻结除最后一层Decoder外的所有模型层，最后一层的K/V LoRA适配器固定下投影矩阵A，仅更新上投影矩阵B，保证每个token的基础投影和低秩坐标跨LoRA版本不变
- 闭形式KV迁移：首次推理时保留K/V的基础投影值、固定A输出的低秩坐标，LoRA更新时仅需用新的B矩阵批量重算所有历史token的最终层K/V，无需重跑下层Decoder
- 原子化发布协议：预计算候选K/V和logits时不修改现有服务状态，验证通过后一次性原子提交适配器、KV缓存、下一词logits，保证版本一致性，失败自动回滚
### 关键实验
基于Qwen2.5-3B-Instruct单NVIDIA H200 GPU测试，对比全历史重放baseline：32个8K token活跃会话场景下，LoRA更新的中位数加速比达68.98×；推理解码开销仅比原生缓存解码高~4.8%；对比保留边界重放方案，额外会话存储降低3.42×，整体更新+解码成本基本持平。
### 核心结论
通过结构约束把可变部分限制在Transformer最后层的LoRA上投影，用极小的额外开销就能避免LoRA在线更新时的全历史重放成本，非常适合高频迭代的在线LLM Agent场景。
