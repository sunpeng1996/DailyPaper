---
title: Evaluating safeguarding in multi-turn conversations with AI assistants
title_zh: 多轮对话场景下AI助手安全防护能力评估
authors:
- Charlotte Peart
- Franziska Sofia Hafner
- Luc Rocher
affiliations:
- Oxford Internet Institute, University of Oxford
arxiv_id: '2611.26009'
url: https://arxiv.org/abs/2611.26009
pdf_url: https://arxiv.org/pdf/2611.26009
published: '2026-11-19'
collected: '2026-11-20'
category: Eval
direction: 大模型安全评估 · 多轮对话场景
tags:
- Safety Evaluation
- Multi-turn Conversation
- LLM Safeguard
- Conversational AI
- Mental Health Support
one_liner: 对比单轮集中/多轮分散给出风险线索时主流大模型的安全防护表现，指出现有单轮安全评估的局限性
practical_value: '- 对话式电商Agent、智能客服的风险校验环节，需新增多轮历史上下文风险线索聚合模块，避免漏判用户分散表达的风险或诉求

  - 大模型落地前的安全评估，可新增多轮渐进式风险注入的测试用例，比传统单轮测试更贴合真实交互习惯，降低线上风险漏出率

  - 面向长期用户状态跟进的个性化推荐场景（如心理健康内容、生活服务推荐），可复用「分散线索聚合+金标准对齐」的评估框架，提升推荐合规性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有大模型安全评估多采用单轮显式风险输入模式，未覆盖用户真实交互中逐步、分散透露风险线索的场景，导致安全防护效果被高估。

### 方法关键点
联合3名社区心理健康支持工作者，设计9类涉及抑郁、精神疾病、家暴的风险场景，将5个风险线索分别以「单轮集中输出」「多轮分散穿插在21轮日常对话中」两种形式输入，以专业人员制定的响应金标准（从指引支持到暂停任务处理风险）为评估依据，测试6款主流大模型的表现，总对话量超7400轮。

### 关键结果
- GPT-5.5、Grok 4.3、DeepSeek V4、Llama 4 Maverick：集中线索场景达标率26%~59%，分散线索场景仅3%~6%
- Claude Sonnet 5、Opus 5：集中场景达标率68%~97%，分散场景59%~87%，最优的Claude Opus 5在分散场景仍有13%不达标率
