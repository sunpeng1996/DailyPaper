---
title: 'Atria Dawn: The Dawn of Agentic Superintelligence'
title_zh: Atria Dawn：面向科研工程的智能体大模型与人机协作演化研究
authors:
- Honglin Guo
- Tao Gui
- Yicheng Chen
- Guanting Dong
- Qiming Ge
- Yuyang Hu
- Zixian Huang
- Jiajie Jin
- Alexander Lam
- Yining Li
affiliations:
- 复旦大学
- Atria Team
arxiv_id: '2609.15818'
url: https://arxiv.org/abs/2609.15818
pdf_url: https://arxiv.org/pdf/2609.15818
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: Agent大模型 · 人机协作模式演化
tags:
- Agent
- MoE
- Human-AI Collaboration
- LLM
- Agent Benchmark
one_liner: 提出744B参数MoE架构的科研工程智能体大模型，实证人机协作向项目级伙伴关系的转型
practical_value: '- 训练业务域智能体时可复用Verifiable Experience Pipeline，将工具调用轨迹和可验证的外部结果绑定，过滤无效样本，提升搜索推荐策略迭代、广告素材生成等任务的执行准确率

  - 人机协作可采用「AI提方案、人类做决策」的分工模式：比如推荐系统AB实验设计、选品策略迭代场景，让Agent生成候选方案，人类把控目标和验收标准，大幅提效

  - 智能体执行出错时优先通过补充上下文、明确需求引导其自行修复，而非直接接管，可降低推荐/广告系统自动化运维、用户反馈处理等场景的人力成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI智能体已能胜任代码生成、实验执行等单一任务，但真实研发场景中人与AI的职责分工、协作模式尚未被系统性实证研究，同时面向科研工程场景的通用智能体大模型能力仍有提升空间，亟需明确智能体能力边界和人机协作的演化方向。

### 方法关键点
- 模型底座：基于744B参数MoE架构开发Atria Dawn Preview智能体大模型
- 训练流程：采用Verifiable Experience Pipeline，每个训练任务绑定真实执行环境，仅保留包含任务轨迹、输出产物、外部验证证据的有效样本用于训练，同时基于失败案例迭代优化任务和环境设计
- 实证研究：以Atria Dawn自身研发过程为案例，分析769条来自56名参与者的任务记录和智能体日志，量化人机协作的职责分配

### 关键实验结果
在16个涵盖工具调用、科研搜索、软件工程、网络安全等领域的基准上与DeepSeek V4 Pro、Qwen 3.8 Max、GPT 5.6 sol等前沿模型对比，拿下5个基准的最优成绩，其中AutomationBench领先第二名4.1分，BFCL v4领先2.9分，CyberGym领先2分。实证数据显示：96.5%的研发任务用到AI辅助，33.2%的任务被认为无AI无法完成，方法参数决策中55.4%为「AI提议、人类选择」模式，人类掌握85.5%的最终决策权。

### 最值得记住的一句话
智能体的普及不会替代人类的决策角色，而是将人类精力从执行层解放，集中到判断什么方向值得探索、如何用证据引导研究的更高价值环节。
