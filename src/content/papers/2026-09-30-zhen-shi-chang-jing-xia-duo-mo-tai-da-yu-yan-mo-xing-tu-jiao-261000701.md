---
title: 'From Images to Tasks: Characterizing Multimodal LLM Interactions in the Wild'
title_zh: 真实场景下多模态大语言模型图像交互的任务特征分析
authors:
- Jinyi Ye
- Scott Counts
- Gaurav Verma
- Kate Lytvynets
- Weiwei Yang
affiliations:
- University of Southern California
- Microsoft
- Microsoft Research
arxiv_id: '2610.00701'
url: https://arxiv.org/abs/2610.00701
pdf_url: https://arxiv.org/pdf/2610.00701
published: '2026-09-30'
collected: '2026-10-03'
category: Multimodal
direction: 多模态大模型 · 真实用户行为分析
tags:
- Multimodal-LLM
- User Behavior Analysis
- Benchmark Evaluation
- Task Taxonomy
- Real-world Usage
one_liner: 基于4万+真实多模态会话构建10类能力层级分类，揭示现有benchmark与真实需求的错配
practical_value: '- 设计电商多模态Agent时可参考三层能力链路，优先覆盖高频组合能力：如识别商品截图生成种草文案、解析运营数据表自动生成分析报告

  - 多模态产品迭代可利用用户认知卸载特征：优先支持截图、表格、活动页等视觉输入的自动结构化解析，降低用户输入成本，比如商家上传设计稿自动生成后台配置

  - 自研多模态评估体系时，需补充业务高频的生成类组合任务端到端评估，避免完全复用现有benchmark导致的评估与真实需求错配'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有多模态LLM的研究和评估多聚焦技术能力优化，对真实场景下用户上传图像时的任务需求、能力组合特征缺乏大规模实证分析；且现有benchmark多为专家自上而下设计，与实际用户需求存在明显错配，无法有效指导模型迭代和产品功能设计。

### 方法关键点
- 数据集：采集42617条微软Copilot匿名图像上传会话，23413条ChatGPT多模态会话作为验证集，所有数据先做去标识化处理，生成任务摘要和图像摘要规避隐私风险
- 分类体系：基于TnT-LLM框架迭代构建三层（感知/认知/生成）10类多模态能力层级分类体系，覆盖识别、知识调用、OCR、文本生成、推理、数据分析等核心能力
- 分析方法：统计能力分布与组合特征，对比多模态与纯文本任务的语义空间差异，映射253个现有多模态benchmark的能力覆盖度，用S/D（供给/需求）比值量化匹配度

### 关键结果
- 74.17%的图像上传会话需要调用多种能力，高频组合包括知识+文本生成、识别+推理、知识+识别
- 多模态任务空间比纯文本更宽泛，76%的多模态任务在纯文本任务分布外，30%的多模态任务无法仅通过纯文本输入完成
- 现有benchmark对感知+推理类固定答案任务覆盖充足（S/D最高3.12），但对高频的知识+文本生成（S/D=0.22）、识别+代码生成（S/D=0.09）等生成类组合任务覆盖极低

### 核心结论
现有多模态benchmark多聚焦「图像到固定答案」的单点任务，而真实用户的多模态需求大多是「图像作为输入，最终生成可落地的结构化内容/代码/决策」的组合式链路任务
