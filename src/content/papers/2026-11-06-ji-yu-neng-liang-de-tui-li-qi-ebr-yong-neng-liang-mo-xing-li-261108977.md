---
title: 'Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based
  Model'
title_zh: 基于能量的推理器（EBR）：用能量模型范式构建循环推理架构
authors:
- William Xingxu Chen
- Alexi Gladstone
- Zeyu Michael Li
- Heng Ji
- Yilun Du
affiliations:
- Duke University
- UIUC
- Harvard University
arxiv_id: '2611.08977'
url: https://arxiv.org/abs/2611.08977
pdf_url: https://arxiv.org/pdf/2611.08977
published: '2026-11-06'
collected: '2026-11-09'
category: Reasoning
direction: 循环推理 · 能量模型优化
tags:
- Energy-Based Model
- Recurrent Reasoning
- Iterative Optimization
- Multi-solution Reasoning
- Adaptive Computation
one_liner: 提出基于能量的循环推理框架EBR，统一推理迭代、停止与候选选择逻辑，大幅降低推理算力消耗
practical_value: '- 可借鉴EBR的自适应停止逻辑：在搜索推荐多步检索、Agent规划场景，用能量梯度范数作为停止信号，避免固定迭代步数浪费算力，可根据query难度动态分配计算资源

  - 多候选选择方案可复用：在生成式推荐多候选排序、多解任务（如搭配推荐、多query生成）中，用能量值作为统一排序信号，无需额外训练验证器，降低模块复杂度

  - SXM训练范式可迁移：针对有多解需求的推荐任务（如个性化内容生成、多路径规划），用多轨迹探索+最优匹配监督的方式训练，提升解的多样性同时保证准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有循环推理模型无明确进度度量机制，难以判断迭代停止时机，且迭代更新不受当前状态评估引导，多解场景下解的覆盖率低、推理算力开销高，亟需统一目标函数串联推理全流程。

### 方法关键点
- 架构设计：学习隐层推理状态的能量函数，推理过程通过能量梯度下降迭代更新隐状态，更低能量对应更优推理结果，梯度范数作为收敛停止信号，统一迭代优化、停止判断、候选选择三个核心模块
- 训练优化：提出分段截断反向传播降低长序列训练内存开销，新增收敛损失鼓励正确预测对应能量极小值点，随机化步长与迭代步数提升泛化性
- 多解优化：提出基于探索的SXM训练方法，并行多轨迹推理，仅监督与有效解匹配最优的轨迹，塑造适配多解的能量景观，提升多解覆盖率

### 关键实验
在Sudoku-Extreme、Maze-Hard、N-Queens、图着色4个算法推理基准测试，对比TRM、EqR、GRAM等现有循环推理模型：1）Sudoku-Extreme任务准确率99.9%，推理算力比次优方案低345×；2）多解任务N-Queens 10×10场景下解的覆盖率从57.5%提升至92.0%，同时保持近100%准确率；3）模型参数量仅1.8M，远小于对比基线。

**最值得记住的一句话**：将推理过程转化为能量最小化过程，能够用同一套信号同时实现迭代引导、自适应停止和候选排序，大幅提升推理效率与多解能力。
