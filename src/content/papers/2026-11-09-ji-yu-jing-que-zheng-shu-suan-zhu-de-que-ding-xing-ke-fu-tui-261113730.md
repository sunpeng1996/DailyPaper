---
title: Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable
  Distributed Inference as Its Consequence
title_zh: 基于精确整数算术的确定性可复现推理与可验证分布式推理
authors:
- Sayed Amir Karim
affiliations:
- Pelloran Inc.
arxiv_id: '2611.13730'
url: https://arxiv.org/abs/2611.13730
pdf_url: https://arxiv.org/pdf/2611.13730
published: '2026-11-09'
collected: '2026-11-24'
category: LLM
direction: LLM推理优化 · 确定性可复现推理
tags:
- Deterministic Inference
- Integer Arithmetic
- Verifiable Inference
- MoE
- Distributed Inference
one_liner: 开源tritify运行时，全链路整数推理实现跨硬件、分布式场景的输出位一致
practical_value: '- 跨硬件部署LLM推荐/Agent服务时，可参考全整数推理路径设计，实现端侧云侧输出位一致，避免环境差异导致的推荐结果波动、Agent决策漂移问题

  - MoE大模型分布式部署时，可复用专家分片路由+整数运算一致性方案，用低配置集群部署超内存大模型，同时保证结果和单节点完全一致，降低大模型推荐服务的硬件成本

  - 针对推荐/广告系统的合规审计需求，可借鉴位一致+SHA-256哈希校验机制，实现推理结果可追溯、可第三方验证，满足监管对算法可解释、可复现的要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有浮点推理因IEEE-754加法非结合性、平台数学库舍入差异，跨硬件/环境输出无法位一致，导致分布式推理结果不可复现、离线在线效果漂移，第三方无法验证服务端推理正确性，只能信任服务方，限制了大模型在推荐、Agent等对一致性、合规性要求高的场景的跨环境部署。

### 方法关键点
- 开源tritify运行时，权重离线量化为固定点整数，激活动态逐张量量化，推理全链路（矩阵乘、归一化、非线性层、MoE路由等）均采用精确整数运算，浮点仅用于离线量化和参考校验
- 固定整数宽度、溢出规则、舍入方式、运算顺序，保证整数运算结果不受硬件架构、线程数、执行位置影响
- 每个算子同时实现整数推理路径和浮点参考路径，通过校验门控保证整数路径和浮点参考的误差在设定阈值内
- 支持跨节点分片部署：模型层或MoE专家可拆分到多台异构机器，仅传输激活和专家输出，结果和单节点完全一致

### 关键结果数字
- 跨硬件一致性：ARM/x86 CPU、Apple M3 GPU上推理输出SHA-256完全一致；Qwen2.5-0.5B推理时512个token的argmax和浮点参考匹配率达99.4%（509/512）
- 深度无精度悬崖：16层OLMoE-1B-7B、GLM-4.5-Air（106B参数）的每层残差和浮点参考的余弦相似度中位数均高于0.999，最低值不低于0.97
- 分布式部署：106B参数GLM-4.5-Air拆分到3台均无法单独承载全量模型的机器运行，输出和单节点流式加载结果完全一致；OLMoE-1B-7B拆分到6台异构多地域机器，输出位一致

### 核心结论
全链路精确整数推理的核心价值不是速度提升，而是通过跨环境位一致实现超内存大模型的低成本异构部署和可验证推理，打破本地部署容量受限、云端部署不可信的二元困境。
