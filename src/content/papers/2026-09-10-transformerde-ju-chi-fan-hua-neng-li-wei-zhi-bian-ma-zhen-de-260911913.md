---
title: 'Distance generalization in transformers: why bother with positional encoding?'
title_zh: Transformer的距离泛化能力：位置编码真的必要吗？
authors:
- Daniel Henrik Nevermann
- Claudius Gros
affiliations:
- Goethe University Frankfurt
arxiv_id: '2609.11913'
url: https://arxiv.org/abs/2609.11913
pdf_url: https://arxiv.org/pdf/2609.11913
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: 大模型泛化 · 位置编码优化
tags:
- Transformer
- Positional Encoding
- Generalization
- RoPE
- ALiBi
one_liner: 验证无位置编码Transformer的距离泛化能力优于RoPE、ALiBi，分析数据多样性与迁移学习的影响
practical_value: '- 中大型模型做生成式推荐/Agent长上下文任务时，可尝试关闭显式位置编码（NoPE）提升跨距离依赖泛化能力，适配用户长间隔历史行为召回等场景

  - 训练多任务推荐/搜索模型时，若需保证单任务训练域内精度，可优先选择RoPE编码，其任务间负向干扰程度最低

  - 面向OOD场景的模型训练无需盲目扩大训练距离分布范围，数据多样性对泛化的提升存在边际递减效应，可合理控制训练成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Transformer泛化研究多聚焦长度泛化（上下文长度从短到长的 extrapolation），忽略固定上下文窗口内的**距离泛化**：即训练与推理时token间依赖距离变化下的性能表现。后者直接决定长上下文任务中OOD依赖的召回精度，且和位置编码的实际作用关联不明，是大模型落地长序列场景的核心盲区。

### 方法关键点
- 设计两类合成延迟复制任务：全量复制C、选择性复制S，固定上下文长度256，仅改变源token与召回位置的距离，完全隔离长度泛化的干扰
- 对比三类主流位置编码方案：RoPE、ALiBi、无显式位置编码（NoPE），统一使用8层8头、隐层512的Decoder-only Transformer结构
- 量化两个核心影响因子：训练数据覆盖的距离区间大小（数据多样性）、跨任务迁移学习对距离泛化的作用

### 关键实验结果
- 训练集覆盖距离15~25时，NoPE在OOD距离区间的准确率比RoPE高35%以上，比ALiBi高20%以上，仅小模型（隐层<256）需依赖显式位置编码稳定训练
- 训练距离区间从5扩大到50时，相对泛化率P（OOD精度/域内精度）下降40%，存在明显边际递减效应
- RoPE的跨任务迁移负向干扰最小，NoPE/ALiBi存在中等程度的双向正负迁移效应

### 核心结论
中大型模型的因果注意力本身可编码相对位置，显式位置编码反而会限制距离泛化能力，仅小模型需要依赖显式位置编码稳定训练
