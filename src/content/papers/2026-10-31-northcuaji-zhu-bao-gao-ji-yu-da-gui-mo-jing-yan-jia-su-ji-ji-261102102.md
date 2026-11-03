---
title: 'NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience
  at Scale'
title_zh: NorthCUA技术报告：基于大规模经验加速计算机操作Agent性能提升
authors:
- Chaoyun Zhang
- Bingxuan Li
- Pinxue Guo
- Yangfan Gao
- Zikun Cai
- Tianci Xie
- Hui Li
- Yuqi Huang
- Yifei Cao
- Bo Mao
affiliations:
- Shanghai Qiji Zhifeng Co., Ltd.
arxiv_id: '2611.02102'
url: https://arxiv.org/abs/2611.02102
pdf_url: https://arxiv.org/pdf/2611.02102
published: '2026-10-31'
collected: '2026-11-03'
category: Agent
direction: 计算机操作Agent 全栈训练与推理优化
tags:
- Computer-Use-Agent
- GUI-Agent
- Experience-Flywheel
- SFT
- Reinforcement-Learning
one_liner: 提出含经验飞轮、执行框架、分阶段学习的全栈系统，开源多尺寸CUA模型达开源SOTA
practical_value: '- 可复用「经验飞轮+分阶段训练」框架：先做大规模单步基础技能预训练，再用验证通过的长轨迹SFT，最后结合GRPO做强化学习闭环，适配电商客服Agent、RPA流程自动化Agent、广告投放自动调优Agent的训练

  - 长上下文交互优化trick：可直接套用动作感知视觉滑窗+任务保留上下文压缩+结构化工作记忆的组合方案，降低长流程Agent的上下文开销、提升关键信息留存率

  - 低延迟推理优化方案：面向高并发CUA场景，可参考Ultrafast版本的动作选择头+LoRA微调方案，在效果损失可控的前提下将Web任务执行速度提升2.3倍

  - 多环境执行框架可复用：NorthCUA Harness的统一Runtime+沙箱隔离执行+批量Rollout调度架构，可直接迁移到电商自动化运营、跨平台内容批量发布类Agent的落地部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前计算机操作Agent（CUA）从单步动作向复杂长流程软件任务落地的核心瓶颈是缺乏将决策与最终结果关联的大规模验证经验，现有方案存在训练数据覆盖不足、执行-评估-训练链路断裂等问题，长流程任务完成率低、推理延迟高，无法满足真实场景自动化需求。
### 方法关键点
- 全栈系统三大核心组件：①NorthCUA Harness 全生命周期执行框架，统一桌面/Web端Agent runtime，内置动作感知视觉滑窗、任务保留型上下文压缩、结构化工作记忆三大长交互优化机制，支持智能体自动评估与高并发批量任务调度
- ②Experience Flywheel 经验生产飞轮，同时生产单步UI定位样本与端到端任务样本，针对难任务通过递归自优化保留已验证技能与里程碑，持续扩充高质量训练数据
- ③Staged Learning 分阶段训练流程：先基于400万+步GUI交互数据做中期训练，再用验证通过的长轨迹做长horizon SFT，最后通过桌面/Web联合GRPO强化学习形成训练闭环
- 低延迟推理优化：面向高并发场景推出Ultrafast版本，基于预RL的Nano模型加动作选择头+LoRA微调，平衡效果与延迟
### 关键结果
在6个主流基准上对比Qwen3.8-Max、Kimi-K3等领先闭源模型：397B参数的NorthCUA-Pro在ScreenSpot-Pro准确率达93.3%、OSWorld-G准确率91.0%、WebArena验证成功率73.9%，所有任务均达开源SOTA，性能超过万亿参数闭源模型；Ultrafast版本Web任务执行速度较全生成方案提升2.3倍。
### 核心结论
CUA的能力提升核心是经验生产与训练的协同设计，通过闭环飞轮持续积累验证过的交互经验，是突破长流程复杂任务性能瓶颈的核心路径。
