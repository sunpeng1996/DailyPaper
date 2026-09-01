---
title: 'You Know What I Mean: A Benchmark for Agentic Conversational Reference Grounding'
title_zh: REPOREF：面向工具调用型智能体的对话式指代落地基准
authors:
- Karen Fuchs
- Uri Katz
- Yoav Goldberg
affiliations:
- Bar-Ilan University
- Allen Institute for AI
arxiv_id: '2608.29834'
url: https://arxiv.org/abs/2608.29834
pdf_url: https://arxiv.org/pdf/2608.29834
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent工具调用 · 指代消解基准
tags:
- Agent Benchmark
- Reference Grounding
- Tool Use
- Conversational AI
- LLM Agent
one_liner: 构建400个开发者对话样本的REPOREF基准，测试工具调用Agent的隐式指代落地能力
practical_value: '- 做电商导购/客服Agent时可复用该任务思路：将用户对话中「上次加购的红卫衣」「昨天聊的活动」这类隐式指代，通过调用商品/订单/活动搜索工具落地到具体item，降低答非所问率

  - 低 lexical overlap 检索场景可参考多步探索策略：先从对话上下文提取类型、时间、关联用户等元数据粗筛候选，再逐个校验细节，比单次语义检索准确率更高

  - 构建业务测试集可复用REPOREF构造pipeline：先抓取真实对话中带明确ID/链接的指代，再将显式指代改写为自然隐式表达，过滤歧义case后低成本生成高质量测试集'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
协作场景（办公、客服、开发等）的对话中大量存在隐式指代，如「昨天讨论的修复方案」「上周聊的那款商品」，需结合对话上下文+调用外部工具才能定位到具体资源，但现有检索任务多为单轮明确query场景，缺乏标准化基准衡量Agent解决这类问题的能力。

### 方法关键点
- 定义CoRG（Conversational Reference Grounding）任务：给定多轮对话和带隐式指代的锚点消息，要求Agent仅通过工具调用定位外部系统中唯一对应的目标资源
- 构建REPOREF基准：从真实开发者Gitter对话抽取带GitHub显式链接的样本，将显式链接改写为自然隐式指代，过滤歧义后得到400个高质量样本，覆盖92个仓库、7781条消息，配套22个GitHub只读搜索工具
- 评估维度：除准确率外，还统计工具调用次数、token消耗、多余工具调用量等效率指标

### 关键实验结果
固定10次工具调用预算下，最优的Gemini-3-Flash准确率仅67.0%，Claude Code Opus 4.7准确率63.25%但工具调用效率更高；当工具预算提升到16次时，Gemini-3-Flash准确率提升到73.93%；70%-92%的失败是因为Agent从未召回过正确目标，而非召回后选错。

> 最值得记住的结论：隐式指代落地场景中，大部分失败并非来自候选排序决策，而是来自召回阶段的探索不足，适度的多步搜索对准确率提升远好于单次高效检索
