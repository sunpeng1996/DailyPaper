---
title: 'Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen
  VLA Models'
title_zh: 三思而后行：将树搜索蒸馏为冻结VLA模型的动作评估模块
authors:
- Xinyi Xie
- Zican Hu
- Zhanyu Liu
- Yicheng Dong
- Wenhao Wu
- Zhenhong Sun
- Haoran Li
- Chunlin Chen
- Zhi Wang
- Pichao Wang
affiliations:
- Nanjing University
- Australian National University
- Institute of Automation, Chinese Academy of Sciences
- Nvidia
arxiv_id: '2607.03751'
url: https://arxiv.org/abs/2607.03751
pdf_url: https://arxiv.org/pdf/2607.03751
published: '2026-07-03'
collected: '2026-07-08'
category: Agent
direction: 具身Agent 测试时性能与效率优化
tags:
- VLA
- Monte-Carlo Tree Search
- Test-Time Scaling
- Knowledge Distillation
- Q-Learning
one_liner: 提出SVA框架，为冻结VLA外挂轻量动作评估器，无需微调即提升泛化性与推理效率
practical_value: '- 可复用「大模型生成多候选+轻量评估器选优」范式，生成式推荐场景下让LLM生成多个item候选，外挂业务Q模型排序，避免SFT破坏大模型通用泛化能力

  - 测试时优化性价比远高于盲目扩大模型尺寸，业务中可优先优化候选筛选逻辑，用小参数LLM实现优于大模型的效果，同时降低推理latency

  - 可迁移MCTS蒸馏方案：离线用模拟/历史真实数据探索候选空间打标，蒸馏轻量评估器，上线无需依赖仿真环境，适配搜索推荐冷启动场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
预训练VLA泛化性远弱于LLM/VLM，常规SFT/RL微调虽提升特定任务效果，但会损伤预训练获得的通用能力；核心瓶颈不仅是动作生成质量差，还有动作评估能力不足，诊断实验显示冻结VLA的pass@1成功率仅33%，但pass@32可达92%，其输出分布中已存在优质动作。
### 方法关键点
提出SVA框架：1. 离线阶段用蒙特卡洛树搜索在仿真环境遍历VLA的输出分布，收集带真实回报标注的多样化轨迹；2. 将轨迹知识蒸馏为轻量Q值模型，预测候选动作的长期预期收益；3. 部署阶段冻结VLA生成多个候选，由Q值模型结合不确定性正则选出最优动作，无需访问仿真器。
### 关键结果
9B参数VLA搭配SVA，性能比27B原生VLA高7个点，推理延迟还低27%，测试时评估扩容的性价比远高于扩大模型参数规模，同时可显著提升unseen任务的泛化性。
