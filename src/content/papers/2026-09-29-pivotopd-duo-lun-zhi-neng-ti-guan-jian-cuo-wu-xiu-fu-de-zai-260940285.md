---
title: 'PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents'
title_zh: PivotOPD：多轮智能体关键错误修复的在策略蒸馏框架
authors:
- Yinghui He
- Yapei Chang
- Khushi Bhardwaj
- Daniele Molinari
- Tugrul Konuk
- Jan Kautz
- Ali Hatamizadeh
affiliations:
- Princeton University
- NVIDIA
- University of Maryland
arxiv_id: '2609.40285'
url: https://arxiv.org/abs/2609.40285
pdf_url: https://arxiv.org/pdf/2609.40285
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: 多轮Agent · 在策略蒸馏训练优化
tags:
- Multi-turn Agent
- On-Policy Distillation
- RL
- Error Recovery
- LLM Training
one_liner: 结合关键错误检测与预防+恢复双蒸馏，解决多轮智能体错误累积性能瓶颈
practical_value: '- 电商导购多轮Agent、搜索交互Agent落地时，可复用关键错误检测逻辑：用稍大的teacher模型复盘失败交互轨迹，定位早期关键错误节点，无需全路径人工标注，大幅降低训练标注成本

  - 双蒸馏trick可直接复用进多轮Agent训练流：预防蒸馏用reverse KL纠正关键错误，恢复蒸馏用forward KL学习错误后的兜底路径，相比纯RL训练收敛速度提升30%以上，适配电商场景用户交互容错需求

  - 无外部大teacher时可启用自蒸馏版本：用当前学生模型自身作为teacher挖掘最优路径，性能仍优于现有10+种基线，适合端侧小模型多轮Agent轻量化落地'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
多轮交互场景下Agent的单个早期错误会导致后续状态偏离最优路径，错误累积最终引发任务失败。现有on-policy distillation（OPD）只能消除非关键路径错误，对决定最终成败的关键错误（pivotal mistake）修复效果极差；统计显示超过50%的失败轮次都源于早期可恢复的关键错误，但学生模型几乎不会自发采样到恢复路径，缺乏有效学习信号。
### 方法关键点
1. 关键错误检测：用teacher模型复盘全轨迹，定位学生动作与最优gold action不一致的关键节点，同时输出后续K步的恢复动作序列
2. 特权自教师构造：冻结当前学生模型，注入gold/recovery动作hint作为自教师，生成符合学生自身推理风格的监督样本，避免跨模型蒸馏的风格 mismatch
3. 双蒸馏联合训练：预防蒸馏用reverse KL引导学生避开关键错误，恢复蒸馏用forward KL提升学生在错误后状态下的恢复动作概率，两类损失和标准PPO loss联合优化
### 关键实验
在ALFWorld、WebShop（模拟电商导购）、搜索QA、SWE-Bench四个基准上对比13种基线：Qwen3-1.7B学生模型在ALFWorld上较最强基线提升+5.5%，WebShop任务成功率提升+14.1%；Nemotron-3.5学生模型在SWE-Bench上较标准OPD多提升+3.2%；无外部teacher的自蒸馏版本也较基线平均提升+3.9%。
### 核心结论
多轮Agent的失败大多源于早期少数可恢复的关键错误，针对性给这些节点加监督信号的效率远高于全路径无差别优化。
