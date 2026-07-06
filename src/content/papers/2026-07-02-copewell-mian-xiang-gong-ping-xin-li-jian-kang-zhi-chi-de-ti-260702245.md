---
title: 'Copewell: A Multi-Agent Swarm Architecture for Equitable Mental Wellness Support'
title_zh: Copewell：面向公平心理健康支持的多智能体集群架构
authors:
- Seren Yenikent
- Jack Vinijtrongjit
- Katherine Ng
affiliations:
- Copewell, Singapore
arxiv_id: '2607.02245'
url: https://arxiv.org/abs/2607.02245
pdf_url: https://arxiv.org/pdf/2607.02245
published: '2026-07-02'
collected: '2026-07-06'
category: MultiAgent
direction: 多智能体集群 · 负责任AI场景落地
tags:
- MultiAgent
- Affective Computing
- Responsible AI
- Human-Centered AI
- Multi-modal Assessment
one_liner: 提出融合多源评估、情绪路由、双模式干预的公平性多智能体心理健康支持架构
practical_value: '- 多智能体路由机制可直接复用：可基于用户实时状态（如电商场景下的浏览行为、购买意向、情绪反馈）做标签映射，路由到专属服务/导购Agent，提升用户留存与转化

  - 多源数据融合评估框架可迁移：整合用户显式反馈、隐式行为、场景上下文三类数据，可有效降低推荐/广告系统的群体偏见与冷启动误差

  - 内置专属监督Agent的架构设计可参考：在推荐、营销场景增设合规校验Agent，从输出层规避歧视性、违规内容推送，满足监管要求'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
全球近10亿人受精神疾病困扰，中低收入国家75%人群因资源不足、成本、病耻感无法获得治疗；现有单模态AI心理健康方案弃用率高，无法匹配用户动态情绪状态提供精准即时干预。
### 方法关键点
1. 多源评估框架融合自报告、生理、上下文三类数据，缓解算法偏见；
2. 基于罗素情绪效价唤醒模型做情绪映射，将用户路由到对应细分领域的专业Agent；
3. 双模式干预链路，结合对话支持与循证感官健康方案；架构采用隐私优先设计，内置专属Ethics Supervisor Agent做伦理校验，全流程有心理健康从业者参与设计。
### 关键结果
已完成早期从业者调研与Beta部署，验证了架构的落地可行性，为负责任AI从设计阶段嵌入公平性、安全性原则提供可复用实践范式。
