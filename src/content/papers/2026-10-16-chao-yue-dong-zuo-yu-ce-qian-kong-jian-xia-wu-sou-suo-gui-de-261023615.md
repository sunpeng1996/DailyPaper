---
title: 'Beyond Action Prediction: Learning Search-Free Planning in Latent Space'
title_zh: 超越动作预测：潜空间下无搜索规划的学习方法
authors:
- Guanchen Du
- Jinhao Du
- Yanpeng Sun
- Shan Zhang
- Na Zhao
- Zechao Li
affiliations:
- Nanjing University of Science and Technology
- University of Oxford
- Singapore University of Technology and Design
- University of Adelaide
arxiv_id: '2610.23615'
url: https://arxiv.org/abs/2610.23615
pdf_url: https://arxiv.org/pdf/2610.23615
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 无搜索潜空间规划优化
tags:
- Latent World Model
- Search-free Planning
- Inverse Dynamics
- JEPA
- Goal-conditioned Control
one_liner: 提出HIJP无搜索潜空间规划框架，对齐动作预测与潜态转移，速度较搜索方案提升1.9-16.5x
practical_value: '- 电商导购/用户运营Agent的长路径决策可借鉴后见目标重标记思路，用历史行为轨迹中不同未来节点作为目标做数据增强，无需额外人工标注

  - 推荐/广告的多步触达序列规划可复用逆动力学+前向预测对齐的训练范式，将预测的触达动作与预估的用户状态转移做一致性约束，降低离线在线效果差

  - 对低延迟要求的实时Agent场景（如直播导购、实时推荐链路），可将测试时的搜索优化迁移到训练阶段做模型对齐，大幅降低推理延迟同时保证效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有基于Latent World Model的规划方法依赖CEM、MPPI等测试时搜索优化，推理延迟高，且单独的动作预测既无法保证目标表征包含动作相关信息，也无法保证预测动作和潜态预测模型的一致性，难以落地低延迟的实际业务场景。
### 方法关键点
- 提出HIJP端到端框架，联合训练视觉编码器、目标条件逆动力学模型、潜态预测器3个核心模块
- 采用后见目标重标记：从离线轨迹中随机采样未来不同时间步的观测作为目标，让梯度回传到目标表征，塑造动作相关的视觉特征
- 新增动作-转移一致性损失：将逆动力学模型预测的动作输入潜态预测器，将输出的下一潜态与真实观测编码对齐，约束动作生成与转移的一致性
- 推理时交替调用逆动力学模型和潜态预测器生成多步动作序列，无需在线搜索
### 关键实验
在TwoRoom、Reacher、PushT、OGCube4个视觉控制任务上对比INTACT、LeWM等8个基线，整体成功率达86.8%，超出最强基线4.9个百分点；规划速度较LeWM提升1.9-16.5×；高难度场景下动作平滑度较CEM方案高14.7-26.4×。
### 核心结论
将测试时的搜索计算转移到训练阶段，通过目标表征塑造和逆-前向模型对齐，可同时实现高规划效率与高控制性能。
