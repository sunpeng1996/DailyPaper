---
title: Solar Open 2 Technical Report
title_zh: Solar Open 2 技术报告：面向长周期Agent任务的250B MoE大模型
authors:
- Sungrae Park
- Sanghoon Kim
- Gyoungjin Gim
- Jungho Cho
- Hyunwoong Ko
- Minbyul Jeong
- Minjeong Kim
- Keunwoo Choi
- Chaehun Shin
- Chanwoong Yoon
affiliations:
- Upstage
arxiv_id: '2607.20062'
url: https://arxiv.org/abs/2607.20062
pdf_url: https://arxiv.org/pdf/2607.20062
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: 面向Agent任务的长上下文MoE大模型
tags:
- MoE
- Long Context
- NoPE
- Linear Attention
- Agent
- Knowledge Distillation
one_liner: 推出250B总参15B激活参1M上下文MoE大模型，多语言与Agent能力领先同等规模开源模型
practical_value: '- 混合注意力架构可直接复用：1软max+3线性注意力的4层堆叠方案、NoPE无位置编码、负特征值线性注意力优化，可大幅降低长上下文场景的KV
  cache开销，适合处理用户全周期行为、全店经营数据的电商Agent落地。

  - MOPD多教师蒸馏方案适配多场景Agent整合：先训练垂直领域专家再通过On-Policy蒸馏合并为单模型的范式，可解决电商多场景（售前/售后/运营/数据分析）Agent单模型多任务能力滑坡问题。

  - 异步RL训练工程技巧可迁移：新鲜token比例网关、长度/ stale感知采样、环境失败过滤等方案，可直接优化Agent RL训练流程，解决长轨迹训练的设备空闲、数据浪费问题。

  - 高价值数据筛选策略可复用：20T原始语料筛至10T、4:6真实/合成数据配比、math/code占比不低于15%的配方，可提升垂直领域大模型微调/预训练的性价比，同等算力预算下提升垂直任务表现。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有开源大模型在长周期Agent任务上存在明显短板：上下文窗口不足无法容纳完整Agent轨迹，小语种垂直场景Agent能力覆盖薄弱，同时跨架构大模型迭代训练成本高，同等算力下性能提升天花板低，亟需兼顾长上下文、多语言、Agent能力与训练效率的大模型方案。

### 方法关键点
- 架构：250B总参数、15B active参数的MoE结构，混合注意力堆叠（每4层1层softmax+3层线性注意力，softmax前置），采用NoPE取消位置编码，线性注意力支持负特征值，上下文窗口达1M token，推理成本仅为全softmax架构的1/4。
- 训练效率优化：选择性权重迁移，复用前代模型2.3%兼容参数，训练到相同损失的token量减少42%；20T原始语料经质量、稀有度、去重筛选后得到10T训练集，采用4:6真实/合成数据比例，math/code占比均不低于15%，同等token预算下性能显著优于前代配方。
- Agent能力增强：先训练12个垂直场景领域专家，再通过Multi-teacher On-Policy Distillation（MOPD）合并为单模型，配合全异步RL训练框架解决长轨迹训练的效率问题。

### 关键结果数字
- 英文基准：同等规模开源模型中MMLU-Pro（86.2）、LiveCodeBench v6（92.4）、APEX-Agents（16.6）位列第一，整体性能与DeepSeek-V4-Flash、MiMo-V2.5相当。
- 韩语基准：平均得分85.4，超过DeepSeek-V4-Flash、GPT-5.4 mini、Claude Haiku 4.5等闭源API；韩语办公Agent基准Ko-GDPval得分86.8，仅比1.6T的DeepSeek-V4-Pro低0.1，参数量仅为后者1/6。

最值得记住的一句话：仅复用前代2.3%的兼容参数+高价值数据选优，就能让跨架构迭代的大模型训练成本降低近一半，同时实现1M上下文与领先的Agent能力。
