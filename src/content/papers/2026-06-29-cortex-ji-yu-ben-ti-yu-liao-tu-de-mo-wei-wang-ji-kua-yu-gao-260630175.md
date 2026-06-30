---
title: 'CORTEX: High-Quality Cross-Domain Organization of Web-Scale Corpora through
  Ontological Corpus Graph'
title_zh: CORTEX：基于本体语料图的万维网级跨域高质量语料组织框架
authors:
- Chengtao Gan
- Xiaoke Guo
- Yushan Zhu
- Zhaoyan Gong
- Zhiqiang Liu
- Songze Li
- Huajun Chen
- Wen Zhang
affiliations:
- Zhejiang University
- JIUTIAN Research, Beijing
arxiv_id: '2606.30175'
url: https://arxiv.org/abs/2606.30175
pdf_url: https://arxiv.org/pdf/2606.30175
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: LLM预训练 · 语料结构化组织
tags:
- knowledge distillation
- corpus construction
- ontology
- cross-domain
- LLM pretraining
one_liner: 提出首个统一质量精炼、本体构建、跨域关联建模的万维网级语料组织框架CORTEX
practical_value: '- 大模型质量评估的知识蒸馏方案可复用：将大模型多维度质量评估能力蒸馏到0.3B小模型，实现1000×压缩，适合电商海量UGC、商品文案的低成本质量筛选

  - OCG的LLM驱动增量本体演化方法，可直接借鉴用于电商类目体系自动化构建，自动从海量内容中生长层级类目，支持跨域关联挖掘

  - 基于TFS权重的跨域关联计算方法，可用于推荐系统挖掘跨类目商品关联、跨域用户兴趣关联，提升个性化推荐效果

  - 结构化语料组织方式适合构建Agent/RAG用的高质量知识库，支持任意粒度跨域检索，提升检索准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：大语言模型训练对数据规模和质量要求不断提升，现有语料构建 pipeline 仅输出平面无结构的文档集合，缺少多维度质量评估、系统化知识组织和跨域关联建模；直接用大模型做万亿token级质量评估成本过高，无法落地，亟需可扩展的高质量结构化语料构建方案。

**方法关键点**：
1. 提出三层异质结构Ontological Corpus Graph (OCG)，统一质量精炼、本体构建和跨域关联建模；
2. 高质量内容层：通过知识蒸馏将多教师大模型的多维度质量评分能力压缩到0.3B参数学生模型，提出Ordinal-Aware Regression (OAR)损失，同时拟合连续评分和优化离散分类边界，压缩比超1000×；
3. 轻量本体层：从维基百科初始化概念体系，通过LLM驱动自动化增量演化，自动扩展覆盖语料的层级概念，收敛后做准入控制得到最终本体；
4. 对齐层：通过TFS（Typicality–Fidelity–Specificity）加权建立文档-概念-关键词关联，支持任意层级粒度的跨域关联计算和检索。

**关键结果**：在中文Common Crawl上产出24.14 B-token精炼高质量语料，学生模型评分与教师的Spearman相关系数达0.805~0.922，高置信度优质内容召回超95%；持续预训练验证中，Qwen2.5-7B在金融领域评测平均得分从基线39.4提升到加入跨域数据后的52.1；构建的CORTEXBENCH跨域推理基准上，最优GPT-5闭卷准确率仅47.2%，具备足够区分度。

最值得记住的结论：语料构建已经从单纯的平面过滤升级到结构化知识组织阶段
