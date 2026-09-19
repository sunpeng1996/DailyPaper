---
title: 'CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding'
title_zh: CoRef-GS：面向多智能体场景理解的协同指代高斯泼溅框架
authors:
- Zhikun Zhou
- Kunyu Peng
- Runyi Yang
- Junhao Cai
- Di Wen
- Ruiping Liu
- Danda Pani Paudel
- Yi Zhou
- Luc Van Gool
- Kailun Yang
affiliations:
- School of Artificial Intelligence
- State Key Laboratory of Autonomous Intelligent Unmanned Systems
- Deutsche Forschungsgemeinschaft (DFG)
arxiv_id: '2609.20586'
url: https://arxiv.org/abs/2609.20586
pdf_url: https://arxiv.org/pdf/2609.20586
published: '2026-09-17'
collected: '2026-09-19'
category: MultiAgent
direction: 多智能体协同 · 具身场景理解
tags:
- MultiAgent
- Embodied AI
- Gaussian Splatting
- Scene Understanding
- Benchmark
one_liner: 提出多智能体协同指代高斯泼溅框架CoRef-GS，配套专用基准，大幅提升跨Agent场景语言指代精度
practical_value: '- 多Agent独立采集信息后的对齐可复用几何+语义双一致性校验思路，避免仅靠特征匹配的语义漂移问题，可落地到多端用户行为数据对齐、多导购Agent认知对齐场景

  - 视角条件化的关系推理模块可迁移到电商场景下用户视角的语义检索/指代匹配任务，例如用户拍照后基于场景关系的商品检索匹配

  - 跨局部数据融合无需重训练的架构思路可复用在推荐系统多源异构特征融合链路，降低融合模块的训练和部署成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
具身多Agent协同场景下，现有语言感知高斯方法仅支持单地图查询，高斯配准方法仅优化几何/光度对齐，未保留语言落地所需的语义兼容性，无法支撑跨Agent观测融合后的指代理解任务，需要同时满足几何可对齐、实例级语义可比、视角条件关系推理三大要求。

### 方法关键点
1. 构造局部开放词汇实例感知高斯地图；
2. 设计跨Agent对齐模块，基于几何+语义一致性对齐部分重叠的局部地图，融合过程无需重训练；
3. 采用视角条件化掩码关系图实现指代查询的grounding。

### 关键结果
仿真场景下旋转误差从粗初始化的2.58°降至优化后的0.15°；真实场景下指代mIoU较基准ReferSplat从52.6%提升至68.8%；同步开源CoQuad-Ref双四足机器人真实/仿真室内场景基准。
