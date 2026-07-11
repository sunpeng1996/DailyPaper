---
title: 'RoboTALES: Learning Reasoning-Guided Robot Policies via Task-Aligned Simulated
  Futures'
title_zh: RoboTALES：基于任务对齐模拟未来的推理引导机器人策略学习
authors:
- Hanan Gani
- Tejal Kulkarni
- Madhoolika Chodavarapu
- Nicklas Hansen
- Manmohan Chandraker
affiliations:
- University of California, San Diego
arxiv_id: '2607.06018'
url: https://arxiv.org/abs/2607.06018
pdf_url: https://arxiv.org/pdf/2607.06018
published: '2026-07-06'
collected: '2026-07-11'
category: Agent
direction: 具身Agent · 分层规划策略优化
tags:
- LLM
- VLM
- Hierarchical Reasoning
- Policy Optimization
- Diffusion Model
- Video Generation
one_liner: 提出融合分层LLM规划与VLM奖励反馈的单阶段具身Agent策略学习框架
practical_value: '- 长周期业务任务（如用户全链路转化、多步搜索意图满足）可复用分层LLM拆解子目标的思路，避免执行路径偏离核心业务目标

  - 生成式推荐/内容生成场景可引入VLM类判别器对输出做目标对齐的奖励反馈，提升生成结果的业务相关性

  - 模拟未来+奖励反馈的架构可迁移到推荐系统的用户行为预判，提前筛选符合长期业务目标的推荐策略'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
预训练视频生成模型作为视觉运动控制backbone时，生成的想象未来易偏离任务意图、动作条件性不可靠，难以直接用于规划或策略提取。
### 方法关键点
1. 单阶段RoboTALES框架，同步学习任务对齐的模拟未来并训练机器人策略
2. 分层LLM规划器将复杂任务拆解为子目标序列，引导视频生成模型的想象过程
3. VLM-based critic评估生成的想象未来，基于奖励反馈约束模型表征聚焦核心目标，保障时序一致性与动作连贯性
### 关键结果
在RoboCasa、LIBERO10的多类操纵任务上性能全面超越现有方法，长horizon任务上优势尤为突出
