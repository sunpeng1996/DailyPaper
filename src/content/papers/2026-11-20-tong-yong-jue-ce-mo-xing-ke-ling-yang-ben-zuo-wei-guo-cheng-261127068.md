---
title: Decision Models Are General-Purpose Process Reward Models
title_zh: 通用决策模型可零样本作为过程奖励模型用于Agent RL步级信用分配
authors:
- Jiajun Fan
- Qinglong Zheng
- Ziwen Wang
- Bangji Yang
- Neil He
- Ruihan Guo
- Chaoran Cheng
- Ge Liu
affiliations:
- UIUC
- NYU
- Yale
arxiv_id: '2611.27068'
url: https://arxiv.org/abs/2611.27068
pdf_url: https://arxiv.org/pdf/2611.27068
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: Agent RL训练 · 步级信用分配
tags:
- PRM
- Reinforcement Learning
- Policy Gradient
- LLM Agent
- Credit Assignment
one_liner: 零样本复用通用决策模型作为PRM，无需标注/微调/critic，即插即用提升各类策略梯度方法的Agent训练效果
practical_value: '- 电商导购Agent、搜索推荐多轮交互Agent训练可直接复用DM-PRM思路：无需标注步级数据，仅针对业务场景设计1条yes/no进度判断问题，即可获得步级奖励信号，大幅降低RL训练冷启动成本

  - 可将DM-PRM作为插件接入现有业务用的GRPO/PPO等策略梯度训练框架，无需改动原有训练逻辑，仅在优势计算环节叠加标准化后的决策模型打分即可提升训练效率和效果

  - 业务落地前可先做首迭代校验：统计各动作类型的平均打分，若核心目标动作（如下单、点击）平均打分低于整体均值，需改用同类动作内做标准化的baseline，避免训练出偏好无意义浏览的Agent

  - 若没有商用决策模型API，可微调小参数LLM做专用二分类决策模型，成本远低于训练全量PRM或调用大模型做judge，适合业务规模化落地'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有语言Agent RL训练依赖episodic级奖励，步级信用分配长期是核心痛点：GRPO等方法所有步共享同一个奖励，当所有rollout都失败时完全没有训练信号；critic类方法需要额外训练价值网络，训练不稳定且成本高；标注PRM依赖领域步级标注泛化性差，LLM judge成本高、速度慢，无法适配规模化训练需求。

### 方法关键点
- 提出DM-PRM：零样本调用通用二分类决策模型，每个步仅询问1个固定问题「该步是否推动了任务进展」，直接获得0-1的概率打分，无需微调、步级标注或额外训练critic
- 打分标准化后作为步级信用叠加到原有策略梯度方法的优势项上，可即插即用接入GRPO、GiGPO、GraphGPO等任意策略梯度方法，不改动原有训练逻辑
- 针对不同场景适配标准化策略：若核心完成动作的平均打分高于整体均值，用全量步均值做baseline；若低于（如电商场景下新手Agent下单错误率高导致下单动作打分低），则仅在同类型动作内做标准化，避免Agent偏好无意义浏览动作

### 关键结果
在ALFWorld（家居任务）和WebShop（电商购物任务）两个Benchmark上测试，base模型为Qwen2.5-1.5B：
- ALFWorld上，DM-PRM+GRPO比原生GRPO成功率高23.7个百分点（seen环境）、29.2个百分点（unseen环境），达到90%、92.9%的成功率，超越SOTA的GiGPO、GraphGPO
- WebShop上，DM-PRM+GRPO比原生GRPO成功率高13.1个百分点，达到72.2%，训练速度快一倍，仅需一半迭代就能达到原生GRPO的最终效果
- 叠加DM-PRM后GiGPO、GraphGPO的效果也均有提升，最优的DM-PRM+GraphGPO在WebShop上成功率达75.9%，超过所有基线方法

**最值得记住的一句话：语言Agent的步级信用不需要学习，直接问就可以得到**
