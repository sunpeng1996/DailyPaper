---
title: Extending LLM Context via Associative Recurrent Memory
title_zh: 基于关联循环记忆的大语言模型上下文扩展方案
authors:
- Gleb Kuzmin
- Ivan Rodkin
- Aydar Bulatov
- Yuri Kuratov
- Lyudmila Rvanova
- Mikhail Katkov
- Ilia Sochenkov
- Misha Tsodyks
- Timothy Baldwin
- Mikhail Burtsev
affiliations:
- FusionBrain Lab
- MBZUAI
- Cognitive AI Systems Lab
- RUDN
- London Institute for Mathematical Sciences
arxiv_id: '2607.11614'
url: https://arxiv.org/abs/2607.11614
pdf_url: https://arxiv.org/pdf/2607.11614
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: LLM长上下文扩展 · 关联循环记忆
tags:
- Long-Context-LLM
- Associative-Recurrent-Memory
- ARMT
- Training-Recipe
- Memory-Optimization
one_liner: 提出关联循环记忆Transformer训练方案，低成本扩展LLM上下文窗口，省30%FLOPs且长场景性能不降
practical_value: '- 电商/Agent场景下的长上下文任务（多轮会话理解、长商品评测聚合、全文档RAG推理）可直接复用ARMT架构，不需要全量重训LLM，仅需LoRA微调即可获得超原生窗口的稳定性能，GPU内存占用随长度恒定，大幅降低部署成本

  - 训练领域长上下文小模型时，可直接复用论文的4步训练配方：持续预训练初始化记忆模块+合成拼接长数据+课程学习逐步提升上下文长度+仅预选20%层加记忆块，训练速度提升30%，参数规模降低30%，无明显性能损失

  - 业务缺乏长上下文标注数据时，可复用其合成数据方案：将多个短文档拼接为长上下文，保留每个短文档对应的原有标注（QA/分类标签等），低成本构建长训练集，适配电商商品问答、客服知识库等场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Transformer长上下文处理受限于自注意力平方级计算成本，Mamba等全循环架构需从头训练、复杂推理任务性能弱于原生Transformer，小参数领域LLM缺乏低成本长上下文扩展方案，超过原生窗口后性能暴跌，无法满足电商多轮用户会话理解、长文档RAG、多商品评测聚合等业务的长序列处理需求。
### 方法关键点
- 核心架构ARMT：将长输入切分为固定长度片段，片段内保留全注意力保证短序列性能，层间新增关联记忆块跨片段传递关键信息，实现GPU内存随序列长度恒定
- 适配训练四件套：① 持续预训练：用长语料初始化新增记忆模块参数，降低下游微调难度；② 课程学习：逐步增加训练样本的片段数（从2段到8段），避免冷启动无有效梯度；③ 合成长数据：拼接多个短文档并保留原有标注，低成本补充长上下文训料；④ 层预选：仅在20%左右的关键层（中层+末尾层各选若干）加记忆块，无需全层改造
### 关键结果
以Gemma-3-1B、SmolLM-2-360M为 backbone，在代码类型预测、长文档QA数据集上测试：① 原生上下文窗口内性能与基线持平，总FLOPs降低30%；② 超过32k的长OOD场景下，原生Gemma的EM指标暴跌至46.3%，ARMT稳定保持74%以上，最高达80.1%；③ 仅保留5层记忆块的ARMT性能优于全层版本，训练速度提升30%，GPU内存占用更低。

最值得记住的结论：小参数领域LLM的长上下文扩展无需全量重训或更换底层架构，通过增量增加关联记忆模块+适配训练配方，即可用极低开销实现超原生窗口的稳定性能。
