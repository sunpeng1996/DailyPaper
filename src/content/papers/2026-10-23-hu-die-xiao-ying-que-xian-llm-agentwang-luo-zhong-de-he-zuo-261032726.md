---
title: 'The Butterfly Defects: Tracing Cooperation in LLM Agent Networks'
title_zh: 蝴蝶效应缺陷：LLM Agent网络中的合作行为追踪
authors:
- Maria Sampani
- Maria Lymperaiou
- Angeliki Dimitriou
- Giorgos Filandrianos
- Chrysoula Zerva
- Giorgos Stamou
affiliations:
- National Technical University of Athens
arxiv_id: '2610.32726'
url: https://arxiv.org/abs/2610.32726
pdf_url: https://arxiv.org/pdf/2610.32726
published: '2026-10-23'
collected: '2026-10-26'
category: MultiAgent
direction: 多智体协作 · LLM Agent网络稳定性
tags:
- MultiAgent
- LLM Agent
- Cooperation
- Game Theory
- Prompt Sensitivity
one_liner: 揭示LLM Agent网络合作的高敏感性，微小提示变动可跨多跳传导影响全局协作效率
practical_value: '- 搭建电商多Agent协同系统（如流量调度、商家运营、客服Agent组网）时，不能仅验证单Agent策略效果，需额外测试异构模型混合部署、不同网络拓扑下的协作稳定性，避免单Agent行为引发全局策略偏移

  - Agent决策类prompt上线前需做选项顺序鲁棒性校验，尤其是优惠券发放、流量加权等二分类决策场景，避免语义完全等效的prompt选项顺序变动导致决策结果大幅波动

  - 多Agent系统中高连接度核心节点（如全局流量分配Agent）的prompt或策略变更需做严格灰度验证，论文验证核心节点微小干预的影响可扩散至多跳外节点，易引发全链路效率损失

  - 评估多Agent协作效果时不能仅看单节点或单轮收益，需追踪多轮交互下的行为溢出效应，平衡单个Agent成本与全局系统福利，避免局部最优损害整体效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent正从孤立任务执行转向多Agent组网协同，业界普遍默认单Agent的合作属性会直接传递到组网场景，但多Agent协作的实际影响因素（网络结构、模型异质性、prompt细节）尚未被系统性验证，微小局部变动是否会引发全局协作崩溃的问题直接影响多Agent系统的落地稳定性，亟待明确。
### 方法关键点
- 基于网络版迭代囚徒困境（IPD）框架，要求Agent向所有邻居广播同一决策，而非针对单个邻居独立决策，还原真实组网下的决策耦合约束
- 控制变量覆盖三类拓扑（线形/环形/星形）、3~20节点的网络规模、同构/同模型族跨规模异构的模型组成、全局/局部注入的不确定性提示、动作标签顺序（C在前/D在前）五类维度
- 评估指标包含各Agent合作率、个体累积成本、全局社会成本，以及标签顺序敏感性指数SI
### 关键结果
- 异构组网下模型合作率较同构基线最高偏移95%，如Qwen-32B与Qwen-3B混合组网时合作率从同构场景的1.0降至0.05
- 单个Agent注入不确定性提示的影响最远可传导到10跳外的未暴露Agent，星形拓扑下核心节点干预可使未暴露节点合作率最高变动0.41
- 动作标签顺序反转可使部分模型合作率从0直接升至1，叠加不确定性提示时敏感性最高达SI=0.99，相同干预在不同标签顺序下可使全局社会成本从下降0.458转为上升0.228

最值得记住的一句话：LLM Agent的合作性不是稳定的模型级属性，多Agent系统的全局协作效果由模型组成、网络结构、prompt表述共同决定，必须在真实部署的组网环境和prompt变体下做充分验证。
