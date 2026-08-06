---
title: 'ExplainBench: Evaluating Code Explanations from Agents'
title_zh: ExplainBench：面向代码Agent生成解释的自动评测基准
authors:
- Zhiyuan Pan
- Sungmin Kang
- Imam Nur Bani Yusuf
- Abhik Roychoudhury
affiliations:
- Zhejiang University
- National University of Singapore
arxiv_id: '2607.26451'
url: https://arxiv.org/abs/2607.26451
pdf_url: https://arxiv.org/pdf/2607.26451
published: '2026-07-28'
collected: '2026-08-06'
category: Agent
direction: Agent 可解释性与评测
tags:
- LLM Agent
- Code Agent
- Explainability
- Benchmark
- Evaluation
- Agent Audit
one_liner: 首个自动评测代码Agent补丁解释可信度的基准，配套通用审计Agent提升解释质量
practical_value: '- 可复用「基于问答验证解释质量」的评估思路：对电商场景下Agent生成的推荐理由、投放文案、搜索query改写解释，可构造带标准答案的MCQ，用LLM作答准确率量化解释可信度，无需大规模人工标注

  - 可借鉴「解释审计Agent」架构：对业务中生成式模型输出的内容（如商品详情、活动规则解释），配套独立校验Agent，通过工具调用（规则校验、模拟用户问答）验证内容准确性，修正错误表述，降低客诉

  - 需注意Agent任务效果和解释可信度是独立维度：不能只看推荐/广告的点击转化效果，也要单独评估模型给出的解释（如个性化推荐理由）的准确性，避免误导用户损害平台信任'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM代码Agent已在软件工程领域广泛落地，但生成的补丁解释经常与实际效果不符（如宣称修复bug实际无效），人工审核大规模Agent输出成本极高；现有Agent基准仅评估任务完成效果，缺乏针对解释可信度的自动评测方案，无法支撑Agent的可信落地。

### 方法关键点
- 核心评测逻辑：高质量解释应支持LLM基于解释准确回答关于问题意图、补丁效果的问题，以答题准确率作为解释质量量化得分
- 设计4类多选择评测维度：端到端意图（是否讲清bug预期行为）、端到端效果（是否讲清补丁实际执行结果）、局部意图（是否讲清故障函数预期逻辑）、局部效果（是否讲清补丁对函数的实际改动）
- 配套ExplanationAuditAgent：通过差分测试、调用链分析等工具校验原解释，自动修正错误表述、补充验证证据，可适配任意代码Agent

### 关键结果
基于SWE-bench Verified构建297个真实代码bug的评测集，测试5个主流代码Agent：
1. Agent任务效果排名与解释质量排名完全无关，效果第一的trae-agent解释质量仅排第四
2. 现有Agent对错误补丁的平均过自信率达79.3%，普遍宣称无效补丁修复了问题
3. 审计Agent可提升所有被测Agent的解释得分，单条解释优化平均成本仅0.05美元

### 核心结论
Agent的任务效果和其输出解释的可信度是完全独立的评估维度，仅优化任务效果无法保障用户对Agent输出的信任
