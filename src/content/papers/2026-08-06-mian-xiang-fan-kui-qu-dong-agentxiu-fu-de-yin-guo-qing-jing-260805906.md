---
title: Causal Episodic Memory for Feedback-Driven Agent Repair
title_zh: 面向反馈驱动Agent修复的因果情景记忆框架MERIT
authors:
- Khang Nhat Hoang Vo
- Tam Minh Chu
- Anh Trac Duc Dinh
- Thuyen Vinh Ha Bui
- Tho Quan
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- Ho Chi Minh City University of Technology
arxiv_id: '2608.05906'
url: https://arxiv.org/abs/2608.05906
pdf_url: https://arxiv.org/pdf/2608.05906
published: '2026-08-06'
collected: '2026-08-07'
category: Agent
direction: Agent 记忆优化 · 跨轮次错误修复
tags:
- LLM Agent
- Episodic Memory
- Text-to-SQL
- Training-free
- Hybrid Retrieval
one_liner: 提出免训练双极性因果记忆框架，跨episode复用修复经验提升Text-to-SQL任务性能
practical_value: '- 可复用双极性记忆设计：给Agent的记忆拆分正（验证成功的修复方案）、负（已失败的尝试）池，无需微调就能让Agent在同场景下避免重复踩坑、复用成功经验，适合电商客服Agent、智能查询系统这类有明确对错反馈的场景

  - 错误类型前置筛选检索trick：先通过规则对当前错误做粗分类，再在同类型记忆池里做混合lexical-dense检索，能大幅降低检索噪声，比全局语义检索的召回准确率更高，可直接迁移到商品查询纠错、SQL生成类工具的修复模块

  - 同场景记忆优先的落地参考：跨领域/跨Schema迁移修复经验的收益远低于同场景的过往经验，做推荐/搜索的Agent记忆系统时，优先复用同品类、同业务场景的历史经验，不要盲目做跨域经验迁移

  - 成本权衡参考：Reflexion类反思型记忆精度更高但推理成本是MERIT的2倍以上，业务中如果token成本敏感，优先选MERIT这类检索增强的轻量记忆方案，平衡收益和成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent的错误修复多局限在单episode内，修复成功的经验不会留存，遇到同类错误需要重新摸索，效率极低；已有的跨episode记忆方案没有区分成功/失败经验，纯语义检索容易召回无关内容，修复收益不稳定。

### 方法关键点
- 完全免训练设计，无需微调LLM参数，仅通过外挂记忆模块实现跨episode经验复用
- 双极性记忆池：区分正样本（Oracle验证过的错误→正确修复对）和负样本（最终未成功的修复尝试），正负样本分别检索
- 规则驱动错误粗分类：通过DBMS返回的错误信息做7类错误的规则分类，优先在同错误类型的记忆池检索，样本不足时fallback到全池
- 混合排序策略：语义相似度（权重0.75）+ BM25（权重0.25）的混合排序，最多召回3条正记忆、1条负记忆加入prompt引导修复

### 关键结果
在Spider、BIRD两个Text-to-SQL基准上，基于Qwen2.5-7B-Instruct底座，对比无状态迭代修复、Reflexion、动态RAG三类baseline：
- Spider数据集上MERIT准确率从66.34%提升到69.79%，和动态RAG持平，比Reflexion少消耗20%左右的token
- BIRD数据集上MERIT准确率从47.35%提升到48.44%，Reflexion虽然达到51.24%的准确率，但token消耗是MERIT的1.27倍，总推理成本高1倍以上
- 消融实验显示负记忆贡献不足0.2个百分点，同Schema的本地经验贡献最稳定，跨库检索会带来2.74个百分点的准确率下降

### 核心结论
无需微调的因果情景记忆能稳定提升Agent的错误修复效率，记忆的场景/领域相关性比复杂的分类、排序策略对最终收益的影响更大。
