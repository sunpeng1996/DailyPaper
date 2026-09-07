---
title: 'Iris: Climbing to the Search Frontier'
title_zh: Iris：达到前沿性能的开源搜索Agent训练全流程方案
authors:
- Ziyuan Liu
- Hengqi Liu
- Zichuan Wang
- Yang Qin
- Jiachen Liang
- Xu Chu
- Shaowei Chen
- Yuantao Gu
- Mu Chuan
affiliations:
- AllSpark Team
arxiv_id: '2609.04304'
url: https://arxiv.org/abs/2609.04304
pdf_url: https://arxiv.org/pdf/2609.04304
published: '2026-09-02'
collected: '2026-09-07'
category: Agent
direction: 搜索Agent · SFT-RL迭代训练优化
tags:
- Search Agent
- SFT
- Reinforcement Learning
- ReAct
- Context Management
- MoE
one_liner: 提出SFT-RL迭代爬升训练范式，开源两款高性能搜索Agent及完整训练、数据、评估流程
practical_value: '- 数据构造可复用：从领域知识图谱/商品链接关系反向构造多跳检索任务，替换实体为描述性引用来避免直接字符串匹配，能低成本生成高质量训练数据，适配电商商品搜索、导购Agent的多轮推理训练

  - 训练范式可借鉴：采用轨迹级+轮次级双层过滤的SFT，结合RL与SFT迭代爬升的训练流程，把RL探索出的优质轨迹回喂SFT，适合优化导购Agent、搜索推荐的多轮交互策略

  - 工程优化可复用：推理侧采用discard-all+重试的上下文管理策略，训练侧用请求级部分回滚+前缀复用降低长序列训练成本，同时在训练集群内部署奖励模型与摘要服务，减少外部API依赖

  - 评估逻辑可参考：评估时区分有无上下文管理的效果，剥离推理侧策略增益，更准确衡量Agent本身的检索推理能力，适合电商搜索、导购Agent的效果评测'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有搜索Agent训练存在三大痛点：自然搜索问题难度不足无法训练多跳推理能力、训练轨迹良莠不齐导致学习信号噪声大、推理侧上下文管理（CM）的增益容易掩盖模型本身的能力差异，评估结果可解释性差，难以落地到真实长程交互场景。

### 方法关键点
- 数据构造：从网页超链接结构反向构造多跳任务，将非答案实体改写为无直接搜索价值的描述性引用，仅保留参考模型闭卷答错、给上下文能答对的高难度可解问题
- 训练流程：先基于优质教师模型生成ReAct轨迹，经轨迹级（正确性、无退化、搜索深度达标）+轮次级（数据驱动的判据过滤坏轮次）双层过滤后做SFT，再对接实时搜索做RL优化，交替SFT与RL形成「爬升」循环，将RL产出的最短优质轨迹回喂下一轮SFT，自动生成自步curriculum
- 工程优化：训练侧用请求级部分回滚+前缀复用降低长序列训练成本，集群内部署统一的奖励模型与检索结果摘要服务，无外部API依赖。

### 关键实验
在BrowseComp、BrowseComp-ZH、DeepSearchQA、HLE四个主流搜索Agent基准上评测，35B规模的Iris-mini较同尺寸SOTA最高提3.4个点，397B的Iris-pro较同尺寸SOTA最高提3.8个点，CM策略最高可带来21.2个点的性能增益，模型本身的无CM性能也领先同尺寸基线7~10个点。

### 核心结论
搜索是Agent的原子能力而非垂直场景，其训练得到的不完全信息下的决策行为可迁移到所有需要多轮交互的Agent场景。
