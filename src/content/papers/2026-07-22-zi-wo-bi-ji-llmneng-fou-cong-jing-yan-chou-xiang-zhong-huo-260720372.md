---
title: 'Notes to Self: Can LLMs Benefit from Experiential Abstractions?'
title_zh: 《“自我笔记”：LLM能否从经验抽象中获得性能提升？》
authors:
- Chang Liu
- Xinyu Li
- Artur Dubrawski
affiliations:
- Carnegie Mellon University
arxiv_id: '2607.20372'
url: https://arxiv.org/abs/2607.20372
pdf_url: https://arxiv.org/pdf/2607.20372
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: LLM 经验蒸馏与自我优化
tags:
- Experiential Abstraction
- GRPO
- Retrieval Augmentation
- Self-Improvement
- Reasoning
one_liner: 从LLM推理轨迹蒸馏可复用经验抽象库，通过检索或RL微调提升推理能力
practical_value: '- 电商客服/导购Agent可从历史会话的成功/失败案例中蒸馏应对策略（如优惠规则解释、退货流程引导）和避坑提示（如不承诺超权限权益），构建经验库，推理时检索注入，比全量会话检索更省token且错误率更低

  - 垂直场景小模型优化可复用「自蒸馏经验抽象+GRPO微调」范式，无需大模型标注就能提升小模型在电商规则计算、商品属性推理等场景的准确率，降低推理成本

  - 检索增强场景可参考双query召回+分类型存储策略/避坑提示的方案，提升检索相关度，避免无关提示扰乱模型输出

  - RL微调后的模型不要再额外注入同类检索提示，避免干扰已收敛的输出分布，反而导致效果下降'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM经验学习方案大多依赖前沿大模型作为监督信号，小模型难以自主从历史推理轨迹中提炼可复用知识，而人类天然能将过往经验总结为通用策略、避坑提醒等抽象知识，这种能力在LLM上的落地价值尚未得到充分验证。
### 方法关键点
- 从目标LLM的训练集推理轨迹蒸馏两类经验抽象：正确轨迹提炼可复用的解题策略，错误轨迹提炼需要规避的错误模式，去重后构建可检索的经验库，支持教师大模型蒸馏或目标LLM自蒸馏两种提取方式
- 提供两种落地模式：①推理时针对查询召回Top-6相关抽象注入prompt；②训练时将抽象与查询拼接作为输入，基于GRPO做RL微调
- 检索采用双query择优方案：默认使用带主题标签的原问题，当重写为抽象风格的query召回Top1得分比原query高0.02以上时切换，策略和避坑提示分桶存储召回。
### 关键结果
在MATH-500数学推理基准上，Llama-3.2-3B自蒸馏抽象结合RL微调，pass@1比原生基线高6.34，比原生GRPO微调高2.56，且自蒸馏效果与前沿大模型教师蒸馏的效果相当；经验抽象对模型不擅长的难任务提升更显著，在难度更高的OlympiadBench上，pass@1比原生GRPO高1.3，可跨领域迁移到逻辑推理任务。

最值得记住的结论：小模型无需大模型监督，就能从自身成功和失败的经验中提炼可复用的抽象知识，实现低成本自我迭代提升。
