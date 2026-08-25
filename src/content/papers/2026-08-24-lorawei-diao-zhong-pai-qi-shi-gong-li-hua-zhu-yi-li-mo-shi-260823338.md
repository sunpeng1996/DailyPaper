---
title: The Emergence of Relevance Through Axiomatic Attention Patterns During LoRA
  Fine-Tuning
title_zh: LoRA微调重排器时公理化注意力模式的相关性涌现机制
authors:
- Matthew Perlman
- Atharva Nijasure
- James Allan
affiliations:
- University of Massachusetts Amherst
arxiv_id: '2608.23338'
url: https://arxiv.org/abs/2608.23338
pdf_url: https://arxiv.org/pdf/2608.23338
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: LLM重排 · LoRA微调可解释性
tags:
- LoRA
- Reranking
- Interpretability
- Attention
- RankLLaMA
- IR
one_liner: 定位RankLLaMA LoRA微调提升重排性能的关键层，证明其与公理化IR注意力模式高度相关
practical_value: '- 做LLM重排LoRA微调时，7B规模decoder-only模型可优先仅给中间10-18层左右的注意力加LoRA，全层保留MLP
  LoRA，可节省超50%的LoRA参数，同时拿到全层注意力LoRA一半以上的性能增益，降本提速

  - 计算重排模型的注意力特征占比时，去掉首位sink token的注意力权重做归一化，可更准确地衡量模型真实的相关性注意力模式，避免sink干扰

  - 可将公理化IR特征（稀有词匹配、query-doc跨段交互等）加入重排模型的效果验证指标，甚至作为辅助监督信号，提升重排的可解释性与泛化性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LoRA是LLM适配重排任务的标配方案，但此前相关性能力在网络中的习得位置不明确，注意力层面的变化是否符合经典IR公理化规律也未知，LoRA微调策略的优化缺乏可解释性指导。
### 方法关键点
- 基于RankLLaMA-7B开展实验，固定全层MLP均添加LoRA，仅对注意力层做定向消融，设计keep（仅指定组件加LoRA）、omit（仅指定组件不加LoRA）两种策略，覆盖头、单一层、连续窗口三个粒度
- 提出Normalized Feature Attention指标，剔除首位sink token的注意力后统计公理化IR特征（词汇匹配、稀有词敏感度、query-doc跨段交互）的注意力占比，对比微调前后的差异
### 关键结果
- 实验基于MS MARCO passage重排任务，base模型NDCG为0.199，全层LoRA微调后NDCG达0.911
- 仅给10-18层注意力加LoRA即可恢复全层注意力LoRA 50%以上的性能增益，省略该区域的LoRA微调带来的性能下降远高于其他区域
- 稀有词敏感度、query-doc交互的注意力变化与性能增益的Spearman相关系数分别达0.92、0.71，多特征组合的相关性更高
### 核心结论
7B规模decoder-only重排器LoRA微调时，相关性能力的习得高度集中在中间层注意力模块，且与经典IR公理化特征高度对齐，无需对全层注意力加LoRA即可获得大部分性能增益
