---
title: 'Semantic Abstraction for Natural Language Inference: a Methodological Framework
  for Discovering and Compensating Semantic Knowledge and Reasoning Gaps in Large
  Language Models'
title_zh: 面向自然语言推理的LLM语义知识与推理缺口发现补全框架
authors:
- David Torres-Moreno
- Jorge Hermosillo-Valadez
affiliations:
- Universidad Autónoma del Estado de Morelos, México
arxiv_id: '2609.26610'
url: https://arxiv.org/abs/2609.26610
pdf_url: https://arxiv.org/pdf/2609.26610
published: '2026-09-22'
collected: '2026-09-23'
category: Reasoning
direction: LLM推理优化 · 语义知识补全
tags:
- LLM
- Natural Language Inference
- Semantic Abstraction
- Knowledge Gap
- Knowledge Graph
- Prompt Engineering
one_liner: 提出基于语义关系抽象的框架，补全LLM在NLI任务的知识与推理缺口，精度最高提升超10%
practical_value: '- 电商Query语义匹配、商品文案fact校验场景可复用语义兼容/不兼容抽象规则，将知识图谱关系按层级分类后注入prompt，降低LLM幻觉，提升匹配准确率

  - 多路径推理结果融合时优先选用轻量决策树学习不同prompt维度的权重，小参数LLM场景下比多数投票、加权投票效果更优，成本低收益明显

  - Agent的事实核查、用户意图理解场景可复用间接语义关系推理逻辑，通过知识图谱子图交集补全跨层级语义关联，减少LLM对表面语义的依赖'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在自然语言推理（NLI）任务中过度依赖表面语义线索，缺乏抽象推理能力，存在大量语义知识与推理缺口，传统直接注入外部知识的方法效果有限，无法解决推理路径僵化、非蕴含类判断准确率低的问题，多数投票类多prompt融合策略也难以充分利用不同维度的语义信号。
### 方法关键点
- 定义语义兼容性（向上泛化/等价）、语义不兼容性（向下具象/互斥）两类抽象语义关系，基于ConceptNet抽取前提和假设中的实体-属性对，按规则分到G1（兼容）、G2（互斥不兼容）、G3（具象不兼容）、G4（无关联）四个关系组
- 基于四个关系组分别构造prompt引导LLM生成四路独立推理结果，采用决策树而非多数投票作为融合策略，学习不同组信号的决策权重
- 支持通过知识图谱子图交集挖掘间接跨层级语义关系，扩展关系组覆盖范围，补全LLM缺失的关联知识
### 关键结果
在SNLI、SICK、SciTail、RTE等多个NLI基准数据集测试，对比原始prompt基线，小参数LLM（如Llama3.1）精度最高提升11.6个百分点，整体平均提升超10%，非蕴含类任务F1提升尤为显著；在SuperGLUE诊断集上，最高可修复17.4%的基线错误，仅引入3%-6%的额外错误。
### 核心结论
LLM弥补推理缺口需要的是结构化的抽象知识，而非单纯更多训练数据或更大的模型规模。
