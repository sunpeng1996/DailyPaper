---
title: 'No Model Required: Text Entropy Rate Filtering Mitigates Iterative Fine-Tuning
  Collapse'
title_zh: 无需模型依赖：基于文本熵率过滤缓解迭代微调模型坍塌
authors:
- Lewis Mitchell
affiliations:
- Adelaide University
arxiv_id: '2610.01493'
url: https://arxiv.org/abs/2610.01493
pdf_url: https://arxiv.org/pdf/2610.01493
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: LLM训练 · 迭代微调坍塌缓解
tags:
- Model Collapse
- Fine-tuning
- Entropy Estimation
- QLoRA
- Data Filtering
one_liner: 提出无模型的Kontoyiannis熵率过滤，比主流logprob类方法更有效缓解LLM迭代微调坍塌
practical_value: '- 垂域LLM（电商文案生成、推荐话术、Agent回复生成）迭代微调时，若使用闭源API生成的合成训练数据，可直接用ĤK做数据过滤，无需获取模型logprob，比传统HL/surplexity过滤效果更好，计算成本几乎可忽略

  - 生成式推荐/Agent的在线输出质量校验，可接入ĤK作为低延迟重复坍塌检测指标，单千词样本耗时<10ms，无需调用大模型打分即可快速拦截重复率过高的输出

  - 合成训练数据预处理可搭配「全局去重 + ĤK过滤」双pipeline，去重解决跨文档重复问题，ĤK过滤解决单文档内部短语重复问题，双重规避训练数据多样性下降导致的模型坍塌'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LLM迭代使用合成数据微调时会发生模型坍塌：输出多样性持续收窄、罕见模式丢失，核心表现为短语级重复。现有缓解方案均存在门槛：要么需要访问模型logprob、依赖外部Oracle模型，要么需要持续注入高成本人类标注数据，闭源API蒸馏、跨机构数据共享等场景无法落地。
### 方法关键点
- 采用无参数Kontoyiannis熵率估计器ĤK，完全基于原始文本的子串匹配长度统计：长匹配对应文本重复，短匹配对应内容新颖，无需任何模型、GPU、参考语料支持
- 过滤逻辑为域内按ĤK降序排序取Top-k样本，避免自然高熵域（如创意文本）样本被过度选择，可直接嵌入现有训练数据预处理流程
- 计算效率极高，1500词样本评分耗时<10ms，支持大规模并行处理
### 关键实验
在Llama-3.1-8B的6代QLoRA迭代微调全合成闭环实验中，对比无过滤、logprob-based HL过滤两类基线：ĤK过滤相对无过滤实现+42% unique trigrams、+30%词汇量、-19%重复率（所有指标p<0.001），而HL过滤三类多样性指标均无显著提升（p>0.23）。跨4个域、2种温度、2组生成-打分模型对验证，ĤK与logprob熵的相关系数β=0.924，R²=0.746，是稳定的熵代理指标。
### 核心结论
微调坍塌的核心表现是短语级重复，针对短语级结构的统计指标比token级模型不确定性更适合作为坍塌缓解的过滤信号
