---
title: Looped Models are Fast Multi-Token Predictors
title_zh: Floodgates：基于循环语言模型的高速多Token无损解码
authors:
- Ayhan Suleymanzade
- Sean McLeish
- Sehoon Kim
- Jinwoo Kim
- Antoine Bosselut
affiliations:
- EPFL
- University of Maryland
- KAIST
arxiv_id: '2611.33896'
url: https://arxiv.org/abs/2611.33896
pdf_url: https://arxiv.org/pdf/2611.33896
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: LLM推理加速 · 自投机解码
tags:
- Speculative Decoding
- Looped LLM
- LoRA
- KV Cache
- Inference Acceleration
one_liner: 针对循环语言模型提出轻量LoRA适配的自投机解码方案，实现最高7.5倍无损推理加速
practical_value: '- 做生成式推荐、电商导购Agent等LLM驱动业务时，若采用循环LLM架构，可直接复用Floodgates方案，仅用几十M LoRA参数就能实现2-7倍无损推理提速，大幅降低在线服务GPU成本

  - 多token并行生成的mask token+深度前缀KV cache复用思路，可迁移到非循环LLM的投机解码优化，尤其适合商品推荐理由、营销短文案等短序列生成场景，提升单卡吞吐量

  - 高并发服务下的动态验证预算选择策略，可直接复用到现有LLM推理服务，大batch场景下吞吐量可提升19%-54%，应对电商大促高流量场景效果显著

  - 循环LLM的全深度训练范式让浅层loop即可编码未来token信息，做端侧推荐/轻量Agent时可优先考虑循环架构，灵活调整计算量平衡速度与效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有自回归LLM解码存在串行瓶颈，投机解码要么用额外小draft模型（容量有限接受率低），要么用非循环模型的前几层（仅用部分参数效果差）；循环LLM的现有自投机解码方法一次只能生成1个token，还需要维护多深度KV cache，高并发下内存瓶颈严重，无法充分发挥循环架构的参数复用优势。

### 方法关键点
- 提出Floodgates自投机解码：在当前token后追加k个可学习mask token，仅用1次浅层loop跑通全量模型参数，并行生成k个draft token，仅微调仅在draft阶段激活的LoRA参数，不改动base模型保证解码无损
- 复用验证阶段生成的深度前缀KV cache，让浅层draft loop可以直接获取全深度上下文表示，提升draft接受率
- 针对高loop数的深层循环模型，新增无训练的弹性draft机制：用多次预训练loop迭代优化初始draft，平衡draft成本和接受率
- 高并发场景下动态选择验证预算：仅验证接受概率最高的M个draft，避免计算浪费，提升大batch吞吐量

### 关键结果
在7款循环LLM（Ouro、Recurrent Llama 3.2等）、5个基准数据集（GSM8K、HumanEval+等）上测试：贪心解码下所有场景均为最快无损方法，batch size=1时最高比原生解码快7.5倍，部分场景比SOTA基线快近1倍；大batch下吞吐量最高是最强基线的1.9倍，比原生解码高2.7倍，动态验证策略在最大batch下可提升吞吐量19%-54%；深度前缀KV cache相比浅层cache能带来10%-32%的速度提升。

### 核心结论
循环语言模型的全深度训练让浅层loop天然具备未来token预测能力，仅需极小参数适配就能实现远超独立draft模型的投机解码效率。
