---
title: 'Where Should a Document Live: Context, Representations, or Parameters?'
title_zh: LLM知识注入选型对比：上下文、表征缓存与参数微调的权衡
authors:
- Nathanaël Carraz Rakotonirina
- Momchil Hardalov
- Gonzalo Iglesias
- Adrià de Gispert
affiliations:
- Amazon AGI
arxiv_id: '2609.17346'
url: https://arxiv.org/abs/2609.17346
pdf_url: https://arxiv.org/pdf/2609.17346
published: '2026-09-15'
collected: '2026-09-16'
category: LLM
direction: LLM 知识注入方法对比评估
tags:
- Knowledge Injection
- KV cache
- LoRA
- RAG
- Catastrophic Forgetting
one_liner: 系统对比三类LLM知识注入方法的性能、效率、遗忘特性与多场景适配性
practical_value: '- 多文档知识库RAG场景（如电商客服知识库、商品规格库问答）优先选Cartridges方案，是唯一能匹配ICL效果的注入方法，比LoRA合并方案高29分，比Compaction高15分，可大幅降低长上下文prefill成本

  - 单文档高频访问场景（如单个大促活动规则问答、爆款商品详情问答）可选用低压缩率Compaction，效果匹配ICL且完全无灾难性遗忘，比LoRA性能高约9个点

  - 小体量垂直知识注入且无多文档合并需求时，优先选LoRA而非MLP adapter或全量微调，LoRA几乎无通用能力遗忘，参数体积固定不随文档长度变化，部署成本最低

  - 所有知识注入训练均可复用KL蒸馏目标，相比传统next token prediction平均提升4个点性能，无需额外成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM外部知识注入分为上下文（ICL/RAG）、表征（压缩KV缓存）、参数（PEFT/全量微调）三类方案，此前对比存在场景局限（仅单文档）、数据污染（用预训练见过的维基内容）、未做存储匹配等问题，业务选型缺乏无偏参考依据。
### 方法关键点
- 公平对比7种主流方案：无上下文基线、ICL、Cartridges（训练型KV前缀）、Compaction（无训练KV压缩）、LoRA、MLP adapter、全量微调
- 覆盖两类核心场景：单文档oracle（隔离检索误差，仅测注入能力）、多文档RAG（检索top-k后合并对应适配器）
- 所有方法用统一自合成训练数据、KL散度蒸馏目标，严格控制适配器存储大小做对标，同时测试通用能力遗忘情况
### 关键结果
- 单文档场景：低压缩率（2×）Compaction平均得分73.4，匹配ICL基线的73.6，比LoRA高8.9分；高压缩率下Cartridges性能稳定，领先参数类方法10分
- 多文档场景：仅Cartridges可匹配ICL效果，领先LoRA合并方案29分、Compaction拼接方案15分；LoRA合并、Compaction拼接随召回文档数k增大性能暴跌
- 遗忘情况：LoRA、Compaction几乎无通用能力损失，Cartridges平均性能降6%（代码任务降13%），MLP adapter、全量微调遗忘严重
### 核心结论
没有普适最优的知识注入方案，选型需结合场景：多文档RAG选Cartridges，单文档高频场景选低压缩率Compaction，小体量无合并需求选LoRA
