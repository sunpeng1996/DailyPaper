---
title: 'Memento 3: Model-Based Recursive Self-Improvement through Reflective Rulebooks'
title_zh: Memento 3：基于反思规则库的模型驱动递归自改进Agent
authors:
- Haoyu Zhao
- Zhengxu Yu
- Zhiyuan He
- Meng Fang
- Rasul Tutunov
- Haitham Bou-Ammar
- Weilin Luo
- Jun Wang
affiliations:
- University College London
- Huawei Noah’s Ark Lab, UK
- University of Liverpool
arxiv_id: '2610.11794'
url: https://arxiv.org/abs/2610.11794
pdf_url: https://arxiv.org/pdf/2610.11794
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: Agent 外置规则库驱动递归自优化
tags:
- RecursiveSelfImprovement
- ExternalMemory
- LLMAgent
- WorldModel
- RuleLearning
one_liner: 冻结LLM通过外置规则库与可执行代码双记忆实现无需微调的递归自改进
practical_value: '- 可复用「自然语言规则库+可执行代码」双层外置记忆架构，无需微调LLM即可让业务Agent持续学习电商营销、广告投放等动态规则，大幅降低迭代成本

  - 双校验机制可直接迁移到业务规则更新流程：代码全量历史重放保证执行正确性，LLM规则一致性校验保证和业务意图对齐，避免资损

  - 多并行世界模型的探索策略可用于推荐冷启动场景，同时验证多个用户行为假设，缩短收敛周期，减少线上试错成本

  - Git版本化记忆管理思路可落地到高可用业务Agent，支持规则迭代的可追溯、快速回滚，满足广告/推荐的稳定性要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent在陌生动态环境下的持续学习面临两大痛点：一是微调LLM更新规则成本高、不可解释，易出现灾难性遗忘；二是纯参数化自改进方案缺乏可审计性，无法满足业务场景对规则可追溯、可修正的强要求。

### 方法关键点
- 核心采用Code as Model设计，外置两层记忆：自然语言规则库记录可解释的环境规则假设，可执行代码是规则的落地实现，用于预测和规划，底层LLM完全冻结无需微调
- 迭代闭环：观测→反思→规则修订→代码编译→验证的5步循环，预测错误触发规则/代码更新，只有通过「历史交互全量重放校验+LLM规则一致性校验」的更新才会被采纳
- 拓展能力：支持N个并行世界模型，共享交互数据，每个规划轮次随机采样不同模型指导探索，降低单模型初始假设错误导致的路径依赖
- 记忆版本化：用Git管理所有历史规则和代码版本，支持回溯、对比和回滚

### 关键实验结果
- 在ARC-AGI-3的25个公开游戏上，单模型通关所有关卡，平均RHAE达100（满分），动作消耗仅为人类的44%，比次优基线高1个百分点，动作消耗低8.7%
- 消融实验显示，加入规则库后动作消耗降低9%，迭代轮次减少18%；双模型并行在wa30游戏上动作消耗比单模型降低34%
- Atari Pong案例中，习得的控制器无需额外LLM调用就能以21:0赢下所有测试局

### 最值得记住的一句话
不依赖LLM参数微调，通过可解释、可校验的外置记忆层实现自改进，是兼顾Agent性能、可控性和迭代效率的可行路径
