---
title: 'AutoEnvScaling: Automating the Data Flywheel with Terminal Agents'
title_zh: AutoEnvScaling：基于终端Agent的RL训练环境自动生成数据飞轮
authors:
- Simon Yu
- Baolin Peng
- Bo Liu
- Zhengyan Shi
- Zhaoyang Wang
- Hao Cheng
- Qianhui Wu
- Wenlin Yao
- Natasha Jaques
- Weiyan Shi
affiliations:
- Northeastern University
- Microsoft
- Stanford University
- University of Washington
- University of North Carolina at Chapel Hill
arxiv_id: '2610.14163'
url: https://arxiv.org/abs/2610.14163
pdf_url: https://arxiv.org/pdf/2610.14163
published: '2026-10-08'
collected: '2026-10-14'
category: Agent
direction: Agent 训练环境自动生成与自进化
tags:
- Terminal Agent
- Reinforcement Learning
- Data Flywheel
- Recursive Self-Improvement
- Environment Generation
one_liner: 将环境设计转化为终端任务，实现RL训练环境自动生成与模型递归自进化
practical_value: '- 可迁移数据飞轮思路到推荐系统冷启动：用现有推荐模型的bad case引导Agent自动生成个性化训练样本，降低人工标注成本

  - 训练样本验证校准逻辑可复用：给生成样本设置0.25~0.75的通过率区间，过滤过难/过易样本，提升RL训练效率

  - 跨角色共享模型权重思路可借鉴：让同一个LLM同时承担训练样本生成和下游任务执行角色，降低多模型部署成本

  - 弱模型能力放大方案可复用：给弱模型配带执行、校验能力的sandbox harness，提升生成样本合格率，降低对强基座的依赖'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
终端Agent的RL训练依赖大量适配当前模型能力的高质量环境，现有环境多靠人工设计，成本高、迭代慢，是Agent性能提升的核心瓶颈；纯LLM prompt生成环境的合格率极低，无法满足大规模训练需求。

### 方法关键点
- 将环境设计转化为终端任务：proposer Agent在sandbox中基于solver的失败rollout，自动编写、调试、验证完整的Harbor训练环境，支持web访问、子沙箱测试
- 双校验机制：生成环境先过validation（参考解全过、空解通过率<50%、无benchmark污染），再通过calibration（当前solver通过率在0.25~0.75之间）才进入训练池
- 数据飞轮闭环：solver在新环境训练后的新rollout反馈给proposer，引导下一轮环境生成；支持单模型同时承担proposer和solver角色，实现双角色共进化
- 双奖励机制：solver奖励为测试用例通过率，proposer奖励根据环境校验结果分级设置，用DPPO算法联合训练两个角色

### 关键实验
对比纯prompt生成、prompt+环境反馈两类基线，测试8款前沿基座模型，核心结果：有效环境生成率最高提升25×，单有效环境成本最高降低75%；用GPT-5.6-sol生成的环境训练Qwen3.5-35B-A3B，Terminal-Bench 2.1得分比静态Tmax基线高4.3分；单模型双角色自进化场景下，Qwen3.6-35B-A3B的Terminal-Bench 2.1得分提升12.2分，4.0版本得分从1.6涨到3.2。

### 核心结论
给Agent配好可执行、可校验的harness，弱模型也能生成高质量训练数据，实现不需要人工介入的递归自进化。
