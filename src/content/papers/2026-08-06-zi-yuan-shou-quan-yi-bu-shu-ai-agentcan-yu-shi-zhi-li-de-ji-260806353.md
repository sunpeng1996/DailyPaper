---
title: Resourced Authority A Mechanism-Design Model for Participatory Governance of
  Deployed AI Agents
title_zh: 资源授权：已部署AI Agent参与式治理的机制设计模型
authors:
- Praphul Chandra
- Sujit Gujar
- Ganesh Ghalme
affiliations:
- Atria University
- IIIT Hyderabad
- IIT Hyderabad
arxiv_id: '2608.06353'
url: https://arxiv.org/abs/2608.06353
pdf_url: https://arxiv.org/pdf/2608.06353
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: Agent 参与式治理 · 机制设计
tags:
- mechanism_design
- AI_governance
- compute_budget
- multi_agent_system
- trusted_computing
one_liner: 基于算力预算分配设计自执行的已部署AI Agent参与式治理机制
practical_value: '- 可借鉴算力绑定授权逻辑，给业务侧部署的推荐/广告Agent设置动态算力配额，避免越权调用资源生成不合规推荐文案/商品

  - 参考带滞环的双阈值授权机制，对用户/商家反馈的推荐规则调整请求设置触发阈值，减少规则频繁抖动影响业务稳定性

  - 可复用利益相关方广度加权投票逻辑，用于多部门协同管控大模型推荐系统的合规迭代，平衡各业务方诉求'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
已部署AI Agent的外层治理缺乏自执行机制，传统对齐方案仅解决训练侧内层问题，无法管控上线后的实际运行行为，急需可落地的参与式治理框架。
### 方法关键点
1. 以算力分配为核心治理杠杆，采用独立于Agent算力的治理代币，让验证通过的利益相关方在供给/否决市场参与投票
2. 对原始投票做广度加权计算有效支持度，通过带滞环的双阈值门生成二元授权结果，结合外部认证的安全上限输出计量化算力预算，硬件层用签名算力许可证实现决策自执行
### 关键结果
明确机制可覆盖的Agent类别：俱乐部/公共品类Agent、利益相关方边界清晰、影响可逆且与算力正相关、结果可认证，同时指出被治理Agent操控投票群体是核心待解决问题
