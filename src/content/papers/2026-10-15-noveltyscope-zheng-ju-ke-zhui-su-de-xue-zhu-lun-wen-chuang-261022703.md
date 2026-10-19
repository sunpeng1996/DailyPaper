---
title: 'NoveltyScope: A Multi-Agent Research Assistant for Evidence-Grounded Novelty
  Assessment of Scientific Papers'
title_zh: NoveltyScope：证据可追溯的学术论文创新性评估多智能体助手
authors:
- Yueran Tian
- Huizhi Liang
affiliations:
- Newcastle University
arxiv_id: '2610.22703'
url: https://arxiv.org/abs/2610.22703
pdf_url: https://arxiv.org/pdf/2610.22703
published: '2026-10-15'
collected: '2026-10-19'
category: MultiAgent
direction: 多智能体协作 · 证据可追溯评估框架
tags:
- Multi-Agent
- RAG
- Hybrid Retrieval
- Evidence-grounded
- LLM Evaluation
one_liner: 提出四角色多智能体+混合检索框架，输出带证据链的5档论文创新性评分，误差低于单LLM方案
practical_value: '- 四角色辩论+单轮审校的多智能体决策范式可直接迁移到电商选品、广告素材创意新颖度评估、召回结果多样性打分等场景，单轮交互token成本可控，同时决策可解释

  - BM25+稠密检索的RRF融合方案，搭配任务/贡献维度分别构建查询的检索策略，可复用在垂域（如电商商品、广告文案）的相似性召回场景，提升召回准确率

  - 生成内容引用源原文校验的机制，可迁移到RAG生成的商品卖点、营销文案的事实性核验环节，有效降低幻觉

  - 明确评分标尺+正反方证据锚定的设计，可降低大模型决策的随机性，适合所有需要可解释、可追溯的业务打分类任务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
学术论文创新性评估高度依赖人工评审，存在工作量过载、评审人意见一致性低的痛点，现有自动化评估方案普遍缺乏可追溯的证据支撑，评分误差高，无法满足实际评审辅助需求。
### 方法关键点
- 检索层：采用BM25+稠密检索的RRF加权融合方案，分别基于提取的论文核心任务、作者声明的最多2项贡献构建两类查询，从本地闭源语料召回相关 prior work
- 证据校验层：逐篇对比待评论文与召回文献的任务、贡献差异，匹配双方原文段落作为支撑证据，校验引用段落与缓存源文本的一致性，排除幻觉证据
- 评分层：设计四角色固定工作流：Prosecutor输出低创新性证据、Defender输出高创新性证据、Judge基于双方论点+校准样例打分、Critic做评分标尺校验，最多支持1次评分修订，所有决策严格锚定已检索到的证据
### 关键实验
在50条类平衡的RINoBench样本上测试：向量相似度映射基线MAE=1.68；单LLM方案Gemini MAE=1.48、Qwen3 MAE=1.22；多智能体方案Gemini MAE=1.26（相对单Gemini降14.9%）、Qwen3 MAE=1.16（相对单Qwen3降4.9%），相对基线最高降低31%的MAE。
### 核心洞见
角色明确分工+证据强锚定的多智能体决策范式，相比单LLM能稳定降低打分类任务的误差，同时保留完整的决策可追溯性。
