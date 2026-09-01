---
title: 'Memory-First Fact-Checking: A Knowledge-Graph-Grounded Multi-Agent System
  for Misinformation Detection'
title_zh: 内存优先的事实核查：基于知识图谱的多Agent虚假信息检测系统
authors:
- Amelia Petrenciuc
- Alexandru Lecu
- Adrian Groza
affiliations:
- Technical University of Cluj-Napoca
- Artificial Intelligence Research Institute AIRi@UTCN
arxiv_id: '2608.29617'
url: https://arxiv.org/abs/2608.29617
pdf_url: https://arxiv.org/pdf/2608.29617
published: '2026-08-30'
collected: '2026-09-01'
category: MultiAgent
direction: 多智体事实核查 · 知识图谱落地
tags:
- MultiAgent
- Knowledge Graph
- Fact Checking
- Misinformation Detection
- NLI
- RAG
one_liner: 融合KG语义内存与多Agent对抗推理的事实核查框架，准确率超Llama 3.3 70B近10个百分点
practical_value: '- 「内存优先+外部fallback」架构可直接复用在电商内容风控、商品信息真实性校验场景，先查内部知识库，无匹配结果再调用外部检索，显著降低调用成本

  - 三角色（支持/反对/裁判）多Agent对抗仲裁设计可迁移到推荐场景的商品评价真实性判别、用户投诉内容核验，提升结果可信度与可解释性

  - 双索引KG（宏观完整声明+微观原子事实）的设计可复用在电商知识图谱构建，兼顾长文本语境和短事实的匹配需求

  - 6:3:1加权融合（语义相似度+NLI置信度+图结构支持）的路由逻辑可直接用在RAG系统的召回结果可靠性判断，减少无效外部调用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有自动事实核查方案存在多重缺陷：纯内容分类模型无独立可验证的外部证据；大模型推理存在幻觉，输出不可信；单KG方案受覆盖度限制无法应对新兴事实；多Agent辩论虽能提升事实性，但缺乏结构化记忆复用机制，重复调用成本高，无法形成迭代优化的闭环。

### 方法关键点
- 核心采用「内存优先、web fallback」架构：输入声明优先匹配内部KG，仅在内部证据置信度不足时调用可信源web检索，大幅降低高成本外部调用占比
- 双索引KG设计：MACRO索引存储完整声明保留语境，MICRO索引存储SPO原子事实，均用Sentence-BERT生成768维向量做语义检索，按长度/相似度规则选择最优匹配候选
- 图感知置信度路由：按6:3:1权重融合语义相似度、NLI置信度、KG邻域结构支持度，判断内部证据是否足够，新增数值差异、高中立性防护规则避免错误判决
- 三Agent对抗仲裁庭：支持Agent提取支撑证据、反对Agent提取矛盾证据、裁判Agent仅基于证据输出最终判决，所有结论绑定来源URL，可解释性强
- 知识闭环设计：外部核验后的结论自动转化为SPO三元组存入KG，增量更新语义内存，后续同类请求可直接复用

### 关键结果
在人工标注的333条COVID-19声明测试集上，方案覆盖率90.7%，已解决声明的准确率达97.4%、macro F1 92.6%，比Llama 3.3 70B基线的87.7%准确率高9.7个百分点；其中31.2%的请求直接从KG返回，准确率93.3%，耗时仅2-3s；59.5%的请求走web仲裁路径，准确率99.5%，耗时50-60s。

### 核心洞见
内存优先+可迭代的知识闭环设计，是平衡Agent系统准确率、调用成本、可解释性的核心可行路径。
