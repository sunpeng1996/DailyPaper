---
title: Recurrent Harness for Agentic Continual Learning
title_zh: 面向智能体持续学习的循环运行时框架ReHarness
authors:
- Yuxin Xiao
- Zhiyun Lu
- Jianyu Wang
- Yangtian Zhang
- Yang Song
- Qifan Wang
- Bailin Wang
affiliations:
- Massachusetts Institute of Technology
- Meta MRS Research
- Yale University
arxiv_id: '2610.12668'
url: https://arxiv.org/abs/2610.12668
pdf_url: https://arxiv.org/pdf/2610.12668
published: '2026-10-07'
collected: '2026-10-12'
category: Agent
direction: 智能体持续学习 · 运行时框架优化
tags:
- Agent Continual Learning
- Agent Harness
- Online Learning
- Reflection Revision
- LLM Agent
one_liner: 为纯在线流式场景下的LLM智能体新增反向经验修正机制，无需更新模型参数即可提升持续学习效果
practical_value: '- 电商导购/客服Agent的长周期用户交互场景可复用反向修正逻辑：每次交互后用实际效果修正之前提取的用户画像/偏好规则，避免过时/过泛的经验误导后续推荐，不需要更新模型参数

  - 推荐系统的在线规则池可借鉴该框架的修正机制：每次规则召回效果不达预期时，自动补充规则适用条件，不用离线重训即可适配流量分布变化

  - 纯在线流式场景优先选择结构化经验存储而非全量历史上下文：实验显示ReHarness比全量历史上下文省3.4倍token，仅比Top-K Raw高2倍左右成本，效果提升显著

  - 经验修正的grounding约束可直接复用：要求所有修正后的经验必须可被原始来源轨迹支撑，避免引入幻觉信息误导后续决策'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM智能体的持续学习Harness仅支持前向信息流动，写入的记忆/反思一旦生成就不会根据后续使用效果更新，容易出现过泛、过时的经验误导后续决策；且大多依赖离线重放/验证集优化，无法适配无额外标注的纯在线流式场景。

### 方法关键点
- 新增独立Revision Agent，每次决策完成后，用当前交互轨迹的反馈，反向修正本次决策用到的所有历史反思
- 修正严格遵循grounding约束：所有修正后的内容必须可被该反思对应的原始源轨迹支撑，仅补充适用条件、修正错误假设，禁止泄露当前轨迹的信息
- 修正后的经验一方面替换原有记忆库中的旧经验，另一方面作为示例引导本次新经验的提取，形成闭环

### 关键实验
在3个持续学习基准（CL-Bench、MemoryBench、MemoryArena）、3个主流大模型（Claude 4.8、GPT-5.5、Gemini 3.7）上测试，对比Mem0、RBank、全量上下文等7个强基线，平均归一化增益达0.240，比Top-K Raw高42.9%，比全量上下文高46.3%，所有提升均统计显著（padj<0.05）；修正后的经验源轨迹支撑率达95%以上，几乎无信息泄露；token消耗仅为全量上下文的29%，比Top-K Raw省21%。

### 核心结论
纯在线持续学习场景下，仅靠前向积累经验不足以适配分布漂移，增加基于下游反馈的可落地反向修正机制，能以较低成本同时提升智能体的稳定性和可塑性。
