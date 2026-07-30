---
title: Scientific Knowledge Discovery in the Age of Large Language Models
title_zh: 大语言模型时代的科学知识发现
authors:
- Eleni Adamidi
- Serafeim Chatzopoulos
- Thanasis Vergoulis
affiliations:
- IMSI, ATHENA RC
arxiv_id: '2607.26670'
url: https://arxiv.org/abs/2607.26670
pdf_url: https://arxiv.org/pdf/2607.26670
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: LLM 科研文献检索与筛选综述
tags:
- LLM
- Literature Retrieval
- Literature Screening
- Survey
- Information Retrieval
one_liner: 系统调研34篇LLM在文献检索与筛选任务的应用，覆盖技术选型、评测方案等核心维度
practical_value: '- 可复用其梳理的「LLM检索匹配→候选 eligibility 核验」两阶段架构，迁移到电商公域搜推的Query理解+商品/广告候选粗筛链路，降低人工规则维护成本

  - 其总结的prompt工程、轻量微调（如LoRA）等模型适配技术，可直接复用到垂域（如电商商品检索、评论舆情筛选）的LLM落地场景

  - 可参考其多维度评测框架设计思路，构建搜推系统全链路效果评估体系，覆盖召回准确率、筛选合规性、用户满意度等多维度指标'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
科研文献量级爆发式增长，传统检索系统重度依赖人工撰写Query与人工核验，效率低、漏检率高，研究者容易遗漏相关工作、重复研究，亟需更智能的科学知识发现工具。
### 方法关键点
对OpenAIRE Graph检索得到的1589篇相关文献做多轮筛选，最终纳入34篇 peer-reviewed 工作做系统性综述，从选用LLM类型、模型访问与适配方案、prompting与架构技术、真值数据源、评估指标5个维度做分类梳理，核心覆盖文献检索、文献筛选两大核心任务。
### 关键结果
完整梳理了当前LLM在科研知识发现领域的技术栈与落地路径，明确了现有方案在低资源垂域适配、长文本理解、可解释性等方面的核心优化方向。
