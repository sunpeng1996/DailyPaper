---
title: 'Beyond Parallel Blindness: Information Floors and Model Gaps in Block Drafting'
title_zh: 超越并行失明：块并行解码中的信息下限与模型差距
authors:
- Xinwei Qiang
- Xiang Fang
- Chang Chen
- Yue Guan
- Yufei Ding
affiliations:
- University of California San Diego
arxiv_id: '2608.27339'
url: https://arxiv.org/abs/2608.27339
pdf_url: https://arxiv.org/pdf/2608.27339
published: '2026-08-27'
collected: '2026-08-28'
category: LLM
direction: LLM推理加速 · 块并行投机解码
tags:
- Speculative Decoding
- Block Drafting
- LLM Inference
- Serving Optimization
- Information Decomposition
one_liner: 将块并行解码的拒绝率拆解为信息下限与模型差距，明确并行代价与优化方向
practical_value: '- 部署LLM投机解码服务时，优先选择order-1块解码架构，仅需增加极轻量的Markov头即可消除86%-100%的并行失明代价，相比全并行架构的接受率上限提升近30%

  - 现有块解码器的优化优先级应向模型拟合倾斜：43%-92%的拒绝率来自模型gap而非固有信息约束，通过更好的蒸馏、训练数据优化就能获得明显收益，远高于调整架构信息约束的投入产出比

  - 服务端性能评估不要迷信自由rollout的理论拒绝率：实际请求中只有前序token通过验证的路径会到达深槽位，深槽位的实际拒绝率比理论值低3倍，优化资源应优先倾斜前3个槽位

  - 针对电商文案生成、Agent多轮对话等开放域场景，并行块长度建议设置为3-5，比代码、数学推理等约束域的块长度短2-4个token，平衡生成速度和接受率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
块并行投机解码是当前主流的LLM推理加速方案，能通过一次前向传播生成多个候选token大幅提升吞吐，但现有评估仅用平均接受长度衡量效果，无法区分拒绝来源是并行架构下无法观测块内前序已生成token的固有信息损失（并行失明），还是解码器本身对可观测信息的建模不足，导致优化方向模糊，无法判断是该调整架构的信息约束还是提升模型拟合能力。

### 方法关键点
- 提出拒绝率的正交分解框架：观测拒绝率 = 信息下限 + 模型gap，其中信息下限是给定信息约束下（如全并行/依赖前m个token）理论上能达到的最低拒绝率，仅由目标模型的生成分布决定，和具体解码器无关；模型gap是实际拒绝率超出下限的部分，完全来自解码器的拟合不足
- 信息下限通过目标模型的自由rollout采样估计：对每个上下文采样多条生成路径，计算所有路径下最优公共候选的平均拒绝率即可得到对应约束的信息下限
- 引入条件阶数m量化信息价值：order-m表示解码器在生成第k个token时可观测前m个块内已生成token，通过对比不同m的下限即可量化新增信息的增益

### 关键实验结果
在gsm8k（数学）、mbpp（代码）、alpaca（开放指令）、arena-hard（长对话）4个领域，覆盖Qwen3-4B/8B/14B、Gemma-4-12B 4个开源模型和DeepSeek-V4-Pro商用API，得到核心结论：
1. 全并行（order-0）架构的第7个槽位信息下限达0.286，对应最高接受率上限仅71%，开放域的信息下限是约束域的2倍以上
2. 仅将条件阶数提升到1（仅依赖前1个块内已生成token），就能消除86%-100%的全并行信息下限，剩余下限最高仅0.041
3. 现有开源解码器的模型gap占比极高：DFlash（全并行）的拒绝率中43%-64%来自模型gap，DSpark（order-1）的oracle条件下85%-92%的拒绝率来自模型gap
4. 实际服务中深槽位的拒绝率比自由rollout低3倍，第0个槽位的优化收益是第7个槽位的4倍

**最值得记住的一句话**：块并行解码的优化收益排序：先做1阶依赖消除并行失明的固有损失，再优化模型拟合缩小模型gap，最后优先倾斜资源优化前几个槽位的效果
