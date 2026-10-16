---
title: Learning Self-Orchestration in Decentralized Agent Swarms
title_zh: 去中心化Agent集群的自编排学习方法
authors:
- Guowei Xu
- Zhenting Qi
- Amani Kiruga
- Himabindu Lakkaraju
- Yilun Du
affiliations:
- Harvard University
arxiv_id: '2610.22322'
url: https://arxiv.org/abs/2610.22322
pdf_url: https://arxiv.org/pdf/2610.22322
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: 多智能体 · 去中心化自编排训练
tags:
- MultiAgent
- Decentralized
- SelfOrchestration
- ReinforcementLearning
- LLMAgent
one_liner: 提出基于市场的后训练框架MPT，实现去中心化Agent集群动作与自编排联合学习
practical_value: '- 电商多Agent分工场景（如Query理解、内容生成、客诉处理）可复用MPT的竞价+信用分配机制，替代手动定义的固定路由规则，降低流程维护成本

  - 多模型协作的推荐链路（召回/粗排/精排）可借鉴联合训练思路，让不同阶段模型同时学习自身策略与任务优先级，比固定调度效果更优

  - 生产级Agent集群可复用论文的扩展与容灾方案：训练好的集群支持推理时动态扩容，Agent掉线时性能下降幅度更小，适配高可用的电商业务需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent系统普遍采用固定编排结构，将单个Agent能力学习与集群协作规则解耦，忽略了两者的耦合关系：Agent能力提升后最优协作规则会动态变化，固定编排会限制集群性能上限，同时去中心化场景下的长链路信用分配也缺乏有效方案。

### 方法关键点
- 提出市场导向的后训练框架MPT，每个Agent独立输出参与当前任务的竞价，最高竞价者获得执行权，无需中心调度节点
- 信用分配采用桶队列机制：执行Agent保留(1-竞价)比例的奖励作为自身训练信号，剩余竞价比例的奖励回传给上一个执行Agent，实现长链路任务的信用回溯
- 自编排学习采用反事实对比思路：对存在竞价竞争的决策点，生成次高竞价者执行的备选分支，基于两个分支的奖励差用Bradley-Terry偏好目标优化竞价策略，每4轮动作训练穿插1轮竞价训练

### 关键实验
在具身建造、机器人导航、深度研究三个任务上测试，对比单模型RL基线：具身建造任务奖励从20提升至41.5，导航任务奖励从0.52提升至1.23，深度研究准确率从9%提升至21%；对比现有协作策略（Round-Robin、Graph-of-Agents等），在Iron Pickaxe任务上相对最优基线GoA提升63.4%；推理时Agent规模从3扩到12，子任务pass@3最高提升19个百分点，90%掉线率下12Agent集群性能仍比3Agent集群高73.7%。

### 核心结论
去中心化Agent集群的能力不仅来自单个Agent的性能，更来自协同策略与个体能力的联合进化，无需中心调度的自编排可以同时带来性能、扩展性和鲁棒性的三重收益。
