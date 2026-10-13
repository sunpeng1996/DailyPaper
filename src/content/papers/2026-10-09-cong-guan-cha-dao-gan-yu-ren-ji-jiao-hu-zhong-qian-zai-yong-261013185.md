---
title: 'From Observation to Intervention: Identifiability of Latent User Bias in Human-AI
  Interaction'
title_zh: 从观察到干预：人机交互中潜在用户偏见的可识别性
authors:
- Lucas Biechy
- Yuxiao Li
- Zhonghao He
- Tianyi Qiu
affiliations:
- Inria
- INSA-CVL
- Oxford Human-Centered AI Lab
- Johns Hopkins University
- Stanford University
arxiv_id: '2610.13185'
url: https://arxiv.org/abs/2610.13185
pdf_url: https://arxiv.org/pdf/2610.13185
published: '2026-10-09'
collected: '2026-10-13'
category: RecSys
direction: 推荐系统用户建模 · 偏好与偏见识别
tags:
- User Modeling
- Cognitive Bias
- Preference Elicitation
- Multi-Armed Bandit
- Alignment
one_liner: 证明被动观察无法区分用户真实偏好与认知偏见行为，提出主动干预实现可识别
practical_value: '- 电商/推荐系统做用户偏好建模时，不可完全信任被动收集的点击、浏览行为数据，避免因用户确认偏误等认知偏见陷入信息茧房、恶性反馈循环

  - 冷启动或用户偏好模糊场景，可设计低干扰的零收益干预（如随机推送少量非当前兴趣域的商品/内容），区分用户真实偏好与偏见驱动行为

  - 多臂老虎机的主动干预框架可直接复用在推荐系统exploration模块，提升偏好识别鲁棒性，降低对齐偏差'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有对齐、推荐类方法普遍将用户行为作为真实偏好的可靠代理，未考虑用户认知偏见会导致行为信号失真，易引发确认陷阱、恶性反馈循环，且此前缺乏该场景下偏好可识别性的严谨理论证明。
### 方法关键点
将人机交互建模为多臂老虎机问题，首先给出被动观察下的不可识别性定理证明；进一步提出主动偏好引导框架，通过有限长度的对抗零收益干预序列打破观测等价性。
### 关键结果
1. 仅依靠被动行为数据的偏好估计器表现不优于随机猜测；
2. 长度为$m_δ$的有限次零收益干预即可让干预后用户行为分布任意可分，实现真实偏好与偏见驱动行为的有效区分。
