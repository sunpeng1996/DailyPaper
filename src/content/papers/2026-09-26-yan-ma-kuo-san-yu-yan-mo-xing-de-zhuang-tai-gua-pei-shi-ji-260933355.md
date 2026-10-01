---
title: 'Unmask the State: When Does State Adaptation Matter for Masked Diffusion Language
  Models'
title_zh: 掩码扩散语言模型的状态适配时机与选择性优化方法
authors:
- Injin Kong
- Sunghwan Choi
- Yohan Jo
affiliations:
- Seoul National University
arxiv_id: '2609.33355'
url: https://arxiv.org/abs/2609.33355
pdf_url: https://arxiv.org/pdf/2609.33355
published: '2026-09-26'
collected: '2026-10-01'
category: LLM
direction: 掩码扩散LLM · 推理策略优化
tags:
- Masked Diffusion LLM
- Inference Optimization
- State Adaptation
- Selective Policy
- Decoding Strategy
one_liner: 提出掩码扩散模型五轴推理策略框架，通过选择性状态适配仅干预少量状态即可大幅提升生成质量
practical_value: '- 生成式推荐/电商文案生成场景若采用扩散LLM并行解码，可复用五轴策略框架拆解现有解码逻辑，仅针对性优化单轴即可快速迭代，无需全链路改造

  - Agent决策、推荐系统实时规则调度等场景可复用「高收益状态识别+选择性干预」架构，相比全局自适应开销更低、收益更稳定，避免全量适配的负向效果

  - LLM推理加速业务可直接复用轻量状态检测器设计，仅用验证集校准阈值，即可用10%以内的额外开销捕获50%+的潜在性能收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
掩码扩散语言模型（MDM）支持灵活的非自回归生成顺序，现有解码策略多采用固定unmask规则，无法适配不同生成阶段的状态差异，全局自适应策略又容易引入不必要开销甚至负向效果，此前没有明确框架判断何时调整解码策略可获得最大收益。
### 方法关键点
- 将MDM的unmask策略拆解为5个独立轴：score（优先级打分规则）、cardinality（每步解锁token数）、region（可解锁区域）、commitment（预测是否可修改）、planning（是否考虑未来去噪），实验聚焦前4个单轴优化
- 定义适配机会为最优状态依赖动作相对固定验证策略的单步效用增益，通过策略反转分解将增益拆分为反转频率和平均增益幅度两部分，量化收益分布
- 提出选择性适配架构：先用单轴诊断器生成候选调整动作，再用验证集校准的轻量检测器识别高适配机会的状态，仅对符合阈值的状态调整策略，其余保留默认固定策略
### 关键实验
在LLaDA-8B、LLaDA-1.5、Dream-7B三个主流MDM，10个生成任务上验证：仅对10%的最高机会状态做region轴适配，即可在LLaDA-8B约束JSON填充任务上捕获56.9%的oracle收益，单步效用提升0.0453；端到端生成中，选择性适配相比固定策略在三个模型上分别获得20.5、15.4、10个百分点的任务效用提升，远优于全局自适应策略（全局适配在多个任务上出现效果下降）。
### 核心结论
MDM的状态适配收益高度集中在少量特定状态，选择性干预高收益状态的效果远优于全局统一适配
