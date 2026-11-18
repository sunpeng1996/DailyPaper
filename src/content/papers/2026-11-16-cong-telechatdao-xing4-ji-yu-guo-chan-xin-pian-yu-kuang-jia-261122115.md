---
title: 'TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and
  Frameworks'
title_zh: 从TeleChat到Xing4：基于国产芯片与框架的前沿Agent大模型演进
authors:
- Xingchen AGI Lab
- Baotian Hu
- Bingkai Yang
- Boyang Wang
- Changzai Pan
- Chao Lyu
- Chao Wang
- Chen Li
- Chenshuo Pan
- Chenyu Lin
affiliations:
- Xingchen AGI Lab, China Telecom
arxiv_id: '2611.22115'
url: https://arxiv.org/abs/2611.22115
pdf_url: https://arxiv.org/pdf/2611.22115
published: '2026-11-16'
collected: '2026-11-18'
category: Agent
direction: Agent大模型全栈优化 · 国产算力适配
tags:
- MoE
- Long-Context
- Speculative Decoding
- Agent
- Distributed Training
- Ascend
one_liner: 在昇腾NPU与MindSpore生态下实现Agent大模型全栈优化，开源支持256K上下文的29B MoE模型
practical_value: '- 长上下文Agent服务优化：可复用MLA+DSA+IndexShare的组合注意力方案，实测提升长上下文prefill吞吐量4.68倍，降低KV缓存访问压力，适合引入长用户行为序列、多轮对话历史的推荐Agent、导购Agent场景

  - MoE模型部署效率优化：可参考宽而浅的MoE拓扑设计，在相同总参数量与激活参数量下，训练吞吐量提升10%、推理吞吐量提升11%，适配国产算力的矩阵计算优势，降低大模型落地成本

  - 国产算力训练工程优化：若基于昇腾NPU训练大模型，可直接复用HSDP混合分片、Owner-based Muon优化、细粒度选择性重计算等工程trick，最高提升训练吞吐量16.1%

  - Agent对齐训练框架设计：可参考TeleGym的异步执行+部分rollout设计，解决异构Agent任务时长不均的问题，适合电商导购、智能客服、广告投放决策类Agent的RLHF/RLAIF训练流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主流开源大模型多基于GPU生态研发，基于国产昇腾NPU、MindSpore框架训练大规模Agent大模型，面临架构适配性差、训练效率低、长上下文支持成本高等系统级挑战，需协同优化模型架构、训练基础设施、Agent后训练全链路，平衡模型能力与计算开销。

### 方法关键点
- 模型架构：采用宽而浅的MoE拓扑，结合MLA+DSA+IndexShare优化长上下文注意力，搭配DSpark块级投机解码提升推理吞吐量；开源29B MoE版本单token仅激活4B参数，原生支持256K上下文；285B版本支持1M上下文，单token激活17B参数。
- 训练基础设施：基于MindSpore HyperParallel实现拓扑感知的HSDP混合分片并行，取消流水线并行消除结构气泡；优化Owner-based Muon优化器减少冗余正交计算，细粒度选择性重计算平衡显存与算力开销，层式索引器反向传播降低长序列训练延迟。
- Agent后训练：推出TeleGym统一Agent执行平台，采用解耦异步执行、有界过采样、部分rollout方案适配异构Agent任务时长差异，实现执行、评估、轨迹构建与策略优化的端到端联动。

### 关键结果
- 推理侧：285B模型256K上下文场景下，MLA+DSA+IndexShare相比仅MLA基线prefill吞吐量提升4.68倍；DSpark投机解码相比基线推理吞吐量提升2.67~3.77倍。
- 训练侧：HSDP相比传统1F1B流水线并行训练吞吐量提升16.1%；Owner-based Muon、细粒度选择性重计算、层式索引器反向传播分别提升训练吞吐量9.1%、6.9%、15.2%；整套方案可支撑8192张昇腾910C卡训练285B参数MoE模型。

### 核心结论
国产算力栈下的大模型优化需要架构、系统、训练框架的协同设计，而非单一模块的孤立优化，可在兼顾模型能力的同时实现效率的大幅提升。
