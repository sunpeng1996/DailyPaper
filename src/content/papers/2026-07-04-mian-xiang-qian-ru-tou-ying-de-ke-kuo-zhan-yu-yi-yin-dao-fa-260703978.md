---
title: Scalable Semantic Steering of Embedding Projections
title_zh: 面向嵌入投影的可扩展语义引导方法
authors:
- Wei Liu
- Eric Krokos
- Kirsten Whitley
- Rebecca Faust
- Chris North
affiliations:
- Virginia Tech
- Department of Defense
- Tulane University
arxiv_id: '2607.03978'
url: https://arxiv.org/abs/2607.03978
pdf_url: https://arxiv.org/pdf/2607.03978
published: '2026-07-04'
collected: '2026-07-08'
category: LLM
direction: LLM嵌入语义调控 · 混合原型设计
tags:
- Semantic Steering
- Hybrid Prototype
- Embedding Alignment
- LLM Efficiency
- Multimodal Embedding
one_liner: 将LLM语义引导从逐item推理改为单调用生成组级混合原型，降本超1000倍且全局对齐效果持平
practical_value: '- 做召回/粗排的自定义意图对齐时，可复用混合原型设计：将少量标注样本embedding质心与LLM生成的类语义描述embedding加权融合，替代逐样本LLM推理，大幅降低调用成本

  - 多模态商品分类/打标场景，可直接复用自适应阈值软分配+对齐缩放更新机制，无需微调即可快速适配业务自定义分类体系

  - 语义召回bad case修复场景，可基于少量正负例组生成混合原型，对query/item embedding做批量校准，替代逐样本标注调优'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM增强的嵌入投影语义引导方法需逐样本调用LLM推理，成本随数据集规模线性增长，无法支撑大规模语料/商品库的交互式语义调控需求；而用户通常在组级表达语义意图，无需逐样本重复推理。
### 方法关键点
- 仅发起1次LLM调用，生成所有用户自定义组的结构化语义档案（含名称、描述、准入/排除规则），编码为组级profile embedding
- 构建混合语义原型：将组内种子样本的embedding质心与profile embedding做凸组合，兼顾原始嵌入的局部几何特征与自然语言语义的泛化性
- 自适应组级阈值软分配：基于组内/组外种子与原型的平均相似度设置阈值，相似度低于阈值的样本保持原embedding不变，避免误调整
- 对齐缩放更新：样本与原型的相似度越高，embedding向原型偏移的幅度越大，更新后再重投影得到语义对齐的低维表示
### 关键实验
在5K篇规模的LitCovid文本数据集上，对比逐item LLM引导基线，混合原型方案全局对齐效果（ΔSil=0.302）优于基线的0.259，LLM调用量从5001次降至1次，成本降低1294倍；在2.5K张Stanford-40动作图像数据集上也实现ΔSil=0.20的对齐效果，原生支持多模态场景。
### 核心结论
将语义计算粒度匹配用户交互的组级单元，而非逐样本推理，是大幅降低LLM应用成本同时保障效果的核心思路。
