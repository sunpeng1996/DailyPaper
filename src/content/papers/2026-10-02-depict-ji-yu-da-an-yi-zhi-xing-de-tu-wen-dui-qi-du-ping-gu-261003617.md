---
title: 'DEPICT: Scoring Text-to-Image Alignment by Answer Agreement'
title_zh: DEPICT：基于答案一致性的图文对齐度评估方法
authors:
- Vasco Ramos
- Sandra Godinho Silva
- Joao Magalhaes
- Ricardo Rei
- Pedro Henrique Martins
affiliations:
- Sword Health
- NOVALINCS, NOVA University of Lisbon
arxiv_id: '2610.03617'
url: https://arxiv.org/abs/2610.03617
pdf_url: https://arxiv.org/pdf/2610.03617
published: '2026-10-02'
collected: '2026-10-05'
category: Multimodal
direction: 多模态 · 图文对齐评估
tags:
- Multimodal
- Image-Text Alignment
- Training-Free
- VLM
- T2I Evaluation
- Metric
one_liner: 提出免训练图文对齐评估指标DEPICT，大幅提升细粒度尤其是否定场景的对齐检测准确率
practical_value: '- 电商生成式商品图/海报合规校验：可复用DEPICT「细粒度答案一致性+整体评分融合」框架，检测生成图是否匹配商品文案要求，尤其可大幅提升「无logo」「非红色」等否定类约束的识别准确率

  - 多模态检索/推荐训练数据清洗：用该免训练指标过滤图文不匹配的商品素材，无需额外标注与微调，降低数据治理成本

  - VLM幻觉检测逻辑可迁移：将「固定参考答案替换为跨模态答案一致性」思路，用到Agent生成内容的事实性校验场景，例如商品介绍配图的一致性校验'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图文对齐评估方法存在三类缺陷：微调类指标绑定特定backbone与训练分布、整体评估易漏检细粒度错误、分解式评估依赖固定YES假设，否定类场景准确率极低，无法满足T2I生成、多模态数据治理等场景的高精度校验需求。
### 方法关键点
1. 完全免训练设计，无需偏好标注数据微调即可使用
2. 用图像侧VQA答案与纯文本侧VQA答案的一致性替代固定参考答案，按文案对问题的决定性程度加权计算细粒度得分
3. 融合细粒度一致性得分与整体对齐得分，弥补分解式评估损失的上下文信息
### 关键结果
- 否定类场景对齐检测准确率从19%提升至88%
- 在5个基准、11个不同backbone上测试，性能超过所有免训练对齐指标，在2/3的人类相关性基准上优于微调类评估器
