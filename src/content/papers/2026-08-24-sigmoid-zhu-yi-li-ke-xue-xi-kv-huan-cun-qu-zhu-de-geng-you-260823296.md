---
title: Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction
title_zh: Sigmoid 注意力：可学习 KV 缓存驱逐的更优基底
authors:
- Isaac
- Li
affiliations:
- University of Pittsburgh
arxiv_id: '2608.23296'
url: https://arxiv.org/abs/2608.23296
pdf_url: https://arxiv.org/pdf/2608.23296
published: '2026-08-24'
collected: '2026-08-25'
category: LLM
direction: LLM 推理优化 · KV 缓存驱逐
tags:
- KV cache
- Sigmoid Attention
- LLM Inference
- Learned Eviction
- Softmax Attention
one_liner: 验证 Sigmoid 注意力相比 Softmax 更适配可学习 KV 缓存硬驱逐，软到硬转移损失更低
practical_value: '- 电商LLM导购、推荐文案生成等推理服务优化KV缓存降本时，可优先采用Sigmoid注意力+可学习门控方案，相比Softmax+门控能在近乎无损PPL的前提下实现19.8%~32.2%的KV缓存压缩，效果优于H2O、KeyDiff等后处理方法

  - 可直接复用论文的可学习门控双注入设计（logit加log(g+ε)、value乘g），训练用交叉熵加门控均值正则即可学到可阈值化的保留/删除信号，无需复杂损失设计

  - 门控的Token选择性规律（优先删除停用词、换行符，保留内容词、空格、数字）可直接用于自定义规则化KV缓存驱逐策略，无需训练即可实现无/低损缓存压缩，适配电商话术分布'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
可学习KV缓存驱逐普遍存在软硬不匹配问题：训练时只能用可微分软门控衰减Token贡献，无法真正删除KV条目；推理时只有物理删除KV才能释放内存，软衰减到硬删除的转移稳定性直接决定缓存压缩后的效果损失。现有工作大多聚焦驱逐策略本身，很少关注注意力基底对软到硬转移效果的影响。

### 方法关键点
- 设计2×2×2对照实验，变量为注意力类型（Softmax/Sigmoid）、是否加可学习门控、是否使用RoPE位置编码，所有模型为GPT-2规模（12层、12头、d_model=768），在1B Token的OpenWebText数据集训练3个epoch
- Sigmoid注意力加入逐查询负偏置`b(i) = -log(i+1)`稳定行和，解决非归一化注意力的数值不稳定问题
- 可学习门控采用双注入设计：训练时对注意力logit加`log(g+ε)`、对value乘`g`模拟删除效果；推理时直接删除门控值小于阈值τ的KV条目，阈值通过验证集搜索确定，要求PPL上升小于0.1
- 训练损失为交叉熵加门控均值正则，拉低门控值鼓励压缩，λ固定为0.03，无需针对不同架构调参

### 关键实验结果
无驱逐场景下Softmax效果更优，PPL比Sigmoid低0.36（带RoPE）/1.21（不带RoPE）；加可学习硬驱逐后Sigmoid表现反超：带RoPE的Sigmoid门控模型可删除19.8%的KV条目，PPL几乎无损失（22.424 vs 无驱逐的22.440），效果优于同缓存大小的H2O、KeyDiff后处理基线；不带RoPE的Sigmoid门控模型可删除32.2%的KV条目，PPL仅上升0.034，同样优于同规模的后处理基线，而Softmax门控模型在同压缩率下效果不如H2O。

最值得记住的结论：KV缓存驱逐不只是推理侧的启发式优化，与注意力架构的联合设计能实现更优的压缩效率与性能平衡。
