---
title: Leveraging Low-Level Symbolic Competences for Unsupervised Grounding in Hallucination
  Detection
title_zh: 利用LLM底层SQL符号能力实现无监督幻觉检测
authors:
- Renato Vukovic
- Hsien-chin Lin
- Carel van Niekerk
- Benjamin Ruppik
- Michael Heck
- Shutong Feng
- Nurul Lubis
- Milica Gasic
affiliations:
- Heinrich Heine University Düsseldorf
arxiv_id: '2609.05025'
url: https://arxiv.org/abs/2609.05025
pdf_url: https://arxiv.org/pdf/2609.05025
published: '2026-09-04'
collected: '2026-09-07'
category: LLM
direction: LLM 无监督幻觉检测 · 神经符号方法
tags:
- Hallucination_Detection
- Text-to-SQL
- Neurosymbolic
- RAG
- Zero_Shot
one_liner: 提出无监督Text-to-SQL幻觉检测框架TeQHallu，无需领域微调性能媲美有监督SOTA
practical_value: '- 电商商品问答、客服RAG系统可直接复用TeQHallu的SQL结构化校验流程，无需标注数据就能上线幻觉检测能力，降低给用户传递错误商品/活动信息的风险

  - 搭建生成式推荐的文案/内容校验模块时，优先采用「半结构化存储+符号校验」组合，比纯LLM直接校验的精度高10%左右，还能输出可审计的校验依据，满足合规要求

  - 多轮导购Agent场景可借鉴增量式SQL库构建逻辑，把对话上下文、用户历史、商品信息结构化存储，避免重复解析的同时提升对话类幻觉的检测召回率

  - 若使用的开源小模型Text-to-SQL能力较差，可先替换为JSON键值对结构化校验，虽然精度略低于SQL方案，但也比纯直接预测的F1高3-5个点，性价比更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM生成幻觉是RAG系统、对话Agent、生成式推荐落地的核心风险，现有检测方案要么是黑盒模型无解释性，要么依赖大量领域标注微调，零样本方法普遍存在精度低、误报率高的问题，亟需可解释、无需标注就能跨场景迁移的高准确率检测方案。
### 方法关键点
- 提出TeQHallu神经符号检测框架，全程无监督无需微调，仅依赖LLM通用的底层Text-to-SQL能力：
  1. 多步Prompt引导LLM把参考文档增量转化为SQL关系库，结构化存储所有事实信息并保留来源溯源能力；
  2. 拆解待校验回复的事实claim，生成对应SELECT查询从SQL库拉取匹配的事实证据；
  3. 神经符号对齐校验，结合初始LLM直接预测结果和SQL查询证据，输出最终幻觉分类与可解释依据。
### 关键结果
在RAGTruth和DiaHalu两个权威基准上测试：
1. RAGTruth数据集上，Gemini 2.5 Flash底座的TeQHallu宏观F1达71.3，比零样本直接预测高9.7，超过微调的Llama-2-13B（71.8）接近持平，仅略低于有监督SOTA RAG-HAT（78.0），是所有无监督方法中精度最高。
2. DiaHalu任务型对话子集上，TeQHallu比GPT-4 CoT基线F1高6.46，比Gemini 1.5 Pro CoT基线高6.48，非事实类幻觉检测召回提升15%以上。

**最值得记住的结论**：利用LLM已经掌握的底层通用符号能力做结构化校验，不需要领域微调就能获得媲美有监督方法的性能，还能天然获得可解释的推理链路。
