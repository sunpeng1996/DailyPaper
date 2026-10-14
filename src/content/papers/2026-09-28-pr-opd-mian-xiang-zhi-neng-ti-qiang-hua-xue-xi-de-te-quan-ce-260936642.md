---
title: 'PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic
  Reinforcement Learning'
title_zh: PR-OPD：面向智能体强化学习的特权表征在策略自蒸馏方法
authors:
- Muyang Li
- Jie Yang
- Zhengyu Fang
- Junchao Zhu
- Zhengkun Xiao
- Ruining Deng
- Zhe Jiang
- Shigang Chen
affiliations:
- University of Florida
- University of Illinois at Chicago
- Case Western Reserve University
- Vanderbilt University
- Weill Cornell Medicine
arxiv_id: '2609.36642'
url: https://arxiv.org/abs/2609.36642
pdf_url: https://arxiv.org/pdf/2609.36642
published: '2026-09-28'
collected: '2026-10-14'
category: Agent
direction: Agent强化学习 · 自蒸馏优化
tags:
- LLM Agent
- Reinforcement Learning
- Self-Distillation
- On-policy Training
- Representation Alignment
one_liner: 通过对齐隐层表征而非token概率的自蒸馏，无推理开销提升LLM智能体多轮任务表现
practical_value: '- 电商导购/客服LLM Agent训练可直接复用PR-OPD范式：GRPO暖身后新增隐层对齐损失，相比传统token级自蒸馏增益更高，且无推理开销不影响上线性能

  - 轻量化部署的小参数LLM Agent（如7B以下端侧导购Agent）务必加入层内轻量MLP projector做隐层对齐缓冲，避免直接对齐导致的性能下降

  - 多轮交互类任务（如搜索推荐Session优化、用户多轮需求理解）的Agent训练，需先完成GRPO暖身至基础能力达标后再加自蒸馏信号，避免过早蒸馏引入噪声

  - 自蒸馏的特权信息无需额外构建外部技能库，可直接让同模型基于轨迹后验生成技能，大幅降低训练数据准备成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM智能体多轮任务训练通常用GRPO配合token级特权自蒸馏补充稀疏奖励信号，但实验发现：特权信息（如后验技能）仅会改变不到25%采样token的概率，却会改变80%以上响应token的隐层状态，token级蒸馏信号过于稀疏，无法传递特权信息带来的性能增益。

### 方法关键点
- 两阶段训练：第一阶段先用GRPO做暖身，直到模型具备基础任务执行和轨迹复盘能力
- 自生成后验技能：每个轨迹完成后，由同模型生成对应后验技能（成功轨迹总结可复用流程，失败轨迹指出错误和修正方案），无需外部技能库
- 隐层表征对齐：同模型分别执行不带技能的学生前向、带技能的stop-gradient教师前向，学生每层隐层经过轻量MLP projector后与教师对应层隐层做余弦对齐，仅新增projector模块，推理时可直接丢弃无额外开销
- 联合优化：GRPO奖励损失 + 隐层对齐损失联合训练，无输出空间蒸馏项

### 关键结果
在ALFWorld文本交互环境、WebShop电商导购环境测试，用Qwen2.5-3B、Qwen3-1.7B两个backbone，对比GRPO、SDAR等6个基线：Qwen2.5-3B上ALFWorld成功率较GRPO提升4.7个百分点，WebShop准确率提升11.7个百分点；Qwen3-1.7B上WebShop准确率较GRPO提升14个百分点，所有设置下均取得最优结果。

### 核心结论
智能体从自身后验经验中学习时，读取其特权状态的隐层表征，远比模仿其输出token有效
