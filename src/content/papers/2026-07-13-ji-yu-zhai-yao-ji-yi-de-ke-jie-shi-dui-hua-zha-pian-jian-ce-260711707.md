---
title: An Explainable Agentic System for Detection of Conversational Scams with Summary-Based
  Memory
title_zh: 基于摘要记忆的可解释对话诈骗检测智能体系统
authors:
- Ahmed Omar Salim Adnan
- Yogananda Manjunath
- Shivanjali Khare
affiliations:
- University of New Haven
arxiv_id: '2607.11707'
url: https://arxiv.org/abs/2607.11707
pdf_url: https://arxiv.org/pdf/2607.11707
published: '2026-07-13'
collected: '2026-07-15'
category: Agent
direction: Agent多智体 · 多轮对话风险检测
tags:
- Multi-Agent
- Summary-based Memory
- Conversational Fraud Detection
- Open Benchmark
- Privacy-preserving
one_liner: 提出模块化可解释多Agent对话诈骗检测系统，开源多类别对话诈骗基准ConScamBench-278
practical_value: '- 多Agent分工+自适应调度架构可直接复用在电商客服风险检测、黑灰产广告识别等场景，拆分轻量触发、信息提取、校验、决策模块，相比端到端LLM调用降低30%以上无效计算，同时具备可解释性，符合风控场景的审计要求

  - 摘要式长对话记忆机制可迁移到长会话推荐、私域运营Agent场景，无需每次传入全量对话历史，降低70%以上的上下文token开销，同时避免长上下文信号丢失、模型幻觉问题

  - 垂直领域评测集构建的「真实样本+LLM生成对抗样本」思路可复用在业务的黑产攻击防御场景，覆盖新型未知攻击路径，提升模型鲁棒性

  - 敏感场景优先采用自托管开源模型+本地工具链的方案，避免第三方API泄露用户支付、身份等敏感数据，满足电商、金融场景的合规要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
生成式AI降低了多轮对话式诈骗的实施成本，这类诈骗通常跨越数周通过信任构建诱导用户转账或泄露隐私，现有单消息检测系统无法捕捉跨轮次诈骗信号，且公开多轮对话诈骗评测数据集稀缺，闭源API依赖还存在严重的用户隐私泄露风险。

### 方法关键点
- 采用模块化7Agent架构：由Orchestrator调度Artifact Trigger（轻量检测风险线索触发流程）、Extractor（结构化提取联系信息/链接/品牌）、Verifier（身份真实性校验）、SMD（单消息检测）、Investigator（自适应更新对话摘要与威胁等级）、CSD（对话级检测）、Advice Generator（生成用户友好提示）。
- 创新摘要式长对话记忆：替代全量历史传入，大幅降低上下文开销；Investigator执行频率随威胁等级自适应调整，低风险每5轮运行、高风险每2轮运行，平衡性能与成本。
- 全栈替换闭源依赖为自托管开源模型与本地工具链，避免敏感对话数据外泄。
- 开源多类别对话诈骗基准ConScamBench-278，覆盖8类诈骗场景，含128条诈骗（110条真实+18条LLM生成对抗样本）、150条正常对话，标注一致性κ=0.89。

### 关键结果
- 单消息检测对比基线SmishX，钓鱼召回率从91.3%提升至100%，正常消息召回率从97.2%提升至98.5%。
- 对话级检测在LoveFraud02恋爱诈骗语料上召回率100%，平均首次检测仅9.06轮；在ConScamBench-278上准确率97.8%，诈骗召回率98.4%，误报率2.7%。
- 对比全量对话输入基线，长对话场景召回率高2.4pct，上下文成本仅为其1/10。

> 最值得记住：长会话Agent的核心竞争力不是大模型，而是通过架构设计在成本可控前提下实现高性能、可解释性与隐私安全的平衡
