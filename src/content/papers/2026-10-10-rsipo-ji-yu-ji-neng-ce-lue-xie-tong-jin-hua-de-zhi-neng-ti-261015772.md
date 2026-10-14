---
title: 'RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement
  Learning via Skill-Policy Co-Evolution'
title_zh: RSIPO：基于技能-策略协同进化的智能体RL递归自优化框架
authors:
- Fan Zhang
- Hao Wu
- Jinyang Wu
- Hongyu Qu
- Zheng Lian
- Xiao Luo
- Yefeng Zheng
- Bo Zhang
- Haoxuan Li
- Pheng-Ann Heng
affiliations:
- CUHK
- THU
- NUS
- Tongji University
- UW-Madison
arxiv_id: '2610.15772'
url: https://arxiv.org/abs/2610.15772
pdf_url: https://arxiv.org/pdf/2610.15772
published: '2026-10-10'
collected: '2026-10-14'
category: Agent
direction: 智能体强化学习 · 自进化优化
tags:
- Agentic RL
- Policy Optimization
- Self-Evolution
- Skill Distillation
- On-Policy Training
one_liner: 提出技能-策略协同进化的智能体RL框架，动态校准教师权重，大幅提升长周期任务性能
practical_value: '- 技能-策略协同进化思路可迁移到电商导购Agent训练：从用户交互轨迹中自动提取可复用的导购技能，动态更新技能库同时优化策略，避免静态技能库的分布偏移问题

  - 动态信任校准机制可直接用于LLM4Rec的蒸馏训练：不需要固定蒸馏权重，根据skill辅助生成的效果自适应调整蒸馏损失权重，避免不可靠教师信号干扰模型收敛

  - 轨迹重放验证技能有效性的方法可复用：在搜索推荐的模拟环境（如WebShop电商交互仿真）中验证生成的query改写、商品推荐策略的实际增益，降低线上AB测试成本

  - 无测试时技能依赖的设计适合落地：训练时用技能辅助优化，推理时不需要额外技能prompt，不增加线上推理延迟，适配推荐/搜索的低延迟要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有混合架构智能体RL结合RLVR与OPSD解决长周期任务信用分配问题，但存在两大核心缺陷：一是技能生成依赖静态离线库或预训练生成器，无法随策略迭代同步进化，存在严重分布偏移；二是默认技能增强的教师信号始终可靠，实际上教师在15%以上场景表现不如学生，会引入噪声干扰训练。
### 方法关键点
- 新增轨迹重放校验模块：每轮训练将单个任务的8次rollout随机分为证据集与控制集，从证据集的成功轨迹中由策略本身生成技能，用技能增强的策略重放4次任务，对比控制集表现计算技能重放增益
- 同策略技能进化：将重放增益减去同类型任务平均增益作为技能生成的奖励，直接优化策略的技能生成能力，实现技能与任务执行策略的协同进化
- 信任校准自蒸馏：用经验贝叶斯收缩对重放增益降噪得到任务级信任系数，自适应加权OPSD蒸馏损失，当教师表现差时直接关闭蒸馏，避免噪声干扰
### 关键结果
在ALFWorld具身交互、7个搜索类智能体任务上对比13个基线：
- Qwen2.5-7B基座下，ALFWorld平均成功率达98.6%，较次优基线SEED高2.5%，较标准GRPO高17.4%
- 搜索类任务平均准确率达50.8%，较GRPO高8.8%，优于所有基线
- 推理时无需依赖任何技能prompt，性能仍超过测试时带技能输入的基线
### 核心结论
智能体训练中技能与策略的协同进化+动态教师信任校准，可在不增加推理成本的前提下大幅提升长周期任务表现
