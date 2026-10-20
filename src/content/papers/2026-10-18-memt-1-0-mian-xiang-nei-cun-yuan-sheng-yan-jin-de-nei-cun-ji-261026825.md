---
title: 'MemT-1.0: Towards Memory-Native Evolution'
title_zh: MemT-1.0：面向内存原生演进的内存基础模型架构
authors:
- Zhiyu Li
- Zeyu Zhang
- Linyun Liu
- Yiwei Bu
- Chenyang Xi
- Xichong Zhang
- Yi Yu
- Yu Yu
- Zhichen Liu
- Yuxiao Yi
affiliations:
- MemTensor Team
arxiv_id: '2610.26825'
url: https://arxiv.org/abs/2610.26825
pdf_url: https://arxiv.org/pdf/2610.26825
published: '2026-10-18'
collected: '2026-10-20'
category: LLM
direction: 大模型原生内存架构 · Agent任务优化
tags:
- Memory-LLM
- Native-Memory
- Mixture-of-Storage
- Gated-DeltaNet
- Inference-Optimization
- Agent-Memory
one_liner: 提出内置原生内存的MemT-1.0模型族，兼顾长时记忆能力、通用能力与高推理效率
practical_value: '- 电商客服Agent、长会话推荐场景可复用Gated DeltaNet-2的稳定token级内存更新机制，替代传统KV cache存储长用户交互历史，128K历史长度下可实现1.86倍推理加速、66倍存储开销降低，大幅降低长会话服务成本

  - 多轮交互类场景可借鉴Mixture-of-Storage(MoS)内存扩容方案，通过多独立内存专家+共享地址的读写分离路由，在不显著提升推理开销的前提下扩展原生内存容量，支撑更长的用户行为序列建模

  - 落地LLM4Rec/Agent持续训练时可复用两阶段训练+全上下文教师蒸馏范式，在保留骨干模型原有通用能力的前提下，快速强化长时记忆能力，避免新增内存模块破坏原有业务效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型依赖外部KV cache或RAG实现长上下文记忆，存在存储开销随历史长度线性增长、推理延迟高、长时记忆可靠性差的问题，无法支撑多轮交互、Agent任务等场景的原生持续记忆需求。
### 方法关键点
- 架构：Transformer块中并行插入原生内存块，包含存储在线信息的动态本地内存和训练获得通用记忆能力的超参数内存，基于Gated DeltaNet-2实现稳定token级内存更新，避免内存状态发散
- 扩容：提出Mixture-of-Storage(MoS)架构，通过多独立内存专家+共享地址的读写分离路由，实现原生内存容量可扩展，无稀疏路由损失
- 训练：采用两阶段训练范式，基于34B token训练数据，第一阶段继续预训练建立内存加持的语言建模能力，第二阶段用全上下文大模型做教师蒸馏，对齐内存模型与全上下文模型输出，保留通用能力
### 关键结果
- 11个内存基准测试中，MemT-1.0-Flash/Nano平均得分50.6/47.0，比最强参数内存基线高12.5/8.9分，通用能力接近原生骨干模型
- 128K历史长度下，MemT-1.0-Nano推理速度是全上下文KV cache方案的1.86倍，持久存储减少66倍；256K场景下存储仅40MiB，远低于全上下文的5GiB
- 内置检索到的流程经验后，Agent编码任务成功率显著提升，接近显式文本经验的效果

> 核心结论：将内存内化为大模型计算的固有组件而非外部附加模块，是实现长时可靠记忆、高推理效率的核心路径
