---
title: 'HyQuant: Hybrid-Precision Quantization for LLM Attention'
title_zh: HyQuant：面向LLM注意力模块的混合精度量化框架
authors:
- Jiatong Ding
- Bingxin Xing
- Yu Zhang
- Dian Ding
- Xiaodong Yi
- Xianbin Ouyang
- Feihu Zhou
- Kun Zhang
- Zhenyu Guo
- Hao Pan
affiliations:
- 上海交通大学
- 西安交通大学
- 腾讯蓬莱实验室
- 厦门大学
arxiv_id: '2608.27875'
url: https://arxiv.org/abs/2608.27875
pdf_url: https://arxiv.org/pdf/2608.27875
published: '2026-08-27'
collected: '2026-09-11'
category: LLM
direction: LLM推理优化 · KV cache量化
tags:
- Quantization
- KV Cache
- Long Context Inference
- Attention Optimization
- LLM Inference
one_liner: 保留少量高注意力token与局部窗口全精度，实现低损高效的LLM注意力量化与KV cache压缩
practical_value: '- 电商多轮导购、长会话推荐、Agent类场景可直接复用混合精度策略：保留5%高关注历史token+128长度近会话窗口全精度，其余KV用4bit量化，几乎无损效果前提下降低显存占用、提升长上下文推理速度。

  - 工程实现可直接复用开源的fused反量化+注意力算子，避免单独反量化的带宽开销，32K上下文下Decode端到端速度可提17%，支持更大batch规模，适配大流量商品文案生成、批量智能客服场景。

  - 业务调优可根据场景灵活调整参数：短上下文场景垂直token保留比例设为2%即可，长上下文多轮推理场景调到5%-7%，局部窗口大小可在64/128/256间调整，平衡精度与效率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长上下文LLM推理（如电商多轮导购、长文档商品检索场景）中，Prefill阶段为计算密集型，Decode阶段受KV cache显存与带宽约束，全精度推理成本极高；传统低比特量化对占比极低的高注意力敏感token误差会被反复放大，导致长推理链、CoT场景效果明显下降，而稀疏KV策略又容易丢失长尾有效信息。

### 方法关键点
- 基于列聚合注意力得分识别占比<5%的垂直高关注token，叠加固定长度近期滑动窗口，两类token保留全精度，其余KV做低比特量化
- Prefill阶段设计融合算子，同时处理低比特路径与全精度路径，逻辑对齐FlashAttention，额外开销可忽略
- Decode阶段KV cache按混合精度存储，将反量化嵌入注意力计算流程，避免全精度中间态落地，降低带宽开销
- 垂直token识别开销仅占总runtime的3%~5%，无需训练即可适配任意模型

### 关键实验
在Qwen3、Llama3.1、GLM-4等主流模型上，对比FlashAttention2、KIVI、SageAttention等baseline，LongBench、GSM8K、MATH500任务精度与全精度基本持平；Decode kernel速度最高提升3.58×，端到端Decode速度最高提升1.17×，32K上下文下batch size最大支持到32，远高于同类量化方案。

### 核心结论
仅保留5%高贡献token加局部窗口全精度，就能让4bit注意力量化达到接近全精度的效果，同时大幅降低长上下文推理成本。
