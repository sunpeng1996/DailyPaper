---
title: 'Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM
  Discussions'
title_zh: LLM多智能体讨论中的隐性信念崩溃测量：信而不言的虚假传播
authors:
- Liangjie Huang
- Henry Peng Zou
- Wei-Chieh Huang
- Wooseong Yang
- Yuwei Han
- Philip S. Yu
affiliations:
- University of Illinois Chicago
arxiv_id: '2610.22138'
url: https://arxiv.org/abs/2610.22138
pdf_url: https://arxiv.org/pdf/2610.22138
published: '2026-10-15'
collected: '2026-10-17'
category: MultiAgent
direction: 多智能体协作 · 对抗鲁棒性评估
tags:
- MultiAgent
- Adversarial Robustness
- Belief Tracking
- LLM Safety
- Misinformation Propagation
one_liner: 提出公私双轨测量方法，证实少量对抗Agent可导致多智能体群体多数隐性感染虚假信息
practical_value: '- 搭建多Agent协作系统（如智能导购群、内容审核多Agent流水线）时，不能仅依赖公开对话日志做健康度检测，需增加独立私域探针定期抽查各Agent的真实输出，避免隐性错误扩散

  - 做Agent选型时，除基准准确率外需增加「抗同伴误导压力测试」：少量植入固定错误主张的对抗Agent，检测目标Agent的信念保持率，基准知识掌握度不代表抗干扰能力

  - 电商场景下的多Agent内容生成/选品投票系统，需在前3-4轮对话做错误检测，80%的隐性感染在讨论前4轮就已发生，后期干预基本无效

  - 若允许外部Agent接入多Agent工作流，必须对外部输入做严格事实校验，仅1个恶意Agent就能使44.8%的良性Agent私下接受错误信息，群体冗余防护效果极差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多Agent系统普遍假设群体讨论可交叉校验错误、提升输出可靠性，但忽略了对话通道本身就是攻击面，少量恶意Agent仅通过发言就能注入虚假信息，且现有仅检测公开对话的评估方式无法发现未公开表达的隐性信念变化，导致风险被严重低估。

### 方法关键点
- 设计10人Agent讨论组，设置0/1/3个固定鼓吹合理虚假答案的对抗Agent，就事实类QA问题讨论16轮，所有Agent共享同一基座模型
- 搭建公私双轨测量机制：每轮结束后通过独立私域探针（对其他Agent不可见）查询每个良性Agent的真实答案，同时标注其公开发言对虚假主张的态度（支持/反对/模糊/忽略）
- 覆盖6款主流LLM、3个事实QA数据集（COUNTERFACT、POPQA、SIMPLEQA），所有数据先经过筛选，确保基准情况下模型输出虚假答案的概率≤5%

### 关键结果
- 无对抗Agent时，良性Agent最终隐性感染率仅0.6%；加入1个对抗Agent时感染率升至44.8%，3个时升至60.5%
- 3个对抗Agent场景下，51.6%的讨论轮次中良性Agent私下已接受虚假答案，但仅19.7%的轮次会公开支持，7成以上感染完全隐藏在对话日志之外
- 模型基准事实准确率与抗干扰能力无相关性：两款基准准确率同为85%的模型，被感染率分别为25%和80%

**最值得记住的一句话：多Agent系统的公开对话健康度是假象，仅靠增加Agent数量无法提升鲁棒性，隐性信念感染的传播速度远快于公开表现**
