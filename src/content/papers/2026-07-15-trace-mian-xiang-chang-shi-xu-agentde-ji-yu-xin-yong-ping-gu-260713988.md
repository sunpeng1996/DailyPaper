---
title: 'TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon
  Agents'
title_zh: TRACE：面向长时序Agent的基于信用评估的轮次级奖励分配
authors:
- Leitian Tao
- Baolin Peng
- Wenlin Yao
- Tao Ge
- Hao Cheng
- Mike Hang Wang
- Jianfeng Gao
- Sharon Li
affiliations:
- University of Wisconsin–Madison
- Microsoft Research
arxiv_id: '2607.13988'
url: https://arxiv.org/abs/2607.13988
pdf_url: https://arxiv.org/pdf/2607.13988
published: '2026-07-15'
collected: '2026-07-16'
category: Agent
direction: Agent强化学习 · 轮次级信用分配
tags:
- Reinforcement Learning
- Credit Assignment
- Long-Horizon Agent
- GRPO
- Tool Use
one_liner: 提出无需额外标注与critic的轮次级信用分配框架，大幅提升长时序搜索Agent性能
practical_value: '- 做多轮导购/搜索Agent RL训练时，可直接复用TRACE无critic信用分配思路，用frozen参考模型计算黄金答案log概率的log比值作为状态值，省去训练过程奖励模型或标注中间步骤的成本

  - 以工具调用边界为粒度分配奖励，可解决电商长路径转化（浏览→加购→下单）场景下终端奖励稀疏、梯度方差大的问题，给有效中间动作分配对应正向反馈

  - 超参可直接复用论文结论：turn-level奖励权重设为0.2（outcome权重1.0）、TD look-ahead窗口设为3，避免过度放大局部信号偏离最终业务目标'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长时序多轮Agent需要通过数十次工具交互完成复杂任务，仅依赖终端结果奖励的强化学习存在奖励稀疏、梯度方差大的问题：失败轨迹中的有效动作会被统一分配负反馈，有效探索无法被强化；而现有过程监督方案需要标注中间步骤、训练过程奖励模型或调用强LLM judge，成本高且容易偏离最终正确性目标。
### 方法关键点
- 以工具调用边界划分轨迹状态，使用与初始化策略权重一致的frozen参考模型，计算每个前缀状态下黄金答案的平均log概率，转化为log比值形式的状态值，衡量轨迹向答案推进的相对进度
- 用相邻状态值的TD差分作为轮次级奖励，结合K步截断TD备份传播延迟效果，同时锚定终端GRPO outcome优势，保证最终结果正确性
- 无需额外训练critic、标注过程数据、调用强Judge模型或冷启动SFT阶段，纯RL即可完成训练
### 关键实验
训练使用合成多文档搜索数据集，测评覆盖闭网BrowseComp-Plus、开网BrowseComp/GAIA/xbench-DeepSearch四个基准，对比GRPO/GSPO/GiGRPO等同条件基线：Qwen3-4B在BrowseComp-Plus准确率从7.2提升至35.6，Qwen3-30B-A3B从8.4提升至42.6，四基准平均分别提升4.5、5.6个点，训练收敛速度较GRPO快30%以上。
### 核心结论
仅用冻结参考模型的黄金答案概率变化即可生成高质量轮次级奖励信号，无需额外标注或模型训练就能大幅提升长时序Agent的训练效率与效果。
