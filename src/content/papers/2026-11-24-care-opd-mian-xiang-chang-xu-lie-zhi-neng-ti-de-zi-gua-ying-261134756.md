---
title: 'Collect for Coverage, Replay with Evidence: Adaptive and Efficient On-Policy
  Distillation for Long-Horizon Agents'
title_zh: CARE-OPD：面向长序列智能体的自适应高效同策略蒸馏框架
authors:
- Haowen Hou
- Gen Li
- Ruilin Li
- Yicheng Liu
- Zhen Huang
- Shuai Dong
- Congcong Wang
- Kaiwen Tuo
- Hongrui Wu
- Zelin Peng
affiliations:
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- JD.com
arxiv_id: '2611.34756'
url: https://arxiv.org/abs/2611.34756
pdf_url: https://arxiv.org/pdf/2611.34756
published: '2026-11-24'
collected: '2026-11-26'
category: Agent
direction: 长 horizon Agent · On-Policy 蒸馏优化
tags:
- On-Policy Distillation
- Long-Horizon Agent
- Prefix Replay
- Knowledge Distillation
- Training Efficiency
one_liner: 提出CARE-OPD前缀重放蒸馏框架，大幅降低长horizon Agent训练成本同时提升任务效果
practical_value: '- 训练多轮交互类Agent（电商导购、搜索多轮、长会话推荐Agent）时，可直接复用前缀重放架构，将环境交互与模型更新解耦，无需等待长rollout完成即可做批量更新，大幅降低训练端到端耗时

  - 「学生种子轨迹+置信度门控」的样本构造trick可直接迁移：混入10%左右的学生/真实用户行为前缀，再过滤batch内10%置信度最低的样本，既能覆盖真实场景下的异常交互状态，又避免低质量老师信号误导训练

  - 事后重放分配方法可复用：放弃按交互轮次位置加权的传统策略，基于全轨迹执行结果（比如电商场景的下单、加购结果）回溯筛选高价值决策轮次，将训练算力集中在影响最终转化的关键轮次，降低训练成本

  - 工程上可复用KV cache复用技巧：做轨迹价值判断时直接复用rollout阶段已生成的轨迹KV cache，几乎不增加额外推理开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长horizon Agent的在线On-Policy Distillation（OPD）依赖实时环境rollout生成训练样本，在多轮交互场景下，不同轨迹的执行耗时差异大，同步训练等待成本高、异步训练易引入stale策略数据，整体训练效率极低。现有前缀重放优化方案仅依赖教师模型生成轨迹，无法覆盖学生模型自身行为诱导的历史状态，且固定按轮次位置衰减的重放策略无法捕捉长轨迹中任意位置出现的高价值决策，导致效果显著弱于在线OPD。

### 方法关键点
- 可靠性控制的历史覆盖：按α比例（默认0.1）混入学生种子生成的前缀轨迹，学生生成前Ki轮后由教师补全剩余轨迹，覆盖学生实际运行中可能遇到的非教师分布状态；新增响应级置信度门控，计算教师对学生当前响应的平均top1 token概率，过滤每个batch中置信度最低的γ比例（默认0.1）样本，过滤低质量监督信号。
- 事后重放分配：轨迹收集完成后，复用教师的轨迹KV cache，基于全轨迹执行结果和下游反馈筛选出r比例（默认0.4）有证据支撑的高价值决策轮次，仅对这些轮次做重放训练，避免算力浪费在无学习价值的常规交互步骤上。

### 关键实验
在SWE-bench Verified软件工程任务、BrowseComp-Plus深度研究任务上测试，对比异步在线OPD、vanilla前缀重放、ReOPD等基线：
1. SWE-bench任务：CARE-OPD成功率达59.5%，比异步在线OPD高2.4pct，端到端训练时间降低45%，环境交互次数减少44%；
2. BrowseComp-Plus任务：准确率达49.6%，比在线OPD高2.4pct。

### 核心结论
长序列Agent的蒸馏训练无需追求全量在线交互，通过合理的历史覆盖设计和高价值决策筛选，前缀重放可以在成本远低于在线OPD的情况下取得更优效果。
