---
title: Mitigating Retaliatory Algorithmic Collusion in Repeated Games
title_zh: 重复博弈中报复性算法合谋的通用缓解框架
authors:
- Karthik Sivachandran
- Rohan Paleja
affiliations:
- Purdue University
arxiv_id: '2609.20548'
url: https://arxiv.org/abs/2609.20548
pdf_url: https://arxiv.org/pdf/2609.20548
published: '2026-09-17'
collected: '2026-09-18'
category: MultiAgent
direction: 多智能体博弈 · 算法合谋抑制
tags:
- Multi-Agent RL
- Algorithmic Collusion
- Reward Shaping
- Repeated Games
- Q-Learning
one_liner: 基于TV惩罚与信念注入的CURB框架 可证明抑制多智能体算法合谋
practical_value: '- 电商定价场景可复用TV距离检测逻辑：通过统计商家定价在对手降价/维持原价两种历史下的分布差异，识别报复性合谋行为，提前进行合规干预

  - 广告竞价系统可引入CURB奖励塑形机制：给依赖对手历史出价的报复性调价策略加惩罚，避免竞价方合谋抬高广告成本，兼顾平台与中小广告主利益

  - 多Agent系统开发可借鉴信念注入技巧：定期向智能体回放缓冲区注入「违规不会被报复」的合成样本，引导智能体放弃合谋策略，降低反垄断合规风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
近年RL智能体在电商定价、广告竞价、租赁平台定价等多智能体重复互动场景中，无需通信即可自发形成合谋，推高商品/服务价格损害消费者利益，如2024年美国司法部起诉RealPage算法抬租事件。现有合谋缓解方案多绑定特定场景（如修改拍卖规则、平台中心化流量调控），无法跨场景通用，且无法从机制层面消除合谋的报复性惩罚基础。
### 方法关键点
- 建立算法合谋与重复博弈简单惩罚码（SPC）的理论关联，证明非平凡合谋策略必然在智能体动作分布上产生可检测的总变差（TV）距离差：对手背叛和合作两种历史下的动作分布TV≥仅由博弈参数决定的正阈值
- CURB框架包含两个核心组件：一是奖励塑形，在Q学习奖励中加入TV距离惩罚项，提高报复性行为的成本；二是信念注入，定期向回放缓冲区注入「背叛不会被报复」的合成经验，打破合谋的惩罚预期
- 理论证明惩罚强度足够时，所有依赖报复的合谋均衡都会被拆解，仅剩无报复行为的平凡均衡
### 关键结果
在Bertrand价格竞争、Cournot产量竞争两类经典博弈场景验证，对比无干预、平台流量调控（PDP/DPDP）、不完全监控等基线：
- λ=0.2的CURB将双主体Bertrand博弈的合谋指数CI（0为完全竞争，1为完全合谋）从基线的0.88降到0.0029，接近纳什均衡
- 适配DQN的CURB仍能将CI从基线的0.8降到0.1以下，跨学习算法、跨博弈场景有效
### 核心结论
算法合谋的核心是报复性惩罚策略的隐性共识，通过惩罚策略的历史依赖属性即可从机制层面拆解合谋，无需修改博弈规则或中心化管控
