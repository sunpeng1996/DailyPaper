---
title: 'Next Best Action: Causal Constrained Offline RL for Business Action Targeting'
title_zh: 面向业务动作触达的因果约束离线RL最优动作决策框架
authors:
- Surya Ramachandiran
- Yiming Li
- Juan Mancilla-Caceres
- Tao Ye
- Jun Liu
affiliations:
- Lyft, Inc.
arxiv_id: '2610.26817'
url: https://arxiv.org/abs/2610.26817
pdf_url: https://arxiv.org/pdf/2610.26817
published: '2026-10-19'
collected: '2026-10-20'
category: RecSys
direction: 用户运营触达 · 因果约束离线RL
tags:
- Offline RL
- Causal Inference
- Constrained MDP
- LTV Optimization
- Recommendation System
one_liner: 融合因果校正、约束优化与离线RL的用户触达决策框架，可显著提升客户长期价值
practical_value: '- 电商优惠券、权益触达场景可直接复用SNIPW因果校正思路，修正历史日志的策略偏差，得到无偏的用户转化/状态转移估计，解决现有uplift模型短视的问题

  - 多约束CMDP+LP求解框架可直接落地，支持预算上限、人群分配、曝光频次、公平性等6类业务约束，无需像深度RL那样做约束对齐的黑盒调优，可解释性强

  - LP输出的约束影子价格可直接用于预算规划，量化每个约束放松1单位带来的LTV增益，为运营决策提供数据支持，无需额外做大量AB测探索预算最优值

  - 离散用户分群（如RFM）场景下，这套框架比深度RL样本效率高，无需大量训练数据即可落地，适合冷启动的运营活动'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有用户触达方案存在三类核心痛点：1）基于历史日志训练的策略未做因果校正，动作效果估计受历史策略偏差影响，存在严重confounding；2）离线RL优化长期价值的方案无法显式满足预算、公平性、曝光频次等业务硬约束，落地难度高；3）uplift建模+数学规划的两阶段方案仅优化即时收益，未考虑当前动作对用户长期LTV的影响，短视问题突出。行业缺乏同时解决三个问题的统一可落地方案。
### 方法关键点
- 将最优动作决策建模为CMDP，状态采用用户RFM生命周期分群，动作对应干预（如发券）/不干预，奖励为用户当期业务价值，目标最大化长期LTV
- 采用SNIPW（自归一化逆倾向权重）校正历史日志的策略偏差，得到无偏的因果转移概率和奖励估计，解决训练数据有偏问题
- 将CMDP转化为对偶LP问题求解，可显式嵌入6类业务约束：平台预算、人群分配、曝光频次、互斥动作分配、动作eligibility、公平性，求解得到的最优状态-动作占用率直接归一化得到最优策略
- LP输出的约束影子价格可量化每个约束放松1单位带来的LTV增益，直接用于预算规划和场景分析
### 关键实验
基于Lyft 68周（52周训练、16周时序验证）的千万级用户骑行数据验证，对比历史行为策略、短视uplift基线，最优策略在相同预算约束下，LTV相对提升19%（对比历史策略）、8%（对比短视基线）。
### 核心洞察
做用户长期价值优化的触达策略，必须同时兼顾因果无偏估计、业务约束落地、长期收益优化三个维度，缺一不可
