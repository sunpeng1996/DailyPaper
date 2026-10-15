---
title: 'ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid
  Linear Attention Large Language Models'
title_zh: ReaDy：基于混合线性注意力循环状态的推测解码加速方案
authors:
- Bohan Sun
- Zunhai Su
- Xialie Zhuang
- Jianjin Li
- Ngai Wong
- Chuan-Wei Kuo
affiliations:
- StartLux
- University of Chinese Academy of Sciences
- The University of Hong Kong
arxiv_id: '2610.20503'
url: https://arxiv.org/abs/2610.20503
pdf_url: https://arxiv.org/pdf/2610.20503
published: '2026-10-14'
collected: '2026-10-15'
category: LLM
direction: LLM推理优化 · 推测解码
tags:
- Speculative Decoding
- Hybrid Linear Attention
- LLM Inference
- Low-rank Adaptation
- Recurrent State
one_liner: 面向混合线性注意力大模型，提出复用循环状态的推测解码方法，Qwen3.8-27B单卡吞吐量较基线提升7.97%
practical_value: '- 业务侧用HLA架构LLM做生成式推荐文案、Agent多轮回复时，可直接复用这套推测解码方案，无精度损失前提下提升约8%的推理吞吐量，降低部署成本

  - 低秩查询+算子融合的设计可复用在所有需要访问模型内部状态的推理优化场景，比如RAG上下文注入、个性化生成的用户特征嵌入，大幅降低额外I/O开销

  - 两阶段微调策略（先训新增模块再用LoRA微调整个drafter）可迁移到所有基于预训练小模型的推理加速/业务适配任务，减少微调数据量和算力成本

  - HLA的固定大小循环状态可替代部分长上下文KV cache查询需求，适合电商长商品描述生成、多轮客服Agent等长序列场景，降低内存占用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有推测解码依赖目标模型隐藏特征生成草稿，其上下文侧重无法匹配后续草稿位置的需求，若通过KV cache补充上下文，又会随序列长度增长带来过高I/O开销；混合线性注意力（HLA）模型天然维护固定大小的循环状态，可作为低成本的补充上下文来源。
### 方法关键点
- 每个草稿位置配置可学习查询，直接从目标模型已提交的循环状态中检索位置专属补充上下文，通过残差更新注入草稿表示
- 采用低秩状态查询、融合算子设计，严格控制额外计算与I/O开销
- 两阶段适配策略：第一阶段冻结原有draft模型仅训练状态读取器，第二阶段联合训练读取器与draft模型的LoRA参数，目标模型全程冻结
### 关键实验
跨数学、代码、对话7个基准测试集验证，单卡NVIDIA B200部署Qwen3.8-27B，相比自回归解码平均获得3.16×提速；相比SOTA基线DSpark，平均吞吐量提升7.97%、平均接受长度提升8.50%，所有测试集性能均超过基线。
### 核心结论
对HLA架构大模型，复用其内置的固定大小循环状态做上下文补充，是几乎无精度损失、低额外成本提升推理效率的有效路径。
