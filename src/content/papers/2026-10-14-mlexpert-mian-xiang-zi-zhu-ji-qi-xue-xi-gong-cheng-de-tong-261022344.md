---
title: 'MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning
  Engineering'
title_zh: MLExpert：面向自主机器学习工程的通用Agent模型
authors:
- Shangheng Du
- Jinxin Shi
- Shuaiyu Zhang
- Yiming Wu
- Junpeng Zhao
- Shiyang Feng
- Xin Li
- Liang He
- Xiangchao Yan
- Bo Zhang
affiliations:
- East China Normal University
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.22344'
url: https://arxiv.org/abs/2610.22344
pdf_url: https://arxiv.org/pdf/2610.22344
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 通用Agent · 长时序决策训练
tags:
- Agent
- MoE
- SFT
- Reinforcement Learning
- Long-Horizon
one_liner: 35B MoE Agent模型MLExpert，经分层SFT+WIRL训练，在MLE任务上性能追平更大规模前沿模型
practical_value: '- 分层SFT的outcome-guided轨迹筛选方法可直接复用在推荐/广告Agent训练中，仅保留达到效果阈值的轨迹片段做监督，过滤长序列中的无效决策噪声，降低标注成本

  - WIRL窗口式RL方案可迁移到电商长周期优化场景（如广告投放策略迭代、推荐链路调优），按反馈节点拆分执行窗口绑定共享奖励，无需等待全链路结束即可更新策略，大幅降低训练延迟

  - 异步采样加token级策略修正的方案可解决在线RL优化推荐/广告策略时的策略漂移问题，提升异步更新的稳定性和效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于预定义工作流的MLE Agent高度依赖人工编写的控制逻辑，长时序优化任务难以获取高质量监督信号，且实验反馈滞后导致传统RL更新效率极低，亟需可自主规划实验、从中间反馈高效学习的Agent训练方案。

### 方法关键点
- 搭建Kaggle-MLE Factory，自动将历史Kaggle竞赛转化为标准化可执行MLE训练任务，配套支持模型自主决策的交互Harness，存储实验状态并提供完整工具集
- 分层Agentic SFT：第一阶段用通用编码/工具调用轨迹做基础能力训练，第二阶段用MLE领域高质量轨迹做域适应，通过执行结果自动过滤轨迹中效果退化的尾部片段
- Windowed Interaction RL（WIRL）：将两次实验结果之间的多轮决策作为执行窗口，绑定共享的结果奖励，支持异步窗口收集加token级策略修正，无需等待全轨迹结束即可完成策略更新

### 关键实验结果
在MLE-Bench Lite（22个Kaggle任务）上，MLExpert（35B MoE）将基模型的平均奖牌率从37.9%提升至72.7%，性能追平GLM-5.3、Kimi-K3等更大规模前沿模型；WIRL相比传统GRPO将训练等待率从87.6%降至39.3%，大幅提升训练效率。在NatureBench Lite上，Surpass-SOTA率从基模型的0%提升至50%，优化能力可迁移到Agent脚手架优化、算法组件优化等跨领域任务。

### 核心结论
长时序优化决策能力是可训练的模型能力，通过分层SFT+窗口式RL，35B规模模型即可达到更大前沿模型的Agent任务性能
