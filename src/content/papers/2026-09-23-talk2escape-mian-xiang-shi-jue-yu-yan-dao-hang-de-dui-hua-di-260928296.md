---
title: 'Talk2Escape: Conversational Grounding for Vision-and-Language Navigation'
title_zh: Talk2Escape：面向视觉语言导航的对话接地交互框架
authors:
- Zerui Li
- Sihao Lin
- Yanyan Shao
- Jiwen Zhang
- Xiangyu Shi
- Shijie Li
- Qi Wu
arxiv_id: '2609.28296'
url: https://arxiv.org/abs/2609.28296
pdf_url: https://arxiv.org/pdf/2609.28296
published: '2026-09-23'
collected: '2026-09-27'
category: Agent
direction: 视觉语言导航Agent 闭环交互优化
tags:
- VLN
- Multimodal
- Agent
- Human-in-the-loop
- Closed-loop
one_liner: 提出模型无关的主动对话干预框架，通过闭环交互提升视觉语言导航鲁棒性与成功率
practical_value: '- 可复用「异常触发+主动问询」的闭环Agent设计范式，解决推荐/导购Agent执行路径偏离、意图理解模糊时的错误恢复问题

  - 模型无关的外挂干预模块设计思路，无需改造原有基座模型，仅通过轻量监控模块即可提升系统鲁棒性，适合业务快速迭代

  - 多反馈源兼容设计（算法oracle/人在回路）可直接迁移到电商导购Agent，复杂场景下自动切换系统兜底/人工介入流程'
score: 5
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有视觉语言导航（VLN）采用单点开环范式，无内置错误恢复机制，感知混淆、传感器噪声、里程计漂移等问题会导致误差累积，最终引发任务失败，真实场景落地泛化性差。
### 方法关键点
1. 推出模型无关的主动对话干预框架Talk2Escape，将导航重构为闭环交互流程
2. 内置轻量视觉语言模块实时监控Agent运动状态，检测到局部绕路、轨迹严重偏离时，将第一视角观测转化为简洁接地查询，向算法oracle或人在回路请求定向矫正反馈
### 关键结果
在R2R-CE、RxR-CE、VLNVerse等高保真模拟器上对各类基座Agent均有稳定提升，R2R-CE数据集上成功率达66.0%，优于现有监督及零样本SOTA；在Unitree Go2四足机器人上完成仿真到真实环境的迁移验证，主动对话可显著提升物理环境下导航鲁棒性
