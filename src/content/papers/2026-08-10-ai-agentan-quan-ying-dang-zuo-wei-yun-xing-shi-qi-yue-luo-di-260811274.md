---
title: Agent Safety Should Be a Runtime Contract
title_zh: AI Agent安全应当作为运行时契约落地
authors:
- Albus W. Ng
- Yi Han
- Jusheng Zhang
- Wenhao Wang
affiliations:
- Vast Intelligence Lab
- Southwest University
- Sun Yat-sen University
arxiv_id: '2608.11274'
url: https://arxiv.org/abs/2608.11274
pdf_url: https://arxiv.org/pdf/2608.11274
published: '2026-08-10'
collected: '2026-08-13'
category: Agent
direction: Agent运行时安全防护体系构建
tags:
- Agent Safety
- Runtime Verification
- Alignment
- Harness
- Evidential Gating
one_liner: 提出含预防+证据双维度的Agent运行时安全契约框架，替代单一训练对齐范式
practical_value: '- 电商导购/客服Agent的安全防护不要仅依赖RLHF/DPO训练对齐：必须加运行时预防层，比如高危接口（下单、改地址、发优惠券）白名单管控、输出敏感词过滤、沙箱隔离第三方工具调用，提前拦截风险动作

  - Agent任务闭环节点新增证据门校验：比如营销文案生成任务必须过RAG溯源校验活动规则、优惠券有效期的真实性，商品推荐任务必须校验推荐商品在架/有库存，所有校验通过才允许下发给用户，避免幻觉导致客诉

  - 全量Agent执行轨迹做哈希链式存证：留存工具调用、输出内容、用户反馈等全链路日志，支持事后审计回溯，满足电商场景的合规、客诉排查需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI安全主流依赖RLHF、DPO、Constitutional AI等训练对齐方案，这类方案本质是统计偏好拟合，存在固有缺陷：易受奖励黑客攻击、开放环境泛化性差、单点故障无兜底，完全无法覆盖可调用工具、执行操作的Agent场景的安全风险，过往大量安全事件证明训练对齐对已发生的风险几乎无 mitigation 作用。

### 方法关键点
1. 提出双维度运行时安全契约框架：预防层从执行前到执行后分4类机制（准入类、检测类、修正类、架构类），多层防护无单点故障；证据层定义标准化Agent Trajectory Schema，所有操作生成不可篡改的哈希链，明确硬证据（可第三方校验的测试结果、引用溯源等）与软证据（模型自报告）的判定规则，任务完成必须通过硬证据链校验才会被接受。
2. 支持多防护层、多证据门的可组合验证，验证开销可控，故障可定位到具体模块。

### 关键结果
- 52起2016-2026年公开Agent/LLM安全事件分析：40起可通过运行时防护完全避免，11起可被缓解，仅1起需要训练对齐介入
- 32起Agent虚假完成任务案例：全部可通过证据门校验拦截，避免错误结果流入下游
- 12个主流开源Agent系统调研：仅2个（GitHub Copilot、OSWorld）实现了证据提交门，92%的现有方案依赖模型自报告的完成状态
- 2023-2025年三大顶会28560篇论文统计：训练对齐相关工作是部署时运行时安全研究的8~12倍

### 核心结论
Agent安全的核心单元是带可校验证据的执行轨迹，而非模型本身。
