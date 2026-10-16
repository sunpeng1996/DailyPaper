---
title: 'Cowork-Gym: Synthesizing Interactive Work Environments at Scale'
title_zh: Cowork-Gym：可规模化生成的人机协作交互式工作环境框架
authors:
- Anni Zou
- Cheng Chen
- Jiaji Deng
- Weikang Zhou
- Xinji Mai
- Yue Wu
- Jianing Lin
- Lipeng Xie
- Lixiong Qin
- Qingyue Zhao
affiliations:
- Alibaba Token Foundry
arxiv_id: '2610.17670'
url: https://arxiv.org/abs/2610.17670
pdf_url: https://arxiv.org/pdf/2610.17670
published: '2026-10-12'
collected: '2026-10-16'
category: Agent
direction: Agent 训练环境自动化合成
tags:
- Agent Training
- User Simulation
- Environment Synthesis
- SFT
- RL
- On-policy Distillation
one_liner: 通过构建-执行-修正流水线生成64.9K人机协作环境，大幅提升不同规模模型的Agent能力
practical_value: '- 可复用「build-execute-revise」闭环流水线生成业务场景Agent训练数据，比如电商客服、运营助理交互环境，降低人工标注成本

  - 训练业务Agent时可引入状态化用户模拟器，模拟用户动态改需求、调共享资源的真实场景，提升Agent动态适配能力

  - 轨迹筛选阶段可针对目标模型规模适配NLL/RSR筛选标准，70%筛选比例即可保效果同时降训练数据成本

  - 用On-policy Distillation替代直接SFT，可在迁移Agent能力的同时减少通用能力退化，适配业务兼顾垂直能力和通用理解的需求'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前人机协作（Cowork）类Agent需要适配动态变化的用户需求、共享工作区修改，但现有训练环境构建成本高、覆盖场景有限、难以还原真实用户动态交互特征，无法支撑规模化Agent训练。

### 方法关键点
- 双路径任务生成：顶层分类引导生成覆盖指定能力和场景，底层资源落地生成基于真实文档、代码库等资源的任务，保障场景多样性
- build-execute-revise闭环：由Builder、Verifier Constructor、Issue Detector三类专用Agent完成环境实例化、验证和缺陷修复，确保环境可执行、规则一致
- 内置状态化用户模拟器：可根据Agent执行进度给出对话反馈、直接修改共享工作区，还原真实协作中用户动态调整需求的场景
- 训练链路支持SFT、基于混合验证的GRPO RL、On-policy Distillation三种模式，适配不同训练需求

### 关键结果
合成14类场景共64.9K可执行环境，基于该数据训练9B、27B、35B-A3B三个规模的Qwen模型，在6个Agent基准上平均比基线分别提升8.7、6.4、4.1个点；其中27B模型总排名第二，在PawBench和ClawEval上超过所有100B+参数的参评模型。

### 核心结论
可规模化构造的可执行环境是自进化Agent的核心数据驱动力，环境池随业务场景动态扩展即可支撑Agent能力持续迭代。
