---
title: Bridging Physical Reasoning and Task Generalization via Visual Action Outcome
  Reasoning Alignment
title_zh: 通过视觉动作结果推理对齐提升VLM物理推理与任务泛化能力
authors:
- Han-Jun Ko
- Jr-Jen Chen
- Haobo Yuan
- Hsin-Ying Lee
- Tiancheng Shen
- Ming-Hsuan Yang
- Yu-Chiang Frank Wang
affiliations:
- National Taiwan University
- The University of California, Merced
arxiv_id: '2607.06522'
url: https://arxiv.org/abs/2607.06522
pdf_url: https://arxiv.org/pdf/2607.06522
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: 交互Agent · VLM物理推理对齐
tags:
- VLMs
- Chain-of-Thought
- Reward Design
- Generalization
- Physical Reasoning
one_liner: 提出双对齐奖励框架VAORA，解决VLM物理推理的CoT幻觉与推理-动作错位问题，提升跨场景泛化
practical_value: '- 解决VLM+Agent的CoT幻觉与推理-动作错位问题时，可复用VAORA的双奖励设计思路：独立锚定推理与视觉上下文的奖励+对齐推理与动作结果的奖励，比单纯SFT或成功驱动RL效果更稳定

  - 稀疏奖励场景下的VLM训练，可复用「预训练领域专家生成稠密成功概率估计」的方法，替代原生二元奖励，大幅降低RL训练不稳定与模型崩溃风险

  - 涉及多模态推理的推荐场景（如内容种草/搭配推荐的合理性校验），可借鉴结构化推理+符号对齐的思路：将CoT解析为结构化命题，和视觉/业务真实状态做一致性校验，减少生成结果的幻觉'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前VLMs在交互式物理推理场景泛化能力差，存在两类核心问题：一是CoT推理幻觉，不符合物理现实；二是推理与动作错位，模型依赖视觉捷径而非可迁移的物理原理。传统SFT仅模仿推理形式未接地到现实，仅优化任务成功的RL会让模型跳过CoT走捷径，均无法建立推理与物理现实的对齐监督。
### 方法关键点
- 提出VAORA双互补奖励框架：①视觉对齐奖励：将推理链的结构化符号命题和初始场景真实符号状态做一致性校验，从源头抑制CoT幻觉，与动作无关；②视觉-动作对齐奖励：包含碰撞奖励（对齐推理预测的碰撞事件与动作后视觉结果）、放置奖励（对齐推理预测的放置位置与动作后真实位置），同时解决幻觉和推理动作错位
- 引入预训练领域DQN专家生成稠密平滑的动作成功概率估计，替代稀疏二元任务奖励，稳定RL训练，且视觉-动作对齐奖励由成功概率门控，仅对物理合理的动作奖励推理质量
- 采用GDPO联合优化两类奖励，基座为Qwen3-VL-8B-SFT
### 关键实验
在PHYRE跨任务泛化测试集上，VAORA的Pass@1最高达0.382，超过DQN专家的0.338、Gemini-3.1-Flash的0.170，优于Gemini-3.1-Pro的0.278；零样本迁移到Virtual Tool跨环境场景，Pass@1达0.167，超过Gemini-3.1-Flash的0.111，和Gemini-3.1-Pro持平；在CRAFT VQA物理推理测试集上整体准确率达46.06%，较SFT基线提升1.92pct。
### 核心结论
通过对齐推理过程与视觉动作结果的奖励设计，可让VLM获得真正可迁移的物理理解能力，而非依赖训练数据的视觉捷径。
