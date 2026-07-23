---
title: Statistical Inference for Rank Allocation in Low-Rank Adaptation
title_zh: 基于统计推断的低秩适配（LoRA）秩分配方法
authors:
- Yihang Gao
- Vincent Y. F. Tan
affiliations:
- National University of Singapore
arxiv_id: '2607.20205'
url: https://arxiv.org/abs/2607.20205
pdf_url: https://arxiv.org/pdf/2607.20205
published: '2026-07-22'
collected: '2026-07-23'
category: Training
direction: 参数高效微调 · LoRA秩动态优化
tags:
- LoRA
- Parameter Efficient Fine-Tuning
- Statistical Inference
- Hypothesis Testing
- AdamW
one_liner: 将LoRA秩分配转化为统计假设检验问题，同等参数预算下性能优于主流自适应秩LoRA方法
practical_value: '- 业务侧做LLM/多模态模型LoRA微调适配场景时，可直接复用StatLoRA的p值排序剪枝策略，在固定参数预算下提升微调效果，无需手动调整各层秩超参数

  - 优化器轨迹的统计推断思路可迁移到推荐系统低秩双塔模型的秩动态分配、用户冷启动embedding冗余维度剪枝等场景，提升参数效率

  - 训练中基于batch-means估计指标方差的trick可直接复用，无需计算高维协方差矩阵，额外计算开销极低，适配大规模工业训练流程

  - Agent微调场景可针对工具调用、思考链等特定能力对应的LoRA模块，用统计显著性筛选有效组件，优先分配秩资源，减少无效参数开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LoRA是当前LLM参数高效微调的主流方案，但现有自适应秩分配方法多基于梯度敏感度等启发式规则，无明确统计解释，无法区分真实适配信号和训练噪声，易导致秩资源分配不合理，在固定参数预算下难以平衡效果和效率。

### 方法关键点
1. 将LoRA秩分配转化为逐秩1组件的统计假设检验问题，零假设为对应组件贡献足够大需保留，通过p值判断是否剪枝
2. 证明AdamW、Adam、Adafactor等常用深度学习优化器的迭代轨迹满足渐近正态性，通过delta方法推导得到LoRA组件经验得分的极限分布
3. 采用batch-means方法直接从得分轨迹估计长期方差，无需计算高维协方差矩阵，额外计算开销极小，无需修改原有LoRA训练流程
4. 自适应设置检验阈值为当前活跃组件得分的q分位数，根据预设预算逐步剪枝p值最小的组件

### 关键实验
在DeBERTaV3-base、BART-Large、Qwen2.5-7B三类模型，自然语言理解、生成、问答三类任务上测试，同等秩预算下StatLoRA效果优于vanilla LoRA、AdaLoRA、IGU-LoRA，部分任务上相对基线提升1.2~2.1个百分点。

**最值得记住的结论**：LoRA秩分配不需要依赖人工设计的启发式重要性得分，基于统计推断的剪枝策略既能提升参数效率，又有严格的理论保证。
