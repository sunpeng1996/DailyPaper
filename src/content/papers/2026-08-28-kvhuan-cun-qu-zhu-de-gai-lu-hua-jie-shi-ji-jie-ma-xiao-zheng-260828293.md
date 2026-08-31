---
title: A Probabilistic Interpretation of KV Cache Eviction
title_zh: KV缓存驱逐的概率化解释及解码校正方法
authors:
- Renato Geh
- Alex Chen
- Daniel Israel
- Aditya Grover
- Guy Van den Broeck
affiliations:
- University of California, Los Angeles
arxiv_id: '2608.28293'
url: https://arxiv.org/abs/2608.28293
pdf_url: https://arxiv.org/pdf/2608.28293
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM推理优化 · KV cache 驱逐
tags:
- KV cache
- LLM Inference
- Importance Sampling
- Long Context
- Probabilistic Reasoning
one_liner: 将KV缓存驱逐形式化为期望估计问题，提出带解码校正的概率驱逐策略，跨任务鲁棒性更强
practical_value: '- 现有KV驱逐策略（H2O、StreamingLLM等）可直接适配该框架：将原有驱逐得分归一化为采样提议分布，叠加解码校正即可降低误差，无需完全重构策略

  - 电商/Agent场景下的长上下文LLM服务部署，可引入带温度调节的概率KV驱逐，相同显存预算下降低特定任务灾难性失效概率，提升服务稳定性

  - 推荐系统排序模块的多兴趣注意力可复用该思路：通过采样+重要性校正近似注意力计算，降低长序列推理复杂度，提升线上QPS

  - KV缓存预算可向下层注意力头倾斜、上层少分配，与PyramidKV结论一致，同等压缩率下可进一步提升生成效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有KV缓存驱逐策略大多基于启发式规则，缺乏理论形式化支撑，且普遍忽略驱逐后解码阶段的分布偏移问题：被驱逐的KV条目会扭曲注意力分布，导致偏差无界，容易在特定任务出现灾难性失效，同时最优KV驱逐的问题复杂度此前也没有明确证明。

### 方法关键点
- 严格证明最优KV驱逐问题是NP-complete，不存在多项式时间的精确解
- 将Attention计算等价为值向量的期望估计，KV驱逐转化为期望估计的采样近似问题，所有现有启发式驱逐策略都可以纳入该概率框架
- 提出解码阶段校正算法：驱逐时基于现有启发式得分构造提议分布采样，记录采样计数，解码时用自归一化重要性采样校正扭曲的注意力分布，偏差和方差均为O(1/m)（m为采样数）
- 引入温度参数调节校正强度，灵活实现偏差-方差权衡，适配不同压缩率场景

### 关键结果
在Llama3.2-3B、Qwen3-4B上测试，覆盖LongBench、RULER两个长上下文benchmark，对比H2O、SnapKV、StreamingLLM、TOVA等SOTA驱逐策略：相同压缩率下，概率驱逐+校正的平均得分最高提升3.2%，跨任务鲁棒性win score比最优baseline高5.7%，在0.2~0.6的中低压缩率区间优势尤为突出。

最值得记住的结论：现有启发式KV驱逐是零方差但偏差无界的估计器，通过概率化采样加解码校正，可在不增加显存开销的前提下大幅提升长上下文任务的鲁棒性
