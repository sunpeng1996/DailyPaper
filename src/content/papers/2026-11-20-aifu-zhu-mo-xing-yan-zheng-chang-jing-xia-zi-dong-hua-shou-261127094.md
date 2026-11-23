---
title: Separating Automation Gains from Agent Contributions in AI-Assisted Model Validation
title_zh: AI辅助模型验证场景下自动化收益与Agent贡献的分离方法
authors:
- M. Ahmadi Achachlouei
arxiv_id: '2611.27094'
url: https://arxiv.org/abs/2611.27094
pdf_url: https://arxiv.org/pdf/2611.27094
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: Agent评估 · 贡献归因与价值核算
tags:
- Agent Evaluation
- LLM Agent
- Attribution Protocol
- Model Risk Management
- Evaluation Validity
one_liner: 提出分阶段架构与归因协议，精准分离AI辅助流程中自动化增益与Agent贡献
practical_value: '- 评估Agent业务价值时必须设置纯自动化无LLM的基线组，禁止直接和纯人工流程对比，避免将规则/自动化本身的收益错误算为Agent贡献，可直接复用在电商客服、推荐系统调优等Agent的效果评估中。

  - 可复用归因规则：仅对基线未覆盖的故障/问题给Agent算贡献，Agent发现的可自动化规则可回灌到基线流程，仅给一次性发现奖励，避免重复计算价值。

  - Agent上线前的成本收益门限可参考文中公式，提前核算固定成本、单次调用成本对应的人力节省阈值，达不到阈值直接不立项，适配业务侧ROI评估需求。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前金融领域LLM Agent辅助模型验证的评估普遍直接对比人工流程，会把数字化证据、确定性测试等自动化环节的增益错误算到Agent头上，甚至会奖励Agent重复输出自动化基线已经发现的问题，无法真实衡量Agent的增量价值，也存在Agent越权审批的安全风险。

### 方法关键点
- 分阶段架构：保留无LLM的确定性工作流P1作为 fallback和控制组，Agent任务P2仅在P1基础上运行，无决策权限仅输出提案，所有审批由人工完成。
- 归因协议：仅对P1未发现的故障给Agent算检测贡献，P1已发现的问题仅计算Agent的人力节省价值，不记检测贡献；Agent发现的可自动化检测规则可回灌到P1，仅给一次性发现奖励；误报、不必要操作、采纳开发者错误断言都会被扣分，无效输出直接算漏检。
- 落地约束：提前设定安全阈值和成本收益门限，只有人力节省的95%置信区间下限超过阈值才允许上线。

### 关键实验
用6个合成信用评分卡变体做测试，朴素评估指标把4种存在缺陷的策略（复读P1结果、全量上报、误报诱饵、锚定开发者断言）都打成4/6准确率、3/5故障检出率，无法区分优劣；而提出的协议可清晰区分所有5种策略，仅完美策略能拿到P1外的2/2故障检出贡献。一次规则回灌后，复读策略的朴素评分涨到5/6，但增量贡献仍为0。

**最值得记住的一句话**：LLM Agent的业务价值永远要和你已经能做到的最好自动化基线比，而不是和纯人工比。
