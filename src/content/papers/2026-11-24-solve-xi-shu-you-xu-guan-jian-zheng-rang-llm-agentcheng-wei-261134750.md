---
title: 'SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot
  Manipulator'
title_zh: SOLVE：稀疏有序关键帧让LLM Agent成为高效通用机器人操纵器
authors:
- Xiang Li
- Hongyu Zhou
- Ya-Li Li
- Tao Li
- Rui Zhang
- Junjie Lai
- Weihua Zhang
- Shengjin Wang
affiliations:
- Tsinghua University
- NVIDIA
arxiv_id: '2611.34750'
url: https://arxiv.org/abs/2611.34750
pdf_url: https://arxiv.org/pdf/2611.34750
published: '2026-11-24'
collected: '2026-11-26'
category: Agent
direction: LLM Agent 机器人操纵效率优化
tags:
- LLM Agent
- Robot Manipulation
- Sparse Keypose
- Training-Free
- Inference Efficiency
one_liner: 提出无训练SOLVE框架，通过稀疏有序关键帧降低LLM机器人Agent推理成本并提升性能
practical_value: '- 可复用「稀疏关键决策点+底层模块插值补全」架构，替代LLM逐step推理，大幅降低调用成本：例如电商全链路Agent任务拆解仅输出关键节点，下游执行层补全操作细节

  - 可借鉴Agent自主决策输出粒度的设计，根据任务复杂度动态调整输出步长，兼顾长流程效率和细粒度精度：适配大促活动调度、复杂客服咨询等多场景Agent需求

  - 训练-free的反馈迭代思路可直接复用：无需微调仅通过执行反馈蒸馏少量规则更新策略，适合业务Agent冷启动快速上线'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前LLM Agent落地机器人操纵场景时，存在推理成本高、逐step稠密控制效率低、工具依赖瓶颈三大痛点。

### 方法关键点
1. 无训练多模态LLM Agent架构，单次调用输出稀疏有序的6自由度末端执行器关键帧序列，由运动规划器负责帧间插值补全全量动作
2. Agent自主决定关键帧数量与间隔，兼顾长距离快速运动和细粒度操纵需求，输出粒度匹配遥操作天然稀疏性，DROID数据集演示可被压缩为少量关键帧
3. 支持多源带噪深度输入做关键帧grounding，可基于执行反馈反思蒸馏任务规则，抗噪性强。

### 关键结果
RoboDojo基准准确率74.5%，RoboLab基准准确率84.5%，单episode平均成本1.7美元，比此前稠密控制策略低12倍；真实机器人16项零样本任务成功率达88%。
