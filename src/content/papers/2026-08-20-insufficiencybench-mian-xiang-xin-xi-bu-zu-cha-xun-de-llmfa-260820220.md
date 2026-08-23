---
title: 'InsufficiencyBench: Evaluating LLM legal advice on underspecified user queries'
title_zh: InsufficiencyBench：面向信息不足查询的LLM法律咨询能力评估基准
authors:
- Samuel J. Vincent
- Daniel Calloway
- Fangyi Yu
- Andrew M. Bean
- Nabeel Seedat
affiliations:
- Thomson Reuters Foundational Research
- Imperial College London
arxiv_id: '2608.20220'
url: https://arxiv.org/abs/2608.20220
pdf_url: https://arxiv.org/pdf/2608.20220
published: '2026-08-20'
collected: '2026-08-23'
category: Eval
direction: 大语言模型 · 垂直领域评估基准
tags:
- LLM Evaluation
- Legal LLM
- Query Understanding
- Benchmark
- Ambiguity Detection
one_liner: 首个针对查询信息不足场景的法律LLM评估基准，含律师标注的多域多司法管辖区测试集
practical_value: '- 垂直领域咨询类Agent可复用「查询信息缺失检测→引导用户补全关键要素→生成合规答案」的处理逻辑，避免基于默认假设输出错误结果，适配电商客服、合规咨询等场景

  - 构建垂直领域LLM评测集时可借鉴三类查询缺失故障模式的分类框架，分层标注缺陷类型，提升评测的场景覆盖度和实用价值

  - 高风险垂直领域LLM服务可参考F2分数作为缺失要素识别任务的核心指标，优先降低漏检风险，减少客诉与合规问题'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有法律LLM评估基准均默认用户查询信息完备，实际场景中用户常遗漏直接影响法律结论的关键事实，现有模型易基于隐含假设输出错误结论，缺乏对应能力的标准化评测体系。

### 方法关键点
形式化定义switch、gating、fatal prerequisite三类结构性故障模式下的8种标准缺失要素分类；构造202条执业律师标注的基准样本，包含58条基础查询、144条缺陷变体，覆盖6个法律领域、24个美国司法辖区；围绕「信息不足识别、缺失要素定位、规避过早结论」三个核心能力设计评测指标。

### 关键结果数字
10个前沿大模型的缺失要素识别F2最高仅0.46，召回率中位数为0.44，普遍存在无差别模糊回复或基于虚构假设作答的问题，无模型可同时实现缺陷查询识别提示、完备查询直接准确回复的要求。
