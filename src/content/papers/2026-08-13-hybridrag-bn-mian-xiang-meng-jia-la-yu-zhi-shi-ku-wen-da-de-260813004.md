---
title: 'HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification
  for Bangla KBQA'
title_zh: HybridRAG-BN：面向孟加拉语知识库问答的带微调验证的检索增强框架
authors:
- Rathijit Aich
- Nirjhar Das
- Mahfuzulhoq Chowdhury
affiliations:
- Chittagong University of Engineering & Technology
arxiv_id: '2608.13004'
url: https://arxiv.org/abs/2608.13004
pdf_url: https://arxiv.org/pdf/2608.13004
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: 低资源语言RAG · 答案校验优化
tags:
- RAG
- KBQA
- LoRA
- BM25
- BGE-M3
one_liner: 结合混合检索、LoRA微调校验、多级后处理的孟加拉语KBQA RAG框架 获竞赛第一
practical_value: '- 可复用双路RAG Pipeline设计：一路做高召回宽松生成、一路做高精度保守生成，结果互补，适配电商客服、商品属性问答、详情页生成等对准确率和召回率都有要求的场景

  - 可直接复用「生成初版答案→LoRA微调轻量校验模型精修→规则兜底替换→外部搜索补全」的多级校验链路，大幅降低RAG幻觉，适合电商导购、广告文案生成等业务

  - 混合检索的BM25权重0.65、BGE-M3权重0.35的参数配置，以及优先按段落/标点切分、重叠150字符的边界感知分块策略，可直接迁移到中文商品/内容库的RAG系统'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
低资源语言KBQA面临检索相关研究不足、语料资源稀缺、生成结果难以对齐外部知识的痛点，现有RAG方案在小语种场景下 hallucination 率高、召回率不足，亟需高鲁棒性的框架适配低资源场景。
### 方法关键点
- 知识库双路预处理：高精度策略激进清理维基百科冗余噪声，分块长度1000字符、重叠150字符；高覆盖策略轻度清理噪声，分块长度800字符、重叠150字符，优先按段落/标点切分保障语义连贯
- 混合检索链路：BM25做词法匹配、BGE-M3做语义匹配，按0.65:0.35加权融合结果，再用BGE-Reranker-v2-M3做交叉编码器重排，选中Top片段后补全前后相邻段落构造上下文
- 双路生成+多级校验：高精度Pipeline要求无证据时返回上下文缺失标记，高覆盖Pipeline允许调用预训练知识补全、禁用缺失标记；用LoRA微调Gemma-4-31B-Instruct做答案校验，仅修正有明确上下文支持的错误；再用高精度Pipeline结果替换校验后的缺失标记，剩余缺失案例提取实体后调用搜索引擎补答
### 关键结果
实验基于Indic-RAG-Suite衍生的孟加拉语KBQA数据集，含3000训练三元组、1500测试问题、6500条维基百科知识库。对比单路高精度RAG基线（Public F1 0.693、Private F1 0.691）、单路高覆盖RAG基线（Public F1 0.702、Private F1 0.699），最终框架Public F1达0.7165、Private F1达0.7291，拿下竞赛第一。

**最值得记住的一句话**：RAG系统的性能提升，不仅来自检索和生成模块的优化，分层校验+多链路兜底的后处理策略能以极低的计算成本带来显著的效果增益
