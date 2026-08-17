---
title: 'DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding'
title_zh: DeaMoE：面向小批量解码优化的高效MoE架构
authors:
- Zewen Jin
- Shen Fu
- Zeping Duan
- Shannon Wang
- Weihao Wu
- Chengjie Tang
- Congkun Ai
- Ping Gong
- Zijian Dai
- Youhui Bai
affiliations:
- University of Science and Technology of China
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
- Shanxi University
arxiv_id: '2608.14385'
url: https://arxiv.org/abs/2608.14385
pdf_url: https://arxiv.org/pdf/2608.14385
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM MoE · 小批量解码效率优化
tags:
- MoE
- Decoding Efficiency
- Small Batch
- Parameter Sharing
- LLM Inference
- Routing Strategy
one_liner: 通过部门式专家参数共享+两级路由，降低MoE小批量解码权重加载开销，提升推理速度
practical_value: '- 业务部署MoE类LLM做智能客服、商品文案生成、Agent推理等低延迟ToC场景时，可参考DeaMoE的部门式专家分组+参数共享设计，在不损失效果的前提下降低小批量请求的TPOT，提升用户体验

  - 路由策略可借鉴两级路由思路，先选共享参数的专家组再选组内专家，大幅减少同batch内的参数重复加载，尤其适合请求QPS不高但延迟要求严格的个性化交互场景

  - MoE训练可复用两个实操trick：共享层与专家私有层之间加SiLU激活、专家私有参数用单位矩阵初始化，避免训练不稳定同时保证模型效果不下降

  - 若业务使用大参数MoE模型（如DeepSeek-V3级别的多轮对话/生成模型），优先适配DeaMoE结构，A40最高2倍、H100最高1.97倍的小批量解码加速可直接降低推理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE 架构已成为 LLM 扩容的主流方案，但在实时交互场景（如智能客服、语音助手、Agent 推理）的小批量解码模式下，推理受限于专家权重加载的内存瓶颈，现有后训练压缩、预训练细粒度专家设计等方案要么损失模型精度，要么额外引入计算通信开销，亟需针对性的低延迟优化方案。

### 方法关键点
- 专家分组为「部门」：同部门专家共享大部分门控、上/下投影参数，仅保留少量私有参数实现差异化，大幅降低参数冗余
- 两级路由策略：先将 token 路由到对应部门，部门共享参数统一处理所有分到的 token 后，再分配到组内专家做私有层计算，避免重复加载共享参数
- 训练优化：共享层与私有层之间加 SiLU 激活，专家私有参数用单位矩阵初始化，采用软约束的部门 top-k 路由，不强制覆盖固定数量部门以保证模型效果

### 关键实验
- 预训练 7.3B 参数 DeaMoE 与同参数量、同 FLOPs 的标准 MoE 对比，10 个下游任务效果持平，语言建模 perplexity 在 PTB、WikiText-2 数据集上更优
- 端到端 vLLM 部署在 A40 上，小批量（4~128）TPOT 最高提速 1.33 倍；同延迟预算下吞吐量最高提升 1.83 倍
- 适配 DeepSeek-V3 的 DeaMoE 微基准测试，A40 上最高提速 2.00 倍，H100 上最高提速 1.97 倍

> 核心结论：MoE 小批量解码的核心瓶颈是专家权重加载而非计算，通过跨专家参数共享+路由优化降低重复加载，是兼顾效果与延迟的最优路径
