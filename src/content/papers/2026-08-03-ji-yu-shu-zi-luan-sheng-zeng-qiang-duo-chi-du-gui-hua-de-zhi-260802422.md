---
title: Agentic Incident Response through Digital Twin-Enhanced Multiscale Planning
title_zh: 基于数字孪生增强多尺度规划的智能体事件响应框架
authors:
- Yiran Gao
- Tao Li
- Kim Hammar
affiliations:
- City University of Hong Kong
- Imperial College London
arxiv_id: '2608.02422'
url: https://arxiv.org/abs/2608.02422
pdf_url: https://arxiv.org/pdf/2608.02422
published: '2026-08-03'
collected: '2026-08-05'
category: Agent
direction: Agent 网络安全事件响应多尺度规划
tags:
- LLM Agent
- Digital Twin
- Multiscale Planning
- Incident Response
- LoRA
one_liner: 融合决策论规划、轻量LLM与数字孪生的多尺度事件响应框架，性能显著优于前沿大模型基线
practical_value: '- 可复用多尺度规划架构：将高层全局最优决策（如用RL/优化算法定推荐优先级、资源分配）与底层LLM适配执行（如生成推荐话术、执行运营动作）解耦，平衡策略合理性和落地灵活性

  - 数字孪生/影子环境验证思路：在推荐/广告/运营场景搭建离线仿真影子环境，新策略/LLM生成内容先在仿真环境验证收益与风险，再上线，降低线上故障概率

  - 垂直场景LLM落地经验：针对特定业务场景（如电商客服、违规治理、活动运营）用LoRA微调小参数垂直模型，效果可超过通用大模型，同时降低推理成本、避免数据外泄'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
传统网络安全事件响应依赖人工操作平均耗时超100天，决策论规划方法仅能输出高层抽象策略无法直接落地，纯LLM驱动的响应方法幻觉严重、规划 horizon 短，亟需兼顾策略最优性和执行可行性的自动化响应方案。
### 方法关键点
- 多尺度分层规划：战术层基于决策论rollout算法，通过数字孪生仿真模拟攻击扩散，输出全局最优的节点恢复优先级策略；执行层用轻量LLM将抽象策略转化为可执行系统命令
- 数字孪生双模式设计：仿真模式支撑战术层快速评估多组候选策略的收益，仿真模式支撑执行层验证生成命令的有效性，避免对生产系统造成影响
- 轻量LLM微调：基于6.8万条公开事件响应对，用LoRA微调DeepSeek-R1-14B，拆分事件评估、状态信念生成、响应动作生成三个子任务适配场景，可本地部署无需依赖外部大模型服务
### 关键结果
在3种多阶段攻击场景下，对比GPT-5.5、Gemini 3.1 Pro等前沿通用大模型，以及IRCOPILOT、LLM-IR等SOTA基线，平均恢复执行时间降低15.1%，恢复成功率提升33.6%，整体成功率稳定在90%以上。
### 核心洞见
垂直领域Agent落地无需盲目追求大参数通用模型，将传统优化方法的全局规划能力、LLM的灵活生成能力、仿真环境的风险校验能力三者结合，小参数微调模型即可实现更优的落地效果。
