---
title: 'Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents
  under Execution Audit'
title_zh: 面向执行审计的可演进LLM Agent人格-执行分离架构模式
authors:
- Yisen Xi
affiliations:
- Independent Researcher, Beijing, China
arxiv_id: '2608.27427'
url: https://arxiv.org/abs/2608.27427
pdf_url: https://arxiv.org/pdf/2608.27427
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: LLM Agent 架构设计与合规治理
tags:
- LLM_Agent
- Architecture_Pattern
- Trust_Domain
- Governance
- Audit
one_liner: 将LLM Agent的人格与执行层拆分到不同信任域，通过合规契约桥同时支持自由迭代与执行可审计
practical_value: '- 企业级Agent（电商客服、智能运营Agent等）可借鉴PES架构：将人设话术、规则调优放在低管控域，支付、改订单等高风险操作放在高管控域，大幅降低迭代的合规成本

  - 跨域交互可复用契约桥设计：仅允许状态摘要、身份标识双向流通，核心业务数据默认留在高管控域，仅通过分级DLP开放例外，降低数据泄露风险

  - 可复用人设分层思路：将核心身份（工号、权限范围）固化在高管控域，表面人设（语气、话术模板）允许自由迭代，既保证审计锚点稳定，又支持快速调优'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有单域LLM Agent架构无法同时满足两类刚需：一是运营需频繁调整Agent的人设、指令、话术，要求迭代零合规成本；二是金融、电商等监管场景下，Agent的状态变更操作（资金操作、订单修改等）必须全程可追溯、不可篡改。单域架构要么冻结人设阻碍迭代，要么放松管控丢失审计能力，需新架构解耦两者。

### 方法关键点
- 双信任域拆分：将Agent拆为低管控人格域（存放人设、指令、交互界面，支持自由迭代）和高管控执行域（无对话人设，仅运行标准化SOP、存储核心数据、留存全量审计日志），二者同属一个Agent身份
- 受控契约桥：跨域仅允许三类流量：执行状态摘要返回人格域、核心数据默认留在执行域仅通过分级DLP开放例外、身份标识跨域保持连续，所有跨域请求经过审批矩阵、DLP检查、审计留痕三重校验
- 绑定而非投影：人格域通过能力绑定列表调用执行域SOP，不拷贝执行域逻辑，避免多源数据漂移

### 关键结果
在金融数字员工平台试点1个月，5次架构决策均验证方案可行性；5种不同模型配置下，人设扰动不会触发执行侧重校验，硬校验字段无人设指纹残留；对比8款开源Agent平台，现有方案均无法同时满足自由迭代、执行可追溯、解耦三个目标。

最值得记住的一句话：在LLM Agent人设与执行指令语义不可区分的前提下，单域内任何满足双需求的方案本质都是更高耦合成本的PES重构，跨域拆分是最低成本的解法。
