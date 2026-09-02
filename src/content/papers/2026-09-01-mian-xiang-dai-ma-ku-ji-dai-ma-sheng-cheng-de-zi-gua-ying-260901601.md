---
title: Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation
title_zh: 面向代码库级代码生成的自适应关键令牌感知检索框架
authors:
- Kefeng Duan
- Dewu Zheng
- Yanlin Wang
- Terry Yue Zhuo
- Mingwei Liu
- Jianxing Yu
- Jiachi Chen
- Ensheng Shi
- Xilin Liu
- Yuchi Ma
affiliations:
- 中山大学
- 莫纳什大学
- CSIRO Data61
- 浙江大学
- 华为云
arxiv_id: '2609.01601'
url: https://arxiv.org/abs/2609.01601
pdf_url: https://arxiv.org/pdf/2609.01601
published: '2026-09-01'
collected: '2026-09-02'
category: RAG
direction: 检索增强生成 · 动态按需触发
tags:
- RAG
- Critical Token
- Dynamic Retrieval
- Dense Retriever
- Code Generation
one_liner: 生成过程中识别关键令牌触发按需RAG，搭配位置感知加权检索，代码生成效果最高相对提升15.4%
practical_value: '- 可复用关键令牌识别框架：采用token mismatch、生成熵、后续注意力权重三个无监督规则标注，搭配轻量MLP分类器识别生成路径上的高风险节点，可直接迁移到电商推荐文案生成、Agent工具调用等场景的错误拦截与实时修正

  - RAG成本优化方案：无需全局多轮检索，仅在关键节点触发定向检索，大幅降低RAG调用量与token开销，适配电商商品详情生成、客服Agent长会话问答等对latency敏感的场景

  - 稠密检索性能优化trick：采用首尾双高斯加权的pooling策略，提升query、核心属性和上文生成内容的权重，检索精度提升同时无额外推理开销，可直接替换现有召回层的均值pooling逻辑

  - 小样本分类优化技巧：用token自信息筛选高价值难负样本平衡分类数据集，大幅提升小样本场景下关键节点分类器的识别准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有代码库级代码生成的RAG方案多为任务级静态检索，未关注自回归生成过程中少量关键令牌的错误会引发级联语义偏差，最终导致整体功能失效；全量代码库上下文喂入超过LLM长度限制，全流程多轮检索又会带来过高推理开销。
### 方法关键点
- 离线阶段：基于token与真值不匹配、生成熵、后续Top5注意力均值三个规则标注关键令牌，通过自信息筛选高价值难负样本平衡训练集，训练仅百万参数级的轻量MLP分类器识别关键令牌
- 检索优化：提出首尾双高斯加权的稠密检索pooling策略，提升序列头部（如query、核心属性）和尾部（如上文生成内容）的权重，权重可预计算，无额外推理开销
- 推理流程：生成时逐token输入分类器判断，仅识别到关键令牌时用当前上下文构造新query触发二次检索，更新上下文后重生成当前token，后续生成复用更新后的上下文
### 关键实验结果
在RepoExec、CoderEval两个代码库级代码生成基准上对比RawRAG、RepoCoder、RLCoder等SOTA方案，Pass@5相对提升最高8.4%（RepoExec）、15.4%（CoderEval）；仅需增加3.3ms per token的延迟，端到端耗时比多轮检索的RepoCoder低40.9%；关键令牌仅占总生成token的5%~11%。
### 核心结论
自回归生成中绝大多数错误集中在占比不到11%的关键令牌上，定向优化这些节点的上下文供给，性价比远高于全局检索或全流程优化。
