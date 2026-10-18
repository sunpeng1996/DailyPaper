---
title: 'LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation'
title_zh: LIBERO-PeRM：具身机器人个性化操作能力评测基准
authors:
- Zhixu Li
- Keqian Tang
- Litian Gong
- Jingyu Yao
- Wenqian Zhang
- Tianze Xu
- Zehao Wang
- Yuping Wang
- Junge Zhang
- Jiachen Li
affiliations:
- University of California, Riverside
- Yale University
- Georgia Institute of Technology
- University of Michigan, Ann Arbor
- University of Toronto
arxiv_id: '2610.22372'
url: https://arxiv.org/abs/2610.22372
pdf_url: https://arxiv.org/pdf/2610.22372
published: '2026-10-15'
collected: '2026-10-18'
category: Agent
direction: 具身Agent 个性化偏好学习评测
tags:
- Embodied Agent
- Personalization
- Benchmark
- Preference Learning
- Robotic Manipulation
one_liner: 推出可控个性化机器人操作基准，覆盖5类研究问题、312个任务与配套度量
practical_value: '- 偏好建模可复用其分层分类框架，将用户偏好拆解为操作层、技能层、用户画像层三类，降低偏好对齐复杂度

  - 训练策略可参考其混合训练范式，相比顺序微调能更好保留原模型通用能力，同时提升上下文prompt响应效果

  - 偏好评测可借鉴「任务完成度+偏好满足度」双维度度量方案，避免为了满足偏好牺牲核心任务效果'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
通用机器人落地家庭场景需适配用户个性化偏好，但当前个性化机器人操作（PeRM）领域缺乏可控基准，无法区分任务完成度与偏好满足度两类指标，阻碍相关研究落地。
### 方法关键点
1. 提出仿真环境下可观测偏好的可控定义与分类体系，覆盖动作、技能、用户画像三类可通过语言表达的偏好，无需修改任务目标即可落地、自动评估、跨任务复用；
2. 搭建流水线生成带/不带偏好的配对演示数据集，构建5个任务套件共312个任务，配套标准化偏好满足度度量。
### 关键结果
现有VLA策略零样本个性化表现极差，SFT可让偏好可学习；混合训练相比顺序适配保留无偏好任务能力更强，相比仅偏好训练的上下文提示效果提升明显，但会削弱动作偏好学习效果；偏好泛化、分解、冲突处理仍是未解决的核心难题。
