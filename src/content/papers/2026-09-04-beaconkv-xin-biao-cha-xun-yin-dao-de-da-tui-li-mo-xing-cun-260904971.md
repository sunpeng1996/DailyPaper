---
title: 'BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient
  Large Reasoning Model Inference'
title_zh: BeaconKV：信标查询引导的大推理模型KV缓存压缩方法
authors:
- Janghyeon Kim
- Minsoo Kim
- Kyuhong Shim
- Jungwook Choi
affiliations:
- Hanyang University
- Sungkyunkwan University
arxiv_id: '2609.04971'
url: https://arxiv.org/abs/2609.04971
pdf_url: https://arxiv.org/pdf/2609.04971
published: '2026-09-04'
collected: '2026-09-07'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV cache
- Large Reasoning Model
- Compression
- Inference Optimization
- Training-free
one_liner: 无训练的KV缓存压缩方法，通过全局查询簇的信标表征保留推理关键上下文，大幅降本提效
practical_value: '- 部署服务端Agent/LLM4Rec应用时，可直接复用BeaconKV的训练-free压缩方案，在不损失推理准确率的前提下降低GPU内存占用，提升单卡吞吐量，降低部署成本

  - 做长链CoT推理的Agent（比如电商智能导购、复杂用户需求拆解）时，可借鉴「Thought Revisiting Tokens」的观察，主动缓存早期任务规划、用户原始需求相关的KV，避免推理后期上下文丢失

  - 在线动态特征选择/缓存场景，可复用Continual FPS的在线采样思路，用固定内存开销保留历史特征的几何多样性，避免频繁重建特征索引'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大推理模型（LRM）依赖长链CoT生成实现复杂推理，KV缓存随序列长度线性增长，单卡80GB GPU在Qwen3-4B生成32K token、batch=16时KV缓存就超过77GB，内存瓶颈严重。现有KV压缩方法仅依赖最近查询估计未来token重要性，无法捕捉长推理过程中会回访早期上下文的Thought Revisiting Tokens（TRT），易误删关键KV导致推理准确率下降。

### 方法关键点
- 观察到对应TRT的全局查询在嵌入空间会聚为少数相似簇，无需存储全量历史查询，只需为每个簇维护紧凑的信标查询即可预判未来会回访的KV对
- 提出在线Continual FPS算法，用固定大小缓冲器动态保留几何上最具区分度的历史查询作为信标，避免全量历史查询的内存开销
- 观测查询集合同时包含16个最近查询（保障局部连贯性）和16个信标查询（覆盖全局回访模式），对KV重要性打分采用max聚合避免稀疏的TRT信号被均值稀释
- 完全训练-free，无需修改模型结构，可直接集成到现有Transformer推理框架

### 关键结果
在4个开源LRM和AIME24、MATH-500、GPQA-Diamond、LiveCodeBench等推理基准上测试，相对现有方法准确率最高提升31.7个百分点；激进压缩下峰值GPU内存最高降低5.8×，吞吐量相对无压缩基线提升4.3×，准确率接近全KV缓存推理水平；同KV预算下相比RPC、SnapKV等SOTA方法，吞吐量、内存开销相当，准确率最高提升12.3个百分点。

**最值得记住的一句话**：长推理场景下的KV缓存优化不能只看局部最近查询，通过捕捉全局查询的几何聚类特性，可以用极低的额外开销大幅保留推理关键上下文。
