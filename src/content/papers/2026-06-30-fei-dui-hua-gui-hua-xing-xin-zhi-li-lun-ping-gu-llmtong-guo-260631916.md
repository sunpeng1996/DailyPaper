---
title: 'Theory of Mind and Persuasion Beyond Conversation: Assessing the Capacity
  of LLMs to Induce Belief States via Planning and Action'
title_zh: 非对话规划型心智理论评估：LLM通过行动诱导他者信念状态的能力测试
authors:
- Ben Slater
- Matteo G. Mecattaf
- Lucy G. Cheke
- John Burden
- Winnie Street
affiliations:
- University of Cambridge
- Leverhulme Centre for the Future of Intelligence
- Prolific
- Google Paradigms of Intelligence Team
arxiv_id: '2606.31916'
url: https://arxiv.org/abs/2606.31916
pdf_url: https://arxiv.org/pdf/2606.31916
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent心智理论 · 信念诱导规划评估
tags:
- Theory of Mind
- LLM Agent
- Agent Evaluation
- Social Reasoning
- Belief Induction
one_liner: 提出NCP-ExploreToM评估框架，测试6款前沿LLM及人类的非对话信念诱导规划能力
practical_value: '- 做智能导购/客服Agent时，可参考NCP-ToM思路，通过调整内容露出（而非直接话术劝说）引导用户形成对商品的正向认知，比如优先露出真实好评、物流时效数据降低用户决策顾虑

  - Agent能力评估可借鉴本文item级Q&A/agentic任务对比方法，不要仅靠静态Q&A衡量推理能力，要结合动态行动场景验证落地表现，避免评估和实际效果脱节

  - 做多Agent协作/博弈场景（如流量竞价、商家运营助手）时，可参考本文信念状态建模方法，判断对端Agent/用户的信念阈值，优先用真实信息引导信念，降低欺骗性操作的合规风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM的Theory of Mind（ToM，心智理论）评估多为被动问答格式，但Agent化部署的LLM普遍需要通过非对话行动主动诱导他者信念的能力，该能力既可以用于辅助用户决策、信息保密等正向场景，也存在误导、操纵的安全风险，当前缺乏对应的评估体系。

### 方法关键点
- 基于ExploreToM框架改造提出NCP-ExploreToM评估范式，将被动问答改为主动规划任务：给Agent指定信念目标，要求其通过移动角色/物品、调整对象属性等6类操作完成目标，无需对话
- 覆盖1/2阶意向性信念目标，包括真实信念、虚假信念及二者的嵌套组合，目标复杂度分为1/2/3个基础目标组合，设置政府大楼、医院等5类不同场景验证上下文敏感性
- 同时设计同结构的Q&A版本任务，item级对比静态推理和动态规划的能力差异，加入人类测试数据作为基线

### 关键实验结果
测试6款前沿LLM（GPT-5、Gemini 2.5 Pro、Claude 3/3.5/4系列）和40名人类参与者，共600个任务实例：
- GPT-5在agentic任务中通过率约80%，是唯一超过人类表现的模型，但上下文波动方差是人类的3倍以上，鲁棒性更差
- 所有模型和人类的真实信念任务表现均显著优于虚假信念任务，虚假信念任务下agentic版难度是Q&A版的7-8倍，仅GPT-5在两类任务上表现无显著差异
- 中性能梯队模型（Claude Sonnet 4.5、Gemini 2.5 Pro等）的Q&A表现可预测agentic表现，高低性能梯队该相关性失效

### 核心结论
静态Q&A评估不一定能代表LLM在动态Agent场景下的真实能力，尤其是前沿模型的agentic任务表现可能反超静态问答表现。
