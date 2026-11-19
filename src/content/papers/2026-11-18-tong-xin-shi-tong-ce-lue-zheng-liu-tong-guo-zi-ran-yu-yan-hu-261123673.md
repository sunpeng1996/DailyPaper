---
title: 'Communicative On-Policy Distillation: Distilling Black-Box Teacher Capabilities
  through Communication for Long-Horizon Tasks'
title_zh: 通信式同策略蒸馏：通过自然语言交互蒸馏黑盒大模型能力用于长序列任务
authors:
- Lirui Luo
- Kelong Mao
- Xinwei Yang
- Rongqing Li
- Luyu Chen
- Kieran Wong
- Yudong Guo
- Xinrui Wang
- Jiayin Zhu
- Gu Simiu
affiliations:
- Peking University
- JD.com
- Sichuan University
- Beijing Institute of Technology
- Renmin University of China
arxiv_id: '2611.23673'
url: https://arxiv.org/abs/2611.23673
pdf_url: https://arxiv.org/pdf/2611.23673
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 黑盒知识蒸馏优化
tags:
- On-Policy Distillation
- Black-Box LLM
- Agent Training
- Long-Horizon Task
- Knowledge Distillation
one_liner: 提出COPD框架，通过学生自主自然语言交互从黑盒教师蒸馏能力，大幅提升长序列任务无教师推理性能
practical_value: '- 垂直领域Agent小模型轻量化可复用COPD范式：不需要黑盒大模型的logits，仅通过自然语言问答就能把GPT-4o/DeepSeek等商用API的能力迁移到小模型，大幅降低蒸馏的门槛

  - 长序列任务（如电商全链路运营Agent、复杂售后处理Agent）训练可借鉴「成功交互轨迹入库+同策略自蒸馏」pipeline，无需人工预设求助模板，模型自主学习何时/如何求助，同时避免推理时依赖大模型

  - 蒸馏目标可复用PPO+自蒸馏损失的联合优化方式，比单纯SFT拟合成功交互轨迹的效果提升4.4个百分点，能更好地把交互获得的知识内化到小模型参数中'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统On-Policy Distillation (OPD) 依赖教师模型的logits输出，但商用闭源黑盒大模型仅返回文本结果，无法获取logits，导致现有蒸馏方法无法实现黑盒教师向小模型迁移长序列任务能力。而人类学习无需logits，通过向经验更丰富的对象请教并内化知识即可独立解决问题，可借鉴该逻辑实现无logits依赖的黑盒蒸馏。

### 方法关键点
- 学生模型自主决策何时向黑盒教师发起开放域自然语言求助，无预设问题模板或干预时机，求助动作和任务执行动作共享同一套参数，用PPO联合训练
- 仅保留带教师交互且任务成功的轨迹存入滚动语料库，作为特权参考信息
- 同策略自蒸馏阶段，同一条无教师执行的token同时用普通学生视角和带成功参考轨迹的特权学生视角打分，用两者对数概率差作为蒸馏信号，和PPO任务损失联合优化

### 关键实验
在CAMG-II长序列任务基准（含电商Shop、代码、视觉等5个领域）训练，以DeepSeek-V4.1-Flash为黑盒教师，对比5种现有黑盒OPD基线：COPD-4B平均任务成功率达59.8%，比基线最优的ActionOPD高8.6个百分点，增益是其2.46倍；比冻结Qwen3.5-4B基线高14.5个百分点。能力可迁移到Terminal-Bench 2.1和SWE-Bench Pro V2，COPD-9B性能接近35B同系列大模型。消融实验显示，去掉自蒸馏损失性能掉12.3个百分点，用SFT替代自蒸馏掉4.4个百分点，去掉交互环节掉7.7个百分点。

### 最值得记住的一句话
成功的交互本身不代表能力内化，只有通过同策略自蒸馏把任务相关的指导信息整合到学生自身策略中，才能实现无教师时的性能提升。
