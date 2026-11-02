---
title: 'Context as Infrastructure: Knowledge Compilation for Retrieval in Agentic
  Systems with Harnesses'
title_zh: 上下文即基础设施：智能体系统检索的知识编译与管控框架
authors:
- Zhichang Yu
- Baining Cao
- Sbaaoui Idriss
- Qi Wang
- Gangqiang Xu
- Ling Qin
- Xiaoling Jin
- An Liu
- Shaohao Cai
- Xiaoyang Bao
affiliations:
- InfiniFlow Inc.
- East China Normal University
arxiv_id: '2610.41172'
url: https://arxiv.org/abs/2610.41172
pdf_url: https://arxiv.org/pdf/2610.41172
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent 检索优化 · 知识编译
tags:
- Agentic_RAG
- Knowledge_Compilation
- Retrieval_Harness
- Token_Efficiency
- Cost_Optimization
one_liner: 提出知识编译层与检索管控框架，在不损失准确率前提下大幅降低智能体RAG的token消耗与延迟
practical_value: '- 可复用「BM25/grep足够胜任智能体检索」的结论，放弃高成本的向量索引优化，直接用纯 lexical 检索降低工程复杂度，尤其适合商品标题/营销文案/用户评论这类短文本检索场景

  - 可落地claim-evidence对编译机制：上游预处理阶段将商品详情、评论、客服话术等文本拆分为原子断言+原文证据对，召回后直接替换原始chunk输入LLM，平均降38%token成本，仅需2%的命中率即可回本

  - 可借鉴检索harness的5站式流程：能力检查→证据预取→充分性判断→工具循环→确定性关闭，避免智能体无意义的重试/冗余读取，搭配决策门控可将多轮检索的latency从140s压到30s

  - 部署前先跑shadow对比：阈值调优阶段先不生效编译逻辑，仅记录决策，确认准确率不下降再上线，避免编译错误导致的业务损失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
当前智能体RAG的迭代检索框架已将准确率推到饱和：仅用BM25+grep搭配MiniMax M3就能在FRAMES多跳QA基准上达到91%准确率，在BrowseComp-Plus上达85%，传统向量索引、召回优化不仅无增益反而会降低准确率。当前核心痛点是无约束的检索循环存在大量重复查询、冗余文本读取，导致token浪费、延迟高，无效上下文挤占模型窗口。
## 方法关键点
- 新增前置知识编译层： ingestion阶段将原始文档转换为带完整溯源的结构化 artifacts，包括叶子节点为「原子声明+原文证据对」的导航树、实体关系图、本体、时间线等，编译仅做语义富集，不改动底层召回逻辑
- 检索管控harness：5站式刚性流程约束检索循环，预取编译证据后先做充分性判断，证据足够则直接回答，不足才触发原始文本读取，严格限制工具暴露范围避免无效调用
- 三种兼容的服务模式：证据优先检索、证据替换（默认，召回chunk后自动替换为声明-证据对输入模型）、决策门控读取，可适配不同业务场景
## 关键结果
在FRAMES多跳QA基准上测试，所有编译方案准确率与无编译baseline无显著差异：证据充分时总token降低91%，证据不足时仅增加1.9%，全基准平均token降低38%；搭配轻量决策门控后，端到端延迟从140s降至30s，token额外降低52%；编译回本的最低证据命中率仅2%，FRAMES实测命中率达43%，平均26次查询即可覆盖单文档编译成本。

**最值得记住的一句话**：智能体RAG的核心矛盾已经从召回准确率不足转向上下文供给效率不足，与其优化检索索引，不如优化输入模型的上下文结构。
