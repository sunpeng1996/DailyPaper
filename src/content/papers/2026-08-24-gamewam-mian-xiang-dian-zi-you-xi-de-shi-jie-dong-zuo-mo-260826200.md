---
title: 'GameWAM: A World Action Model for Video Games'
title_zh: GameWAM：面向电子游戏的世界动作模型
authors:
- Yuncheng Guo
- Zhanqiu Zhang
- Yiwen Guo
- Weijia Li
affiliations:
- Fudan University
- LIGHTSPEED
- Independent Researcher
- Tsinghua Shenzhen International Graduate School
arxiv_id: '2608.26200'
url: https://arxiv.org/abs/2608.26200
pdf_url: https://arxiv.org/pdf/2608.26200
published: '2026-08-24'
collected: '2026-08-28'
category: Agent
direction: 游戏Agent · 世界动作模型构建
tags:
- Game Agent
- World Action Model
- Flow Matching
- Closed-loop Control
- Generative Control
one_liner: 首个面向原生闭环游戏玩法与GUI控制的世界动作模型，同步生成视觉观测与可执行键鼠轨迹
practical_value: '- 做电商平台智能导购、广告投放自动化等GUI交互类Agent，可复用模态分发生成逻辑：先预测操作模式，再输出模式专属的动作分布，降低异构操作的生成误差

  - 长时序交互Agent可借鉴块循环控制架构：每次生成超执行长度的动作序列，仅执行短前缀后重规划，同时保留跨周期上下文保证时序连续性，平衡规划效率与实时性

  - 生成式控制类任务（如自动出价、定向调整）可参考LASI故障模式排查方案：校验采样动作源的低频分量对粗粒度动作的影响，规避固定条件下的动作漂移问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有游戏Agent要么直接映射感知上下文到动作，缺失显式世界动态建模，要么仅能基于给定动作预测视觉未来，无法直接作为任务策略使用，WAM在游戏动态开放交互场景下的研究仍属空白。

### 方法关键点
1. 采用并行视觉+动作生成流，基于块因果条件与flow matching，同步生成未来视觉观测与可执行键鼠轨迹；
2. 每步预测gameplay/GUI操作模式，输出模式专属动作分布+连续动作归一化，适配异构原生控制；
3. 长时序交互采用块循环控制：生成超执行horizon的序列，仅执行短动作前缀后重规划，结合跨周期层级历史保证时序连续性。

### 关键结果
实验达成与对比Agent相当的任务成功率，原生动作执行数量低于对比方案；同时发现生成式控制的LASI故障模式：固定条件下采样动作源的低频分量会系统性引导粗粒度相机运动，存在源敏感缺陷。
