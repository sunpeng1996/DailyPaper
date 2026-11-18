---
title: 'From Repositories to Training Environments: Scaling Long-Horizon Coding Agents
  with Environment Evolution Loop'
title_zh: RepoFactory：基于环境演化循环规模化构建长时序编码Agent训练环境
authors:
- Yang Tian
- Tianyu Zheng
- Xiyuan Yang
- Yaxin Du
- Chengran Yang
- Bo Zhao
- Jian Yang
- Bryan Dai
affiliations:
- Beihang University
- Shanghai Jiao Tong University
- IQuest Research
arxiv_id: '2611.21152'
url: https://arxiv.org/abs/2611.21152
pdf_url: https://arxiv.org/pdf/2611.21152
published: '2026-11-16'
collected: '2026-11-18'
category: Agent
direction: Agent训练环境自动化构建与优化
tags:
- CodingAgent
- TrainingEnvironment
- EnvironmentEvolution
- LongHorizonTask
- SFT
one_liner: 提出RepoFactory流水线将真实代码仓库转为可验证训练环境，用低成本指标优化长时序编码Agent训练价值
practical_value: '- 做Agent训练时可复用低成本环境演化思路，无需依赖耗时的模型rollout反馈，用「有效性+复杂度+耦合度」三类可快速计算的代理指标迭代优化训练环境/数据集，大幅降低环境构建成本

  - 对于电商场景下的长时序Agent任务（如全链路运营、自动搭建活动页/店铺、智能客服复杂问题处理），可照搬「真实业务案例提取任务规范→可验证环境构建→指标驱动迭代」的流水线，将零散业务案例转为高质量训练素材，提升Agent落地表现

  - SFT数据筛选方案可直接复用：先设置奖励阈值做初筛，再通过规则校验工具调用一致性、交互逻辑合理性，最后用LLM judge二次审核歧义样本，有效提升训练数据质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时序编码Agent训练需要带可验证反馈的交互环境，现有线性构建流程会丢弃大量可修复的候选仓库，且依赖模型rollout的反馈成本高、延迟大，还缺乏对训练价值的显式优化，无法支撑长时序Agent的规模化训练。

### 方法关键点
- RepoFactory流水线从公开代码库筛选可测试、无外部依赖、代码量适中的候选仓库，构建隔离运行时环境，自动生成任务规范、API清单与验证器
- 设计Environment Evolution Loop，优化乘法目标Q=A·C·S：A为有效性（oracle实现全过测、空工作空间得0分），C为结构耦合度（静态调用图可达函数对占比），S为实现复杂度（代码量+依赖数的对数组合），全程无需模型求解任务，仅靠静态分析和验证器反馈迭代优化环境
- 基于生成的环境收集SFT轨迹，过滤低奖励、逻辑冲突的轨迹后用于Agent微调

### 关键结果
生成10159个覆盖17个软件领域的可验证训练环境，训练后的RepoHorizen-35B-A3B相比基线Qwen3.5-35B-A3B，在NL2Repo-Bench上提升22.6pp，5个长时序编码Agent基准平均提升8.5pp；环境演化环节额外贡献了5.1pp的NL2Repo提升和2.1pp的平均基准提升，环境规模增加到5577个时性能仍未饱和。

最值得记住的一句话：低开销的结构指标+验证反馈组合，可替代成本高昂的模型rollout反馈，实现训练环境的规模化迭代，同时显著提升Agent下游性能。
