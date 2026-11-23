---
title: Speculative Decoding Is Less Speculative Than You Think
title_zh: 利用预采样验证随机数的无训练投机解码加速框架DICE
authors:
- Guanning Zeng
- Andrea Zanette
affiliations:
- Carnegie Mellon University
arxiv_id: '2611.27891'
url: https://arxiv.org/abs/2611.27891
pdf_url: https://arxiv.org/pdf/2611.27891
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM推理优化 · 投机解码加速
tags:
- speculative_decoding
- inference_acceleration
- LLM_serving
- training_free
- sampling
one_liner: 预采样并同步验证随机数指导投机候选选择，无训练下实现解码吞吐量最高24.6%提升
practical_value: '- 业务侧LLM服务（智能客服、商品文案生成、Agent决策调用）可直接将DICE集成到现有EAGLE/Medusa等投机解码流水线，无需重新训练drafter即可获得5%~20%的吞吐量提升，降低推理成本

  - 电商大促等高并发场景可优先适配DICE，其在并发数64时仍比自回归解码快1.19~1.28倍，性能优于其他同类型投机解码基线，可有效应对峰值流量

  - 异步预取类场景（RAG查询预生成、推荐prompt预生成、多轮对话下一轮候选预判）可复用DICE的随机数同步思路，用已知采样种子预判候选优先级，提升缓存命中率10%以上'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
投机解码是当前主流LLM推理加速方案，通过轻量drafter预生成候选、目标模型单次并行验证降低推理延迟，但其效率受限于drafter有限算力下的候选路径选择，现有优化多聚焦于缩小drafter与目标模型分布差异，忽略了验证过程的采样随机数可提前生成，这一免费信息可大幅降低候选选择的不确定性。
### 方法关键点
- 提出DICE无训练框架：预生成验证用的Gumbel/Uniform随机数，在drafter和目标模型间同步，完全保留原目标采样分布，无额外训练成本
- 树形解码场景：将已知随机数与drafter logits加权融合，计算路径被访问的概率，指导候选生成、树扩展、节点选择，仅需1~3个prompt的少量数据即可完成α、σ超参数校准
- 异步预取场景：基于已知随机数估算验证接受长度和修正token的概率，优先预取高概率的下一轮候选，提升缓存命中率
### 关键结果
在Spec-Bench、SPEED-Bench等数据集上，覆盖EAGLE系列、MTP、独立小drafter等18种模型-后端配置，对比原生投机解码基线：
1. 树形解码吞吐量最高提升24.6%，异步预取场景吞吐量最高提升13.7%，缓存命中率从基线的45.6%~67.6%提升至69.8%~80.7%
2. 跨采样温度、并发数、硬件配置均稳定生效，并发数达64时仍比自回归解码快1.19~1.28倍，性能优于所有对比基线

> 最值得记住的结论：采样随机数无需在投机计算时当作未知量，提前同步可在零训练成本下大幅提升推理资源利用率
