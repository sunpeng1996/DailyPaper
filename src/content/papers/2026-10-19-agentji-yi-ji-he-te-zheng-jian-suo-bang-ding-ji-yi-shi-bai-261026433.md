---
title: 'The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures,
  and Characterizing Its Limits'
title_zh: Agent记忆几何特征：检索绑定记忆失败预测及能力边界刻画
authors:
- Iliya Zhechev
- Radoslav Ralev
- Chris Coleman
- Srijith Rajamohan
- Jen Agarwal
- Tyler Hutcherson
- Simba Khadder
affiliations:
- Redis
- Northwestern University
arxiv_id: '2610.26433'
url: https://arxiv.org/abs/2610.26433
pdf_url: https://arxiv.org/pdf/2610.26433
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: Agent记忆 · 检索失败预测
tags:
- Agent-Memory
- RAG
- Retrieval-Diagnosis
- Embedding
- QA-Correctness-Prediction
one_liner: 基于对话、记忆、查询的嵌入空间几何特征预测Agent回答正确率并刻画其性能边界
practical_value: '- 电商客服/导购Agent场景可对单会话咨询类query，用query到最近记忆的cosine距离做低门槛预筛，超过阈值触发扩大检索/转人工，无额外LLM调用成本

  - RAG系统选型对比时，必须加入问题难度、系统固有准确率作为控制变量，避免误将系统差异归因于新增诊断特征的效果

  - 记忆召回阶段可将query与记忆的cosine相似度TopK作为兜底策略，多数场景下表现优于随机召回，部分场景优于自定义原生召回逻辑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
带记忆的LLM Agent（尤其是RAG架构）的回答错误目前只能在生成后通过LLM Judge检测，成本高延迟大，若能在生成前通过已有嵌入特征预判错误，可实现提前干预（扩容检索、拒答等），大幅降低运行成本。

### 方法关键点
- 用同一个embedding模型将对话历史、已存储记忆文本、用户query映射到共享向量空间，提取25维几何特征：包括query可达性（最近记忆距离、Top5平均距离等）、记忆-对话匹配度、对话结构三类
- 训练逻辑回归分类器预测回答正确性，无需额外LLM调用，仅依赖预计算的嵌入特征

### 关键实验
- 数据集采用LongMemEval-small（2367个query-系统对，覆盖6类问题）、LoCoMo对话数据集
- 对比baseline包括问题难度baseline、系统身份baseline、仅用最近记忆距离的特征
- 核心结果：整体几何特征AUROC为0.640，低于问题难度baseline的0.655；控制系统身份和问题难度后，几何特征仅带来0.002的无统计显著性提升；单会话助手类问题上AUROC最高达0.841，但仅用系统身份特征就达到0.826；按cosine相似度选Top15记忆的回答准确率达0.790（gpt-4o），远高于随机选择的0.091。

### 核心结论
嵌入空间的几何相似度仅能反映检索相关性，无法验证事实覆盖度，也不能区分记忆构建、检索、生成三类错误，不足以作为线上可靠的错误诊断依据。
