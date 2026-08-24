---
title: 'Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge
  Poisoning in Generative AI Systems'
title_zh: 用于检测生成式AI错误信息与知识投毒的可信RAG评估Agent
authors:
- Balkrishna Giri
- Md Toufique Hasan
- Jussi Rasku
- Muhammad Waseem
- Pekka Abrahamsson
affiliations:
- Tampere University
arxiv_id: '2608.21095'
url: https://arxiv.org/abs/2608.21095
pdf_url: https://arxiv.org/pdf/2608.21095
published: '2026-08-21'
collected: '2026-08-24'
category: RAG
direction: RAG安全 · 知识投毒与错误信息检测
tags:
- RAG
- Knowledge Poisoning
- Misinformation Detection
- Trustworthy AI
- NLI
- Evaluation Agent
one_liner: 提出双阶段RAG评估Agent，通过多信号融合可信指数检测知识投毒与错误信息
practical_value: '- 可复用双阶段检查架构：检索后生成前做多信号投毒初筛，生成后用NLI做事实一致性校验，适合电商RAG客服、商品问答、营销内容生成等场景防外部输入投毒

  - 可信指数的加权融合+非线性阻尼设计可直接迁移：优先给高置信度的事实一致性信号更高权重，高污染场景加阻尼降低可信分，平衡召回与误杀，适配业务对误报的容忍度

  - 针对业务场景做阈值校准：不同LLM生成风格（比如严谨的客服话术vs活泼的营销话术）对NLI entailment分数影响远大于模型大小，仅需小批量干净样例即可校准可信分阈值

  - 可复用5类投毒检测信号：语言模式、结构异常、文档内一致性、跨文档一致性、语义离群点，适合电商UGC内容入库、检索结果实时过滤场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统默认信任所有检索内容，存在「安全-可靠性缺口」：语义相关性高不代表事实正确，攻击者可通过知识投毒插入恶意文档诱导LLM输出错误信息。而现有RAG评估框架仅校验生成结果与检索上下文的一致性，不校验上下文本身的可信性，离线语料清洗也无法应对实时出现的投毒内容，亟需在线可信校验层填补缺口。
### 方法关键点
- 双阶段架构：生成前先对检索到的文档做多信号投毒检测+跨文档一致性校验，生成后用`bart-large-mnli` NLI模型校验生成结果与检索文档的事实一致性
- 5维投毒检测信号：覆盖语言模式（指令注入特征）、结构异常（格式异常）、文档内一致性、跨文档一致性、语义离群点，按检索相关性加权聚合投毒概率，降低低相关异常文档的误影响
- 可信指数（Trust Index）设计：加权融合0.4*事实一致性分+0.35*跨文档一致性分+0.25*(1-投毒概率)，高污染场景（投毒概率>0.7）加非线性阻尼进一步降低可信分，输出0-1可信分与4档可信等级
### 关键实验结果
在TruthfulQA、FEVER公开数据集及自研OWASP/CWE安全编码知识库上测试，对比全信基线：
- 针对指令注入攻击，Llama 3.3 70B场景下达到100%召回、96.8% F1，混合攻击下准确率91%、精度100%（零误报）
- 跨3款LLM的ROC-AUC达0.73~0.81，针对不同LLM做阈值校准可将Qwen 3.5的准确率从65.5%提升至74.5%
- 安全编码场景下指令注入攻击检测F1达92.3%，但实体替换、语义弱化等无表面痕迹的投毒召回极低（0~20%）

基于表面信号的RAG投毒检测可有效拦截显性攻击，但无痕迹的事实篡改需要接入外部可信知识库才能解决，LLM生成风格对可信校验的影响远大于模型规模。
