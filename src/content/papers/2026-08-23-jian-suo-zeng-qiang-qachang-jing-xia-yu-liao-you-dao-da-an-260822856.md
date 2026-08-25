---
title: 'Same Agent, Different Answers: A Repeat-Aware Audit of Corpus-Induced Answer
  Churn in Retrieval-Augmented QA'
title_zh: 检索增强QA场景下语料诱导答案波动的可感知审计方案
authors:
- Jingjie Ning
- Xueqi Li
affiliations:
- Carnegie Mellon University
arxiv_id: '2608.22856'
url: https://arxiv.org/abs/2608.22856
pdf_url: https://arxiv.org/pdf/2608.22856
published: '2026-08-23'
collected: '2026-08-25'
category: RAG
direction: RAG效果评估 · 语料更新兼容性
tags:
- RAG
- LLM Evaluation
- Answer Churn
- Retrieval QA
- Corpus Update
one_liner: 提出快照兼容性审计方法，剥离生成随机性，量化RAG语料更新带来的超额答案波动
practical_value: '- 上线RAG语料/召回规则迭代时，不要仅依赖整体准确率指标，增加快照兼容性审计流程，先计算超额答案波动，避免小的准确率变化掩盖大量用户可感知的答案变更，尤其适配电商导购、活动规则问答等用户预期明确的场景。

  - 评估RAG答案一致性时，剥离LLM本身的生成随机性：对同一个query每个版本跑至少2次独立请求，用同版本重复请求的一致率做基线，减去跨版本的一致率得到真实的变更幅度，避免误判波动原因。

  - 对于电商高优query（如爆款商品、大促规则相关），额外增加repeat-stable语义翻转校验：如果同一个query在两个版本下的两次返回语义都稳定但完全不同，必须人工审核，避免旧规则被错误覆盖、引发用户投诉。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RAG系统语料扩容、索引更新时，仅靠整体准确率指标无法反映单query的答案变化：准确率会抵消效果提升和回落的case，同时LLM本身的生成随机性会让单次对比高估更新的影响，这种隐藏的答案波动会破坏用户预期、影响下游依赖RAG输出的自动化流程，但此前缺少可落地的量化方案。

### 方法关键点
- 定义快照兼容性审计：固定模型ID、Prompt、检索策略、生成参数等所有变量，仅变更语料/索引，对每个query在新旧快照各生成2次独立回答
- 计算超额答案churn：用同一快照下两次回答的平均相似度，减去跨快照回答的两两平均相似度，得到剥离生成随机性后的真实波动幅度
- 双维度相似度评估：归一化精确匹配（字符串完全一致）、盲审语义等价（隐藏版本信息，判定答案事实是否一致）
- 新增repeat-stable语义翻转诊断：标记同一快照下两次回答语义完全一致、但跨快照所有回答语义都不同的query，方便人工排查

### 关键实验结果
- 实验将FineWeb语料从1个分片扩容到7个分片，在400条Natural Questions测试集上，归一化精确匹配超额churn为6.44pp，语义超额churn为10.25pp，但整体精确匹配准确率仅变化-1.50pp，准确率几乎不变但大量答案发生了实质性变更
- 200条TriviaQA测试集上，超额churn为3.00pp（精确匹配）和2.125pp（语义），准确率反而提升1.25pp，证明准确率和兼容性无直接关联
- 100条子集用DeepSeek v4-pro验证，语义超额churn为8.75pp，准确率提升3pp，结论跨生成配置稳定

**最值得记住的一句话**：RAG语料/索引迭代的上线评估不能只看整体准确率，必须同时审计答案兼容性，否则小的准确率波动下可能隐藏大量用户可感知的答案变更。
