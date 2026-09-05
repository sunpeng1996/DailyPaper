---
title: Investigating the Ability of Large Language Models to Analyze Recipes for Diabetes
title_zh: 大语言模型针对糖尿病适配食谱的分析能力研究
authors:
- Revathy Venkataramanan
- Aditya Luthra
- Venkatesan Nadimuthu
- Amit Sheth
affiliations:
- AI Institute, University of South Carolina
arxiv_id: '2609.03967'
url: https://arxiv.org/abs/2609.03967
pdf_url: https://arxiv.org/pdf/2609.03967
published: '2026-09-03'
collected: '2026-09-05'
category: Eval
direction: LLM 垂直领域能力评测
tags:
- LLM Evaluation
- Prompt Engineering
- Benchmark Dataset
- Reasoning
- Health Informatics
one_liner: 构建7607条糖尿病食谱适配基准数据集，对比三类prompt下不同LLM的食谱适用性判断性能
practical_value: '- 做控糖膳食、特殊人群食品等垂直领域推荐时，可采用三级递进prompt设计：直接提问→注入领域规则→规则+示例，逐层提升LLM判断准确率

  - 涉及健康风险的推荐场景可利用LLM保守预测特性，优先选型Mistral-7B这类支持显式规则推理的小模型，平衡成本与安全性

  - 垂直领域分类任务构建评测基准时，可参考1:1均衡正负样本配比，提升评测结果的可信度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM在通用膳食规划场景表现已得到验证，但针对糖尿病这类特殊人群的食谱适配性分析能力缺乏系统评测；核心难点为LLM需准确召回专业膳食指南、拆解食谱成分与烹饪方式、结合规则完成推理判断。

### 方法关键点
设计三类递进式prompt：① Direct Query Prompt ② 注入权威糖尿病膳食指南的Context-Guided Prompt ③ 指南加示例的Exemplary Context Prompt；构建包含7607条食谱的均衡基准数据集（3807条适配糖尿病、3800条不适配），评测多款LLM的任务表现。

### 关键结果
多数LLM倾向保守预测，避免错误放行不适配食谱；支持基于显式膳食指南推理的模型表现更优；Mistral-7B和Llama 70B的表现领先同类模型。
