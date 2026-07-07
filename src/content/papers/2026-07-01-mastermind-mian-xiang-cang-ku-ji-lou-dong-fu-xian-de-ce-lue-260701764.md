---
title: 'Mastermind: Strategy-grounded Learning for Repository-Scale Vulnerability
  Reproduction'
title_zh: Mastermind：面向仓库级漏洞复现的策略锚定学习框架
authors:
- Mingzhe Du
- Luu Anh Tuan
- Tianyi Wu
- Renyang Liu
- Zhijiang Guo
- Dong Huang
- See-Kiong Ng
affiliations:
- National University of Singapore
- Nanyang Technological University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2607.01764'
url: https://arxiv.org/abs/2607.01764
pdf_url: https://arxiv.org/pdf/2607.01764
published: '2026-07-01'
collected: '2026-07-07'
category: Agent
direction: Agent 高层策略学习与跨执行器迁移
tags:
- LLM Agent
- GRPO
- Dual-loop Framework
- Strategy Learning
- Policy Optimization
one_liner: 提出双循环策略学习框架，训练可迁移高层决策策略，适配多冻结执行器提升Agent长路径任务表现
practical_value: '- 长路径Agent系统可拆分高层策略规划与底层执行模块，策略模块用SFT+GRPO训练通用决策逻辑，执行器全程冻结，大幅降低多LLM后端适配的训练成本，适合电商导购、智能客服类Agent架构

  - 引入双循环存储设计：经验循环存储任务级局部事实（如单用户历史反馈、单次推荐实验失败原因）避免模型权重记忆无效信息，策略循环学习跨任务可迁移的决策模式，兼顾个性化匹配与跨场景泛化性

  - 长路径稀疏奖励任务可设计分层里程碑式奖励，配合GRPO组内相对优势归一化提升训练稳定性，解决推荐/广告多步优化中最终转化信号稀疏的收敛困难问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent在仓库级漏洞复现这类长路径复杂任务中，瓶颈不在底层命令执行、代码生成能力，而在高层策略选择；过往方案要么仅训练规划器但不保留跨轮次任务经验，要么存储经验但规划器保持冻结，策略优化效率低、跨执行器迁移性差，大量rollout浪费在无效探索方向。
### 方法关键点
- 双循环架构：经验循环由Curator存储任务局部事实（失败假设、文件位置、解析器行为等），策略循环用SFT+里程碑式GRPO训练可迁移的策略生成器，执行器全程冻结，实现策略与执行逻辑解耦
- 策略作为核心学习单元：限制单策略长度不超过2000token，比完整执行轨迹更紧凑稳定，天然适配跨执行器迁移
- 8种slot条件采样：训练时每组生成8个差异化方向的策略，避免重复同质尝试，提升探索效率
- 分层里程碑奖励：将任务拆分为7个递进里程碑，提供密集奖励信号，解决长路径任务最终奖励稀疏的训练难题
### 关键实验
在CyberGym基准的200个holdout任务上测试，对比Best-of-8采样、迭代改进、PAGENT等基线：搭配冻结GPT-5.5执行器时，Mastermind pass率达84.5%，比Best-of-8高21.5pp，比迭代改进高7.5pp；同一个训练好的规划器可直接迁移到GPT-5.4 mini、GLM5.1执行器，分别将pass率从45%提升到60%、58.5%提升到71%，推理rollout成本比基线低30%以上。

最值得记住的一句话：对于执行能力足够但策略选择困难的长路径Agent任务，把高层策略而非完整执行轨迹作为学习单元，是兼顾效率、泛化性与迁移性的核心路径。
