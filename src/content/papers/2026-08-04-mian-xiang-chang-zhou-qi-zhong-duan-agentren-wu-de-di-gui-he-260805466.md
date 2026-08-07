---
title: Recursive Synthesis for Long-Horizon Terminal Tasks
title_zh: 面向长周期终端Agent任务的递归合成框架
authors:
- Zhongzhi Li
- Yucheng Shi
- Zongxia Li
- Ruhan Wang
- Anhao Li
- Zixun Huang
- Junyao Yang
- Lei Ke
- Ninghao Liu
- Haitao Mi
affiliations:
- Tencent HY LLM Frontier
- University of Georgia
- University of Maryland, College Park
- University of Pennsylvania
- University of Minnesota, Twin Cities
arxiv_id: '2608.05466'
url: https://arxiv.org/abs/2608.05466
pdf_url: https://arxiv.org/pdf/2608.05466
published: '2026-08-04'
collected: '2026-08-07'
category: Agent
direction: Agent长周期任务合成与自训练
tags:
- Agent
- Long-Horizon Task
- Recursive Synthesis
- SFT
- PPO
- Synthetic Data
one_liner: 提出RST递归验证合成框架，低成本规模化生成可训练的长周期终端Agent任务
practical_value: '- 可复用RST的「种子任务→扩展解决方案→对齐验证器/指令→沙箱验证→回退为新种子」递归合成范式，低成本生成电商客服、运营自动化、商家工具等场景长周期Agent的训练任务，解决人工标注成本高的痛点

  - 任务合成时优先落地「参考方案可执行+验证器与公开指令完全对齐」双校验规则，避免生成无效训练数据，可直接迁移到生成式推荐的候选召回/排序训练数据自动合成场景

  - 可参考「难度渐进式递归合成数据+SFT后接PPO」的训练范式，提升导购Agent、用户旅程运营Agent等长周期交互类系统的复杂任务完成率，实验验证相对增益可达20%以上

  - 递归合成时加入多样性控制（领域、算子、血统上限）避免数据坍缩，可复用在推荐系统的训练数据增强环节，保证训练数据分布的多样性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期终端Agent的高质量训练数据生产成本极高，单任务可达数百到数千美元，人工标注无法规模化，LLM直接生成的任务常存在指令、环境、参考方案、验证器不一致的问题，严重制约长周期Agent能力迭代。
### 方法关键点
- 提出RST递归验证合成框架：从已验证的种子任务出发，先扩展参考解决方案生成长工作流，再对齐验证器与公开指令，最终在沙箱中完成有效性校验，通过的任务直接作为下一轮合成种子
- 全流程无人工参与，每轮加入多样性上限控制（父系血统、类别、算子家族、生成队列），避免任务分布坍缩到少数模式
- 生成任务同时支持SFT（收集模型成功执行轨迹做监督微调）与PPO训练（基于内置验证器计算奖励做强化学习）
### 关键结果
- 从639个种子任务出发，15轮递归合成共生成37484个验证通过的终端任务，单任务成本仅约$0.05，较人工标注成本下降超1000倍
- 任务难度随轮次持续提升：R1到R15，参考方案中位数长度从67行增长到374行（5.6×），执行命令中位数从40增长到244（6.1×），DeepSeek-V4-Pro pass@4从90%下降到2.5%
- 用生成数据训练的Qwen3.5-27B，在三个终端Agent基准上，SFT后最高提升10分，PPO训练后相对基准模型分别提升20.0%、41.2%、21.9%
### 核心洞察
递归合成是低成本规模化生成高难度长周期Agent训练数据的可行路径，当前实验未观察到能力天花板
