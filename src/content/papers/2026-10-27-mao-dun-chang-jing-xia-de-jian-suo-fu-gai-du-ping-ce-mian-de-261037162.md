---
title: 'Coverage Under Contradiction: A Benchmark for Negation-Aware Retrieval'
title_zh: 矛盾场景下的检索覆盖度评测：面向否定感知检索的基准
authors:
- Pasha Abrishamchian
- Eugene Yang
- Andrew Yates
- Nazli Goharian
- Ophir Frieder
affiliations:
- Georgetown University
- Johns Hopkins University
arxiv_id: '2610.37162'
url: https://arxiv.org/abs/2610.37162
pdf_url: https://arxiv.org/pdf/2610.37162
published: '2026-10-27'
collected: '2026-10-29'
category: Eval
direction: RAG检索评测 · 否定感知覆盖度基准
tags:
- RAG
- Retrieval
- Benchmark
- Negation-Aware
- Information-Coverage
one_liner: 构造带受控矛盾的检索覆盖度基准，测试检索器对与预训练知识冲突的语料的召回能力
practical_value: '- 电商商品问答、客服RAG场景可复用该基准的否定样本构造流程，生成和业务场景匹配的测试用例，验证检索模块能否正确召回含否定语义的商品属性、规则类内容，降低下游回答幻觉

  - 检索模块选型可参考实验结论，在否定语义高发的场景（如售后规则、商品参数辟谣）增加BM25作为兜底检索通道，弥补密集检索器对近孪生否定文本区分能力差的缺陷

  - 可复用该论文的配对否定数据构造pipeline，为业务的检索、排序模型生成对比训练样本，增强模型对否定语义的感知能力，提升语料忠实度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG检索覆盖度评测基准大多基于通用事实，而当前主流的密集检索器、LLM查询扩展等模块均继承了预训练阶段的参数知识，当语料中存在与预训练知识矛盾的证据时，极易优先召回符合常识的内容，忽略语料实际存在的否定表述，导致下游RAG生成内容与语料不符，产生幻觉。现有基准无法验证检索器在该矛盾场景下的表现，亟需针对性评测资源。
### 方法关键点
- 复用CoverageBench的284个查询主题、3496个原子信息点（nugget）、11.6万条nugget-文档关联关系，为每个nugget生成语义、实体、上下文一致的否定版本，确保正反表述互斥。
- 对每条关联关系定位原文档中支持nugget的文本片段，仅改写该片段生成支持否定nugget的新文档，保留其余上下文不变，隔离语义翻转的干扰变量。
- 配套输出全链路质量元数据（否定类型、语义相似度、编辑长度、多轮异源LLM验证结果、人工抽检结果），支持用户按需过滤测试集适配不同评测场景。
### 关键实验
基准覆盖6个公开检索数据集，共6.3万条正反配对证据。对比BM25、Qwen3-Embedding、Jina-Embedding三类主流检索器：① 加入否定样本后，BM25的α-nDCG@20平均下降0.083，两类密集检索器下降0.14~0.146，覆盖度下降幅度显著更高；② 针对编辑长度<2%的近孪生文档对，BM25能在84%的配对中正确区分正反表述，而Qwen3、Jina的区分准确率仅为58%、56%，接近随机水平。
### 核心结论
当前主流密集检索器对仅存在否定语义差异的近孪生文本几乎没有区分能力，业务RAG系统如果只依赖密集检索，很容易漏召回与常识矛盾的语料证据，导致幻觉。
