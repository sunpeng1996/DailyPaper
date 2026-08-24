---
title: 'PromptResponse: Optimizing Prompts for LLM Coding Tasks'
title_zh: 《PromptResponse：面向LLM编码任务的提示词优化研究》
authors:
- Erik Thureck
- Robert Kühnen
- Tim Jacobowitz
affiliations:
- Humboldt-Universität zu Berlin
- Institute of Informatics, HU Berlin
- Human-Computer Interaction Lab, HU Berlin
arxiv_id: '2608.21074'
url: https://arxiv.org/abs/2608.21074
pdf_url: https://arxiv.org/pdf/2608.21074
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: LLM提示工程 · 结构化生成优化
tags:
- Prompt Engineering
- LLM Code Generation
- Prompt Tuning
- GPT-4o
- Evaluation Metrics
one_liner: 基于8200次GPT-4o编码实验，量化验证提示词格式与调优方式对生成效果的影响规律
practical_value: '- 所有需要LLM输出结构化结果的场景（如标签生成、属性抽取、Semantic ID映射）优先用JSON格式prompt，可大幅降低输出异常率，减少后处理成本

  - 避免盲目使用通用LLM生成的调优prompt，prompt调优必须适配当前业务所用的基座模型偏好，否则可能出现效果负向

  - Prompt优化优先做低成本的格式统一调整，无需一开始就投入复杂的Few-Shot/CoT设计，低投入即可拿到可量化的效果提升'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM输出对输入prompt的表述差异高度敏感，但当前针对任务prompt的格式优化、自动调优效果缺乏系统量化的对照实验结论，尤其结构化生成场景缺少可落地的选型依据。
### 方法关键点
基于HumanEval数据集生成语义完全一致、仅语法格式不同的5类prompt：基线版、JSON版、Markdown版、YAML版、LLM自动调优版，调用GPT-4o完成8200次代码生成任务，从生成性能、效率、输出稳定性三个维度做对照评估。
### 关键结果数字
1. 统一结构化格式（尤其JSON）可提升生成效率与语法稳定性，同时任务性能有小幅正向收益
2. LLM自动调优的prompt导致任务性能显著下降，且其余维度无任何显著提升
3. 仅做低成本的prompt格式重写，即可获得可测量的效果提升，自动prompt调优必须充分对齐目标模型的偏好
