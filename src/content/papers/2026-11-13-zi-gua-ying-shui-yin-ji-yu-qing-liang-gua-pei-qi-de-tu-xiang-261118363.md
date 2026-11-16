---
title: 'Adaptable Watermarking: Transforming Image Watermarking Models via Lightweight
  Adapters'
title_zh: 自适应水印：基于轻量适配器的图像水印模型转换方法
authors:
- Mehrdad Saberi
- Vishal Asnani
- Shruti Agarwal
- Soheil Feizi
- John Collomosse
affiliations:
- University of Maryland
- Adobe Research
- University of Surrey
arxiv_id: '2611.18363'
url: https://arxiv.org/abs/2611.18363
pdf_url: https://arxiv.org/pdf/2611.18363
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 图像水印 · 参数高效迁移适配
tags:
- Image Watermarking
- Parameter Efficient Fine-Tuning
- Adapter
- Multi-domain Loss
- Model Adaptation
one_liner: 通过轻量适配器加多域残差对齐损失实现图像水印模型跨范式高效转换，无需全量重训
practical_value: '- 电商商品图、AIGC营销图防盗/溯源场景可复用该轻量适配方案，无需全量重训即可快速切换不同水印范式，适配多场景合规要求

  - 空间+梯度+频率的多域残差对齐损失设计可复用在图像类小样本微调任务中，有效保证微调后内容的视觉一致性

  - 1~2M参数量的低开销Adapter架构可直接集成到AIGC内容生成链路，水印嵌入/检测环节推理延迟几乎可忽略'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图像水印范式迭代快，不同模型互操作性差，全量重训适配新水印需求的成本高，无法快速满足版权保护、AI生成内容溯源等多场景诉求。
### 方法关键点
1. 给编解码结构的水印模型外挂轻量参数高效Adapter，无需全量重训即可实现水印范式转换
2. 训练引入多域残差对齐损失（覆盖空间、梯度、频率三个维度），同时新增秘密信息损失项保障水印比特准确率
3. 支持跨模型适配、多解码器并行推理架构
### 关键结果
在TrustMark、InvisMark、RoSteALS等5种主流水印模型上验证：单组件仅需1~2M可训练参数即可完成适配；适配后编码器输出残差与目标模型高度一致；解码器在常规图像增强、失真场景下的水印恢复精度接近最优水平，多解码器推理流水线仅需2M参数量的解码器Adapter。
