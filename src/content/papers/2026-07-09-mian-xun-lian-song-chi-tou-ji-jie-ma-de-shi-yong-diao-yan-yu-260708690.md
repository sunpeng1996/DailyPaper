---
title: A Practical Investigation of Training-free Relaxed Speculative Decoding
title_zh: 免训练松弛投机解码的实用调研与工程落地指南
authors:
- Guoxuan Xia
- Luka Ribar
- Paul Balanca
affiliations:
- Graphcore
- Imperial College London
arxiv_id: '2607.08690'
url: https://arxiv.org/abs/2607.08690
pdf_url: https://arxiv.org/pdf/2607.08690
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM推理加速 · 投机解码优化
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Training-free
- Latency Optimization
- Relaxed Spec-dec
one_liner: 统一免训练松弛投机解码框架，基准测试各方法，提炼可落地的工程实践结论
practical_value: '- 部署LLM驱动的Agent/生成式推荐/智能客服服务时，优先优化严格投机解码的draft length Ndraft，其提速效果与松弛方法相当，且无需额外效果评估，完全无损输出质量

  - 若要上线松弛投机解码，优先选择CACTUS/mentored-dec这类严格控制与原模型偏差的方法，尤其适配当前主流的MTP专用草稿模型，不会出现明显效果衰减

  - 不要在专用MTP/极小通用草稿模型上使用依赖草稿模型生成质量的松弛方法（如r-fuzzy、spec-casc-opt），会导致输出冗长重复、实际推理速度不升反降

  - 若业务允许可控的效果-速度trade-off，优先选择能力较强的通用小模型作为草稿模型，可实现接近无损的额外提速，松弛参数需按业务场景单独校准，不要跨场景复用'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统严格投机解码是LLM推理无损提速的主流方案，但近年学界提出放松输出分布一致性约束的松弛投机解码，可进一步提升速度甚至优化效果，但现有方法实验设置分散，缺乏统一对比和落地指导，从业者难以判断选型。

### 方法关键点
- 提出统一的松弛投机解码算法框架，将现有6种免训练松弛方法纳入同一范式，仅需替换拒绝、残差采样、bonus采样三个环节的目标分布即可实现不同方法
- 建立更贴合实际的提速估算模型，引入平均生成长度修正系数，避免仅用token吞吐量高估实际提速效果
- 覆盖三类主流草稿-验证模型对：专用MTP草稿模型+27B主模型、0.6B小模型+32B主模型、8B中等模型+32B主模型，在AIME24、GPQA等现代推理基准上做公平对比

### 关键结果
- 优化严格投机解码的Ndraft最高可实现与松弛方法相当的提速（最高2-5倍于原生AR解码），且完全无损效果
- 用8B强通用草稿模型时，松弛方法可实现接近无损的10-20%额外提速；用MTP/0.6B弱草稿模型时，仅CACTUS/mentored-dec可实现可控trade-off，其他方法最多导致效果下降10pp以上，还会引发生成冗长导致实际速度下降
- 松弛参数α跨任务通用性差，相同α在不同任务下的效果损失差可达5pp以上

### 核心结论
松弛投机解码是场景定制化的优化手段，而非严格投机解码的通用drop-in替代品，上线前必须做业务场景专属的效果验证
