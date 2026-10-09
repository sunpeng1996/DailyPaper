---
title: Investigating the Role of Reasoning-Language Alignment in Monolingual Retrieval-Augmented
  Generation
title_zh: 单语检索增强生成场景下推理语言对齐的作用研究
authors:
- Oliver Hauck
- Mario Sanz-Guerrero
- Katharina von der Wense
affiliations:
- Johannes Gutenberg University Mainz
- University of Colorado Boulder
arxiv_id: '2610.03136'
url: https://arxiv.org/abs/2610.03136
pdf_url: https://arxiv.org/pdf/2610.03136
published: '2026-10-01'
collected: '2026-10-09'
category: RAG
direction: RAG 推理语言对齐优化
tags:
- RAG
- Reasoning Alignment
- Multilingual LLM
- Agentic RAG
- LLM Evaluation
one_liner: 验证单语非英语RAG中推理语言与语料对齐可提升效果，仍存在原生英语推理偏好
practical_value: '- 跨境电商/小语种站点的RAG客服、商品问答场景，强制推理语言与用户query、知识库语言对齐，可提升答案准确率，无需优先选择模型基准表现更好的高资源语言

  - Agentic RAG落地需防范推理语言泄露到工具调用：若推理语言与知识库语言不一致，可能生成错误语言的检索query，大幅降低召回质量

  - RAG的推理功能可按需动态开关：简单单跳问题（如商品参数查询）关闭推理可提升响应效率和答案准确率，复杂多跳问题（如跨品类搭配推荐）开启推理收益更高

  - 知识库chunking优先采用结构感知分段（如按商品详情页模块、帮助中心章节拆分），可进一步放大推理语言对齐的收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型推理训练多以英语为主，此前研究显示强制非英语推理会降低模型效果，但仅验证了短prompt场景，未覆盖RAG这类需要处理大量目标语言检索语料的真实落地场景，非英语RAG的推理语言选择缺乏实证依据。

### 方法关键点
- 构建德语单语RAG测试床：基于小众德语文桌游《黑暗之眼》的设定知识库，模型无相关预训练知识，必须依赖检索回答，排除记忆干扰
- 控制变量对比：推理语言维度测德语/英语/法语/无约束/关闭推理5种设置，知识库维度测固定大小chunk、结构感知章节分段2种策略
- 评估方案：585道单跳问题用LLM-as-a-Judge评分，30道多跳问题由领域专家人工评分

### 关键结果
- 强制德语推理得分3.701，显著高于强制法语的3.491，尽管模型法语基准表现优于德语，证明收益来自语言对齐而非语言熟练度
- 切换为结构感知chunk后，强制德语推理得分提升0.29，远高于无约束英语推理的0.08，对齐收益随上下文结构化程度提升而扩大
- 强制德语推理追平原生无约束英语推理得分（3.701 vs 3.718，无统计差异），但未超越，证明prompt层面的语言控制无法完全消除模型的英语训练偏好
- 简单单跳问题关闭推理得分最高（3.903），复杂多跳问题关闭推理得分最低，推理收益仅在任务复杂度超过阈值后显现

**最值得记住的一句话**：非英语单语RAG中，推理语言与语料对齐的收益高于模型本身的单语言熟练度收益，但无法抵消大模型原生训练的英语推理偏好。
