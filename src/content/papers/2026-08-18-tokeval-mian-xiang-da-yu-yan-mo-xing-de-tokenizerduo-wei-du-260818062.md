---
title: 'TokEval: A Tokenizer Evaluation Suite'
title_zh: TokEval：面向大语言模型的Tokenizer多维度评估套件
authors:
- Clara Meister
affiliations:
- EPFL
arxiv_id: '2608.18062'
url: https://arxiv.org/abs/2608.18062
pdf_url: https://arxiv.org/pdf/2608.18062
published: '2026-08-18'
collected: '2026-08-19'
category: Eval
direction: LLM Tokenizer 评估工具
tags:
- Tokenizer
- LLM Training
- Intrinsic Evaluation
- Downstream Performance
- Multilingual LLM
one_liner: 开源覆盖文本/数学/代码/多语言公平性的Tokenizer评估套件，量化内在指标与下游性能的关联
practical_value: '- 自研垂直领域LLM（电商客服、商品文案生成、Agent推理模型）时，可直接用TokEval筛选Tokenizer，无需先做全量预训练，大幅节省算力试错成本

  - 优化多语言/跨境电商场景LLM效果时，优先参考Tokenizer Fairness Gini、per-language fertility等公平性指标，降低小语种token税，提升小语种用户体验

  - 开发数学推理/代码生成类Agent（电商定价测算、活动规则校验、商家后台自动化工具）时，可针对性优化digit boundary F1、AST alignment等结构敏感指标，直接提升对应任务准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM开发流程中Tokenizer选型仅依赖压缩率、词表大小等少量启发式指标，缺乏系统的内在评估体系，且不同Tokenizer特性对下游性能的影响关系不明确，测试新Tokenizer需要全量预训练，成本极高。

### 方法关键点
- 开源TokEval库，覆盖压缩与信息论、语言对齐、多语言公平性、编码保真、数字处理、代码处理六大类共20+内在评估指标，支持HuggingFace、SentencePiece等主流Tokenizer后端，自带16项sanity check与可视化模块
- 控制变量训练46种不同配置的Tokenizer，固定1.27B参数decoder-only LLM的其他训练变量，仅替换Tokenizer做下游效果对齐，验证内在指标与下游性能的相关性
- 采用混合效应回归控制不同语言的基线效果差异，避免聚合相关性掩盖单语言内的真实关联

### 关键结果数字
- 信息论指标（如Rényi效率）与语言建模效果（FLORES BPB）的Spearman |ρ|最高达0.80，可直接用于预训练前的Tokenizer初筛
- 结构敏感指标：digit boundary F1与Code BPB的ρ达-0.62，AST alignment与MBPP pass@1的ρ达0.61，是对应领域任务效果的核心预测因子
- 6/8的开源Tokenizer下游效果预测落在90%置信区间内，可淘汰明显不合格的Tokenizer配置，减少70%以上预训练试错成本

### 核心结论
信息论指标适合快速筛除低质Tokenizer，特定任务性能提升必须优化对应结构敏感指标，不要只用压缩率作为Tokenizer选型的唯一标准
