---
title: 'Gym-Anything for Robotics: Scaling physical simulations with digital agents'
title_zh: Gym-Anything机器人框架：用数字Agent规模化生成物理仿真
authors:
- Pranjal Aggarwal
- Sean Welleck
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.40565'
url: https://arxiv.org/abs/2610.40565
pdf_url: https://arxiv.org/pdf/2610.40565
published: '2026-10-29'
collected: '2026-11-01'
category: Agent
direction: 具身Agent · 仿真环境规模化生成
tags:
- Embodied Agent
- Coding Agent
- Simulation Generation
- RL Benchmark
- Environment Automation
one_liner: 提出用编码Agent自动生成高价值机器人仿真的框架，配套RoboWorld基准与多种性能优化方案
practical_value: '- 编码Agent自动生成仿真环境的思路，可迁移到电商/推荐系统的离线模拟场景，自动生成多样化用户交互仿真环境，大幅降低专家构建测试用例的成本

  - 基于业务价值（如文中GDP维度）排序任务优先级的方法，可复用在电商Agent/推荐迭代中，优先覆盖高GMV场景的仿真与测试，提升迭代ROI

  - 生成-审计的对抗校验循环，可借鉴到RAG/推荐内容生成、文案生成场景，自动校验生成结果的合理性，降低bad case率'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有机器人仿真环境覆盖真实任务与物理现象的范围极窄，核心瓶颈是仿真构建重度依赖专家人工投入，无法规模化，制约具身AI模型的训练与落地。
### 方法关键点
1. 提出Gym-Anything框架，将仿真生成转化为coding Agent任务，Agent能力的提升可直接带动仿真的丰富度与保真度提升
2. 基于美国GDP数据筛选高经济价值的物理任务作为仿真覆盖方向，明确定义优质仿真与任务的标准，配套对抗式生成-审计循环校验生成结果的合规性
3. 构建RoboWorld基准，包含25个仿真、25个测试+175个训练共200个不同难度的RL环境，同时提出in-context learning、特权教师、自辅助学习、代码策略生成演示等优化方法提升模型表现
### 关键结果
前沿大模型在RoboWorld所有测试任务上均失败，平均奖励仅0.06，使用提出的优化方法后性能得到显著提升
