---
title: 'SABER-Math: Automated Benchmark for Information Retrieval Evaluation in Mathematics'
title_zh: SABER-Math：面向数学领域信息检索的自动化评估基准
authors:
- Nikolay Georgiev
- Maria Drencheva
- Kseniia Ibragimova
- Ivo Petrov
- Dimitar I. Dimitrov
- Martin Vechev
affiliations:
- INSAIT, Sofia University "St. Kliment Ohridski"
- ETH Zurich
arxiv_id: '2606.29894'
url: https://arxiv.org/abs/2606.29894
pdf_url: https://arxiv.org/pdf/2606.29894
published: '2026-06-29'
collected: '2026-07-02'
category: Eval
direction: 检索评估 · 垂类自动化基准构建
tags:
- Information Retrieval
- Evaluation Benchmark
- Mathematical Retrieval
- LLM Annotation
- RAG
one_liner: 首个无需专家标注的数学领域IR自动化基准，可精准衡量检索系统的细粒度数学相关性表现
practical_value: '- 构建垂类检索评估基准时可复用「LLM抽取语义标签+多维度相似性召回候选+LLM偏好排序打标」的无专家标注流程，大幅降低benchmark构建成本

  - 垂类检索选型时不要完全依赖通用MTEB等基准得分，需针对自身业务垂类（如电商标品、教育题典）构建专属小样本验证集，避免选型偏差

  - 符号密集类垂域（如电商规格参数、教育公式）检索优化可优先测试最新通用embedding模型，其效果优于传统垂域专用检索系统'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
Agent类数学推理系统对数学IR依赖度提升，但现有通用检索基准无法捕捉数学细粒度相关性，也无法单独隔离检索模块对下游任务的影响，缺乏低成本的数学专属检索评估方案。
### 方法关键点
基于283K高中数学题解数据，分三步构建重排序评估任务：1）LLM抽取每道题的解算摘要与数学主题标签；2）基于本体主题相似性、解算摘要字面相似性召回query相关候选文档；3）采用瑞士制LLM偏好锦标赛生成文档细粒度相关性打分。
### 关键结果
现代embedding模型效果显著优于传统、数学专用检索基线，但最强系统在代数、微积分等符号密集场景仍表现不佳；通用MTEB基准对数学检索性能的预测可靠性差，尤其无法匹配新嵌入模型的垂类表现。
