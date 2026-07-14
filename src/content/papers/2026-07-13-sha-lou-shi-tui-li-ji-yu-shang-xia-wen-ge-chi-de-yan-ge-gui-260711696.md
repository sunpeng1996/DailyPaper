---
title: 'Think Through a Bottleneck: Hourglass Reasoning for Rigorous Induction'
title_zh: 沙漏式推理：基于上下文隔离的严格归纳框架
authors:
- Huan Zhu
affiliations:
- Peking University
arxiv_id: '2607.11696'
url: https://arxiv.org/abs/2607.11696
pdf_url: https://arxiv.org/pdf/2607.11696
published: '2026-07-13'
collected: '2026-07-14'
category: Reasoning
direction: LLM推理 · 上下文隔离归纳优化
tags:
- Hourglass Reasoning
- Inductive Reasoning
- Context Isolation
- Self-Refinement
- LLM Reasoning
one_liner: 提出阶段上下文严格隔离的沙漏推理框架，显著提升冻结LLM的少样本归纳推理能力
practical_value: '- 设计Agent推理链路时，可复用「阶段上下文隔离+仅传递压缩符号状态」的架构，代替传统单上下文自修正流程，减少中间冗余信息干扰，提升优惠规则计算、商品属性匹配等规则类任务的准确率

  - 做生成式推荐的规则归纳（如从用户行为样本抽取偏好规则、从运营案例提炼活动文案规则）时，可拆分归纳→演绎→实现三个独立阶段，强制输出可解释的符号规则，降低幻觉同时方便人工审核

  - 搭建自修正工作流时，避免直接修改下游输出产物，改为先修正上游的schema和规则，再重新生成产物，解决补丁式修改带来的泛化性差的问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM的自修正方法在少样本归纳推理任务上表现极差，核心痛点是稠密上下文窗口中原始样本、错误反馈、中间产物相互纠缠，模型倾向于拟合表面规律而非抽象底层规则，自修正时往往直接对输出打补丁而不更新底层逻辑，导致泛化性大幅下降，仅靠prompt引导显式输出规则无法解决这一问题。
### 方法关键点
- 设计严格上下文隔离的四阶段推理拓扑，每个阶段为独立API调用，无共享会话历史：
  1. Induction阶段：从少样本示例压缩出输入解析schema φ和临时辅助推理脚手架z
  2. Deduction阶段：基于φ、z推导通用转换规则T，永久丢弃z
  3. Implementation阶段：仅用φ、T编译生成可执行产物，禁止引入其他信息
  4. Refinement阶段：发现错误时仅修正φ和T，再重新生成产物，禁止直接修改输出
- 仅压缩后的符号状态(φ,T)可跨阶段传递，所有中间推理痕迹、错误历史均被隔离在所属阶段，杜绝实例相关细节泄露
### 关键实验结果
跨三个异质基准测试，对比主流Self-Refine基线：
1. ARC-AGI-2视觉抽象任务：GPT-5.5 pass@5提升14个百分点，Gemini 3.1 Pro pass@5提升9.8个百分点
2. ChipBench硬件Verilog合成任务：GPT-5.5准确率从31%提升至58%，接近翻倍
3. BBEH-Linguini语言规则归纳任务：抵消了显式规则输出的性能副作用，Gemini 3.1 Pro pass@5比原始基线提升11.8个百分点
消融实验证实核心收益来自阶段隔离的拓扑结构，与prompt措辞、符号输出格式无关。
> 最值得记住的结论：决定冻结LLM归纳推理能力的是推理过程的信息流动方式，而非表达推理的语言形式。
