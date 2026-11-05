---
title: 'Reasoning over Non-Parametric Memory in Multilingual LLMs: A Cognitive-Based
  Analysis of Relational Knowledge'
title_zh: 多语言大模型非参数记忆关系推理的认知维度分析
authors:
- Zohreh Abbasi Liasi
- Batoul Hammoud
- Anas Madkoor
- Ehsaneddin Asgari
affiliations:
- Qatar Computing Research Institute, Hamad Bin Khalifa University
- Universitat Pompeu Fabra
arxiv_id: '2611.06715'
url: https://arxiv.org/abs/2611.06715
pdf_url: https://arxiv.org/pdf/2611.06715
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: 大模型关系推理认知分层评估
tags:
- RAG
- LLM Evaluation
- Multilingual LLM
- Relational Reasoning
- Bloom's Taxonomy
one_liner: 提出REL-BLOOM多语言诊断基准，揭示RAG依赖的上下文关系推理的认知分层缺陷
practical_value: '- 做RAG系统能力评估时，可按Bloom认知层级拆分任务单独统计准确率，避免整体准确率掩盖高难度任务（如电商优惠规则校验、合规回答判定）的缺陷

  - 测试RAG上下文忠实度时，加入反事实、实体中性化变体测试，可区分模型是依赖预训练记忆答对还是真实理解上下文关系，尤其适合长尾商品属性推理等场景

  - 多语言RAG/推荐场景下，题目难度排名跨语言高度稳定，可先完成单语言难度分层测试再翻译到目标语言做初筛，大幅降低多语言评估成本

  - 针对高认知难度的RAG任务，可尝试用实体中性化的prompt模板减少预训练实体关联的干扰，提升推理准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG系统的端到端评估混淆了检索质量、预训练记忆依赖、上下文关系推理三类能力的贡献，无法准确判断模型是否真实基于给定上下文完成推理；同时多语言场景下模型推理行为的跨语言稳定性、Bloom认知分层框架在LLM推理任务中的合理性均缺乏量化验证。

### 方法关键点
- REL-BLOOM诊断基准基于30个分层采样的Wikidata关系生成450道多选题，覆盖Bloom认知框架的5个推理层级：Remember、Understand、Apply、Analyze、Evaluate
- 每个问题对应3种真实性测试条件：Factual（与预训练知识一致）、Counterfactual（修改实体与预训练知识冲突）、Neutralized（实体替换为类型占位符，消除预训练记忆影响）
- 覆盖阿拉伯语、中文、英语、印地语、波斯语、西班牙语6种语言，包含混合跨语言、全翻译2种测试设置

### 关键结果
覆盖43个模型（41个开源+2个Gemini闭源）的22.68万次预测显示：
1. 所有开源模型均存在Apply到Analyze层级的准确率陡降，Large规格Granite模型降幅达47.2个百分点，Gemini系列无此现象；
2. Evaluate层级是所有模型的共同瓶颈，Gemini 3.1 Pro在前4个层级平均准确率达99.5%，但Evaluate层级仅60.7%；
3. 题目、关系的难度排名跨语言高度稳定，Gemini 3.1 Pro的跨语言难度相关系数达0.74；
4. 中小开源模型在Analyze、Evaluate等高认知层级使用Neutralized实体可有效提升准确率。

**最值得记住的结论**：模型规模增长本身无法保证其基于给定上下文的关系推理可靠性，RAG系统评估必须拆分认知层级和上下文真实性条件才能暴露真实缺陷。
