---
title: 'Player-1: Learning to Play from Synthetic Experience'
title_zh: Player-1：基于合成经验的通用游戏控制Agent训练框架
authors:
- Mingyu Ouyang
- Yiran Wang
- Siyuan Hu
- Xingyilang Yin
- Huiqiang Sun
- Guangzhi Wang
- Junfu Pu
- Cheng Cheng
- Honghao Chen
- Ying Shan
affiliations:
- National University of Singapore
- ARC Lab, Tencent IEG
- Nanyang Technological University
arxiv_id: '2610.20584'
url: https://arxiv.org/abs/2610.20584
pdf_url: https://arxiv.org/pdf/2610.20584
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: 游戏控制Agent · 合成经验训练
tags:
- Game Agent
- Synthetic Experience
- RL
- SFT
- Generalist Agent
one_liner: 提出结合少量游戏演示SFT与合成环境RL的通用游戏控制Agent框架，跨游戏泛化能力显著提升
practical_value: '- 交互Agent训练范式可复用：若真实场景交互/标注成本高，可先做少量真实样本SFT初始化，再搭建低成本合成环境覆盖通用基础能力做RL训练，大幅降低真实场景训练代价，可迁移到电商导购Agent、GUI自动化操作Agent等场景

  - 动作空间设计trick可直接复用：扩展相对位移、持续输入、组合动作的思路，适配需要连续、多并发操作的Agent场景，比如电商后台批量操作Agent、直播场控Agent

  - 多任务RL训练trick可复用：跨环境优势归一化解决不同场景reward尺度不一致问题，动作均衡采样提升长尾操作的学习效果，同样适用于推荐系统多场景联合训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前游戏Agent训练高度依赖大规模真实游戏演示数据，仅能覆盖有限的游戏状态，且真实游戏的RL训练环境搭建、奖励设计成本极高，难以规模化扩展，亟需探索低成本、可跨游戏泛化的训练路径。

### 方法关键点
- 扩展电脑操作Agent动作空间：新增相对指针位移、持续输入、组合动作三类游戏场景必需的动作类型，适配动态游戏控制需求
- 轻量化SFT初始化：仅用6044条跨游戏标注轨迹做SFT，对齐不同来源的操作数据，补充任务指令和视觉推理标注，采用动作均衡采样优化长尾动作学习效果
- 合成环境RL训练：搭建PLAYER-1-GYM，包含16个2D/3D合成环境，覆盖瞄准、驾驶、导航、UI交互等跨游戏通用控制需求，支持环境属性随机化、程序化校验奖励，采用PPO做多环境RL训练，通过分环境优势归一化解决不同场景reward尺度差异问题

### 关键结果
9B参数版本在MineDojo-300任务上成功率较SFT阶段提升27.8pp至38.33%，是最强基线GameWAM的3倍；35B版本成功率提升17.7pp至41.04%，在未见过的ViZDoom、GameWorld任务上分别提升25.6pp、3.02pp，跨游戏泛化效果显著。

**最值得记住的一句话**：基于通用基础能力的合成经验训练，可在极低的真实场景标注和交互成本下，显著提升Agent的跨场景泛化能力。
