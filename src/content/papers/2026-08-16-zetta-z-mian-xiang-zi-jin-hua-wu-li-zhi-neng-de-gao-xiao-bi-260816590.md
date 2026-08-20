---
title: 'Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical
  Intelligence'
title_zh: Zetta ζ：面向自进化物理智能的高效闭环具身调度框架
authors:
- Xin Ding
- Liang Mi
- Mingzhe Huang
- Zixuan Wang
- Chao Zhang
- Zixu Hao
- Fu Chen
- Xiangyu Li
- Yikai Zheng
- Yaoyu Guo
affiliations:
- 清华大学人工智能产业研究院（AIR）
- Z-Trans AI
arxiv_id: '2608.16590'
url: https://arxiv.org/abs/2608.16590
pdf_url: https://arxiv.org/pdf/2608.16590
published: '2026-08-16'
collected: '2026-08-20'
category: Agent
direction: 具身Agent · 闭环自进化框架
tags:
- Embodied Agent
- Closed-loop Learning
- Runtime Optimization
- Skill Evolution
- Inference Acceleration
one_liner: 提出三层时间尺度分离的闭环具身调度框架Zetta，冻结基础策略在线进化校验与恢复技能，推理提速11.1倍
practical_value: '- 三层时间尺度分离的闭环优化思路可复用在实时推荐/广告系统：高频层做runtime badcase实时拦截、中频次做单次请求的策略调整、低频次做离线校验后的规则更新，兼顾实时性与迭代效率

  - 冻结基座仅迭代轻量代码化规则的思路可降低大模型落地成本：电商Agent客服/导购场景下无需微调基座，仅在线更新意图校验、异常回复技能，稳定性更高

  - 异构资源解耦的Z-Infra架构可借鉴：Agent逻辑与执行资源分离，适配不同算力硬件，降低多场景部署适配成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前具身Agent执行框架多为开环，仅在单次任务结束后做事后反思，无法应对物理交互中快速变化的环境状态，大模型推理延迟也无法满足实时决策的频率要求。
### 方法关键点
1. 设计三层时间尺度分离的闭环架构：高频动作层做实时决策管控、中频rollout层生成校验与恢复策略、低频层做验证门控的技能更新，全程冻结基础策略，仅在线进化代码化的runtime校验器与恢复技能
2. 配套Z-Infra部署架构，将Agent逻辑与异构执行资源解耦，降低跨硬件适配成本
### 关键结果
在LIBERO-Pro、RoboCasa基准上成功率分别达90.8%、93.6%，推理速度提升11.1倍；成功率随自探索经验增长持续提升，习得技能支持零样本迁移。
