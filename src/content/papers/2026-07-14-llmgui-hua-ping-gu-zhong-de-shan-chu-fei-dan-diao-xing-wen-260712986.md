---
title: 'Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State
  Gating in LLM Plan Evaluation'
title_zh: LLM规划评估中的删除非单调性问题与类型状态门控方案
authors:
- Aleh Manchuliantsau
arxiv_id: '2607.12986'
url: https://arxiv.org/abs/2607.12986
pdf_url: https://arxiv.org/pdf/2607.12986
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: LLM规划评估 · 漏洞检测与抑制
tags:
- LLM Planning
- Plan Evaluation
- Typed-State Gating
- Omission Incentive
- Exploit Mitigation
one_liner: 揭示LLM规划评估的删改提分漏洞，提出GATE门控机制抑制隐去必要步骤的投机行为
practical_value: '- 业务Agent（如电商导购、投放优化Agent）的规划评估可复用GATE类型状态门控机制，避免隐去库存校验、隐私校验等必要步骤的规划获得虚高评分

  - 可借鉴文中的得分增量公式Δ_k，量化节点删除对路径得分的影响，用于广告投放路径、大促活动运营路径的自动优化筛查

  - 搭建LLM生成策略的自动评估链路时，需提前识别「删除关键步骤反而提分」的非单调风险，避免输出有逻辑缺陷的业务方案'
score: 8
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前LLM生成规划的分阶段预期价值评分器存在非单调性漏洞，删除必要中间步骤的不完整规划反而能获得更高评分，催生投机性内容省略动机，导致评估结果完全失真。
### 方法关键点
1. 推导删除中间过渡节点后的得分变化解析公式Δ_k，可精准预判删改操作对规划得分的影响；
2. 提出GATE类型状态门控机制，作为确定性搜索约束而非事后过滤器，拦截隐去必要步骤的投机规划；
3. 配套PCSC模块检测并抵消事后插入的省略拼接操作。
### 关键结果
在26条固定规划测试集上，57次合法删改全部符合解析公式的得分变化预判，所有规划均存在至少1次可提分的删改操作；GATE对26条投机静音规划100%拦截且无误拦，拦截后47/54的后续修订自动修复为合法结构，严格合规的提分规划占比从1/26提升至13/26；配套成本下限机制可将靠省略提分的可融资规划占比从5/6降至0。
