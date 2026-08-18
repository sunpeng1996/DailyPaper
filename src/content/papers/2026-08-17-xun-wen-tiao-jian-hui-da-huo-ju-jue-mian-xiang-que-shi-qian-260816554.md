---
title: 'Ask, Condition or Abstain: Reinforcement Learning for Missing-Premise Reasoning'
title_zh: 询问、条件回答或拒绝：面向缺失前提推理的强化学习框架
authors:
- Yongqi Tong
- Zhenyu Zhang
- Zimi Liu
- Kewei Fu
- Mingli Song
- Haofei Zhang
- Junshao Zhang
- Hong Zhu
- Jiang-Ming Yang
- Xin Zhang
affiliations:
- Ant International
- Zhejiang University
- Dingtalk, Alibaba Group
- Ant Group
arxiv_id: '2608.16554'
url: https://arxiv.org/abs/2608.16554
pdf_url: https://arxiv.org/pdf/2608.16554
published: '2026-08-17'
collected: '2026-08-18'
category: Reasoning
direction: LLM推理对齐 · 缺失前提响应策略
tags:
- Reinforcement Learning
- Missing Premise Reasoning
- LLM Alignment
- Reward Shaping
- Benchmark
one_liner: 提出ACA-RL强化学习框架，训练LLM在输入缺失前提时优先询问、条件回答而非拒绝或幻觉
practical_value: '- 可复用分层奖励设计思路：电商客服/导购Agent遇到用户需求信息不全时，按「主动询问补全>条件化推荐>合理拒绝」的优先级输出响应，替代直接IDK或幻觉推荐，提升用户体验

  - 可借鉴推理图引导的负样本构造方法：构造用户信息不全的query训练样本，标注缺失的关键属性（如预算、品类、使用场景），用于微调推荐对话Agent

  - 缺失前提数据混合比例可参考：训练时用30%的缺失前提样本+70%的正常样本平衡鲁棒性和常规任务效果，避免过度拒绝正常请求

  - 行为评估框架可迁移：将响应分为幻觉、无依据假设、拒绝、条件回答、主动询问5类打分，用于评估电商对话/导购Agent的不确定性处理能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于RL训练的推理模型仅适配前提完备的问题，但现实中用户查询常缺失关键前提（如电商用户问“笔记本推荐”未说明预算、用途），传统方案要么输出幻觉答案，要么统一回复IDK，实用性极低，亟需让模型学会更有价值的响应策略。

### 方法关键点
- 提出ACA-RL强化学习框架：基于推理图引导的流水线，将完备前提的问题扰动为12万条带缺失标注的训练样本，覆盖数值缺失、关系模糊、限定词丢失等6类常见缺失场景
- 设计分层结构化奖励：主动询问补全前提得1.0分，条件化回答（如“如果预算5k可推荐XX”）得0.6分，合理拒绝得0.3分，无依据假设得-0.3分，幻觉回答得-1.0分，引导模型优先输出高价值响应
- 构建274条人工验证的MPB（Missing-Premise Benchmark），用于评估模型处理缺失前提的行为表现。

### 关键实验
在Qwen3、Llama3.1系列模型上测试，对比Vanilla PPO、IDK-RL等基线：Qwen3-8B上MPB行为得分达51.73，比Vanilla PPO高43.07，比IDK-RL高3.01；同时在GSM8K、AIME'24等标准推理数据集上性能下降幅度仅为IDK-RL的40%左右，平衡了鲁棒性和常规推理能力；消融实验显示30%的缺失前提样本混合比例是效果和性能的最优平衡点，比10%配比MPB得分高15.51，比50%配比GSM8K得分高8.04。

### 最值得记住的一句话
大模型的推理能力不仅体现在能答对完备前提的问题，更要能识别任务前提不足的场景，用建设性的方式响应而非只输出确定答案或直接拒绝。
