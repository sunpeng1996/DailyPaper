---
title: 'SPHERE: Adaptive VR Indoor Scene Generation via LLM-Enhanced Spatial Preference
  Learning and Human-in-the-Loop RL'
title_zh: SPHERE：LLM增强空间偏好学习与人在环RL的自适应VR室内场景生成
authors:
- Hyeonmin Lee
- Zheng Wei
- Kyungmin Kwon
- Jumin Seo
- Jiwon Park
- Hayoung Oh
arxiv_id: '2610.02023'
url: https://arxiv.org/abs/2610.02023
pdf_url: https://arxiv.org/pdf/2610.02023
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: LLM增强人在环RL 3D场景生成
tags:
- LLM
- Human-in-the-Loop RL
- Preference Learning
- VR
- 3D Scene Generation
one_liner: 提出SPHERE框架，通过LLM提取用户空间偏好与人在环RL实现跨会话自适应VR室内场景生成
practical_value: '- 多模态偏好提取思路可迁移到家居电商个性化场景推荐，从用户语音、交互操作中持久化空间布局偏好，替代传统仅基于点击的用户建模

  - 人在环RL动态更新策略可复用在定制化内容生成场景，根据用户最终修改结果反向优化召回/生成规则，降低用户后续调整成本

  - 分层约束建模（局部功能+全局拓扑）方法可借鉴到电商3D样板间生成、商品组合搭配推荐场景，避免仅关注单品特征忽略全局合理性'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM驱动的3D室内场景生成流水线无法跨会话留存用户个性化空间偏好，VR沉浸式创作需要用户反复调整，物理负担高、效率低。
### 方法关键点
1. 从语音、控制器编辑等多模态自然交互中提取用户持久化空间偏好；
2. 将原始编辑动作抽象为分层约束，同时建模局部功能与全局拓扑上下文，保障几何鲁棒性、避免空间畸变；
3. 引入人在环RL机制，基于用户最终确认的编辑场景动态更新检索策略，实现持续适配。
### 关键结果
42人混合设计用户研究+离线消融实验表明，SPHERE显著降低用户修正编辑量与物理操作负担，避免生成仅偏向浅层对象特征的结果，产出的布局几何鲁棒性更强、与用户偏好匹配度更高。
