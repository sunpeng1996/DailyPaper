---
title: 'Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond
  Policy Limits'
title_zh: 推理阶段干预（RTI）：突破智能体强化学习的策略能力边界
authors:
- Chen Xi
- Ding Ruixue
- Wang Zhigaoyuan
- Zhang Fanrui
- Zhang Qiang
- Chen Boli
- Wang Shihang
- Wang Tianfu
- Ren Ailin
- Wang Pengyong
affiliations:
- Alibaba Group
- Amap, Alibaba Group
- HKUST (Guangzhou)
arxiv_id: '2610.13438'
url: https://arxiv.org/abs/2610.13438
pdf_url: https://arxiv.org/pdf/2610.13438
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 强化学习训练优化
tags:
- LLM Agent
- Reinforcement Learning
- GRPO
- Trajectory Correction
- On-policy RL
one_liner: 基于推理阶段自干预的RL训练框架，无需强教师即可突破模型原有能力边界
practical_value: '- 电商客服/导购多轮Agent的RL训练可直接复用RTI的Validator-Corrector-Verifier自干预pipeline，仅基于业务reward规则就能修正失败轨迹补充训练信号，解决冷启动成功样本稀疏问题

  - 做Agent RL优化时可直接复用PPL-based分布门控，参考实验最优阈值δ=5过滤偏离原生策略过远的干预轨迹，避免训练不稳定或策略崩坏，比全量off-policy干预数据训练更稳定

  - 业务多轮交互Agent的RL训练可借鉴推理偏移感知token重加权技巧，将更新权重集中在干预修正的关键token上，提升credit assignment效率，减少噪声对训练的干扰'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent RL方法受限于on-policy推理瓶颈：当任务超过模型当前能力边界时，成功轨迹极度稀疏，训练容易崩溃；而教师引导方法的效果又受限于教师模型的能力天花板，无法突破上限。

### 方法关键点
- **奖励感知多智能体干预**：采用Validator（仅检测会导致任务失败的关键错误）→Corrector（最小化修正错误，保留原有推理风格、格式）→Verifier（校验无特权信息泄露、符合业务规则）的三角色pipeline，所有角色可复用当前策略模型本身，无需额外强教师
- **PPL分布门控**：计算干预后轨迹在原生策略下的PPL，仅保留PPL≤阈值的轨迹，过滤分布偏移过大的样本，避免训练不稳定
- **推理偏移感知token重加权**：计算修正后token在干预prompt和原生rollout prompt下的似然比，加权GRPO的优势函数，把更新重点放在修正的关键决策token上，提升梯度利用效率

### 关键结果
在导航、τ2-Bench（电信/零售/航空）、Claw-Eval-Hard20共5个基准上对比GRPO、AEPO、OPD、LUFFY等主流RL baseline：Qwen3-8B下RTI的导航任务Pass@1比GRPO高22pp，τ2-Telecom高24.56pp，Claw-Eval-Hard20高27.5pp；Qwen3.5-9B下Claw-Eval-Hard20的Pass@1达到85%，比次优LUFFY高23.75pp，效果超过Claude-4.6-Sonnet等大模型。

最值得记住的结论：小模型Agent的能力边界并非固定，通过自干预修正失败轨迹提供有效训练信号，完全可以突破原有能力上限，无需依赖更强的教师模型。
