---
title: Shockingly Simple Self-retrospection Improves Agentic Models Without RL
title_zh: 无需RL的极简自回顾微调方法ROFT提升智能体模型性能
authors:
- Jonathan Light
- Christopher Zhang Cui
- Jeonghye Kim
- Roger Creus Castanyer
- Emiliano Penaloza
- Zhengyan Shi
- Alessandro Sordoni
- Marc-Alexandre Côté
- Xingdi Yuan
- Minseon Kim
affiliations:
- RPI
- UC San Diego
- KAIST
- Mila
- Microsoft Research
arxiv_id: '2609.35741'
url: https://arxiv.org/abs/2609.35741
pdf_url: https://arxiv.org/pdf/2609.35741
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: 智能体·无RL自监督训练优化
tags:
- AgentTraining
- ROFT
- Self-Retrospection
- RL-Free
- Fine-Tuning
one_liner: 提出仅训练自生成回顾文本的ROFT方法，训练效率比GRPO高63%且性能更优
practical_value: '- 电商导购/客服Agent低成本迭代：无需复杂RL框架，仅让Agent对历史交互成败生成回顾文本做SFT，即可提升决策准确率，降低标注成本

  - 推荐稀疏奖励场景适配：新商品/新用户无正样本时，可让模型对负反馈轨迹生成归因回顾作为训练目标，突破纯RL无正样本无法训练的限制

  - 训练效率优化：可在现有GRPO/RLHF训练流程中增加回顾文本训练分支，少量额外成本即可提升泛化性、减少过拟合

  - 行为引导：调整回顾生成prompt（如要求回顾最短转化路径），无需额外损失函数即可让Agent输出更短的决策路径，优化推荐/导购转化效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RL类智能体训练依赖稀疏的二进制成功/失败奖励，无法细粒度归因中间决策的对错，全负样本轨迹组无法提供有效梯度，且GRPO等方法训练成本高、易过拟合；过往回顾类方法要么依赖外部教师标注，要么仅把回顾当推理上下文，无法验证仅自回顾训练能否提升智能体性能。

### 方法关键点
- 提出Retrospection-Only Fine-Tuning（ROFT）极简流程：智能体完成任务后，基于轨迹和反馈自生成回顾文本，仅对回顾文本做next-token prediction SFT，任务轨迹仅作为上下文不参与损失计算
- 无需外部教师、无需RL策略更新、无需额外验证器，后续推理不依赖回顾文本，性能提升完全通过权重更新传递
- 支持自定义回顾prompt引导训练方向，可对回顾中证据、修正、经验等片段加权进一步提升效果

### 关键实验
基于Qwen3.5-4B/9B基模型在SWE-bench系列代码任务数据集上验证，对比GRPO等主流RL训练方法：ROFT在SWE-bench Verified上达到49.2% solve rate，比GRPO的48.0%高1.2pp，训练时间仅3.05小时，比GRPO的8.3小时少63%；在全负样本（64次尝试全失败）的任务上也能获得1.75%~3.29%的solve rate，突破RL训练的无正样本限制；调整回顾prompt要求优化路径，可让后续决策长度缩短11.7%，无需额外长度损失。

### 核心结论
智能体无需RL，仅通过训练自生成的经验回顾文本就能实现性能提升，且训练效率更高、泛化性更好，为稀疏奖励场景的智能体训练提供了全新路径。
