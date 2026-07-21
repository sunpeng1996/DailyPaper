---
title: 'FinSAgent: Corpus-Aligned Multi-Agent RAG Framework for Evidence-Grounded
  SEC Filing Question Answering'
title_zh: FinSAgent：面向SEC财报问答的语料对齐多智能体RAG框架
authors:
- Jijun Chi
- Zhenghan Tai
- Hanwei Wu
- Tung Sum Thomas Kwok
- Hailin He
- Zixing Liao
- Bohuai Xiao
- Chaolong Jiang
- Jianliang Lei
- Jerry Huang
affiliations:
- SimpleWay.AI
- McGill University
- University of Toronto
- University of California, Los Angeles
- Mila - Quebec AI Institute
arxiv_id: '2607.18102'
url: https://arxiv.org/abs/2607.18102
pdf_url: https://arxiv.org/pdf/2607.18102
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: 多智能体RAG · 结构化垂直语料问答优化
tags:
- Multi-Agent
- RAG
- Corpus Alignment
- Financial QA
- Evidence Grounding
one_liner: 通过语料侧全链路对齐解决RAG先验与财报语料错配，提升SEC财报问答事实准确性
practical_value: '- 针对结构化语料（如电商商品详情页、平台合规文档、用户评价库）的RAG，可参考按语料固有结构划分智能体角色，降低检索漏召，比如电商可拆分商品参数、营销规则、用户评价、售后政策专属检索Agent

  - 解决RAG的语义召回假阳性问题，可复用特征门控重排思路：在语义重排得分基础上，叠加轻量非语义特征（如chunk来源、重复率、query字面匹配度）的LightGBM打分做加权，压低通用模板类内容的权重

  - Query分解阶段可引入轻量的语料库局部摘要作为先验，避免LLM仅靠内部知识生成的子query和实际语料结构/术语不匹配，降低检索空回概率

  - 多智能体协作优先走并行推理架构，相比串行辩论/迭代的多智能体方案，可大幅降低latency与token消耗，更适合线上业务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有面向SEC财报等长结构化高冗余文档的RAG系统存在**先验-语料错配**问题：前端仅基于用户query生成子查询，与财报的固有结构、专属术语不匹配导致有效证据漏召；后端语义重排优先返回语义相似但证据无效的通用模板内容（如跨公司通用的合规套话），最终回答的事实错误率高、证据支撑不足。

### 方法关键点
- 角色专属并行多智能体：锚定10-K财报的法定章节结构，拆分通用、量化、市场、法律、公司5个专属Agent，各负责对应章节的证据检索，全并行执行降低推理延迟
- 语料感知查询分解：子query生成时引入轻量召回的局部章节摘要作为上下文，对齐语料的实际术语与结构，避免LLM依赖内部先验生成无效子查询
- 多路径检索+特征门控重排：融合BM25、稠密检索、摘要检索三路召回结果；在语义重排得分基础上，叠加31维非语义特征（如chunk来源、重复率、lexical overlap）的LightGBM门控打分，加权压低假阳性候选的权重

### 关键结果
在5个金融QA benchmark（含FinanceBench、SECQUE等公开数据集及2个业务私有数据集）上，相比MoA、FinDebate等多智能体基线，答案正确性平均提升8%~15%，事实一致性维度提升最多12%；1400份匿名用户盲测评分显著优于所有基线；token消耗仅为FinDebate的39%，端到端latency仅为其35%。

**最值得记住的结论**：当RAG应用于结构固定、冗余度高的垂直领域语料时，优先从语料侧对齐优化检索全链路，效果优于单纯提升模型能力或拉长上下文窗口。
