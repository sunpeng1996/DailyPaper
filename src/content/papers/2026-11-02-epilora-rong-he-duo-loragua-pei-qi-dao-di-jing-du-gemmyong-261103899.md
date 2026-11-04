---
title: 'EpiLoRA: Fusing Many LoRA Adapters into Low-Precision GEMMs for Serving and
  RL'
title_zh: EpiLoRA：融合多LoRA适配器到低精度GEMM用于服务与RL
authors:
- Hieu Tran
- Hong Yu
affiliations:
- University of Massachusetts Amherst
- University of Massachusetts Lowell
arxiv_id: '2611.03899'
url: https://arxiv.org/abs/2611.03899
pdf_url: https://arxiv.org/pdf/2611.03899
published: '2026-11-02'
collected: '2026-11-04'
category: Training
direction: LoRA低精度推理训练加速
tags:
- LoRA
- GEMM
- vLLM
- FP8
- RL
- serving
one_liner: vLLM插件通过GEMM尾声融合LoRA计算，大幅降低多租户LoRA服务与RL训练开销
practical_value: '- 多租户定制化LLM服务（如电商不同商家/品类的LoRA微调推荐模型）可直接复用EpiLoRA的vLLM插件，单租户单token时延最高降24%，32租户吞吐量最高提9%，无需修改业务逻辑

  - 推荐系统个性化排序、Agent决策逻辑的LoRA RL微调可复用单FP8基模型共享设计，27B模型可在单48GB L40S上训练，无需维护bf16权重副本，节省显存的同时消弭推理训练精度差

  - GEMM尾声融合、计算重叠的思路可迁移到其他低精度推理优化场景，如MoE推荐模型的专家路由计算、RAG重排序层加速，隐藏小算子时延'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LoRA已成为多租户LLM服务、RL微调的标准方案，但基模型逐步向FP8/4位低精度迁移时，LoRA适配器作为独立小核运行在GEMM之外，时延占比随基模型计算效率提升持续升高；同时RL训练需维护独立bf16基模型副本，显存开销大，还存在推理训练精度不匹配的问题，需要额外重要性权重修正。
### 方法关键点
- 核心观察：LoRA的下投影结果仅在GEMM的尾声（输出写入阶段）需要，无需在GEMM计算结束后单独执行适配器计算
- 推理路径：先启动LoRA下投影核，依赖启动低精度GEMM，GEMM主循环权重流式传输期间重叠下投影计算，仅在尾声阶段加每个租户的上投影结果，省去双流架构下的后加和核开销
- 无侵入vLLM插件：支持CUDA图、张量并行，加载时自动选择最优路径（融合/混合/原生vLLM路径），适配不同GPU架构
- RL训练优化：直接基于推理侧的FP8基模型权重计算，无需bf16副本，支持W8A16精度匹配引擎，消弭推理训练精度差，无需重要性权重修正
### 关键结果
- 测试模型覆盖8B~72B，对比vLLM、SGLang、TensorRT-LLM等主流框架，Hopper GPU上单租户单token时延比vLLM低12%~24%，32租户场景吞吐量比vLLM高5%~9%
- RL训练端，27B模型可在单48GB L40S上训练，9B模型FP8 RL精度与bf16训练持平，精度差小于1%
### 最值得记住的一句话
核等待依赖数据的时机可以放在首次需要数据的位置（如GEMM尾声），而非核启动时刻，通过计算重叠可大幅降低小算子的时延占比。
