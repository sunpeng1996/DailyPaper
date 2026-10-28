---
title: The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents
title_zh: 三位一体：面向多模态Agent的能力驱动递归自提升框架
authors:
- Weidong Tang
- Ruiheng Wang
- Jingxuan Zhang
- Hexin Wang
- Haoyuan Chen
- Zhengfeiyang Zhang
- Yixing Ma
- Zichen Jiang
- Ziyu Guo
- Haodong Li
affiliations:
- InfRec
- Xidian University
- Tongji University
- National University of Singapore
- The Chinese University of Hong Kong
arxiv_id: '2610.36077'
url: https://arxiv.org/abs/2610.36077
pdf_url: https://arxiv.org/pdf/2610.36077
published: '2026-10-25'
collected: '2026-10-28'
category: Agent
direction: 多模态Agent · 递归自提升框架
tags:
- Multimodal-Agent
- Recursive-Self-Improvement
- Harness
- Capability-Driven
- Real2Sim2Real
one_liner: 提出Creator/Explorer/Evolver三角色框架，实现多模态Agent能力驱动的递归自提升与跨任务泛化
practical_value: '- 可复用「按底层能力聚类任务而非表面类目」的思路，把搜索推荐/电商Agent的任务（如意图理解、多轮导购、多模态商品理解）按共享能力分组，减少重复开发，提升跨场景泛化

  - 可借鉴Capability-Driven Real2Sim2Real方案，针对电商复杂真实场景（如直播带货话术优化、用户交互策略迭代）先做低成本仿真训练，再迁移到真实业务，降低标注和试错成本

  - 能力感知的Harness路由方案可直接复用在多场景推荐/Agent调度中，基于任务的能力需求自动匹配最优模块组合，兼顾业务性能和推理效率

  - 可复用模块化Harness的迭代思路，针对冻结基座LLM，通过迭代优化外围控制模块（如记忆、规划、工具调用逻辑）实现业务效果提升，无需反复微调基座'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多模态Agent迭代面临两大核心瓶颈：一是人工构建异构可验证环境成本极高，二是人工迭代Harness（Agent控制框架）的速度跟不上任务复杂度和多样性的增长，现有任务驱动的自提升方案容易过拟合，跨异构任务泛化性差。

### 方法关键点
- 构建Creator、Explorer、Evolver三角色自迭代闭环：Evolver基于已验证的执行轨迹，将原任务树按共享底层能力重构为层级化能力树，打破表面任务形态的限制
- 提出Capability-Driven Real2Sim2Real：Creator针对同一能力节点的异构任务，抽象出简化可验证的仿真环境做能力训练，再用原始任务验证迁移效果，降低训练成本
- Explorer沿能力树通过选择性继承和局部迭代，演化出可复用的模块化Harness树，不同分支的Harness专精不同能力，避免全局Harness的性能冲突
- 配套Capability-Aware Harness Router，基于任务公开信息和历史执行经验自动匹配最优Harness配置，实现能力的高效调度

### 关键实验
基于28个训练基准、18个unseen基准（含2个真实具身任务）验证：迭代4轮后训练集平均性能较基线提升34个点，unseen基准提升26个点；能力感知路由效果接近最优Oracle，仅低2个点左右；真实具身机器人任务成功率从0提升至60%。

### 核心结论
异构任务的底层能力共享是提升Agent跨场景泛化、降低迭代成本的核心抓手，按能力而非任务组织迭代可以实现「少即是多」的效果
