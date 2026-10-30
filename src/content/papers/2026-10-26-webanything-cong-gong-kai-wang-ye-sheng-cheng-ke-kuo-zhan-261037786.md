---
title: 'WebAnything: From the Wild Web to Scalable Agent Environments'
title_zh: WebAnything：从公开网页生成可扩展Web Agent运行环境框架
authors:
- Tianci Xie
- Zikun Cai
- Chaoyun Zhang
- Pinxue Guo
- Bingxuan Li
- Rui Zheng
- Hang Yan
affiliations:
- Zhejiang University
- Nanyang Technological University
- Shanghai Qiji Zhifeng Co., Ltd
arxiv_id: '2610.37786'
url: https://arxiv.org/abs/2610.37786
pdf_url: https://arxiv.org/pdf/2610.37786
published: '2026-10-26'
collected: '2026-10-30'
category: Agent
direction: Web Agent 可复用运行环境自动化构建
tags:
- WebAgent
- EnvironmentConstruction
- SFT
- AutomaticReconstruction
- AgentEvaluation
one_liner: 自动从真实URL构建高保真可复用Web Agent训练评估环境，无需单站点人工开发
practical_value: '- 做电商导购/操作类Web Agent的团队，可复用该框架快速复刻目标电商、商家后台等站点，生成隔离可控的训练/评估环境，避免访问真实站点的合规风险、状态不稳定问题，大幅降低环境搭建的人工成本

  - 「独立校验+证据感知修复」的架构可迁移到推荐/广告系统的落地页自动生成、竞品素材复刻场景：如果现有素材足够就做本地修正，素材不足则触发定向爬取，可显著降低人工校验和修复的工作量

  - 从自定义环境中采集交互轨迹做SFT的方案可参考：使用该框架生成的5856条轨迹微调Qwen3.5-9B，Web Agent任务成功率最高提升13.33pp，电商Agent团队可基于自研环境生成专属微调数据，降低真实环境采数的成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Web Agent的训练评估环境存在明显短板：人工镜像需单站点定制开发成本极高，生成式构建和真实站点差异大，录屏回放的交互覆盖范围受限，无法同时满足自动化、源站保真、交互覆盖三个核心需求，直接导致Web Agent训练效果不稳定、评估复现性差。

### 方法关键点
- 采用Explorer-Builder模块，从真实URL自动抓取浏览器可见的页面结构、资源、交互前后的状态变化，构建可执行的本地路由和状态转换逻辑，无需单站点人工开发和调试
- 独立校验模块将待验证的候选环境冻结后，和源站证据、站点契约做对比，区分两类问题：现有证据足够的实现缺陷触发本地修复，证据不足的触发定向重采源站内容，迭代优化直到符合要求
- 生成的环境自带固定初始状态、重置机制、任务评估接口，可自动生成任务和成功判定条件，采集Agent交互轨迹直接用于SFT

### 关键实验结果
- 构建了覆盖14个领域53个类别的244个站点环境，支持12984个可执行任务，单站点平均模型调用成本仅2.63美元
- 和人工辅助构建的WebHarbor对比，三项保真度指标全面领先，盲审结果为12胜2平0负
- 用生成的5856条交互轨迹微调Qwen3.5-9B，REAL任务成功率提升9.9pp，Odysseys-Easy指标提升6.25pp以上，WebArena-Verified整体成功率提升13.33pp

### 最值得记住的一句话
源站保真度决定Agent的观测输入，交互有效性决定Agent的可执行操作，仅靠更高的视觉相似度无法代表更广的功能覆盖
