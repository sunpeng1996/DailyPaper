---
title: 'From Ranked Documents to Reliable Contexts: An Answer-Oriented Context Construct
  Framework for AI Search'
title_zh: 面向AI搜索的答案导向上下文构建框架：从排序文档到可靠上下文
authors:
- Yunfei Zhong
- Yinqiong Cai
- Lixin Su
- Haosheng Qian
- Lixin Zou
- Yixing Fan
- Sheng Xu
- Jiafeng Guo
- Daiting Shi
- Jingzhou He
arxiv_id: '2609.23354'
url: https://arxiv.org/abs/2609.23354
pdf_url: https://arxiv.org/pdf/2609.23354
published: '2026-09-20'
collected: '2026-09-22'
category: RAG
direction: RAG 上下文构建 · AI搜索优化
tags:
- RAG
- Context Construction
- AI Search
- Information Retrieval
- Evaluation Protocol
one_liner: 提出三阶段答案导向上下文构建框架与工业工作流，提升AI搜索的检索与答案质量
practical_value: '- 电商导购/搜索问答类RAG场景可直接复用三阶段上下文构建Pipeline：先过滤无答案支撑的召回文档，再从来源、时效性、事实维度做可信度校验，最后在窗口限制下结构化整合内容，可有效降低大模型回答幻觉

  - 可直接复用其检索侧上下文质量、最终答案效果的双层评估体系，大幅减少RAG类业务上线前的评估成本，统一前后端优化目标

  - 电商商品搜索的生成式回答场景（如属性查询、选购指南）可复用可信度校验逻辑，过滤过期、非官方、虚假的商品描述内容，提升导购回答可靠性'
score: 9
source: arxiv-cs.IR
depth: abstract
---

### 动机
传统网页搜索面向人类用户，以搜索满意度为目标排序文档，用户需自行整合信息；AI搜索中召回文档是大模型生成的输入，原有排序逻辑无法适配可靠答案生成的上下文需求，易引发幻觉。
### 方法关键点
提出三阶段答案导向上下文构建框架：1）答案支撑识别：筛选可为答案生成提供有效信息的候选文档；2）内容可信度评估：从来源、时效性、事实一致性三个维度校验信息可靠性；3）上下文组织：在有限上下文窗口预算下，对保留信息做筛选、合并、结构化，保障生成稳定性。同时配套覆盖前后置优化的工业落地工作流，以及覆盖检索侧、答案层的系统化评估协议。
### 关键结果
实验在检索层、答案层均取得一致性效果提升，验证了框架及工业实现的有效性。
