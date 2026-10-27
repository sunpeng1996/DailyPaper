---
title: Quantifying Claim Smoothing by LLM Research Agents
title_zh: 量化LLM研究智能体生成报告的主张平滑现象
authors:
- Tiasa Singha Roy
- Manya Wadhwa
- Greg Durrett
affiliations:
- New York University
arxiv_id: '2610.35793'
url: https://arxiv.org/abs/2610.35793
pdf_url: https://arxiv.org/pdf/2610.35793
published: '2026-10-26'
collected: '2026-10-27'
category: Eval
direction: Agent 事实性评估 · 平滑检测
tags:
- Agent Evaluation
- Factuality
- Hallucination Detection
- RAG
- Claim Verification
one_liner: 提出SMOOTHSCORE框架量化LLM研究Agent的结论过度平滑问题，与人类标注一致性达93%
practical_value: '- 电商导购Agent、商品评测内容生成场景，可复用双Agent（支持+质疑）证据提取逻辑，输出结论前先拉取正反证据，避免过度绝对表述，降低客诉

  - 搭建RAG系统事实性校验模块时，可复用aspect聚合计分法，仅用原文档1/10的token量就能达到和全量审核相当的效果，大幅降低推理成本

  - 优化Agent输出校准效果时，优先采用「完整检索文档+校准指令」联合方案，比单独加prompt或单独给文档的效果提升2倍以上

  - 生成商品对比、选购指南类内容时，按aspect维度聚合正反证据，避免把特定场景下的优势夸大为全场景通用的平滑问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM研究Agent生成的报告流畅且附带引用，容易获得用户信任，但普遍存在「平滑」问题：将存在冲突、有明确适用条件的证据整合为过于绝对的统一结论，现有事实性检测方法仅做二分类的支持/反对判断，无法衡量结论与证据整体的校准度偏差。

### 方法关键点
- 定义「平滑」：结论存在部分支持证据，但整体表述的强度、适用范围远超证据可支撑的程度
- SMOOTHSCORE pipeline分为5步：提取报告核心结论主张；通过支持Agent、质疑Agent分别提取对应证据；归纳证据关联的aspect维度；将正反证据匹配到对应aspect下；基于聚合证据给主张打1-5分，分数越高平滑越严重

### 关键结果
在4个研究Agent基准数据集、7个主流系统（含GPT Luna/Sol、Claude、Gemini、开源DR Tulu/QUEST）上测试：
- 平滑现象普遍存在：所有系统至少22%的主张存在实质性平滑（score≥3），Gemini的严重平滑（score≥4）占比达22%-35%，是其他闭源系统的3-12倍
- 联合干预效果最优：同时给Agent提供完整引用文档+校准指令，可将Luna的实质性平滑占比从29%降至12%，Sonnet 5的从61%降至25%，严重平滑几乎消失

### 核心结论
RAG/Agent的事实性校验仅验证「是否有证据支持」远远不够，必须校验结论的强度和范围是否与所有证据的分布匹配，否则即使每个主张都带引用，依然可能存在严重误导。
