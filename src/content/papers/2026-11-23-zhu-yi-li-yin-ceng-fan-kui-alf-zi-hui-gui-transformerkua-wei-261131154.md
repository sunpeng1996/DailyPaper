---
title: Attention Latent Feedback
title_zh: 注意力隐层反馈（ALF）：自回归Transformer跨位置隐状态复用架构
authors:
- Xuyuan Xiong
- Siyu Chen
- Mengzhao Chen
- Yue Su
- Zhuoran Yang
- Ping Luo
- Xihui Liu
affiliations:
- The University of Hong Kong MMLab
- Yale University
arxiv_id: '2611.31154'
url: https://arxiv.org/abs/2611.31154
pdf_url: https://arxiv.org/pdf/2611.31154
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: 大模型架构优化 · 自回归解码提效
tags:
- Transformer
- Autoregressive Decoding
- MoE
- Latent Feedback
- Model Efficiency
one_liner: 为自回归Transformer设计跨层隐层反馈通路，仅1.1%解码FLOP开销提升效果与数据效率
practical_value: '- 业务用小LLM（如文案生成、Agent推理）可直接落地固定最近4隐层的等权ALF变体，仅加<1%解码开销即可拿到89%+的全量ALF收益，无需额外复杂训练

  - 做自回归生成类业务（如搜索query补全、个性化推荐文案）时，可放弃仅复用前一token最终层状态的方案，改为复用中间层隐状态，能获得更高的生成质量提升

  - 迭代时无需从头训练带ALF的模型，可在基础模型训练到75%步长后再开启反馈通路训剩余步骤，大幅降低试错成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
自回归Transformer解码时，前一token的深层隐状态已计算完成，但当前token的浅层无法直接访问；现有隐层反馈方案仅传递前一token的最终层状态，浪费了中间层的高价值信号，且普遍存在训练无法并行、效果提升有限的问题。

### 方法关键点
- 双通路反馈设计：1）token输入层注入前一token最终层状态的低秩投影；2）每个子层可attention前一token自身深度及以上的所有隐层输出，动态加权后混合到当前子层输入
- 低开销工程优化：每个隐层用LoRA式低秩投影映射，初始化为0不影响基础模型收敛；训练仅最后25%步长开启反馈，用2次并行Jacobi迭代实现序列并行，解码仅需缓存前一token的子层输出，单pass即可完成，解码FLOP开销仅1.1%
- 轻量化落地变体：基于注意力权重的局部分布规律，固定仅取前一token当前层及之后3层的等权平均，可保留89%~94%的全量ALF收益，读成本从O(L²)降至O(L)

### 关键实验结果
- 在1.6B/2.6B/4.0B三种规模MoE模型上测试，ALF比标准残差基线降低held-out loss 0.022~0.024 nats，效果全面优于SOTA的FBT反馈方案
- 4.0B MoE上17个下游任务平均准确率从45.1%提升至47.0%；1.6B MoE上ALF的效果等价于基线模型用1.38倍训练token量的效果

### 核心结论
自回归解码时跨位置复用中间隐层的收益远高于仅复用最终层，且可做到极低开销落地。
