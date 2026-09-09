---
title: 'FunnelAudit: Responsibility Auditing in Multi-Route Recommender Systems'
title_zh: FunnelAudit：多链路推荐系统的责任审计框架
authors:
- Jie Li
- Dudu Luo
- Jiayang Niu
- Ke Deng
- Yongli Ren
affiliations:
- Independent Researcher, Australia
- University of Southern Queensland
- RMIT University
arxiv_id: '2609.06964'
url: https://arxiv.org/abs/2609.06964
pdf_url: https://arxiv.org/pdf/2609.06964
published: '2026-09-07'
collected: '2026-09-09'
category: RecSys
direction: 推荐系统可解释 · 多链路审计
tags:
- recommender_system
- accountability
- causal_auditing
- multi_route_retrieval
- causal_reasoning
one_liner: 提出可执行的多路径推荐责任审计框架，解决单变量消融无法定位根因的问题
practical_value: '- 排查推荐BadCase时不要只做单链路消融，可参考梯度实际责任规则，找最小的其他链路变更组合定位根因，避免漏判90%+的隐藏责任链路

  - 多链路召回的融合策略（配额分配、RRF）会显著影响根因定位结果，做审计时必须完整复现从召回变化到排序的全链路，不能只看最终得分

  - 提前给核心链路定义可复现的开关与参考动作，留存各链路召回结果快照，出现客诉时可快速基于合约复现全链路结果生成证据'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业推荐普遍采用多链路召回+融合+排序的漏斗架构，单个物品是否进入Top-K是多组件交互的结果，传统单链路消融无法覆盖链路冗余、下游重计算场景，既会漏判根因，也无法生成可验证的审计证据，无法满足合规与客诉排查需求。
### 方法关键点
- 定义可审计的责任合约：注册争议Top-K事件、可控链路/所有者、允许的参考动作（如关闭某链路、跳过配额分配）、需要重放的下游阶段
- 采用梯度实际责任判定规则：寻找最小的事实保留contingency（其他链路变更组合），使得目标控制变量成为影响物品是否进入Top-K的关键变量
- 审计执行分两步：首先按合约对所有允许的控制配置做阶段忠实重放，生成所有配置下的Top-K结果；再遍历结果找到每个控制的最小有效contingency，输出可验证的审计证书
### 关键结果
实验基于MovieLens-1M、Amazon Beauty、UCI Online Retail三个真实数据集，复现9链路召回+SASRec排序的工业级漏斗，对比单链路消融（LOCO）、Shapley值等基线：
1. 4.24%~16.24%的用户-物品事件存在至少一个责任控制，其中92.55%~99.64%的责任对需要非空contingency，单链路消融仅能覆盖0.36%~7.45%的责任对
2. 即使两种服务策略仅在0.31%~2.39%的事件上有结果差异，两者匹配的排除事件的责任链路集合Jaccard距离可达21.44%~54.05%
3. 独立重放完全复现912万+目标世界结果，穷举搜索和混合整数线性规划验证所有抽样判决的正确性
### 核心结论
推荐系统问责需要明确的服务和重放语义以及可核查的事件级证据，而不是另一个聚合重要性分数。
