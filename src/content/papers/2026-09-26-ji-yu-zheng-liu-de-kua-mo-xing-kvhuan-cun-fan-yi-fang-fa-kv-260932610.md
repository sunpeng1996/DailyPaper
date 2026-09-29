---
title: 'KV-Lingo: Learning KV-Cache Translators with Distillation'
title_zh: 基于蒸馏的跨模型KV缓存翻译方法KV-Lingo
authors:
- Valérie Castin
- Keitaro Sakamoto
- Anastasiia Filippova
- João Monteiro
- Marco Cuturi
- Pierre Ablin
affiliations:
- Apple
- École Normale Supérieure
- The University of Tokyo
arxiv_id: '2609.32610'
url: https://arxiv.org/abs/2609.32610
pdf_url: https://arxiv.org/pdf/2609.32610
published: '2026-09-26'
collected: '2026-09-29'
category: LLM
direction: LLM推理优化 · KV cache跨模型复用
tags:
- KV cache
- Knowledge Distillation
- Model Switching
- Inference Optimization
- Linear Mapping
one_liner: 用蒸馏训练的层间线性映射实现跨模型KV缓存翻译，大幅降低模型切换的首token延迟
practical_value: '- 电商导购、多轮推荐类Agent的多模型切换场景，可直接复用KV-Lingo方案，不用重prefill用户上下文、商品详情等长内容，首响应延迟最高降29×，大幅提升用户体验

  - 端云协同推荐场景中，端侧小模型prefill用户本地敏感对话/行为数据，缓存翻译后传给云端大模型生成推荐结果，既规避隐私风险又降低云端prefill开销

  - MoE大模型生成推荐文案、商品理由的高并发场景，用小模型prefill通用上下文，翻译后传给MoE解码，规避MoE prefill需加载全量专家的高开销，降低推理成本

  - 可复用其蒸馏范式：KV类对齐任务不用追求完美的表征重构，用目标模型自身的next-token分布做蒸馏的效果远好于直接拟合KV的MSE'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多模型路由、多Agent协作场景下不同LLM的KV cache互不兼容，切换模型需重跑全上下文prefill，开销随上下文长度快速增长，长上下文下首token延迟极高，严重影响多模型联动体验。
### 方法关键点
- 分层线性映射结构：每个目标层对应独立的K、V线性翻译矩阵，仅对每个token的KV表征独立变换，计算量随上下文长度线性增长，远低于prefill的平方级开销
- 两阶段训练：第一阶段用闭式解拟合KV的MSE做初始化，第二阶段用自蒸馏优化，最小化目标模型用原生缓存与翻译缓存的next-token分布KL散度，解决KV重构误差与生成质量不匹配的问题
- 支持跨层、跨分词器、跨MoE/稠密模型、多轮反复切换等场景，仅需为每对源-目标模型训练一组翻译矩阵，源目标模型全冻结无需修改
### 关键结果
测试覆盖Qwen3、Gemma、Mistral系列0.6B~30B MoE模型对，在MMLU-Pro、CoQA、LongBench等9个基准上，翻译缓存的下游性能接近原生缓存，多数任务优于小模型原生表现；M3 Ultra上64token prompt的Qwen模型切换首token延迟降低9.6×，H100上32k上下文场景下首token延迟最高降低29×；多轮切换时采用增量翻译策略，10轮切换后性能仍与每次重prefill持平。
> 最值得记住：不同LLM的KV缓存几何结构高度相似，仅用简单线性映射加蒸馏即可实现几乎无损的跨模型KV复用，是多模型联动场景下的低成本优化方案。
