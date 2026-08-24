---
title: 'TreeWY: Speculative Verification for Gated DeltaNet Hybrids'
title_zh: TreeWY：面向门控DeltaNet混合模型的推测验证优化方法
authors:
- Sneha Murthy Ghantasala
affiliations:
- Thomson Reuters
arxiv_id: '2608.20961'
url: https://arxiv.org/abs/2608.20961
pdf_url: https://arxiv.org/pdf/2608.20961
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: LLM推理优化 · 混合模型推测解码
tags:
- Speculative Decoding
- Gated DeltaNet
- KV cache
- LLM Inference
- vLLM
one_liner: 通过树状WY变换消除GDN层逐节点状态快照，大幅降低混合模型推测解码的内存开销
practical_value: '- 若业务使用GDN/Mamba类混合大模型做推荐文案生成/Agent推理，可直接集成TreeWY到vLLM部署链路，内存绑定场景下吞吐量提升1.15x~1.4x，p99
  TTFT最高降40x

  - 推测解码的状态快照瓶颈可参考伪值矩阵替代思路，无需存储全量中间状态，仅验证通过后重建状态，适合KV资源紧张的高并发线上服务

  - 树状推测解码的内存平摊思路可复用，同内存预算下可支持更宽的候选树，提升生成/召回的候选覆盖率，当前无吞吐量增益但可作为长期优化方向'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
混合大模型（软注意力+GDN线性注意力层）内存效率突出，GDN层用固定大小循环状态替代随上下文增长的KV cache，但做推测解码时需要为每个候选token存储全量状态快照，且快照不可跨分支共享，宽树高接受率的推测解码完全不可行，内存瓶颈严重限制服务并发和推理速度。

### 方法关键点
- 基于门控delta规则推导树状WY变换，将GDN状态更新拆解为伪值的衰减加权和，无需逐节点维护中间状态
- 候选链/树的所有节点伪值通过一次前向代入求解下三角线性系统得到，所有节点输出均可基于该解直接计算
- 仅在验证到接受节点后，通过伪值矩阵重建后续需要的循环状态，伪值矩阵大小仅为全量状态的1/128（dk=dv=128场景下）

### 关键实验
在vLLM上实现，测试Qwen3.5 35B、397B两个混合模型，对比vLLM默认全量快照方案，覆盖ShareGPT、spec-bench、BurstGPT等6类workload：
- 同负载下KV cache峰值用量降低2~3倍，内存绑定场景下吞吐量最高提升1.49x，p99 TTFT最高降低40倍，非内存绑定场景吞吐量仅损失3%以内
- 支持任意宽度候选树，同内存预算下可支撑39节点宽树，接受长度比3节点链提升10.5%，全量快照方案完全无法支撑宽树
- 和同期ReplaySSM方案对比，两者释放的KV内存基本相当，ReplaySSM链状推测下吞吐量略优，TreeWY对树状结构的支持更通用

### 核心结论
混合模型推测解码的内存瓶颈核心是GDN中间状态快照冗余，用数学变换替代冗余状态存储是比工程调优更本质的优化路径
