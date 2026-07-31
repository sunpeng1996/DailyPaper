---
title: 'Qwen-UI-Agent Technical Report: Toward Next-Generation Real-World Centric
  Foundation GUI Agents'
title_zh: Qwen-UI-Agent技术报告：面向真实场景的下一代基础GUI智能体
authors:
- Hanzhang Zhou
- Panrong Tong
- Xu Zhang
- Quyu Kong
- Chenglin Cai
- Tianyu Xia
- Gongjie Zhang
- Jianan Zhang
- Long Li
- Long Chen
affiliations:
- Alibaba Group
- MAI-UI Team
arxiv_id: '2607.28227'
url: https://arxiv.org/abs/2607.28227
pdf_url: https://arxiv.org/pdf/2607.28227
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: GUI智能体 · 跨平台真实场景落地
tags:
- GUI-Agent
- Cross-Platform
- Real-Device
- Reinforcement-Learning
- Data-Flywheel
one_liner: 打造跨移动端、桌面、网页的真实场景基础GUI Agent，性能超越GPT-5.6 Sol等前沿模型
practical_value: '- 可复用混合GUI+CLI+批量化动作空间设计，在电商运营类Agent中融合界面操作与脚本执行，大幅降低长链路任务耗时，适配商品上下架、订单批量处理等场景

  - 落地真实设备Agent时可参考健康感知调度器+虚拟多屏方案，用少量物理设备支撑大规模训练/推理，同时通过环境故障自动隔离避免无效训练样本

  - Agent能力迭代可复用AutoResearch风格数据飞轮，用Agent自动生成任务、诊断失败、生成针对性训练数据，减少人工标注成本，适配高频迭代的电商场景Agent'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI Agent大多针对模拟benchmark优化，存在严重的仿真到真实场景的性能落差，无法支撑跨平台长链路任务、混合交互需求，也难以低成本迭代能力，距离真实落地有显著差距。
### 方法关键点
- 环境层：构建万级并发沙箱+百台真实设备集群的混合环境，覆盖移动端、桌面、网页、DeepSearch全场景，统一GUI+CLI+API的混合动作空间，支持单轮生成批量化动作
- 数据层：实现AutoResearch风格Agent驱动的数据飞轮，自动完成任务生成、环境构造、失败诊断、迭代规划，大幅降低人工参与度
- 训练层：采用领域专家模型合并+滑动窗口长轨迹SFT，叠加Action RL修正局部动作错误、Online RL优化长链路决策，支持超过100步的轨迹训练
- 架构层：新增轻量harness层，支持基于通知的主动服务触发、跨平台任务状态流转
### 关键结果
对比GPT-5.6 Sol、Claude Opus 4.8、Gemini 3.1 Pro等前沿模型，移动端MobileWorld-Real基准准确率达92.2%，超竞品最高6个百分点；桌面端OSWorld-Verified准确率达79.5%，浏览器端WebArena准确率达73.6%，均处于领先水平。
最值得记住的一句话：GUI Agent落地的核心瓶颈不在单模型能力，而在真实场景环境基建、低成本数据迭代飞轮以及跨场景能力整合的系统性设计。
