---
title: 'RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving
  Agent Memory via Reduced-Order Utility States'
title_zh: RoMeRL：基于降阶效用状态的自进化Agent记忆平衡框架
authors:
- Yi Yang
- Zhennan Chen
- Yihong Zhuang
- Tiehan Fan
- Yinan Chen
- Jian Li
- Jian Yang
- Ying Tai
affiliations:
- Nanjing University
- Xiamen University
- Zhejiang University
arxiv_id: '2608.02508'
url: https://arxiv.org/abs/2608.02508
pdf_url: https://arxiv.org/pdf/2608.02508
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent 自进化记忆优化
tags:
- LLM Agent
- Reinforcement Learning
- Memory System
- Self-Evolution
- Reward Trap
one_liner: 提出降阶记忆强化学习框架RoMeRL，用固定维度因子化语义坐标解决自进化Agent的记忆-奖励陷阱问题
practical_value: '- 记忆系统设计可借鉴2×2因子化坐标思路，无需全量存储用户/交互轨迹，按正负反馈、历史/动态维度筛选核心记忆样本，大幅降低存储和检索成本

  - 电商Agent客服、导购场景可复用RoMeRL的记忆更新逻辑，每个任务仅保留最优成功案例、首次转败为胜案例、高价值负案例、最新失败案例4类核心记忆，提升反馈利用率

  - 避免记忆奖励陷阱的思路可迁移到推荐系统的多兴趣召回效用更新，解决多召回源联合排序时的奖励错配问题，减少无效召回特征的误更新

  - 跨模型记忆迁移结论可直接复用，训练好的固定维度记忆坐标可在不同LLM backbone间迁移，降低大模型替换后的重训练成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于轨迹索引的自进化Agent记忆RL方法存在两大痛点：一是轨迹效用空间随交互历史持续膨胀，有限反馈被分散到超大状态空间，导致冷启动严重、反馈密度极低；二是轨迹级奖励会被分配给所有协同检索的记忆，无关/弱相关经验会收到误导性效用更新，陷入「记忆-奖励陷阱」——增加探索提升反馈覆盖的同时会大幅提升奖励错配风险，现有方案无法平衡两者。

### 方法关键点
- 提出降阶记忆强化学习RoMeRL，将每个任务持续膨胀的轨迹索引效用空间，替换为固定2×2维度的因子化状态，按 outcome极性（正/负）、记忆动态（历史consolidated/自适应adaptive）拆分为4个固定语义坐标，每个坐标仅存1条代表性记忆
- 4个坐标分别为：正历史坐标PCC存全局最高效成功轨迹，正自适应坐标PAC存首次转败为胜的成功轨迹，负历史坐标NCC存效用最高的失败轨迹，负自适应坐标NAC存最新失败轨迹
- 记忆更新仅在4个坐标内做替换/升级，检索时结合语义相似度和坐标效用加权排序，效用更新沿用Q-learning逻辑，无需微调底层LLM

### 关键实验
在ALFWorld、LifelongAgentBench（OS/DB任务）上对比RAG、Mem0、MemP、MemRL等基线，RoMeRL整体成功率达0.862，超最优基线3.2个百分点；Cold-Q比例降低80.0%，反馈密度提升6倍，记忆存储量减少84.4%，LLM调用量降低21.1%；记忆-奖励陷阱压力测试下，最终噪声比例仅0.15%，远低于基线的1.2%。

**最值得记住的一句话**：解决记忆奖励陷阱的核心不是增加探索覆盖，而是从根源上限制效用状态的维度，把反馈集中在固定语义空间内。
