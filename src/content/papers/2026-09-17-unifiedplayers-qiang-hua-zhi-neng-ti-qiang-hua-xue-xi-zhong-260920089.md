---
title: 'UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement
  Learning'
title_zh: UnifiedPlayers：强化智能体强化学习中的工具集成推理能力
authors:
- Wenjie Liao
- Liangjie Zhao
- Zehong Cao
affiliations:
- Waseda University
- Adelaide University
arxiv_id: '2609.20089'
url: https://arxiv.org/abs/2609.20089
pdf_url: https://arxiv.org/pdf/2609.20089
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: 智能体强化学习 · 多角色协作优化
tags:
- Agent
- Reinforcement Learning
- GRPO
- Tool-Integrated Reasoning
- Multi-Player Collaboration
one_liner: 提出三角色协作的智能体RL框架，通过共享可执行反馈解决循环依赖，提升工具集成推理效果
practical_value: '- 智能体自迭代训练可复用三角色分工+角色专属奖励的设计，避免生成/执行/评估模块互相干扰导致的退化循环，比如电商导购Agent训练可拆分为任务生成、交互执行、效果验证三个独立模块

  - 可迁移可执行验证+扰动样本校验的思路，替代传统LLM-as-judge的评估方式：比如推荐场景下对生成的推荐理由/话术，自动生成可执行校验规则（如是否匹配商品属性、是否含违禁词），再用扰动样本校验规则区分度，大幅提升评估准确率

  - 交替GRPO优化的工程实现思路可直接复用：每次仅更新一个模块、其余模块固定，大幅降低多模块Agent系统RL联合训练的不稳定性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有自进化智能体通常分离轨迹生成与评估，静态校验器无法适配新兴错误模式，自一致性信号容易强化轨迹间的共性错误；若联合适配规划、执行、评估三个模块，又会出现循环依赖问题：每个模块持续改变其他模块的训练数据或反馈，容易引发退化学习循环（如规划偏向简单可验证任务、执行强化被评估器误判的错误轨迹、评估坍缩为全接受/全拒绝规则）。

### 方法关键点
- 三角色协作框架：Planning Player生成难度适中的工具使用任务，Execution Player生成带Python工具调用的多轮交互轨迹，Evaluation Player生成可执行校验器
- 共享裁决矩阵：固定扰动引擎生成轨迹的对抗变体，沙箱执行所有校验器得到原始轨迹和变体的校验结果，形成共享可执行证据
- 角色专属奖励：基于共享裁决矩阵为三个角色设计不同奖励函数，规划奖励偏好边缘难度、可验证、非重复任务；执行奖励为校验器平均接受率；评估奖励结合原始轨迹接受率、变体拒绝率和代码多样性
- 交替GRPO优化：每次仅更新一个角色参数，其余两个固定，避免循环依赖导致的训练不稳定

### 关键实验
基于Qwen3-4B、MiMo-7B两个骨干，在7个数学推理、5个通用推理共12个基准上测试，对比Agent0等7个基线：数学推理超最强基线至少3.5%，通用推理超3.9%；学习到的校验器对抗检测准确率达84.2%，奖励的单问题方差是自一致性基线的2.03倍，区分度显著更高。

**最值得记住的一句话**：多角色智能体协作不需要共享全局奖励，通过共享可执行证据+角色专属目标的设计，就能实现稳定的协同进化，避免退化循环。
