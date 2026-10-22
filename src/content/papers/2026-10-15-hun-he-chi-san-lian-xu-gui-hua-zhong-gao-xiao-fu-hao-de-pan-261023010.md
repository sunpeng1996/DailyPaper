---
title: What Makes a Good Symbol for Hybrid Discrete-Continuous Planning?
title_zh: 混合离散-连续规划中高效符号的判定标准与自动生成方法
authors:
- Yiyuan Pan
- Changliu Liu
- Jiayuan Mao
affiliations:
- Carnegie Mellon University
- University of Pennsylvania
arxiv_id: '2610.23010'
url: https://arxiv.org/abs/2610.23010
pdf_url: https://arxiv.org/pdf/2610.23010
published: '2026-10-15'
collected: '2026-10-22'
category: Agent
direction: Agent规划 · 符号自动生成
tags:
- Planning
- Symbol Abstraction
- Hybrid System
- Energy-based Model
- CEGAR
one_liner: 从求解器视角定义规划符号有效性，提出反例引导的符号生成算法，兼顾效率与最优性
practical_value: '- 搜索推荐/广告的多步出价、库存分配等混合整数优化场景，可借鉴求解器充分符号思路，将高维规划拆解为低维符号搜索+简单凸优化，大幅降低推理耗时

  - 生成式推荐的扩散模型、能量函数推理可复用τ-下降忠实符号分区思路，用少量符号锚定不同决策盆地，减少多起点采样次数同时保留最优性

  - 电商导购Agent、履约Agent的任务规划可借鉴反例引导的符号生成框架，无需预先人工定义符号，自动从优化landscape中提取可解释、可引导的行为符号'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有混合离散-连续规划的符号多依赖人工定义或语言监督，未从求解效率角度定义符号有效性，导致符号要么冗余要么破坏最优性，高维场景下求解复杂度爆炸。

### 方法关键点
1. 提出求解器充分符号定义：符号需保留全局最优性同时降低子问题求解复杂度，将原问题拆解为符号搜索+条件子问题求解两步
2. 针对分段仿射（PWA）系统，基于相对仿射全幺模（RAT）理论，提出反例引导的分区精化（CPR）算法，自动生成最小维度符号，子问题可简化为线性规划求解
3. 针对神经网络参数化的能量函数场景，提出τ-下降忠实符号定义，通过采样识别优化盆地的低维分界方向，用线性投影+量化生成符号，每个符号对应的子问题仅需一次下降即可得到τ-近似最优解

### 关键实验
PWA系统6个机器人操作任务上，相比基线最高实现4.81倍推理加速，成功率达100%；神经网络能量函数场景5个任务上，基于DDPM的符号引导方法将覆盖最优解所需的下降次数最高减少72%，成功率保持与基线一致。

### 核心结论
有用的符号本质是暴露能简化求解的关键离散承诺，而非仅仅是对问题的语义描述。
