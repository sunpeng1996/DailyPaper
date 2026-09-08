---
title: 'ExplainRoute: A Pre-Deployment Audit Framework for Non-Answer-Giving Programming
  Tutors'
title_zh: ExplainRoute：面向非直接给答案编程导师的部署前审计框架
authors:
- Yiming Gai
- Yingying Zhang
- Xuefei Huang
arxiv_id: '2609.03470'
url: https://arxiv.org/abs/2609.03470
pdf_url: https://arxiv.org/pdf/2609.03470
published: '2026-09-03'
collected: '2026-09-08'
category: Agent
direction: Agent 部署前审计框架
tags:
- Auditable Agent
- Pre-Deployment Audit
- LLM Evaluation
- Tutoring Agent
- Response Routing
one_liner: 提出面向非给答案式编程导师的部署前审计框架，验证自适应路由无额外增益
practical_value: '- 做Agent部署前合规审计时，可复用「机器可检查合约」设计思路，明确暴露Agent状态、策略、调用片段、泄露风险四类核心信息，降低合规隐患

  - 验证智能路由类方案时，必须加入固定策略作为基线对照，不要默认自适应方案效果更优，避免不必要的系统复杂度提升

  - 对C端服务类Agent（如电商导购客服、学习助手），可参考其审计维度：信息边界、回复极性、故障闭环、用户输入可见性价值，提前规避答非所问、信息泄露问题'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有编程助教Agent多直接输出答案，部署前评估仅以流畅度为核心指标，缺乏对信息边界、回复合规性的审计，无法保障引导学习者自主思考的设计目标。
### 方法关键点
ExplainRoute审计框架逻辑：输入代码行+学习者解释，先预估解释状态，路由选择费曼式自我解释提示/苏格拉底式引导两类受限回复；内置机器可检查合约，公开状态、策略、引用代码片段、泄露风险四类核心信息；审计维度覆盖信息边界、回复极性、故障闭环、学习者解释可见性价值。
### 关键结果数字
1770对SelfCode语料测试，合约有效性100%；自适应路由与参考规则匹配度60.5%，状态macro-F1 0.238，无明显自适应优势；LLM评分自适应回复4.516/5，略低于固定开放提示（4.598/5）和固定苏格拉底引导（4.658/5），远优于无状态消融版（2.819/5）。
