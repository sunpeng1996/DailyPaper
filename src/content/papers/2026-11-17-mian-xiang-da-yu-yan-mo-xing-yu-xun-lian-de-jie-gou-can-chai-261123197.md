---
title: Structure--Residual Inductive Biases for Language Model Pretraining
title_zh: 面向大语言模型预训练的结构-残差归纳偏置
authors:
- Hai Huang
- Bartosz Żuk
- Rassul Magauin
- Jiaxin Huang
- Xue Liu
affiliations:
- Palona AI
- Institute of Computer Science, Polish Academy of Sciences
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2611.23197'
url: https://arxiv.org/abs/2611.23197
pdf_url: https://arxiv.org/pdf/2611.23197
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: 大语言模型预训练 · 归纳偏置优化
tags:
- Inductive Bias
- LLM Pretraining
- Sparse Attention
- Regularization
- Transformer
one_liner: 提出BBC与CC两种互补结构-残差归纳偏置，无需改动主体架构即可提升LLM预训练效果
practical_value: '- 长序列用户行为建模可复用BBC思路：按会话/时间窗口拆分用户行为序列，跨窗口仅传递边界聚合状态，既降低长序列注意力计算开销，又保留窗口内细粒度行为信息

  - 生成式推荐/Agent的LLM微调可加入CC正则：在上层输出附近加相邻隐状态L2差约束，降低表示波动，提升生成文案、推荐序列的逻辑一致性

  - 可直接复用Transformer层适配经验：序列压缩/长上下文聚合类操作放底层效果最优，表示平滑/输出一致性正则放上层效果最好，减少全层调参成本

  - 长周期训练的正则优化可借鉴自适应dropout方案：当正则项数值过小时自动跳过更新，避免数值不稳定导致的效果波动'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM预训练普遍依赖纯next-token prediction目标，完全靠梯度自动学习内部表示结构，无显式表示约束，存在效率和效果的提升空间。受Kolmogorov复杂度两部分编码思想启发，将表示拆分为结构+残差两部分优化，可在不改动模型主体架构的前提下提升预训练效率。

### 方法关键点
- **Boundary Bottleneck Concept (BBC)**：将输入序列划分为K个token的分段，指定层的注意力仅允许已完成分段的边界token向后续分段传递信息，当前分段内保留完整自回归注意力，既压缩跨段通信量，又保留段内细粒度信息。
- **Continuous Concept (CC)**：在指定层的隐状态上加相邻隐状态的L2差正则，损失函数为$L = L_{NTP} + \beta L_{CC}$，鼓励隐状态轨迹平滑，将表示分解为低频结构分量和高频残差分量，降低表示冗余。
- 二者适配不同Transformer层：BBC放在底层，CC放在上层，通过超参数K和β调整结构与残差的平衡。

### 关键实验
在FineWeb-Edu数据集上预训练GPT-2 Small/Medium、Pythia-410M，对比纯next-token prediction基线、同密度稀疏注意力、其他正则方法：300M训练token时，BBC+CC在GPT-2 Medium上NLL降低1.44%，效果持续到20B训练token规模，在RoPE编码的Pythia-410M上也获得0.83%的NLL提升。BBC效果显著优于同密度滑动窗口/随机稀疏注意力，CC效果优于单独的尺度正则、余弦相似度正则。

### 核心结论
显式对LLM的内部表示结构加归纳偏置，是纯next-token prediction缩放之外，有效提升预训练效果的重要补充路径。
