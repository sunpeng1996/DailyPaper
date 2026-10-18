---
title: 'T2-z: Test-Time Optimization of Environment Latents for Robotic World Models'
title_zh: T2-Z：面向机器人世界模型的环境隐变量测试时优化
authors:
- Chenyuan Zhou
- Yining Hong
- Huang Huang
- Yunfan Jiang
- Wenlong Huang
- David Held
- Vitor Campagnolo Guizilini
- Yue Wang
- Li Fei-Fei
- Jiajun Wu
affiliations:
- Stanford University
- CMU
- Toyota Research Institute
- University of Southern California
arxiv_id: '2610.22364'
url: https://arxiv.org/abs/2610.22364
pdf_url: https://arxiv.org/pdf/2610.22364
published: '2026-10-15'
collected: '2026-10-18'
category: Other
direction: 世界模型 · 测试时隐变量优化
tags:
- World_Model
- Test_Time_Optimization
- Latent_Representation
- Robotics
- Few_Shot_Adaptation
one_liner: T2-Z测试时环境隐变量优化框架，大幅提升机器人世界模型未知环境适配表现
practical_value: '- 可复用测试时隐变量优化思路：针对推荐系统不同用户/场景的未观测隐属性（如用户隐性偏好、场景上下文规则），服务时冻结主模型仅优化专属隐变量，无需全模型微调即可快速适配新场景

  - 两阶段交替训练策略可迁移：主推荐模型与场景/用户隐变量分阶段交替训练，既保证主模型泛化性，又能让隐变量自动捕捉不同场景的分布差异，无需人工标注场景属性

  - 少样本适配结论可用于冷启场景：仅需1条新场景的交互轨迹即可完成隐变量优化，可落地于新用户、新类目的冷启适配，大幅降低冷启数据需求'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
机器人世界模型预测动作反馈时，需处理摩擦、质量、自定义规则等大量无法直接观测、也无标注的环境因子，现有方法在未知环境下泛化性差，预测误差高、任务成功率低。

### 方法关键点
1. T2-Z框架给世界模型新增可学习环境隐变量作为预测条件，无需环境因子的监督标注即可捕获底层环境差异
2. 训练采用两阶段交替范式：先固定隐变量优化世界模型，学习跨环境的通用动作条件动力学；再冻结世界模型优化隐变量，自动涌现结构化隐表示
3. 测试时冻结世界模型，仅用1条及以上测试交互轨迹优化新初始化的环境隐变量，即可快速适配未见过的环境配置

### 关键结果
在7个模拟环境+4个真实机器人任务上，物体预测误差从15.20降至7.00，动作成功率从33.73%提升至72.96%，仅需单条测试交互轨迹即可高效推断环境隐变量。
