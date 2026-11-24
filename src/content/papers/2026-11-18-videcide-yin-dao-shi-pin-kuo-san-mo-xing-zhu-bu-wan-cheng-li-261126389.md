---
title: 'ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step'
title_zh: ViDecide：引导视频扩散模型逐步完成推理与规划
authors:
- Kaiwen Zhang
- Yiming Gao
- Zeqi Xiao
- Xintao Wang
- Pengfei Wan
- Kun Gai
- Xingang Pan
affiliations:
- S-Lab, Nanyang Technological University
- KlingAI Research
- CUHK
arxiv_id: '2611.26389'
url: https://arxiv.org/abs/2611.26389
pdf_url: https://arxiv.org/pdf/2611.26389
published: '2026-11-18'
collected: '2026-11-24'
category: Reasoning
direction: 视频扩散 · 多步推理与规划
tags:
- Video Diffusion
- Multi-step Reasoning
- Planning
- Fine-tuning
- Diffusion Model
one_liner: 提出决策中心的ViDecide框架与CFT微调方法，大幅提升视频扩散模型多步规划推理成功率
practical_value: '- Corrective Fine-tuning（CFT）无需策略梯度即可修正错误决策，可迁移到GenRec、LLM4Rec的模型微调，规避RL优化的不稳定问题

  - 固定长度生成改决策链+自主停止的范式，可复用在电商多轮导购Agent规划、商品生成式秀场的多步骤生成场景

  - 决策聚焦的训练调度思路，可用于优化搜索多步query改写、长序列用户行为建模的下游任务效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有SOTA视频生成模型虽能合成高写实视频，但在多步推理、规划任务中频繁违反物理、逻辑约束，即便基于大规模推理数据训练或用现有扩散RL方法优化仍无法解决，根源为传统训练范式将输出视为定长clip而非决策链。
### 方法关键点
1. 提出决策中心框架ViDecide，训练视频扩散模型因果预测状态转移、自主决策生成停止时机，搭配决策聚焦的训练调度策略
2. 提出Corrective Fine-tuning（CFT），将失败决策对应的噪声映射到模型自身的成功续例，无需策略梯度优化即可实现稳定性能提升
### 关键结果数字
在抽象游戏、规划任务、新增多步机器人规划基准上平均严格成功率达83.8%，远超标准微调的23.3%、此前最优方法的67.8%，可泛化到更大规模谜题与未见布局
