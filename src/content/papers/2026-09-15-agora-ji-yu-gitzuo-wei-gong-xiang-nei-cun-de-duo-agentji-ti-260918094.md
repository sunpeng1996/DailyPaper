---
title: 'Agora: Git as Shared Memory for Collective AutoResearch'
title_zh: Agora：基于Git作为共享内存的多Agent集体自动研究框架
authors:
- Yifan Zhang
- Yunheng Zou
- Shaokun Zhang
- Jian Hu
- Hao Zhang
- Binfeng Xu
- Jan Kautz
- Yi Dong
affiliations:
- NVIDIA
arxiv_id: '2609.18094'
url: https://arxiv.org/abs/2609.18094
pdf_url: https://arxiv.org/pdf/2609.18094
published: '2026-09-15'
collected: '2026-09-17'
category: MultiAgent
direction: 多Agent协同 · 共享内存架构
tags:
- MultiAgent
- SharedMemory
- Git
- AutoResearch
- DecentralizedCoordination
one_liner: 基于Git构建不可变DAG共享内存层，支撑无中心规划的多Agent异步协同研究
practical_value: '- 多Agent协同做推荐/广告的特征工程、模型调优时，可借鉴Git DAG不可变提交设计，留存所有尝试（含负向结果），避免重复踩坑，同时可溯源最优方案的全链路迭代路径

  - 现有多Agent框架易扎堆探索局部最优，可复用论文的多样性感知UCB排序+exploit/explore分槽的注意力分配机制，引导Agent同时兼顾现有最优方案优化和新方向探索，提升全局搜索效率

  - 推荐/广告AB实验管理可复用这套提交+标签体系，给实验打result/hypothesis/verification等标签，自动计算证据分，快速筛选高置信度的有效优化策略'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单Agent自动研究框架的探索结果仅保存在会话本地，多Agent并行时会产生大量重复搜索，容易提前收敛到局部最优；传统多Agent依赖中心规划或角色分配，无法支撑异步、无预设任务的长期协同研究，亟需跨会话的共享状态层。

### 方法关键点
- 用Git存储所有研究贡献为仅追加的DAG节点，每个节点对应一次提交，包含代码/数据、指标、标签、父节点依赖，天然具备不可变性和可溯源性
- 设计标签体系区分result/insight/hypothesis/verification等贡献类型，证据分仅统计其他账户基于该节点的后续贡献，排除自引，避免刷分
- 构建多样性感知的注意力分配机制，基于语义聚类+UCB排序，向Agent提供exploit（优化当前最优）、explore known（探索薄集群方向）、explore novel（探索全新方向）三类候选，避免全局趋同

### 关键实验
13个无预设任务的编码Agent在无训练数据、无梯度更新的约束下，基于141个预训练捐赠模型初始化119.6M参数的混合架构目标模型，运行近12天：累计产生1703次贡献，165次独立验证无失败，最终指标从随机初始化的3.39bpb降到1.899bpb，达到训练后GPT-2 124M 62%的效果；仅一次人工干预（上线多样性视图）就打破了持续5天的单集群趋同状态，24小时内出现更优结果。

### 核心结论
多Agent协同的核心约束是协调层设计，而非单个Agent的推理能力
