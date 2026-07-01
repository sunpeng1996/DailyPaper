---
title: Fork-Think with Confidence
title_zh: 基于置信度的分叉推理：先决策后思考的高效LLM推理范式
authors:
- Zena Al-Khalili
- Rafi Hakim
- Dietrich Klakow
- Ji-Ung Lee
affiliations:
- Saarland University, Germany
arxiv_id: '2606.31484'
url: https://arxiv.org/abs/2606.31484
pdf_url: https://arxiv.org/pdf/2606.31484
published: '2026-06-30'
collected: '2026-07-01'
category: Reasoning
direction: LLM推理 · 并行推理效率优化
tags:
- LLM Reasoning
- Inference Optimization
- Parallel Thinking
- Confidence Estimation
- Efficient Inference
one_liner: 提出先决策后思考的Fork-think推理范式，比传统并行推理省30%token、57%耗时，性能持平更优
practical_value: '- 线上Agent/LLM推理场景可直接替换原有全量并行采样策略：先跑1条贪心种子路径，仅在模型置信度最低的位置分叉采样，可在性能无损前提下降低token成本和推理延迟

  - 电商场景LLM生成query/商品文案/推荐理由时，可复用该置信度选点采样trick：既保证生成多样性，又避免无效重复生成，降低推理算力消耗

  - 搭配SGLang/radix cache类前缀缓存能力，分叉路径的公共前缀可复用KV cache，进一步降低高吞吐场景下的推理耗时，适合线上服务落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有并行推理方法（如Self-Consistency）普遍采用「先思考后决策」范式：开头即生成大量并行推理路径再筛选，不可避免产生大量无效生成，token消耗高、推理延迟长，部分优化方法还需要额外warm-up或离线训练，低资源、低延迟要求的线上场景难以落地。
### 方法关键点
- 采用「先决策后思考」范式，首先用贪心解码生成指定长度的种子路径，每个位置的置信度取top-k候选token的平均对数概率
- 选择置信度最低的m个位置作为分叉点，每个分叉点基于已有前缀采样n条后续推理路径
- 所有路径生成后提取答案，通过多数投票/置信度加权投票聚合得到最终结果，全程无需任何离线训练或预热
### 关键实验结果
在AIME24、AIME25、GPQA三个推理基准，Qwen3-8B、DeepSeek-8B、Phi-4-RP-14B三个模型上验证，对比Parallel Thinking、ASC、DeepConf等基线：
1. 相比传统Parallel Thinking，最多降低30% token消耗、57%推理耗时，准确率持平甚至最高提升1.7pp
2. 加入早停、加权投票的Flex-Fork-think与SOTA方法DeepConf性能持平，最多再省37% token
3. 分叉因子低至4时仍能保持和Parallel Thinking相当的性能，适配低资源场景
### 核心结论
默认从头开始并行采样的「先思考后决策」范式未必最优，在推理过程中模型最不确定的点分叉采样，能用更低成本拿到更优效果
