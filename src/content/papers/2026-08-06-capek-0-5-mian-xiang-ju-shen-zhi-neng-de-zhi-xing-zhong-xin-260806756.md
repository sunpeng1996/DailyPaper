---
title: 'Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence'
title_zh: Capek 0.5：面向具身智能的执行中心型视觉语言模型
authors:
- Ying Chen
- Weizhen Li
- Zhe Hu
- Zhenjiang Li
- Rui Jiang
- Zhifeng Gu
- Lihuang Fang
- Jiangping Liu
- Lei Yi
- Jie Chen
affiliations:
- XPENG ROBOTICS
arxiv_id: '2608.06756'
url: https://arxiv.org/abs/2608.06756
pdf_url: https://arxiv.org/pdf/2608.06756
published: '2026-08-06'
collected: '2026-08-10'
category: Agent
direction: 具身Agent · 多模态能力融合训练
tags:
- Embodied Agent
- Vision-Language Model
- Reinforcement Learning
- Model Merging
- Knowledge Distillation
one_liner: 提出按执行功能划分的四能力族训练融合方案，构建性能更优的统一具身视觉语言模型Capek 0.5
practical_value: '- 多任务能力融合可迁移到电商导购Agent：按业务执行链路（用户理解/商品匹配/话术生成/效果校验）拆分能力族，分别训练后做权重+蒸馏融合，避免多任务冲突

  - 训练范式可复用：用可验证的强化学习奖励训练专项能力小模型，再合并到统一基座，比直接多任务训练的能力保留度更高，适合复杂业务Agent迭代

  - 能力校验思路可借鉴：给Agent不同执行阶段的能力单独设计验证benchmark，可快速定位线上Agent能力短板，降低迭代成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有具身VLM按孤立任务目标训练，各能力未围绕执行流程统一组织整合，难以适配机器人执行的迭代式感知-推理-校验需求。

### 方法关键点
1. 提出执行中心的能力分类法，将具身能力划分为空间推理、时序理解、动作引导、状态校验4个功能族；
2. 共享基座上用带可验证奖励的RL训练各能力的专用专家模型；
3. 先做权重空间合并，再做路由策略蒸馏，得到单checkpoint的推理统一模型。

### 关键结果数字
2B/35B两个规模版本在绝大多数基准项上优于初始化基线，4项专项能力合并后损失可量化控制，模拟闭环具身任务迁移性达标，自建Capek-StateBench基准上通用能力得分达82.9%。
