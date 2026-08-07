---
title: 'ProCAVE: A Self-Adaptive, Full-Lifecycle Edge Caching Framework for Video
  Streaming via Predictive Bandwidth Estimation and Preference-Aware Deep Reinforcement
  Learning'
title_zh: ProCAVE：基于预测带宽与偏好感知DRL的自适应视频流边缘缓存框架
authors:
- Yeganeh Chatri
- Behzad Akbari
- Foad Ghaderi
- Pejman Goudarzi
affiliations:
- Tarbiat Modares University
- ICT Research Institute
arxiv_id: '2608.03313'
url: https://arxiv.org/abs/2608.03313
pdf_url: https://arxiv.org/pdf/2608.03313
published: '2026-08-04'
collected: '2026-08-07'
category: Agent
direction: DRL Agent 边缘视频流缓存优化
tags:
- Edge Caching
- Deep Reinforcement Learning
- Transformer
- PPO
- DDPG
- QoE
one_liner: 融合轻量Transformer带宽预测、PPO ABR与DDPG缓存控制的端到端边缘视频流缓存DRL框架
practical_value: '- 电商短视频/直播边缘分发场景可复用「轻量Transformer带宽预测+DRL自适应缓存/码率控制」架构，降低卡顿率提升播放QoE

  - 多DRL模块协同的思路可迁移到推荐系统多目标联合优化场景，比如分别用PPO做排序、DDPG做流量资源分配的跨模块协同

  - 偏好感知+实时环境状态联合建模的逻辑可用于端侧推荐缓存策略优化，降低回源带宽成本同时提升内容加载速度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
移动视频流量占比持续攀升，现有边缘缓存方案依赖反应式ABR启发式规则，缓存策略与码率适配逻辑松耦合，无法应对无线网络波动与用户偏好动态变化，响应性与跨层协同能力不足。
### 方法关键点
ProCAVE是全生命周期自适应DRL边缘缓存框架，核心包含三个协同模块：①轻量Transformer实现短期吞吐量预测；②PPO驱动的ABR Agent实现主动码率选择；③DDPG-based连续缓存控制器，基于全局高维状态输出缓存决策，端到端打通预测、码率适配、缓存全链路。
### 关键结果
基于MovieLens用户偏好轨迹、Ghent 4G带宽实测数据实验，相比FlyCache等基线方案，字节命中率明显提升，回传负载降低，用户QoE综合表现最优。
