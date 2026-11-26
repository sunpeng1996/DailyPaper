---
title: AliceAI-Foundation-80B-A3B-Base
title_zh: Yandex开源80B参数MoE基座大模型AliceAI-Foundation-80B-A3B-Base技术报告
authors:
- Nikolay Skachkov
- Ekaterina Redina
- Maksim Konoplev
- Evgenii Uskov
- Veronika Zykova
- Ivan Tsarikov
- Artemii Zakharov
- Mariia Godunova
- Dmitrii Lunin
- Maria Nikiforova
affiliations:
- Yandex
arxiv_id: '2611.34529'
url: https://arxiv.org/abs/2611.34529
pdf_url: https://arxiv.org/pdf/2611.34529
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: MoE大模型基座训练与Agent能力优化
tags:
- MoE
- LLM
- Agent
- Reasoning
- OpenSource
- Training
one_liner: 从零训练的80B总参3B激活参MoE基座，推理/多语言/Agent能力超更大规模开源模型
practical_value: '- 训练MoE模型遇激活不稳定问题时，可直接复用MoE输出Z-loss正则方案，无性能损耗还能避免训练损失突增，比Gated RMSNorm节省5%训练开销

  - 做垂直领域LLM（如电商/广告场景领域基座）时，可照搬领域数据过滤级联方案：先轻量模型粗筛，仅5%高潜数据用大模型精标，计算成本降90%的同时保留95%高价值文档

  - 要提升基座Agent能力，可在预训练阶段就加入工具交互轨迹数据，而非仅在SFT阶段注入，实测能显著提升下游Agent任务微调后的表现

  - 做长上下文RAG任务时，训练数据里混入带干扰文档的QA样本，可将无关上下文带来的准确率下降从30-40%压缩到10%，适配搜索推荐场景的噪声环境'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有开源MoE大模型普遍存在推理/Agent能力不足、小语种领域知识薄弱的问题，同时大参数量MoE训练易出现激活不稳定、留出验证损失与下游效果对齐度差的痛点，Yandex需要自研适配俄语场景、高推理能力、低推理成本的开源基座。

### 方法关键点
- 架构：80B总参数、3B激活参数MoE结构，48层Transformer，3:1比例混合Kimi Delta Attention与全注意力，引入Attention Residuals做跨层加权融合，MoE采用DeepSeek-V3无辅助损失路由方案
- 训练流程：分4阶段训练，17.5T token通用预训练→32K上下文扩展→256K上下文扩展→280B token推理与Agent交互训练，优化Muon算子分布式调度，训练步长耗时减半
- 稳定性优化：给MoE输出加Z-loss正则，解决高学习率下MoE激活突增导致的损失spike，无性能损耗
- 数据增强：长上下文训练混入带干扰文档的QA样本，预训练阶段注入Agent工具交互轨迹数据

### 关键结果
对比Qwen3.5-35B-A3B、GLM-4.5-Air、Nemotron-3-Super-120B、DeepSeek-V4-Flash等更大参数量开源基座：零样本推理任务IMO-AnswerBench pass@8达88.7%、LiveCodeBench v5-v6 pass@8达82.9%，为同规模最优；俄语事实知识任务WikiWebFacts 86.5%、HardMultiQA 67.9%，超过参数大3倍的DeepSeek-V4-Flash；128K长上下文任务FinQA准确率74.1%，与DeepSeek持平。

### 核心结论
训练集留出验证损失和下游任务排名的一致性仅42%，用代码/领域Benchmark/高价值网页数据做验证集，一致性可达87%以上。
