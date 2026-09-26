---
title: 'RAPID: Robot Agentic Programming from Demonstrations'
title_zh: RAPID：基于人类演示的机器人具身Agent编程框架
authors:
- Yuyao Liu
- Jiayuan Mao
- David Hsu
- Leslie Pack Kaelbling
- Tomás Lozano-Pérez
affiliations:
- Massachusetts Institute of Technology
- National University of Singapore
- University of Pennsylvania
- NVIDIA
arxiv_id: '2609.30249'
url: https://arxiv.org/abs/2609.30249
pdf_url: https://arxiv.org/pdf/2609.30249
published: '2026-09-24'
collected: '2026-09-26'
category: Agent
direction: 具身Agent · 单演示生成可泛化执行程序
tags:
- Agent
- EmbodiedAI
- ProgramGeneration
- FewShotLearning
- TaskGeneralization
one_liner: 仅需单段人类视觉演示即可自动生成、验证、迭代优化可泛化机器人执行程序的Agent框架
practical_value: '- 单样本演示生成可泛化程序的范式可迁移到电商Agent流程自动化场景，比如仅需1次人工客服操作演示即可生成同类型售后问题标准化处理程序，大幅降低规则配置成本

  - 迭代式代码生成-验证-优化的Agent闭环可复用在推荐系统策略迭代流程中，基于线上ABTest反馈自动修正排序策略代码，减少人工调参工作量

  - 以对象为中心的关系型程序表示思路可借鉴到多场景商品推荐泛化建模，聚焦用户需求本质而非单次交互的具体特征，提升跨品类推荐泛化性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有编码Agent在通用编程任务表现优异，但落地机器人系统时存在三大核心瓶颈：缺乏可测试的任务规范、无适配的机器人执行动作原语、无交互式程序验证环境，人工定义上述组件成本极高，单演示下生成可跨场景泛化的执行程序是核心痛点。
### 方法关键点
1. RAPID框架仅输入单段人类视觉演示，即可自动推导得到任务规范、动作原语、交互验证环境三大核心组件
2. 采用对象为中心的关系型程序表示，聚焦演示策略的底层结构而非单次具体动作，将动作原语抽象为实现对象级运动效果的轨迹优化程序，通过运行时捕获场景几何的关系约束完成组合，保证跨场景泛化性
3. 内置代码迭代优化的Agent循环，自动执行、验证并修复生成的程序
### 关键结果
在仿真8种高难度非抓取操作任务、LIBERO-Pro基准抓取任务上表现优异，在真实Franka机械臂8种非抓取任务中成功落地，可稳定泛化到不同物体位姿、形状、材质、环境
