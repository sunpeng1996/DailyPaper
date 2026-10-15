---
title: Joint Subspace Sparse Attention for Efficient Long-Context Decoding
title_zh: 联合子空间稀疏注意力实现高效长上下文LLM解码
authors:
- Jiwon Song
- Yoongon Kim
- Jae-Joon Kim
affiliations:
- Seoul National University
arxiv_id: '2610.19026'
url: https://arxiv.org/abs/2610.19026
pdf_url: https://arxiv.org/pdf/2610.19026
published: '2026-10-12'
collected: '2026-10-15'
category: LLM
direction: 长上下文LLM · 稀疏注意力推理优化
tags:
- KV_cache
- Sparse_Attention
- Long_Context_LLM
- GQA
- Inference_Optimization
one_liner: 提出训练无关的联合子空间稀疏注意力JSSA，兼顾长上下文LLM解码精度与吞吐量
practical_value: '- Agent场景多轮对话、长用户历史解码可直接复用JSSA，无需修改原有模型参数，仅用业务长文本校准投影矩阵即可，128K上下文下解码吞吐量最高提升6倍，精度损失小于1%

  - 电商推荐的大模型文案生成、长query理解服务端部署，可直接引入JSSA的gather-free索引注意力kernel，消除token级KV选择的gather开销，端到端吞吐量相比传统gather-then-attend提升1~2倍

  - LLM4Rec长用户行为建模场景，可借鉴联合query-key子空间投影思路做低维KV排序，低维度下（如r=4）精度比单独投影key/query的方案高5~24个LongBench点，大幅降低排序开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM解码瓶颈集中于KV cache访问，现有稀疏注意力方案存在明显缺陷：粗粒度块/页级方案精度损失大，token级方案要么低维打分丢失query-key交互结构导致排序不准，要么散乱token的gather开销抵消稀疏收益，且多数方案跨架构适配性差，超大规模模型上需要重新训练才能生效。
### 方法关键点
- 分数保留联合投影：以最小化双线性打分误差为目标，用可解的边际目标上界替代非凸原目标，得到闭式谱解，无需迭代优化或修改模型参数
- GQA适配gather-free kernel：支持每个KV头独立选择token，无需将选中KV gather到连续缓存，直接读取原生GQA布局的KV cache，消除gather overhead
- 低开销投影打分缓存：FP8存储低维投影key缓存，仅占原生BF16 KV缓存的6.25%以内，最终注意力计算仍使用全维度KV保证精度
### 关键结果
在LongBench、RULER、AIME2025等基准上对比FASA、Loki、QUEST等基线：128K上下文下B200 GPU最高达全KV注意力6.43倍吞吐量，精度与全KV差距小于1个点；700B超大规模模型上无需训练即可达到原生稀疏注意力DSA相当的推理精度，吞吐量达DSA的96%~99%；低投影维度下（r=4），LongBench精度比FASA、Loki分别高5.4、24.48个点。
### 最值得记住的结论
训练无关的长上下文稀疏注意力方案只要同时优化选择精度和执行效率，就能达到和原生训练稀疏机制相当的效果，大幅降低落地成本。
