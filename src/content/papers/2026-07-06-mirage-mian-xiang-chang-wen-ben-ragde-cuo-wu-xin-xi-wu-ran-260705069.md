---
title: 'MIRAGE: Defending Long-Form RAG Against Misinformation Pollution'
title_zh: 《MIRAGE：面向长文本RAG的错误信息污染防御方法》
authors:
- Saadeldine Eletter
- Ruihong Zeng
- Yuxia Wang
- Maxim Panov
- Aleksandr Rubashevskii
- Preslav Nakov
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
- INSAIT, Sofia University “St. Kliment Ohridski”
arxiv_id: '2607.05069'
url: https://arxiv.org/abs/2607.05069
pdf_url: https://arxiv.org/pdf/2607.05069
published: '2026-07-06'
collected: '2026-07-07'
category: RAG
direction: 长文本RAG · 错误污染防御
tags:
- RAG
- Misinformation Defense
- Long-form QA
- NLI
- Factuality
one_liner: 免训练模型无关的长文本RAG防御框架，基于跨文档NLI声明图过滤污染证据
practical_value: '- 可直接复用跨源NLI声明一致性校验逻辑，接入电商商品问答、智能客服等RAG场景，过滤竞品恶意差评、虚假商品描述等污染证据，提升生成内容事实性

  - 框架完全免训练、模型无关，无需修改现有RAG的检索、生成模块，仅需在中间插入校验层，工程落地成本极低，可快速上线试点

  - 其提出的4类最小编辑错误污染注入协议，可直接用来构建内部RAG系统鲁棒性评测集，模拟恶意信息攻击场景，量化现有系统的脆弱性

  - Defended-Claims Gate的两个可解释阈值（矛盾率、最小源数）可根据业务需求调整，比如正品导购、医疗咨询等高风险场景可提⾼源数要求，采取更保守的校验策略'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG通过外挂外部证据提升生成事实性，但实际检索结果常存在语义高度相关但包含细微事实错误、误导性表述、虚构内容的污染证据，LLM存在对检索上下文的"谄媚偏误"，哪怕单条高评分污染文档也会引导生成高置信度的错误答案。现有鲁棒RAG方法大多假设语料可信，仅过滤无关内容，无法应对语义匹配的污染证据，亟需在生成前主动校验证据可信度的方案。
### 方法关键点
- 完全免训练、模型无关，可作为插件直接插入标准检索-生成pipeline，无需微调检索模型或LLM
- 从top-k检索段落中提取句子级声明，关联来源、域名、检索得分元数据，通过跨源NLI构建声明支持/矛盾关系图，额外补充反例检索校验高排名声明
- 基于跨源支持数、域名信任度、检索得分综合给声明打分，贪心剪枝得到内部一致的可信声明子集
- 设计可解释的Defended-Claims Gate，通过可信声明集的矛盾率、来源多样性两个阈值判断检索是否可靠：可靠则仅用可信声明生成，不可信则fallback到LLM参数知识回答
- 提出4类最小编辑的污染注入协议（明确错误、冲突、误导、虚构），可构建干净、50%混合、100%全污染三类匹配的评测数据集
### 关键结果
在4个长文本QA基准、5款商用/开源LLM上测试：混合污染场景下，GPT-4o-mini的VeriScore F1从53.88%提升到83.43%；全污染场景下 vanilla RAG的F1暴跌至39.87%（甚至低于无RAG的75.88%），MIRAGE则恢复到78.00%，优于所有现有鲁棒RAG基线，干净场景下性能与 vanilla RAG基本持平。
> 最值得记住的结论：鲁棒RAG不能仅靠检索相关性判断证据质量，生成前做多源一致性校验是抵御错误信息污染的核心有效手段。
