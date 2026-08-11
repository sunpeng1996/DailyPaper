---
title: Multimodal Model Diffing for Feature Discovery and Control
title_zh: 面向多模态大模型特征发现与控制的多模态模型差分框架
authors:
- Hunar Batra
- Lachin Naghashyar
- Ashkan Khakzar
- Philip Torr
- Christian Schroeder de Witt
- Constantin Venhoff
- Ronald Clark
affiliations:
- University of Oxford
- Microsoft
arxiv_id: '2608.09928'
url: https://arxiv.org/abs/2608.09928
pdf_url: https://arxiv.org/pdf/2608.09928
published: '2026-08-10'
collected: '2026-08-11'
category: Multimodal
direction: 多模态大模型特征发现与行为控制
tags:
- MLLM
- SAE
- Model Diffing
- Activation Steering
- Interpretability
one_liner: 提出MMDiff多模态差分框架，通过对比基LM与多模态适配后SAE特征实现MLLM行为审计与精准控制
practical_value: '- 多模态商品理解场景可复用MMDiff的SAE差分流程，精准定位OCR、空间感知等业务相关特征方向，无需全量微调即可定向提升商品图文字识别、货架商品位置识别准确率

  - 多模态内容安全管控场景，可通过该方法快速定位风险特征，消融对应方向即可降低多模态越狱攻击成功率，可落地于电商用户上传图片合规审核、AI生成内容安全控制

  - Activation Steering优化可借鉴MMDiff-CAA的分层+特征定向注入思路，比传统单层CAA效果更优，可用于提升推荐场景多模态Query理解、商品文案生成的准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前MLLM在视觉问答、OCR、空间推理等任务表现优异，但内部特征机制黑盒化，无法精准审计失败原因、抑制不良行为、定向增强特定能力；现有针对MLLM训练的SAE混合了基LM继承特征与多模态适配新增特征，无法区分两类特征，难以实现精准控制。

### 方法关键点
- 基于预训练基LM的SAE热启动，在多模态激活上微调得到多模态SAE，选择仅文本token训练的SAE做差分，保留LM特征对齐性的同时捕捉多模态适配带来的特征变化
- 通过解码器方向余弦相似度、视觉激活能量两个指标，筛选出多模态训练中发生旋转、响应视觉输入的适配特征集
- 用跨分布对比激活频率+词汇不变性过滤，得到任务专属特征，排除prompt词汇干扰
- 提出MMDiff-CAA steering，结合多层任务激活方向与特征关联层的SAE解码器方向注入，比传统单层CAA效果更优

### 关键结果数字
在LLaVA-MORE、PaliGemma 2、InternVL3.5三个MLLM上测试，覆盖空间推理、多模态安全、OCR三个任务：消融目标特征可让空间任务准确率平均降12%、OCR降17%，多模态安全攻击成功率降24%，且对通用VQA性能无影响；MMDiff-CAA相比单层CAA基线，空间推理准确率平均提升3.6%，OCR准确率平均提升1.8%。

**最值得记住的结论**：无需微调，仅通过SAE差分识别到的特征方向做定向干预，即可实现MLLM特定能力的精准调控，是大模型业务侧轻量化优化的高性价比路径。
