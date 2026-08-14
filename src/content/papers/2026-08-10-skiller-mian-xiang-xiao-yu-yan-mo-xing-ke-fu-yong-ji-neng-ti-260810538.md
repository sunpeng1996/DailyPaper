---
title: 'SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction
  in Small Language Models'
title_zh: SKILLER：面向小语言模型可复用技能提取的语言级强化学习框架
authors:
- Chenhao Dang
- Siyuan Xiong
- Conghui He
- Weijia Li
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- Harbin Institute of Technology, Shenzhen
- Tsinghua Shenzhen International Graduate School
arxiv_id: '2608.10538'
url: https://arxiv.org/abs/2608.10538
pdf_url: https://arxiv.org/pdf/2608.10538
published: '2026-08-10'
collected: '2026-08-14'
category: Agent
direction: Agent 技能生成 · 小模型落地优化
tags:
- Agent Skill
- Reinforcement Learning
- Small Language Model
- Actor-Critic
- Natural Language Policy
one_liner: 基于大模型Actor-Critic的语言级RL框架，无需微调即可为小语言模型生成定制化可复用Agent技能
practical_value: '- 可复用「大模型做优化器、小模型做执行器」架构，针对电商客服、广告文案生成等高频重复场景，离线用大模型生成小模型专属执行技能，无需微调即可提升小模型任务成功率，大幅降低推理成本

  - 语言级RL反馈机制可直接迁移到prompt迭代场景：用执行轨迹、参考成功轨迹、验证诊断三元组作为反馈，自动优化prompt/技能，替代人工调prompt流程，适合搜索query改写、商品属性标准化等规则明确的场景

  - 技能生成时优先将复杂逻辑封装为确定性helper脚本、减少prompt冗余的设计，适配边缘端部署的小模型电商Agent，可显著降低小模型幻觉概率，提升执行稳定性

  - 验证了结构化高频任务下，优化小模型执行规则的性价比远高于盲目增大模型参数，电商/推荐场景可优先针对Top N高频任务做技能定制，用7B/14B小模型达到接近70B大模型的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent技能大多为大参数闭源模型设计，部署推理成本极高；开源小模型虽然成本低，但大模型的技能直接迁移到小模型会因能力不匹配出现严重执行失败（如幻觉步骤、跳步、指令过载），缺乏专门针对小模型的自动化技能生成方法，阻碍了小模型Agent的规模化落地。

### 方法关键点
- 将文本形式的Agent技能作为可优化策略，无需更新小模型参数，所有RL信号（状态、奖励、策略更新）全部通过结构化自然语言传递
- 用大参数前沿模型同时作为Actor和Critic：Critic对比小模型实际执行轨迹与参考成功轨迹，定位最早因果错误，输出可落地的技能修改建议；Actor基于建议对技能做增删改的边界编辑，还可自动生成任务本地helper脚本，将复杂逻辑从prompt转移到确定性代码
- 新增文本形式Replay Memory，存储失败特征、诊断记录、有效修改历史，避免重复踩坑，保护已验证有效的技能内容

### 关键实验
基于Qwen3.5-9B、Qwen3.5-4B两个小模型，在5个主流Agent技能基准上对比4个现有技能生成基线：9B模型相对基线最高提升20.4pp，4B模型最高提升13.3pp；SkillsBench单技能任务上，小模型+SKILLER技能效果追平闭源大模型，推理成本降低71~167倍；4B模型+SKILLER技能在SWE-Skills-Bench的通过率超过使用普通技能的9B模型。

### 核心结论
对于结构化高频任务，为小模型定制匹配其能力边界的执行规则，收益远高于盲目增加模型参数规模
