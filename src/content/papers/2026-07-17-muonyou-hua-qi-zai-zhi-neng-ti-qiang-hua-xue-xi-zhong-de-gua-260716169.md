---
title: When Does Muon Help Agentic Reinforcement Learning?
title_zh: Muon优化器在智能体强化学习中的适用场景研究
authors:
- Kai Ruan
- Jinghao Lin
- Zihe Huang
- Ziqi Zhou
- Qianshan Wei
- Xuan Wang
- Hao Sun
affiliations:
- Renmin University of China
- Chinese Academy of Sciences
- Duke University
- Zhejiang University
- Independent Researcher
arxiv_id: '2607.16169'
url: https://arxiv.org/abs/2607.16169
pdf_url: https://arxiv.org/pdf/2607.16169
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: 智能体强化学习 · 优化器适配
tags:
- Muon
- Agentic RL
- Optimizer
- GiGPO
- GraphGPO
- GRPO
one_liner: 通过对照实验明确Muon优化器在智能体强化学习中的增益条件与适配的优势估计器
practical_value: '- 做LLM Agent RL微调时可采用混合优化器配置：仅隐藏层2D权重用Muon，embedding/归一化层等非矩阵参数沿用AdamW，GiGPO场景下可提升88%任务成功率

  - Muon增益与优势估计器粒度正相关，优先搭配带步级/状态级信用分配的RL算法（如GiGPO/GraphGPO），不要直接用于低梯度SNR的单轮RL场景

  - Muon学习率可设置为AdamW基线的10~30倍，同倍率下高学习率AdamW会完全失效但Muon可稳定收敛

  - 长序列多步决策Agent（如电商导购Agent、多轮交互推荐）场景下，联合调优优化器与信用分配策略，可最多节省60步训练达到相同效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Muon优化器在LLM预训练中相比AdamW可节省近50% FLOPs，但在RL后训练尤其是智能体RL场景的适用性存在争议，已有研究结论矛盾，部分场景下出现梯度爆炸、熵值地板等问题，其适用条件、与优势估计器的适配关系尚不明确，亟需系统对照实验验证。

### 方法关键点
- 基准模型采用Qwen2.5-0.5B-Instruct，测试环境为长horizon稀疏奖励的ALFWorld embodied交互任务
- 优化器混合配置：仅对LLM的注意力、MLP层2D隐藏权重采用Muon优化，embedding、归一化层等非矩阵参数沿用AdamW，避免全参数切换的不稳定性
- 对照三组不同粒度的优势估计器：仅episode级信用的GRPO、融合episode+步级anchor状态信用的GiGPO、基于状态转移图的细粒度GraphGPO，控制其他超参完全一致

### 关键实验结果
- 数据集为ALFWorld的6类家庭交互任务，baseline为全参数AdamW优化（lr=1e-6）
- GiGPO场景下Muon（lr=3e-5）将最终窗口验证成功率从0.290提升到0.546，相对+88%，同学习率AdamW控制组完全失去任务成功率
- GraphGPO场景下Muon（lr=1e-5）将归一化AUC从0.399提升到0.556，达到0.5/0.75成功率的步数分别提前30/60步
- GRPO场景下Muon仅将成功率从0.161提升到0.268，增益显著低于细粒度优势估计器

最值得记住的结论：Muon在智能体RL中的增益本质上依赖梯度信噪比，与细粒度信用分配的优势估计器联合使用收益最大，孤立提升AdamW学习率无法复现其效果
