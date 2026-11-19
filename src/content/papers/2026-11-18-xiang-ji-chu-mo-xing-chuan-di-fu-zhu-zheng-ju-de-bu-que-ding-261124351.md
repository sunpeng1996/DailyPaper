---
title: 'Tell Me How Sure You Are: Communicating Uncertainty in Auxiliary Evidence
  to Foundation Models'
title_zh: 向基础模型传递辅助证据的不确定性以提升下游决策效果
authors:
- Soumyajit Chatterjee
- Baturalp Buyukates
- Abhirup Ghosh
affiliations:
- Brave
- University of Birmingham
arxiv_id: '2611.24351'
url: https://arxiv.org/abs/2611.24351
pdf_url: https://arxiv.org/pdf/2611.24351
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: 大模型推理 · 不确定性信息注入
tags:
- Uncertainty_Communication
- Zero_Shot_Learning
- LLM_Inference
- VLM
- Context_Prompting
one_liner: 首次系统验证向大模型传递辅助证据的原生不确定性可显著提升零样本分类效果
practical_value: '- RAG/工具调用Agent改造：将检索chunk的匹配置信度、工具返回结果的原生置信度直接附加到对应证据后输入LLM，无需额外校准跨源置信度尺度，即可提升下游决策准确率

  - 电商生成式推荐/搜索优化：可将召回侧的item语义匹配分、用户行为标签置信度作为上下文输入LLM排序层，无需微调模型即可获得可观测的排序效果提升

  - 下游决策可靠性预判：可利用上游辅助证据的不确定性信号直接预判大模型输出的正确性，无需额外训练大模型置信度探针，降低故障拦截成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型推理流程普遍丢弃辅助证据自带的可靠性信息，而RAG、工具调用、多模态Agent等实际场景的输入证据来源复杂（人类标注、多模态模型输出、任务专属分类器预测等），天然存在可靠性差异，忽略该信息会限制下游决策准确率；且此前研究未严格固定证据内容，无法单独量化不确定性传递的边际收益。
### 方法关键点
- 设计配对零样本评估框架，固定输入证据、大模型权重、主任务上下文，仅调整是否附加证据对应的不确定性信号，严格控制变量测量边际收益
- 覆盖三类不确定性来源：人类标注的序数置信度、通用多模态模型的图文匹配分数、任务专属分类器的max softmax置信度，不做跨源置信度校准，保留原生格式直接输入
- 同时评估不确定性对大模型证据权重分配、下游决策正确性预判的作用，验证收益的鲁棒性
### 关键实验
在CUB鸟类分类、SUN场景分类、Derm7pt皮肤病分类三个数据集上对比仅输入证据和输入证据+不确定性的效果，3款LLM的macro-F1最高分别提升7.84pp、26.18pp、9.10pp；2款VLM也获得最高2.07pp的提升；仅当不确定性与证据正确对应时生效，打乱匹配关系后收益完全消失。
### 核心结论
辅助证据的不确定性是高价值上下文信息，无需额外校准直接附在对应证据后输入大模型，即可零成本提升下游零样本任务效果。
