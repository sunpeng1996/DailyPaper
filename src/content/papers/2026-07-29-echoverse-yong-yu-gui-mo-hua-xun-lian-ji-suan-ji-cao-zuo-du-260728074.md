---
title: 'Echoverse: Deep, Evolving Environments for Training Computer-Use Agents at
  Scale'
title_zh: Echoverse：用于规模化训练计算机操作Agent的深度演化环境
authors:
- Yash Pandya
- Sahil Gupta
- Sarthak Harne
- Archana Yadav
- Kavyansh Chourasia
- Hussein Mozannar
- Vibhav Vineet
- Sara Abdali
- Corby Rosset
- Yash Lara
affiliations:
- Microsoft Research
arxiv_id: '2607.28074'
url: https://arxiv.org/abs/2607.28074
pdf_url: https://arxiv.org/pdf/2607.28074
published: '2026-07-29'
collected: '2026-07-31'
category: Agent
direction: Agent 训练环境构建与协同演化
tags:
- Computer-Use Agent
- Synthetic Environment
- Co-Evolution
- Reinforcement Learning
- Agent Training
one_liner: 提出深度可演化合成训练环境，规模化训练计算机操作Agent缩小与前沿模型差距
practical_value: '- 搭建电商/商家后台操作类Agent的训练环境时，优先做带完整后端状态流转、数据库级结果校验的深度环境，避免使用仅复刻UI的浅层环境——论文证实浅层环境训练会让模型效果低于基线，反而不如不训练

  - 可复用「环境-模型协同演化」训练流程：每次迭代先基于失败case修复环境/任务/校验器的缺陷，再将验证有效的失败case加入训练集，避免用错误的环境信号误导模型

  - 训练Agent的高频专项能力（如电商的日期选择、多条件筛选、表单填写）时，仅生成该能力的多布局变体训练集即可实现跨场景泛化，无需新增大量无关域数据

  - 长流程Agent的RL训练可采用组合奖励设计：终态用数据库校验的可信奖励保证目标正确，步骤级用动作有效性稠密奖励解决长轨迹信用分配问题，无需额外改造环境'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有计算机操作Agent训练依赖真实系统，但登录态业务系统（如电商后台、支付账户）无法直接开放训练，批量生成的浅层合成环境仅复刻UI、无完整状态流转，训练不仅无法提效，反而会让模型习得错误交互习惯，环境质量（而非数量）成为Agent能力提升的核心瓶颈。

### 方法关键点
- 定义环境「深度」的5个可量化属性：行为保真、跨角色状态一致、工作流依赖完整、数据库级权威校验、目标域价值，仅满足深度要求的环境可输出有效训练信号
- 两阶段环境生成流水线：先从种子规则生成带前后端+数据库的完整可运行应用，通过自动化校验修复保证所有目标工作流可执行；再生成基于数据库真实状态的任务集，所有任务都通过真实界面可达性校验
- 「环境-模型协同演化」循环：同一条模型失败轨迹先用于修复环境、任务、校验器的缺陷，确认任务有效后再作为模型训练信号，禁止降低任务难度虚高通过率
- 天然支持RL训练：自带精确状态重置、高吞吐并行能力，采用「终态数据库校验奖励+步骤级动作有效性稠密奖励」的组合设计解决长轨迹稀疏奖励问题

### 关键结果
- 基于12个深度环境训练的9B参数Agent，在14个评估集上准确率从36.5%提升至67.1%，仅比大10倍以上的前沿教师模型低14个百分点
- 同域浅层环境会让真实站点准确率从80.0%降至75.0%，深度环境则提升至85.0%
- 专项能力训练后，未见过的控件泛化准确率提升超20pct，RL训练后任务准确率进一步从58.8%提升至68.0%

**最值得记住的一句话**：低于深度阈值的训练环境不仅无法提升Agent能力，反而会引入噪声让效果倒退，环境的多样性比单环境的轨迹规模对泛化更重要。
