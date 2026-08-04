---
title: 'AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter
  Optimizers'
title_zh: AgentHPOBench：面向LLM Agent序列超参数优化的评估基准
authors:
- Tianyu Huai
- Tingshuo Fan
- Xinchi Chen
- Yining Zheng
- Yuxin Wang
- Shuang Chen
- Jie Zhou
- Xuanjing Huang
affiliations:
- Fudan University
- Shanghai Innovation Institute
- East China Normal University
- OpenMOSS
arxiv_id: '2607.29626'
url: https://arxiv.org/abs/2607.29626
pdf_url: https://arxiv.org/pdf/2607.29626
published: '2026-07-31'
collected: '2026-08-04'
category: Agent
direction: Agent能力评估 · 超参数优化基准
tags:
- LLM Agent
- Hyperparameter Optimization
- Benchmark
- Sequential Decision Making
- HPO
one_liner: 构建含30个可执行ML任务的基准，量化LLM Agent基于实验反馈的迭代调优能力
practical_value: '- 推荐/广告模型调优Agent可复用该基准的交互框架，将历史指标、运行日志、合法调参空间结构化喂给Agent，减少无效调参尝试

  - 可借鉴MBNS、BWR、MAA三个指标，量化调参Agent相对基线的提升、胜场率、对标SOTA的达成度，避免单一指标的评估偏差

  - 序列调优时必须给Agent提供完整中间实验反馈（指标+日志），实验证明去掉中间反馈会使调优效果下降约65%，禁止让Agent做盲搜索

  - 资源有限场景下优先在前2-3步调用强Agent产出候选配置，大部分Agent前2步提升最明显，后续易出现性能波动，可搭配传统HPO做精细调优'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent基准多聚焦静态代码生成、论文复现，传统HPO基准又抽象掉了仓库日志、执行上下文，无法评估Agent基于真实实验反馈迭代调参的能力，这是AI科研Agent落地的核心能力缺口，因此需要专门的基准体系。

### 方法关键点
- 覆盖NLP、CV、时序预测、图学习、RL、LLM、结构化学习7个领域共30个可执行ML任务，每个任务提供官方基线、目标metric、限定调参空间、论文/仓库锚点性能；
- 统一执行框架：自动验证Agent提出的配置合法性、执行实验、记录所有历史配置、指标、日志，每次迭代Agent可获取全部历史反馈后输出下一轮配置；
- 设计3个互补评估指标：MBNS（相对于基线的归一化提升，范围-1~1）、BWR（基线胜场率，即超过基线的任务占比）、MAA（锚点达成率，即达到仓库报告SOTA的比例）。

### 关键实验结果
在5次调参迭代、10%训练预算的设置下，对比12个主流Agent与3种传统HPO基线：Claude Sonnet 4.6表现最优，MBNS达0.407、BWR76.7%、MAA79.5%；开源模型中Qwen3-32B最优，MBNS0.148、BWR60%；传统HPO方法整体弱于头部Agent，随机搜索BWR仅48.9%；去掉中间反馈后Qwen3-32B的MBNS下降65%至0.052。

**最值得记住的一句话**：当前LLM Agent已经具备基础实验调优能力，但跨域稳定性、持续迭代保留收益的能力仍有明显短板，给Agent提供完整中间实验反馈是序列调优效果的核心保障。
