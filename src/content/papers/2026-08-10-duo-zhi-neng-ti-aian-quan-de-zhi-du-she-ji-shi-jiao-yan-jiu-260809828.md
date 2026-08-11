---
title: Multi-Agent AI Safety as an Institutional Design Problem
title_zh: 多智能体AI安全的制度设计视角研究
authors:
- Abdullah X
affiliations:
- POLIS Research Programme, Project AWARE
arxiv_id: '2608.09828'
url: https://arxiv.org/abs/2608.09828
pdf_url: https://arxiv.org/pdf/2608.09828
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: 多智能体·安全治理机制设计
tags:
- Multi-Agent Safety
- Institutional Design
- Provenance Guard
- Prompt Engineering
- Agent Governance
one_liner: 通过5280集受控实验对比6类治理机制，验证多智能体安全由规则、权限溯源与恢复路径共同决定
practical_value: '- 电商/广告多Agent工作流（如隐私数据跨部门流转、投放权限审批）优先用provenance-aware guard替代基于当前可见状态的本地校验，避免权限洗白漏洞

  - 高风险Agent流程可同时叠加constitutional prompt+可恢复防护机制，既从行为层减少违规尝试，又能在拦截后保留任务重跑能力，平衡合规与业务效率

  - 设计多Agent资源分配规则（如大模型算力配额、广告预算分配）时，不要给利己目标的Agent暴露数值上限，避免触发锚定效应导致超额申请'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多智能体系统已广泛应用于任务委派、资源共享等生产场景，但现有安全方案多聚焦单模型对齐，忽略了系统层面的规则表述、权限校验逻辑、拦截后执行路径对整体安全的影响，相同的最终违规率背后可能存在完全不同的风险敞口，需要拆解制度各组件的实际安全贡献。

### 方法关键点
- 搭建两类受控实验环境：核心委派场景（3角色2主体，覆盖合规内部路径、直接违规路径、权限洗白场景、授权脱敏场景4类任务，6个行业域，4级合规成本压力）；共享资源场景（4个Agent共享100算力单位，测试规则信息透明度对行为的影响）
- 对比6种治理机制：无制度、简洁prompt、constitutional prompt、溯源prompt、本地状态guard、provenance guard，明确区分违规尝试、实际违规、合规完成、安全恢复4类指标
- 覆盖7类主流LLM，固定temperature=0，所有安全标签由确定性环境生成，避免主观标注偏差

### 关键实验结果
总样本量5280集，核心委派实验每类机制384集：constitutional prompt与provenance guard均实现0/384实际违规，前者无任何违规尝试，后者拦截51次违规尝试后44次安全恢复，合规完成率达95.6%；本地guard在权限洗白场景出现22/96实际违规，与provenance guard的0违规对比p=4.77×10⁻⁷；共享资源场景暴露上限后，利己目标Agent的顶格申请率从0提升至2.73%，社会福利目标下提升至5.47%。

最值得记住的结论：最终违规率是不完整的安全指标，多智能体安全是规则通信、权限校验逻辑、拦截后恢复路径共同作用的结果，而非仅由模型本身决定。
