---
title: 'CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance'
title_zh: CarryOn：面向个性化可靠机器人辅助的双环管控框架
authors:
- Zixuan Wang
- Yuqi Liu
- Yuxin Chen
- Sengqiao Yang
- Jinhui Ye
- Pengguang Chen
- Changsheng Lu
- Shu Liu
- Bei Yu
- Jiaya Jia
affiliations:
- HKUST
- CUHK
- SmartMore
arxiv_id: '2610.21453'
url: https://arxiv.org/abs/2610.21453
pdf_url: https://arxiv.org/pdf/2610.21453
published: '2026-10-14'
collected: '2026-10-18'
category: Agent
direction: 具身Agent 个性化规划与执行可靠性优化
tags:
- VLA
- Personalized Agent
- Dual-Loop Control
- Embodied AI
- Execution Reliability
one_liner: 提出双环管控架构增强冻结VLA模型，实现机器人辅助任务的个性化适配与高可靠执行
practical_value: '- 双环（规划+执行）架构可复用在电商导购Agent场景：规划环维护用户持久偏好+场景上下文做个性化任务拆解，执行环做话术/动作风险校验，避免违规内容输出

  - 执行失败后的可复用恢复技能+失败反思优化机制，可迁移到推荐系统的负反馈闭环：召回/排序结果触发用户负反馈时自动调用预设兜底策略，同时迭代优化召回逻辑

  - 冻结基座模型+外挂管控层的设计思路，可降低业务侧大模型Agent的迭代成本，不需要反复微调基座，仅调整外挂的记忆、校验、恢复模块即可适配不同业务场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
通用VLA模型已支持开放世界操作，但落地真实场景存在两大核心短板：一是任务拆解仅能输出通用方案，无法对齐用户持久偏好；二是无主动安全校验与失败恢复机制，执行可靠性不足。

### 方法关键点
提出双环架构增强冻结VLA策略：
1. 规划环持久化存储用户偏好、场景上下文，结合新观测与交互迭代更新，支持跨对话、跨场景的个性化任务选择与执行对齐；
2. 执行环主动监督策略输出，拦截预测到的危险动作；执行失败时调用可复用的恢复技能，基于历史失败反思迭代技能效果。

### 关键结果
真实机器人与仿真实验显示：相比已做安全微调的VLA，违规率从52.6%降至6.1%，失败恢复成功率从13%提升至80%，可跨用户、跨场景输出符合偏好的子任务序列
