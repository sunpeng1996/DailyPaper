---
title: 'YANchor-4B: Effective Long-Horizon Reasoning in O(N) Time with O(1) Memory'
title_zh: YANchor-4B：O(N)时间O(1)内存的高效长程推理大模型
authors:
- Huishan Ji
- Hua Xu
- Weiming Zhang
- Qirui Ye
affiliations:
- Rocore Matrix
- Carnegie Mellon University
arxiv_id: '2610.10118'
url: https://arxiv.org/abs/2610.10118
pdf_url: https://arxiv.org/pdf/2610.10118
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: 大模型架构 · 长上下文推理优化
tags:
- Long-Context-Reasoning
- Recurrent-LLM
- Efficient-Inference
- Memory-Anchor
- Constant-Memory
one_liner: 基于Qwen3.5-4B改造，融合记忆锚点机制实现O(N)时间O(1)内存的高效长程推理
practical_value: '- 可将记忆锚点机制迁移到电商长序列用户建模：无需存储全量用户行为KV cache，仅保留Top-K高价值行为锚点，同时降低内存开销、保障召回排序精度

  - 适合端侧/边缘侧推荐Agent部署：O(1)内存的推理架构支持导购、直播互动等长会话场景，无需频繁清理上下文缓存

  - 高并发长序列生成场景可复用其吞吐优化方案：单H100下批量长文本生成（如个性化文案、评论总结）吞吐是同参数量Transformer的3~6倍，显著降低推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长程推理方案存在明显短板：全历史注意力的O(N²)计算+O(N)内存开销导致长序列下吞吐低、显存占用爆炸；循环压缩类方案易丢失关键细节，无法支撑复杂推理任务，亟需兼顾推理效果和效率的长程推理架构。

### 方法关键点
- 架构改造自Qwen3.5-4B，采用「Gated DeltaNet循环层+1024 token局部注意力+独立记忆模块」三层历史表示结构，所有历史路径固定容量
- 独立记忆模块通过准入网络给每个KV组打分，每256 token块仅保留Top-1024高价值记录作为记忆锚点，存储容量不随序列长度扩容
- 分四阶段训练：记忆适配→联合适配→监督后训练→RLVR结果导向微调，平衡记忆能力与通用任务效果

### 关键结果
- 推理性能：AIME 2024-2026 pass@1达82.93%，HMMT 2026 pass@1达63.64%，远超13B参数级同类型循环/状态空间模型，性能接近原Qwen3.5-4B
- 推理效率：单H100上128K输入+输出解码速度213 token/s，批量长生成吞吐是Qwen3.5-4B的4.12~6.58倍，单序列64K上下文内存仅67.7 GiB，远低于同类Transformer的上千GiB需求
- 通用能力：24项基准测试平均得分78.64，比最优同类型基线高22.35分；支持多模态，6项VL基准平均准确率84.94%

最值得记住的结论：通过保留关键记忆锚点的设计，可在O(N)时间O(1)内存约束下实现接近全注意力Transformer的长程推理效果，同时兼顾能力与效率。
