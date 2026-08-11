---
title: Factorized Hypothesis Search for Evidence-to-Taxonomy Retrieval
title_zh: 面向证据到分类体系检索的因子化假设搜索
authors:
- Linhai Ma
- Ethan F. Wei
- Xueqing Peng
- Yan Wang
- Lingfei Qian
- Víctor Gutiérrez-Basulto
affiliations:
- The Fin AI, USA
- Yale University, USA
- Cardiff University, UK
arxiv_id: '2608.06614'
url: https://arxiv.org/abs/2608.06614
pdf_url: https://arxiv.org/pdf/2608.06614
published: '2026-08-05'
collected: '2026-08-11'
category: RAG
direction: RAG检索优化 · 非显式query映射
tags:
- Retrieval
- Hypothesis Search
- Taxonomy Mapping
- Query Generation
- Multi-query Retrieval
one_liner: 提出因子化假设搜索框架，解决间接证据到分类体系映射的检索就绪差，跨领域性能超现有非Oracle方法
practical_value: '- 电商场景中非结构化间接证据映射（如用户评论片段、客服对话、商家短文本映射到标准类目/SPU库）可直接复用FHS框架：先定义类目语义维度，生成多组因子化假设做检索，头部准确率显著高于单query改写

  - 当检索输入不是显式query（如用户行为序列、上下文信息）时，无需强行做单query改写，可并行生成多个因子化语义假设，分别生成规则式标签query和LLM生成的定义式query做多路召回，用RRF融合结果

  - 召回后排序阶段可复用维度级验证思路：基于预定义语义维度，让LLM逐维度验证候选和假设的匹配度，加权到召回得分中，可大幅提升头部准确率，且无需扩展召回深度

  - 检索优化优先做并行多假设检索，不要盲目做迭代式query refinement，论文验证并行首轮效果已经超过迭代多轮，且推理成本低很多，该结论可直接复用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大型分类体系检索默认输入为显式目标概念，但实际场景中输入多为间接证据（如金融表格单元格、临床诊断短提及），存在「检索就绪差」：直接用原始证据检索时目标条目往往排名靠后，单query改写又容易过早锁定错误语义分支，导致头部召回率低，现有方法无法解决语义不确定性带来的检索排序瓶颈。
### 方法关键点
- 因子化假设生成：基于预定义的语义维度（如金融领域的类目族、事件类型、时间维度等），并行生成多组部分赋值的语义假设，不确定维度留空避免错误猜测
- 双路query渲染：每个假设对应两类检索query：规则拼接的标签式query（匹配分类体系标签结构）、LLM生成的定义式query（匹配自然语义），做多路召回
- 共识融合：用RRF融合多路检索结果得到候选池
- 维度级验证：对每个候选逐维度验证与各假设的匹配度，得到支持度得分，和召回得分加权后重排序，仅调整已有候选顺序不扩展召回池
### 关键结果
在金融分类标注、CodiEsp临床ICD编码两个跨领域任务上对比7类基线，均取得非Oracle方法最优性能：金融任务Recall@1达0.185，较最优基线提升4.4个绝对点，MRR达0.257，最终准确率0.255；临床编码任务Recall@1达0.264，较最优基线提升6.3个绝对点，MRR达0.352，最终准确率0.330。消融实验验证迭代式多轮检索相比并行首轮无收益且推理成本高。
### 核心结论
对于非显式query的检索场景，并行生成多组因子化语义假设做多路召回+维度级重排序的效果远优于单query改写和迭代式检索，且推理成本更低。
