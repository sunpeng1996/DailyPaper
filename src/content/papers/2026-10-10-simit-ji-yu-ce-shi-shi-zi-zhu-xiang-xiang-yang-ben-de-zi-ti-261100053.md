---
title: 'SIMIT: Self-Improving Vision-Language Models via Imagination at Test-Time'
title_zh: SIMIT：基于测试时自主想象样本的自提升视觉语言模型框架
authors:
- Mehmet Onurcan Kaya
- Desmond Elliott
- Dim P. Papadopoulos
affiliations:
- Technical University of Denmark
- Pioneer Center for AI
- University of Copenhagen
arxiv_id: '2611.00053'
url: https://arxiv.org/abs/2611.00053
pdf_url: https://arxiv.org/pdf/2611.00053
published: '2026-10-10'
collected: '2026-11-03'
category: Training
direction: 多模态大模型 · 测试时自提升框架
tags:
- VLM
- Test-Time Adaptation
- Self-Improvement
- Data Synthesis
- Multimodal
one_liner: 无需标注与外部模型，测试时生成可控相似练习样本提升视觉语言模型多任务表现
practical_value: '- 电商多模态商品理解/搜索场景，冷启动无标注query可复用SIMIT生成可控相似样本做ICL优化，无需额外标注成本

  - 长尾query优化可借鉴自适应预算策略，给模型低置信度query分配更多生成样本/计算资源，提升长尾case准确率

  - 多模态合成样本校验可复用多阶段验证+难度过滤pipeline，避免无效样本强化模型原有错误'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM测试时自提升方法要么仅优化推理逻辑不更新模型效果有限，要么基于多数投票/自判断的奖励容易强化已有错误，且大多依赖标注数据或外部模型，部署后泛化性差。
### 方法关键点
1. 测试时无需先解出目标query，直接生成答案可控的相似<问题-答案-图像>三元组作为练习样本；
2. 结合原生图像生成能力+结构化视觉（文档/图表/示意图）技能库覆盖多模态任务，搭配多级校验确保样本与答案匹配，通过难度过滤保留高信息度样本；
3. 自适应预算给低置信度query分配更多样本，支持免微调的in-context学习（SIMIT-ICL）和权重微调（SIMIT-FT）两种落地模式。
### 关键结果
在17个多模态基准测试中全面优于现有自提升方法，SIMIT-FT相对BAGEL-7B平均相对提升7.20%，免微调的SIMIT-ICL也可实现6.98%的平均相对提升。
