---
title: Two-Token Features and Small-Large Ensembles for VLM Hallucination Detection
title_zh: 面向VLM幻觉检测的双Token特征与大小模型集成方案
authors:
- Eli Schwartz
affiliations:
- IBM Research
arxiv_id: '2609.10244'
url: https://arxiv.org/abs/2609.10244
pdf_url: https://arxiv.org/pdf/2609.10244
published: '2026-09-09'
collected: '2026-09-10'
category: Multimodal
direction: 多模态大模型 · 幻觉检测
tags:
- VLM
- Hallucination Detection
- Model Ensemble
- OCR Grounding
- Fine-tuning
one_liner: 用4B微调小VLM双token特征分类器与400B零样本大VLM集成，实现高精度多语言VLM幻觉检测
practical_value: '- 大小模型集成策略可直接复用，业务侧用小模型微调实现低时延高精度推理，搭配大模型零样本能力补全泛化性，平衡算力成本与效果上限

  - 双Token特征构建技巧可迁移到生成内容校验场景，比如电商商品文案、商品图OCR识别结果的错误检测，取相邻Token隐藏层拼接做分类器输入可提升精度

  - 用大模型生成合成幻觉数据做训练增强，可解决业务场景下标注数据不足的问题，同时提升大小模型集成的多样性

  - OCR接地方法可复用在多模态内容质检流程中，比如电商图文一致性校验场景引入现成OCR结果可显著降低幻觉误判率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
SHROOM-Visions 2026多语言VLM字符级幻觉检测任务中，零样本超大VLM检测的字符粒度精度不足，微调400B级大模型算力成本极高，亟需平衡效果与开销的落地方案。
### 方法关键点
1. 微调4B参数量小VLM，设计双Token特征头，拼接当前与前一Token的语言塔中间层隐藏状态实现逐Token分类；
2. 预测阶段与400B参数量零样本大VLM的检测结果集成，两个模块均引入现成OCR结果做图文接地减少误判；
3. 用大模型生成合成幻觉数据做训练增强，通过验证集优选特征层、训练数据组合与OCR接地策略。
### 关键结果
在隐藏测试集上平均Cor 0.487、Cor-lbl 0.387，在EN、FR、IT、ZH赛道分别位列6/28、6/21、8/21、7/22，性能领先超50%参赛队伍。
