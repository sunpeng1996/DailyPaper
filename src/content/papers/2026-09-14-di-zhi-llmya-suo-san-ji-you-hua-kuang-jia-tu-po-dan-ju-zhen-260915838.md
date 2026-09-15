---
title: 'Per-Matrix Optimality Is Not Enough: Three-Level Optimization for Low-Rank
  LLM Compression'
title_zh: 低秩LLM压缩三级优化框架：突破单矩阵最优局限
authors:
- Huicheng Zhang
- Xiyao Feng
- Ze-Tong Li
- Chengkai Zhu
- Xiao Shi
- Xiwei Pan
- Jinguo Liu
- Ge Bai
- Xin Wang
affiliations:
- Hong Kong University of Science and Technology (Guangzhou)
- QudeLeap Research
arxiv_id: '2609.15838'
url: https://arxiv.org/abs/2609.15838
pdf_url: https://arxiv.org/pdf/2609.15838
published: '2026-09-14'
collected: '2026-09-15'
category: LLM
direction: LLM低秩压缩 · 三级SVD优化
tags:
- LLM Compression
- Low-Rank Factorization
- SVD
- Model Efficiency
- OOD Robustness
one_liner: 仅用256条校准序列的三级SVD优化链，大幅提升低秩LLM压缩后性能与分布外鲁棒性
practical_value: '- 自有垂域LLM（如电商文案生成、用户意图理解大模型）压缩可复用该三级优化框架，仅需少量（最低32条）领域校准序列即可在不新增参数的前提下大幅降低压缩性能损失，相比SVD-LLM+LoRA方案减少99%以上的外部数据依赖

  - 数据稀缺场景下务必保留block-level joint optimization阶段，可显著提升OOD泛化能力，比如小众品类推荐query理解模型压缩时，该阶段可减少跨域分布偏移带来的精度损失

  - 压缩率≤20%时仅用L1（白化SVD）即可满足需求，无需额外训练开销；压缩率≥50%时再叠加L2、L3阶段，平衡压缩效果与离线算力投入'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有基于单矩阵SVD的LLM低秩压缩方法虽满足单矩阵最优，但忽略了Transformer块内部、块之间的误差累积效应，压缩后困惑度骤升，且需要大量外部数据做LoRA微调才能恢复性能，无法满足边缘部署、小样本校准的业务需求。

### 方法关键点
三级优化链全程仅用256条校准序列，无额外标注数据：
1. **L1 单矩阵白化SVD**：实现单矩阵层面的最优低秩分解，作为初始化
2. **L2 块级联合优化**：同时优化一个Transformer块内7个投影层的低秩因子，损失由块输出重建MSE + 下一块词表分布KL散度组成，捕捉块内误差交互
3. **L3 端到端微调**：用语言模型损失优化全量低秩因子，修正跨块误差累积，无新增参数
块级优化的lookahead探针提供隐式正则，可显著提升压缩后模型的OOD鲁棒性。

### 关键结果
在LLaMA-7B、Mistral-7B等5种7B-13B规模模型上测试，基线对比ASVD、SVD-LLM、SAES-SVD等主流SVD压缩方法：60%压缩率下，LLaMA-7B的WikiText-2困惑度从单矩阵SVD的42.1降到11.4，比需要50K外部样本的SVD-LLM+Sequential LoRA（15.0）效果更优；跳过L2阶段会导致PTB OOD困惑度上升24点，且额外端到端训练无法弥补该差距；压缩率80%时三级优化累计降低困惑度22倍。

**最值得记住的一句话**：低秩压缩的性能缺口本质不是单矩阵分解不够优，而是优化scope没覆盖误差传播的完整计算图。
