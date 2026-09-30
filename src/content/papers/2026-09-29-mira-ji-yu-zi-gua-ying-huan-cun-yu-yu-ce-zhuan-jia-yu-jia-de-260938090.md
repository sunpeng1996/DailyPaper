---
title: 'Mira: Memory-Efficient MoE Inference Using Adaptive Caching and Predictive
  Expert Staging'
title_zh: Mira：基于自适应缓存与预测专家预加载的内存高效MoE推理框架
authors:
- Sanjali Yadav
- Bahar Asgari
affiliations:
- University of Maryland, College Park
arxiv_id: '2609.38090'
url: https://arxiv.org/abs/2609.38090
pdf_url: https://arxiv.org/pdf/2609.38090
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM MoE 推理内存优化
tags:
- MoE
- Inference Optimization
- Quantization
- Caching
- Prefetching
- Single GPU
one_liner: 面向单GPU受限显存场景，通过预测预加载+双层缓存+定制量化实现MoE推理数倍性能提升
practical_value: '- 业务侧若使用MoE LLM做生成式推荐/Agent推理，可复用Mira的定制INT8量化方案：仅对专家参数做INT8量化、共享FFN三矩阵scale因子，精度损失可忽略前提下降低1.6x+元数据传输开销，适配显存受限的边缘/单GPU部署场景

  - 可借鉴HOT+STAGE双层缓存设计，针对MoE专家激活的长尾偏态特性，区分高频常驻专家和短期预加载专家，相比通用LRU/LFU缓存减少显存浪费，降低PCIe传输stalls

  - 对低延时要求的实时推荐/对话Agent场景，可复用i→i+2层预测预加载思路，用轻量路由特征训练小预测头预判未来所需专家，重叠计算与传输时间，最高可降低11.7×Time-to-First-Token，提升用户交互体验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
MoE是LLM扩缩容的主流架构，但单GPU部署时专家参数占内存比高、token级路由动态偏态，传统响应式专家加载方案要么缓存利用率低、要么无法重叠传输与计算，显存受限场景下推理性能差，难以支撑电商推荐/Agent的低延时本地部署需求。

### 方法关键点
- 定制INT8量化：仅对MoE专家的FFN三矩阵做INT8量化，共享行级scale因子，元数据开销降低1.6×以上，精度损失可忽略
- 轻量预测预加载：每层新增极小预测头，基于当前隐状态、路由logit、历史激活特征，预测未来2层所需专家，提前异步预加载到GPU
- HOT+STAGE双层缓存：GPU显存划分为高频常驻HOT区和预加载STAGE区，基于token级路由遥测动态调整HOT区专家，避免缓存污染

### 关键实验
在ShareGPT对话数据集、MMLU下游任务上测试，对比DeepSpeed、MoE-Infinity、Fiddler等SOTA基线：24GB显存下平均吞吐量比MoE-Infinity高5.71×，Time-to-First-Token比Fiddler低11.71×，beam搜索推理速度比Fiddler高3.84×，下游任务精度与FP16基线几乎一致。

### 最值得记住的一句话
MoE推理优化的核心是利用路由偏态特性，从被动响应转向主动预测，通过算法-系统协同设计在显存、带宽、精度三者间找到最优平衡点。
