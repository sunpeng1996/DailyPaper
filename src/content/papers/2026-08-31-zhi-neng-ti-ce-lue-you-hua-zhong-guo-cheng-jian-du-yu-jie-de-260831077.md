---
title: Reconciling Process Supervision with Outcome-Based Credit in Agentic Policy
  Optimization
title_zh: 智能体策略优化中过程监督与结果信用的融合方法
authors:
- Jingxiao Yang
- Wangjie Gan
- Yingxuan Zhuang
- Wenqi Zhang
- Jintao Chen
- Xuhong Zhang
affiliations:
- Zhejiang University
arxiv_id: '2608.31077'
url: https://arxiv.org/abs/2608.31077
pdf_url: https://arxiv.org/pdf/2608.31077
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent策略优化 · 过程监督与结果信用融合
tags:
- Agent Policy Optimization
- Credit Assignment
- Process Supervision
- GRPO
- Privileged Information
one_liner: 提出TASPO框架融合过程监督与结果信用，在Agent任务上较GRPO平均提升10.6%
practical_value: '- 做电商导购Agent、搜索工具调用Agent的RL训练时，可复用TASPO的信用分配逻辑：不推翻结果反馈的全局方向，仅用过程信号调整单步动作的权重，避免优化信号冲突

  - 多轮交互Agent的过程信号不要用token粒度聚合，改为可执行动作粒度（比如一次商品检索、一次属性查询），能降低训练方差，提升策略稳定性

  - 特权信息(PI)不要直接用成功轨迹硬搬，先抽象成适用条件+动作规则，再匹配当前轨迹上下文，适用性更强，还能降低对大模型分析器的依赖

  - 现有基于GRPO的Agent训练pipeline可直接接入TASPO模块，无需新增环境交互，就能获得稳定的效果提升'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长horizon智能体交互任务中，基于结果的RL（如GRPO）仅能给整条轨迹分配统一信用，无法区分不同中间动作的贡献；而现有的过程监督/特权信息（PI）细粒度信号容易与结果优化方向冲突，且token级的监督粒度与实际可执行动作不匹配，存在监督-credit gap，导致训练不稳定、泛化性差。
### 方法关键点
- 严格拆分结果信用与过程监督的作用：验证后的轨迹结果决定优化方向和全局平均权重，PI仅用于重分配单步动作的信用，不改变全局优化目标
- 从同批次成功的兄弟轨迹中抽象带适用条件的经验规则，匹配目标轨迹的交互上下文生成决策适用的PI，无匹配则退化为原始GRPO逻辑
- 计算加/不加PI时可执行动作的对数似然差，聚合为动作级的PI支持度，转换为有界、保均值的权重乘到原始轨迹优势上
### 关键实验
在ALFWorld、Search-QA、WebShop三类Agent基准上测试，对比GRPO、SDAR、StepOPSD等基线，TASPO较GRPO平均提升10.6%，ALFWorld任务上在小模型Qwen3-1.7B上成功率提升达27.4%；动作级聚合比token级聚合成功率高6.6%，训练方差降低50%+，且对PI分析器的模型选择不敏感。
> 最值得记住的结论：过程监督应该用来修正结果信用的分配权重，而不是替代结果反馈决定优化方向。
