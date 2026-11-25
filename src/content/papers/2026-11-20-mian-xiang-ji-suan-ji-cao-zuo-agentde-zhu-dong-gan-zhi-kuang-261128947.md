---
title: 'Don''t Sleep, Keep Watch: Proactive Perception for Computer-Use Agents'
title_zh: 面向计算机操作Agent的主动感知框架NightWatch
authors:
- Jiaqi Su
- Jie-Jing Shao
- Yichen Liu
- Long-Kai Huang
- Haiyan Yin
affiliations:
- National University of Singapore
- A*STAR Centre for Frontier AI Research
- SenseTime
- Hong Kong Baptist University
arxiv_id: '2611.28947'
url: https://arxiv.org/abs/2611.28947
pdf_url: https://arxiv.org/pdf/2611.28947
published: '2026-11-20'
collected: '2026-11-25'
category: Agent
direction: 计算机操作Agent · 主动感知优化
tags:
- Computer-Use Agent
- Proactive Perception
- VLM
- Lightweight Model
- Event Trigger
one_liner: 提出无需修改原有Agent的即插即用轻量主动感知框架，解决感知动作延迟导致的状态过时问题
practical_value: '- 大小模型分层架构可直接复用：核心推理用大VLM，用<1B参数轻量小模型做实时状态监控，latency和算力成本远低于全链路大模型，适合电商导购Agent、商家后台操作Agent等场景的实时性优化

  - 即插即用的感知干预逻辑无需改造存量Agent：仅在Agent外部新增感知层，做中断推理、作废失效动作、提前唤醒三类干预，不修改原有模型、prompt、动作空间，业务改造成本极低

  - 后向标注的界面稳定判断方法可迁移：用未来帧的变化作为黄金标签判断界面是否加载完成，无需人工标注语义，可直接用于电商详情页加载判断、直播界面状态检测等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前基于VLM的计算机操作Agent（CUA）采用定时截图的被动感知逻辑，VLM高推理延迟叠加界面动态变化，导致严重的感知-动作gap：观察状态在动作执行前已过时、固定等待时间过长造成资源浪费、界面突变导致动作失效，静态基准的高成功率在真实动态场景下大幅下降。

### 方法关键点
- 分层即插即用架构：大VLM负责核心任务推理，0.8B参数的轻量System-1模型NightWatch-0.8B做界面流监控，不修改原有Agent的模型、prompt、动作空间，可直接接入存量系统
- 三类事件触发干预：根据监控结果触发三类操作：推理过程中出现弹窗/页面切换等突变时中断推理重新观察、动作执行前目标消失/被遮挡时作废动作重新决策、界面加载完成立刻唤醒Agent代替固定等待
- 训练优化：采用后向标注（用未来N秒无变化定义界面稳定）结合教师模型标注、合成稀有事件数据训练小模型，不需要使用下游基准数据，泛化性强

### 关键结果
在OSWorld-Verified桌面环境、DynaCU-Bench动态Web环境测试，对比定时感知、被动监控基线：
1. OSWorld上非推理耗时降低33%，无效耗时降低53%，任务成功率与原有Agent持平（68.0% vs 66.3%）
2. 动态场景DynaCU-Bench上，大VLM底座的任务成功率从39.5%提升至44.2%，非推理耗时比被动监控基线低35%
3. 0.8B小模型效果优于30倍参数的System-1决策模型，额外Agent API成本仅增加3%

> 最值得记住的一句话：感知的时机和感知的内容一样重要，动态场景下Agent的感知调度效率对整体性能的影响远超过模型本身的推理能力
