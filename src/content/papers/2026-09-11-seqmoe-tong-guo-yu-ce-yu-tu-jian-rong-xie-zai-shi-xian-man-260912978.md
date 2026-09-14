---
title: 'SeqMoE: Toward Full-Load Performance via Predictive and Graph-Compatible MoE
  Offloading'
title_zh: SeqMoE：通过预测与图兼容卸载实现MoE近满负载推理
authors:
- Zihan Wang
- Yuqi Wang
- Lei Gong
- Cheng Tang
- Wenqi Lou
- Teng Wang
- Chao Wang
- Xuehai Zhou
affiliations:
- University of Science and Technology of China
- Suzhou Institute for Advanced Research, University of Science and Technology of
  China
arxiv_id: '2609.12978'
url: https://arxiv.org/abs/2609.12978
pdf_url: https://arxiv.org/pdf/2609.12978
published: '2026-09-11'
collected: '2026-09-14'
category: LLM
direction: MoE LLM推理 · 内存卸载加速
tags:
- MoE
- Inference Optimization
- Offloading
- Sequence Modeling
- CUDA Graph
one_liner: 将MoE专家激活预测转为序列建模，结合图兼容运行时，45%专家驻留即可达80%满负载推理性能
practical_value: '- 业务部署MoE结构LLM做生成式推荐、Agent推理时，可复用Seq2Seq专家激活预测+概率Belady缓存策略，在显存不足场景下提升推理速度，降低部署成本

  - 边缘端（如客户端智能导购Agent、端侧推荐）的MoE模型部署，可借鉴图兼容卸载运行时设计，小批量推理场景下大幅降低调度开销，逼近满负载性能

  - 多任务MoE模型部署场景下，可复用联合预fetch调度的matroid贪心算法，优化有限PCIe带宽下的专家加载优先级，提升带宽利用率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
MoE结构LLM参数规模大，边缘/消费级显卡显存不足问题突出，现有卸载方案因专家预fetch不准、调度低效、执行开销大，仅能达到2%-30%的满负载性能，无法充分利用MoE稀疏激活的结构优势。

### 方法关键点
- 将专家激活预测重构为序列建模任务，采用轻量Mamba2作为预测骨干，支持多步多层激活预测，Top-k+3召回超90%
- 预fetch调度建模为带截止日期的作业排序问题，用matroid贪心算法在带宽约束下最大化专家命中期望
- 缓存替换采用概率Belady策略，基于多步预测结果优先保留近期激活概率高的专家，规避LRU等历史统计策略的局限性
- 设计图兼容运行时，通过全局共享缓存槽+无同步编排规则，支持CUDA Graph端到端捕获，大幅降低调度开销

### 关键结果
在Qwen3-30B、DeepSeek-V4等4款主流MoE模型上对比llama.cpp、MoE-Infinity、FreeToken等基线，45%专家驻留时平均专家命中率达96.97%，推理性能达80.22%满负载水平，较最强基线FreeToken提升55.8%。

最值得记住的结论：MoE稀疏激活的时序依赖可通过序列建模精准捕获，联合优化预测、调度、执行三层设计，可在显存减半的前提下实现近满负载推理。
