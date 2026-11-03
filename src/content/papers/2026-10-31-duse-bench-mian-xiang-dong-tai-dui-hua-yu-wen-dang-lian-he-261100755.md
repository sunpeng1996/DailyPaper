---
title: 'DuSE-Bench: Benchmarking Joint Reasoning over Evolving Dialogue and Documents'
title_zh: DuSE-Bench：面向动态对话与文档联合推理的评测基准
authors:
- Guanjie Cheng
- Jianfeng Gao
- Yufei Tong
- Xinkui Zhao
- Shuiguang Deng
affiliations:
- Zhejiang University Ningbo Global Innovation Center
- Zhejiang University School of Software Technology
- Zhejiang University College of Computer Science and Technology
arxiv_id: '2611.00755'
url: https://arxiv.org/abs/2611.00755
pdf_url: https://arxiv.org/pdf/2611.00755
published: '2026-10-31'
collected: '2026-11-03'
category: Eval
direction: LLM评测 · 动态多源信息联合推理
tags:
- Benchmark
- Conversational Reasoning
- Evolving Document
- RAG
- LLM Evaluation
one_liner: 构建覆盖5场景1000任务的评测基准，实现动态对话与文档联合推理的多维度评估
practical_value: '- 电商客服/咨询Agent开发可借鉴Support Graph机制，关联用户历史需求与动态更新的商品/规则文档，避免用过期规则应答、遗漏用户前置要求等问题

  - 多源RAG系统优化可复用实验结论：联合检索不要设置固定源配额，优先采用稠密+稀疏混合排序策略，避免对话与文档证据互相挤占必要槽位，需协同优化对话记忆与文档检索模块，单一源召回提升无法带来全局最优效果

  - Agent回复评测体系可复用三模块拆分方案：分别评估内容准确性、回复类型合理性（该追问时不硬答、该上报冲突时不回避）、证据溯源完整性，解决现有仅评估内容正确性的盲区'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有对话与文档联合推理评测基准普遍不支持跨会话动态更新的对话记忆、多版本演化的文档，也无法同时覆盖内容正确性、回复类型选择、证据溯源三个维度的评估，导致需要同时处理动态用户需求、实时更新的业务规则/商品信息的落地场景（如电商客服、信息助手）缺乏系统性的能力验证方案。
### 方法关键点
- 覆盖新闻、科学、软件、企业、环境5个场景，共1000个任务，其中700个需同时依赖对话与文档双源信息完成
- 采用演化式Support Graph指导任务构建，全程追踪更新事实、复用结论与原始对话轮次、文档段落的关联，保留完整的信息溯源链路
- 任务按依赖源、状态依赖维度拆分标注，支持三模块独立评测：内容准确率、回复类型Macro-F1、证据溯源F1，回复类型包含回答、追问、冲突上报、弃权四类
### 关键实验
测试11种主流配置（长上下文、单/双源RAG、原始对话历史、三类对话记忆系统），双源任务的内容准确率最高仅56.7%；内容正确的回复中79%~92%存在证据溯源不全问题；双源金标准证据替换实验显示，仅优化单一源的召回收益远低于双源协同优化，双源同时喂入金标准证据时内容准确率可提升至68.6%。
### 核心结论
动态多源推理场景下，对话记忆和文档检索的协同增益远高于单一模块的单点优化，同时需警惕内容准确率提升伴随的回复类型合理性、证据溯源能力下降的问题。
