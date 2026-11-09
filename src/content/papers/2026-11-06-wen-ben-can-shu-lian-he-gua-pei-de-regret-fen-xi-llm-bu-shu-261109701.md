---
title: Where Should Learning Live? Regret Analysis for Text, Parameter, and Joint
  Adaptation
title_zh: 文本/参数/联合适配的 regret 分析：LLM 部署的学习位置选择
authors:
- Jungtaek Kim
- Jaden Park
- Jongwon Jeong
- Emmanouil-Vasileios Vlatakis-Gkaragkounis
- Kangwook Lee
affiliations:
- University of Arkansas
- University of Wisconsin–Madison
- KRAFTON
- Ludo Robotics
arxiv_id: '2611.09701'
url: https://arxiv.org/abs/2611.09701
pdf_url: https://arxiv.org/pdf/2611.09701
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM适配策略 · 在线学习regret分析
tags:
- Online Learning
- Regret Analysis
- LLM Adaptation
- Prompt Engineering
- LoRA
- Parameter Efficient Tuning
one_liner: 从regret视角量化对比LLM部署中纯文本、纯参数、联合三类适配模式的性能与代价
practical_value: '- 做LLM驱动的电商推荐/对话Agent时，可将业务损失拆分为选择regret、候选集限制损失、历史状态效应三个独立项，分别优化，避免混淆适配模式选择与切换策略的效果

  - 若业务场景历史状态有害（比如用户会话被之前的错误推荐干扰），采用Lazy EW策略减少配置切换次数可降15%+累计损失；如果历史状态有益（比如正确上下文继承）则多切换反而更好

  - 纯prompt优化（文本适配）的内部选择regret更低，但候选集性能上限差，预算充足时优先构建prompt+LoRA的联合候选池，可降低30%左右的累计失败数

  - 仅能拿到实际部署反馈时，可采用分块固定配置的策略，块长匹配状态影响窗口，能在无反事实反馈的场景下控制regret上限'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM部署过程中会持续选择prompt、LoRA等适配配置，但纯文本、纯参数、联合三类适配模式的性能差异缺乏统一量化框架，且历史部署状态会影响后续损失，传统regret分析未覆盖这类带状态的持续选择场景，无法指导实际业务的部署策略选择。
### 方法关键点
- 将累计超额损失拆解为三个独立可量化项：对角选择regret（候选池内选择的额外损失）、家族限制损失（候选池相比全联合候选池的固定性能差）、符号状态效应（实际部署历史带来的增益/损失）
- 提出带状态场景下的Lazy Exponential Weights选择策略，通过限制切换次数控制状态带来的regret，给出全反事实反馈、稀疏探针、仅部署反馈三类不同信息条件下的regret上界
- 证明非加性损失场景下，坐标依次采样（先选prompt再选参数）的regret显著高于联合采样
### 关键实验
基于Qwen3.5-9B在Spider、SParC数据集上验证：纯文本适配的族内选择regret比联合适配低15%，但家族限制损失更高，最终累计失败数比联合适配高30%；历史状态有害时，Lazy EW比普通独立采样的累计损失低18%，历史有益时则高21%；仅部署反馈下，块长匹配状态影响窗口时regret比逐轮切换低22%。
### 核心结论
低族内regret、高最优选择率、低切换次数三者都不直接等价于更低的累计部署损失，需结合候选集上限、状态效应选择适配模式与切换策略。
