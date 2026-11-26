---
title: 'RoboEvo^2: Recursive Robot Self-Improvement via Harness-Policy Co-Evolution'
title_zh: RoboEvo²：基于管控层-策略协同进化的机器人递归自改进系统
authors:
- Chenzhi Liu
- Jiehong Lin
- Wei Huang
- Xuzhao Huang
- Haoyuan Li
- Yang Zhang
- Junchao Huang
- Chenyeyang Cai
- Bo Wang
- Kazuhiro Kosuge
affiliations:
- The University of Hong Kong
- Zhejiang University
- Southern University of Science and Technology
- The Chinese University of Hong Kong, Shenzhen
- City University of Hong Kong
arxiv_id: '2611.34675'
url: https://arxiv.org/abs/2611.34675
pdf_url: https://arxiv.org/pdf/2611.34675
published: '2026-11-24'
collected: '2026-11-26'
category: Other
direction: 机器人自主学习 · 策略协同进化
tags:
- Self-Improvement
- Co-Evolution
- Policy Learning
- Coding Agent
- Robot Control
one_liner: 提出harness-控制策略双向协同进化框架，无需额外人工标注实现机器人技能自主迭代提升
practical_value: '- 双向进化闭环可迁移到推荐系统迭代：用推荐策略badcase引导Agent生成补全规则，规则沉淀的优质样本回灌训练模型，实现无需人工标注的自迭代

  - Counterfactual Preference Distillation（CPD）可复用在排序优化：同用户/query上下文下对比正负行为序列做偏好蒸馏，提升排序准确率

  - 多路由并行修复思路可用于Agent容错：为Agent接口失败场景预设纯代码、代码+ICL、代码+原有策略多降级路由，降低推理成本、提升成功率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉-语言-动作机器人策略适配陌生环境需额外人工标注，推理Agent自主探索方案的重复试错成本过高，缺少无人工介入的自迭代框架。

### 方法关键点
1. 设计P2H进化链路：用策略执行失败案例引导编码Agent并行探索纯代码、代码+ICL、代码+原有策略三类修复路由，将验证通过的方案沉淀为可复用技能、路由规则、经验库
2. 设计H2P进化链路：用验证通过的轨迹做监督训练，同时引入反事实偏好蒸馏（CPD），让策略在相同初始状态下优先选择成功修正路径
3. 两类进化形成闭环，无需额外人工标注即可持续迭代

### 关键结果
LIBERO-PRO迭代8轮后，单策略成功率从11.0%提升至84.1%，混合模式成功率达90.5%，API调用成本下降77.0%；RoboTwin C2R迭代5轮后，单策略成功率提升31.5%，API成本下降55.0%；Unitree G1-D真机测试混合模式成功率达95.0%
