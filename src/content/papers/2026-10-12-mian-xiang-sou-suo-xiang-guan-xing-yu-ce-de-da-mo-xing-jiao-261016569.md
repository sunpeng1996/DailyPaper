---
title: From a Large-Scale Teacher to Efficient Multimodal Students for Search Relevance
  Prediction
title_zh: 面向搜索相关性预测的大模型教师-多模态学生蒸馏框架
authors:
- Tomasz Gniazdowski
- Mohammadreza Momenifar
- Nadia Vase
- Shahram Khadivi
- Wiktor Walentynowicz
- Nicola Ueffing
- Jan Pawlowski
- Piotr Szymanski
- Abraham Bagherjeiran
affiliations:
- eBay
- Tooploox
arxiv_id: '2610.16569'
url: https://arxiv.org/abs/2610.16569
pdf_url: https://arxiv.org/pdf/2610.16569
published: '2026-10-12'
collected: '2026-10-14'
category: RecSys
direction: 搜索相关性 · 多模态知识蒸馏
tags:
- Knowledge Distillation
- LLM-as-a-Judge
- Multimodal LLM
- Search Relevance
- E-commerce
one_liner: 通过GPT-4.1教师生成规模化标注，蒸馏得到多模态小模型，兼顾搜索相关性精度与推理效率
practical_value: '- 可复用「少量人工标注校准LLM-as-a-Judge→生成大规模标注→蒸馏小模型」的pipeline，大幅降低电商搜索相关性标注的人力成本，同时解决大模型推理成本过高无法落地的问题

  - 训练多模态相关性模型时，加入教师生成的推理解释同时保留商品图像输入，可提升1~3pct的准确率，且冻结视觉编码器能有效防止合成数据过拟合

  - 部署阶段选择FP8量化的12B参数多模态模型可达到帕累托最优：精度接近GPT-4.1教师，单H100吞吐量可达271 req/s，成本远低于商用大模型API'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索query-item相关性预测依赖人工标注，成本高、规模小，无法满足模型快速迭代需求；LLM-as-a-Judge可生成规模化标注，但商用大模型推理成本高、吞吐低，无法适配生产级搜索的低延迟高吞吐要求。
### 方法关键点
- 构建少量高质量人工标注数据集校准LLM-as-a-Judge pipeline：采用结构化prompt（含分级规则、few-shot示例）迭代优化，GPT-4.1作为教师在3人标注测试集上准确率达83.68%，对齐人类标注水平。
- 用校准后的教师生成48万+条平衡类别的标注数据，包含相关性标签+推理解释，训练Gemma-3系列多模态学生模型，冻结视觉编码器防止合成数据过拟合，同时蒸馏标签与推理信号。
- 学生模型支持轻量化推理模式：仅输出相关性标签时延迟极低，可按需开启解释生成，适配不同业务场景。
### 关键结果
- 12B参数学生模型在独立人工测试集Test2上准确率达65.24%，超过教师GPT-4.1的64.38%，F1也优于教师；在Test1上准确率81.59%，仅比教师低2.1pct。
- FP8量化的12B学生模型单H100上无解释吞吐量达271.54 req/s，较FP16提升40%，精度损失小于0.5pct，推理成本较GPT-4.1降低两个数量级。
### 核心结论
对于电商搜索这类对推理效率要求极高的场景，用对齐人类的大模型教师生成标注蒸馏小模型，是兼顾效果、成本、落地性的最优路径之一。
