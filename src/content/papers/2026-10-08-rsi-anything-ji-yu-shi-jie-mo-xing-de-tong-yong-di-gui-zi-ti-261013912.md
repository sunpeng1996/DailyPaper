---
title: 'RSI-Anything: Unlocking Recursive Self-Improvement with World Models'
title_zh: RSI-Anything：基于世界模型的通用递归自提升框架
authors:
- Taoyong Cui
- Pinxian Zeng
- Wanghan Xu
- Hao Xiao
- Shuhan Xue
- Qiang Gao
- Wanli Ouyang
- Pheng Ann Heng
- Zhenfei Yin
- Yingcheng Wu
arxiv_id: '2610.13912'
url: https://arxiv.org/abs/2610.13912
pdf_url: https://arxiv.org/pdf/2610.13912
published: '2026-10-08'
collected: '2026-10-12'
category: Agent
direction: Agent 递归自提升 · 世界模型落地
tags:
- Recursive Self-Improvement
- World Model
- JEPA
- Agent Optimization
- Self-learning
one_liner: 基于JEPA-Anything搭建通用递归自提升框架，用世界模型引导动作选择与系统迭代
practical_value: '- 可复用「世界模型预测选点+反馈驱动更新+兼容性校验保留」的自提升框架，用于推荐/广告系统的策略迭代，减少A/B测试成本，比如用世界模型预筛候选排序策略，仅放top候选做线上实验

  - 异步更新+组件校验的机制可直接迁移到LLM4Rec系统迭代：排序策略（对应policy）和用户行为预测模型（对应world model）可独立更新，上线前做兼容性校验，避免单侧优化导致的整体效果下降

  - 低反馈预算下的候选排序方法可用于冷启动场景：比如新品推荐/新投放素材选品，用世界模型预评估候选效果，在有限流量下实现更快的效果提升'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
递归自提升（RSI）可将交互经验转化为系统能力的持续提升，但现有方法依赖昂贵的外部反馈，且策略迭代后世界模型的预测可靠性会随候选分布变化而下降，单侧优化策略或预测模型都无法保证整体效果提升，亟需一套通用的跨域RSI框架解决上述问题。

### 方法关键点
- 基于JEPA-Anything的跨域预测能力搭建，核心包含三大环节：世界模型预测引导动作/候选选择，反馈驱动策略与世界模型的异步更新，组件校验+兼容性校验双关卡决定更新后的策略-模型对是否保留
- 区分四类证据源（规则校验/模型预测/高保真仿真/外部实测），仅符合准入阈值的经验数据才会进入训练集，同时支持不确定性感知的候选排序，避免高不确定性的无效动作消耗反馈预算
- 支持策略与世界模型的异步更新：仅当世界模型可靠性低于阈值且数据/预算充足时才触发模型适配，避免不必要的迭代开销

### 关键实验
覆盖4类跨域任务：
1. 代码修复：固定编码模型前提下，对比静态校验器，固定世界模型的方案成功率从26.3%提升至29.2%，加入模型自适应后进一步升至31.2%，测试调用量基本持平
2. GUI交互：MiniWoB++复选框任务成功率从51%升至99%，平均动作数减少39.4%；OSWorld任务相对初始Agent提升18.4%，比RLAnything高5.5%
3. 实验室规划：5轮策略迭代后得分从21.8%翻倍至46.01%，超过业内参考系统
4. 反应优化：40次实验预算下，平均最优产率96.15%，比贝叶斯优化高13.99个百分点

### 核心结论
递归自提升的核心不是单侧优化策略或预测模型，而是通过预测-反馈-校验的闭环，让每次系统更新都能切实提升后续的决策与学习效率。
