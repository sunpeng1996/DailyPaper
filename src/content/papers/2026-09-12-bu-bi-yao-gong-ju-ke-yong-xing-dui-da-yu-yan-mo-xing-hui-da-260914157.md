---
title: 'When Tools Get in the Way: The Effect of Unnecessary Tool Availability on
  LLM Answering'
title_zh: 不必要工具可用性对大语言模型回答能力的影响研究
authors:
- Saanvi Paturi
- Arsen Kenzhebayev
- Arham Sethi
- Vyas Raina
- Ivaxi Sheth
- Vatsal Raina
affiliations:
- UWCSEA East Campus
- Haileybury Astana
- The Shishukunj International School
- Apta AI
- Spark AI Research
arxiv_id: '2609.14157'
url: https://arxiv.org/abs/2609.14157
pdf_url: https://arxiv.org/pdf/2609.14157
published: '2026-09-12'
collected: '2026-09-15'
category: Agent
direction: Agent 工具调用行为优化
tags:
- LLM
- Tool Calling
- Agent
- Prompt Engineering
- Evaluation
one_liner: 发现接入无关工具会显著降低LLM本可回答问题的正确率，单句提示可恢复多数性能
practical_value: '- 部署电商导购/搜索Agent时不要盲目接入大量冗余工具，优先按需加载同域工具，避免LLM对通用商品常识、活动规则类问题出现不必要拒答

  - 可在系统提示中加入1句工具范围说明：「工具仅用于查询实时/专属数据，不限制你回答常识类问题」，实测可提升30-45pct无关工具场景下的回答正确率

  - 评估工具增强Agent时必须加无工具对照组，不能只测工具调用准确率，还要测同域非工具依赖问题的回答准确率，避免出现工具调用达标但用户体验下降的情况'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent普遍接入各类外部工具扩展能力，但现有研究只关注工具是否被正确调用，极少关注无关工具的存在本身会不会影响LLM回答本不需要工具的问题，而这类问题占用户日常query的大部分，一旦出现拒答会直接影响用户体验。

### 方法关键点
- 构建跨10个知识领域的500组query对，每组包含1个必须调用工具的查询、1个同域可直接用参数知识回答的闭域查询，确保变量仅为工具可用性
- 测试4种实验条件：工具可用的工具查询、工具不可用的闭域查询、工具可用的闭域查询、工具可用且有前置工具调用记录的闭域查询，对比不同条件下的回答正确率、工具调用率
- 评估6款主流LLM：Gemini 2.5系列、GPT-OSS 20B、Grok 4.1 Fast、Llama 3.3 70B

### 关键结果
无工具时所有模型闭域查询平均正确率98.2%，接入同域不必要工具后平均正确率骤降到63.5%；其中Gemini 2.5 Flash-Lite从99.4%跌到23.4%，但工具调用率仅7.8%，说明正确率下降不是因为乱调用工具，而是LLM误将工具范围当成回答边界。前置工具调用对效果影响分化：Llama 3.3 70B正确率从38%回升到65.2%，Gemini 2.5系列反而下降3pct左右。加入1句范围感知系统提示后，受影响最大的模型正确率可提升27.8-45.6pct，仅会轻微降低必要场景的工具调用率。

### 最值得记住的一句话
工具可用性是LLM上下文的一部分，而非单纯的能力扩展，接入工具时必须考虑其对非工具依赖query的负面影响。
