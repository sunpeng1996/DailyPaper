---
title: 'IROH: Insightful Ranking Of Humor using Multi-Stage Hybrid Retrieval with
  Rationale-Distilled LLM Judges for JOKER 2026 Track Task 1 English'
title_zh: IROH：多阶段混合检索与推理蒸馏LLM裁判的幽默检索系统
authors:
- Ana-Maria Luisa Mocanu
- Sebastian Mocanu
- Ciprian-Octavian Truică
- Elena-Simona Apostol
affiliations:
- National University of Science and Technology POLITEHNICA Bucharest
- Academy of Romanian Scientists
arxiv_id: '2609.15618'
url: https://arxiv.org/abs/2609.15618
pdf_url: https://arxiv.org/pdf/2609.15618
published: '2026-09-14'
collected: '2026-09-16'
category: RecSys
direction: 幽默内容检索 · LLM裁判蒸馏
tags:
- Hybrid-Retrieval
- LLM-Judge
- Rationale-Distillation
- LoRA
- Cross-Encoder
one_liner: 提出三阶段幽默检索pipeline，采用推理蒸馏LLM裁判集成，获JOKER 2026任务第一MAP 0.6347
practical_value: '- 多阶段检索排序架构可直接迁移到电商场景的创意文案筛选、趣味UGC排序、广告素材合规/吸引力分级等需要细粒度语义判断的任务

  - 推理蒸馏训练优先用轻量通用rationale做监督信号，无需复杂分类体系，7B级小模型蒸馏后效果可超过30B级大模型，大幅降低线上推理成本，适合高并发业务场景

  - 慎用LLM生成的结构化硬负样本做数据增强，此类样本会抬升本地验证指标但降低泛化性，业务场景优先用真实语料挖掘的硬负样本

  - 多个LLM裁判加权集成可进一步提效，核心强模型分配60%左右权重，剩余权重分配给互补能力模型，性价比远高于单独升大模型规格'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
幽默内容检索需要同时满足语义相关性和幽默属性匹配，传统检索pipeline仅能捕捉字面特征，无法识别双关、谐音、反讽等隐性幽默机制，2025年该任务SOTA的MAP仅0.35，性能远未达实用要求。
### 方法关键点
- 三阶段检索架构：1）混合召回：BM25+查询扩展与BGE稠密检索并行，经RRF融合输出Top4000候选；2）交叉编码器重排：微调GTE-Reranker-ModernBERT-Base重排候选，与召回得分加权融合输出Top1000候选；3）LLM裁判集成：3个LoRA微调模型（Qwen2.5-7B、Gemma4-31B通用rationale版、Gemma4-31B结构化rationale版）按0.6:0.3:0.1加权投票，输出软得分与重排得分融合得到最终排序。
- 训练策略：用Gemma4生成通用/结构化两类rationale作为监督信号训练LLM裁判，同时尝试生成4类结构化硬负样本做数据增强。
### 关键结果
在CLEF 2026 JOKER Track Task 1英文数据集上，最优配置MAP达0.6347，获赛道第一名，相比2025年SOTA提升81%；7B级Qwen2.5通用rationale微调版MAP达0.6055，超过所有Gemma4-31B配置；结构化硬负样本会让本地验证分提升，但官方测试分下降10%~30%。
### 核心结论
对细粒度领域判别任务，小模型的微调质量和训练数据的信号一致性，比大模型的参数量更重要，过度结构化的监督信号反而会引入噪声降低效果
