---
title: Runtime Verification of Multiple Natural Language Criteria for Agent Governance
title_zh: 面向Agent治理的多自然语言准则运行时验证方法
authors:
- Silviu Pitis
- Parand A. Alamdari
- Jessica Tang
- Toryn Q. Klassen
- Sheila A. McIlraith
affiliations:
- University of Toronto
- Vector Institute
arxiv_id: '2611.23074'
url: https://arxiv.org/abs/2611.23074
pdf_url: https://arxiv.org/pdf/2611.23074
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: Agent 运行时合规验证
tags:
- Agent Governance
- Runtime Verification
- Tree Attention
- Reward Model
- LLM Alignment
one_liner: 提出树注意力结构的VFM验证模型与394K规模CriteriaBank语料，可高效并行评估上千条Agent运行时合规准则
practical_value: '- 电商客服/推荐Agent合规校验可复用树注意力+共享KV cache架构，一次编码上下文并行校验上百条业务规则，4K上下文下单H100跑1000条规则仅1.8s、VRAM<11GB，完全满足线上延迟要求

  - 低资源规则校验场景可参考CriteriaBank预训练+KL正则方案，避免过拟合损失下游可塑性，小样本下迁移效果比直接微调高2~5pp

  - 多维度内容审核、话术质检可复用VFM三元分类（符合/违反/不适用）设计，可精确归因具体违规规则，对接大模型 cascade 做复杂case二次校验时DynaBench上F1可达0.946'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Agent需同时遵守上百条来自开发者、监管、用户的自然语言规则，但大模型指令遵循能力会随规则数量、上下文长度下降，违规事件频发；现有验证方案要么是固定规则分类器扩展性差，要么逐规则调用生成式Judge成本过高，无法满足运行时低延迟要求。

### 方法关键点
- 架构：树注意力结构的VFM，共享上下文+目标文本的KV cache，所有准则并行独立计算，每个准则分支注意力隔离，最后从各准则分支最后token输出三元分类结果（YES/NO/N/A）
- 数据：构建394K条目的CriteriaBank预训练语料，覆盖321K条不同自然语言准则，包含对话、安全、业务多场景标注样本
- 训练：分类头用base模型的Yes/No/Unknown词嵌入初始化实现热启动，预训练加入KL正则锚定base模型分布，避免损失下游可塑性

### 关键实验
- 合成治理基准：微调后VFM-4B准确率88.8%，优于GPT-5.4的83.9%
- DynaBench多规则基准：VFM-4B的F1达0.885，优于DynaGuard-4B的0.720，对接大模型级联后F1提升到0.946
- 性能：单H100上4K上下文、1000条规则验证仅需1.81s，VRAM占用<11GB

### 核心结论
运行时合规校验最优落地范式是「小模型批量粗筛定位违规规则+大模型级联审核复杂case」，可同时兼顾成本、延迟与准确率。
