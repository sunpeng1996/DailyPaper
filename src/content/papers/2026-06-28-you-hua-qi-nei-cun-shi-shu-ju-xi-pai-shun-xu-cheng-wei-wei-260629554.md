---
title: Optimizer Memory Makes Shuffle Order a First-Order Source of Fine-Tuning Noise
title_zh: 优化器内存使数据洗牌顺序成为微调噪声的一阶来源
authors:
- John Sweeney
affiliations:
- Sideplane.ai
arxiv_id: '2606.29554'
url: https://arxiv.org/abs/2606.29554
pdf_url: https://arxiv.org/pdf/2606.29554
published: '2026-06-28'
collected: '2026-06-30'
category: Training
direction: LLM微调 · 优化器路径依赖噪声量化
tags:
- Fine-Tuning
- AdamW
- Optimization
- Data Shuffle
- LoRA
- A-B Testing
one_liner: 揭示固定时钟优化器将数据顺序对微调的影响从二阶升为一阶，可直接翻转小差距A/B实验结果
practical_value: '- 做LLM SFT（如电商商品文案生成、推荐排序模型LoRA微调）时，若A/B两组效果差距小于1倍顺序噪声σ_ord，至少跑16次不同shuffle种子的重复实验才能保证80%统计功效，避免错误结论

  - 需降低微调波动时，可采用时钟匹配优化器配置：将动量衰减β与学习率η共缩放，可将顺序噪声从O(η)降回O(η²)量级，大幅提升结果稳定性

  - 多域多任务微调（如同时优化搜索query理解、商品排序、推荐召回任务）时，采用窗口式独立重洗牌策略，可让顺序噪声在多窗口间随机平均，避免累计漂移

  - 对外发布或上线微调策略效果时，必须固定shuffle种子，同时报告顺序噪声σ_ord值，标注实验结果的统计置信度，避免误判策略价值'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
过往无记忆优化器的分析认为，相同数据集的不同洗牌顺序对微调结果的影响是二阶（O(η²)）的，可忽略；但工业实践中频繁出现仅shuffle种子不同就导致小差距A/B实验结果翻转的问题，缺少量化的机制解释和噪声控制方案。

### 方法关键点
- 定义固定时钟优化器：AdamW、固定β动量SGD、Lion等优化器的动量缓冲、预条件器状态、去偏计数器随步长索引推进，而非随学习率缩放的连续时间τ=ηk推进，导致相同梯度的权重随位置变化
- 提出lifted-state时钟定理：证明固定时钟优化器下，相同多集数据的顺序差异对微调结果的影响为一阶（O(η)）量级，无记忆优化器（普通SGD）则保持二阶量级
- 推导顺序噪声方差闭式解，给出shuffle种子预算计算公式，可直接估算获得统计显著结论所需的重复实验次数
- 提出匹配时钟优化方案：将动量衰减β与学习率η共缩放，可将顺序噪声降回二阶量级

### 关键结果
- 在Pythia-1B、Llama-3.2-1B的LoRA SFT任务上验证：AdamW/Lion的顺序效应指数接近1，普通SGD/匹配时钟优化器接近2，与理论完全吻合
- 当两组配置的效果差距与顺序噪声σ_ord的比值<1时，单shuffle种子实验的结果符号翻转率高达33%~44%
- 固定状态重放实验显示：AdamW、固定β动量、SGD的顺序方差斜率分别为1.83、2.00、4.00

> 最值得记住的一句话：小差距微调A/B实验的结论不可信，除非你已经量化并控制了洗牌顺序带来的一阶噪声
