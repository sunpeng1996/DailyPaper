---
title: A computational framework for understanding embodied plans
title_zh: 理解具身规划的计算框架
authors:
- Aalap D. Shah
- Basil Saeed
- Joshua B. Tenenbaum
- Tobias Gerstenberg
- Hyowon Gweon
- Ilker Yildirim
affiliations:
- 耶鲁大学心理学系
- 耶鲁大学吴蔡研究所
- 斯坦福大学心理学系
- 斯坦福大学统计系
- 麻省理工学院脑与认知科学系
arxiv_id: '2611.13669'
url: https://arxiv.org/abs/2611.13669
pdf_url: https://arxiv.org/pdf/2611.13669
published: '2026-11-10'
collected: '2026-11-12'
category: Agent
direction: 具身Agent · 长时序规划推理
tags:
- Embodied-Agent
- Embodied-Planning
- Intuitive-Physics
- Generative-Model
- Long-Horizon-Reasoning
one_liner: 融合直观物理仿真的GenEA具身Agent，可推理长时序具身规划，效果优于各类强基线
practical_value: '- 电商场景具身导购Agent开发可参考多层状态空间设计，融合人体动作、商品交互物理规则做长程交互规划，提升导购自然度

  - 做用户消费意图推理时可借鉴「目标+规划」联合概率建模思路，从用户多步交互动作反推真实需求，优化推荐准确率

  - LLM做具身任务效果不佳时，可参考将任务运动规划框架与仿真物理规则结合的trick，补足LLM的物理常识短板'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
从人类动作反推其计划与目标是人机协作具身AI的核心基础能力，但自然具身场景下的该能力形式化建模是长期未解决的挑战。
### 方法关键点
GenEA新型智能体表征核心为多层状态空间：将铰接体粗粒度生物力学、与周边物体的交互逻辑耦合，在机器人领域任务与运动规划框架基础上，引入仿真驱动的直观物理模块；将该状态空间嵌入生成模型，可输出目标与具身规划的联合概率分布。
### 关键结果
在物体操作、导航两个跨域实验中，GenEA可复现人类对具身规划的推理逻辑，效果全面优于启发式方法、标准任务与运动规划、SOTA视觉语言模型等强基线。
