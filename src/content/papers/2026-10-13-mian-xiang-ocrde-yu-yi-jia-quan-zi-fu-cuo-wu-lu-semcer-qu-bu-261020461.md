---
title: 'Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR'
title_zh: 面向OCR的语义加权字符错误率semCER：区分不同错误的实际损害
authors:
- Nguyen Nguyen
- Yongyi Zang
affiliations:
- University of Rochester
- Independent
arxiv_id: '2610.20461'
url: https://arxiv.org/abs/2610.20461
pdf_url: https://arxiv.org/pdf/2610.20461
published: '2026-10-13'
collected: '2026-10-17'
category: Eval
direction: OCR评价指标 · 语义加权字符错误率
tags:
- OCR
- Evaluation Metric
- CER
- LLM Judge
- Multilingual
one_liner: 语义加权OCR评价指标semCER，匹配人类阅读感知效果优于传统CER
practical_value: '- 电商OCR场景（商品包装、资质审核、用户上传图文识别）评价可替换传统CER，重点惩罚商品名、品牌、地址等核心信息错误，降低业务审核漏判/误判率

  - 多模态内容理解、生成类任务的错误评估，可复用「LLM judge给单个编辑操作打语义危害权重」的思路，匹配业务对不同错误的容忍度，无需统一扣分

  - 跨境多语言电商OCR场景，可直接复用开源的semCER多语言权重，适配不同语言声调、变音符号的错误危害，无需重新标注训练'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统CER作为OCR和VLM的标准评价指标，对所有字符错误同等扣分，无法区分普通笔误和核心信息错误（如人名、品牌名错误）的实际损害，和人类阅读感知严重不符。
### 方法关键点
1. semCER保留CER的对齐逻辑和分母，无需分词，通过LLM judge给每个字符编辑操作打语义严重度权重，加权计算错误率；
2. 配套Normalized CER用于整体转录质量评估，semCER可拆解输出单错误的严重度排序。
### 关键结果
1. 中英越三语下，semCER的单错误权重与人类评分一致性达90%+；
2. CER与semCER结论冲突的样本中，人类更认同semCER的比例中英超75%，越南语持平；
3. 覆盖16种语言，开源6100万标注编辑、评分数据集和蒸馏后的轻量打分器。
