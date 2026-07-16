---
title: OvisOCR2 Technical Report
title_zh: OvisOCR2端到端文档解析模型技术报告
authors:
- Shiyin Lu
- Yinglun Li
- Yu Xia
- Yuhui Chen
- An-Yang Ji
- Jun-Peng Jiang
- Qing-Guo Chen
- Jianshan Zhao
- En Lin
- Haijun Li
affiliations:
- ATH-MaaS, Alibaba Group
arxiv_id: '2607.13639'
url: https://arxiv.org/abs/2607.13639
pdf_url: https://arxiv.org/pdf/2607.13639
published: '2026-07-14'
collected: '2026-07-16'
category: Multimodal
direction: 多模态文档解析 · 图像转结构化文本
tags:
- OCR
- Document Parsing
- Knowledge Distillation
- Reinforcement Learning
- Multimodal
one_liner: 0.8B参数量端到端文档解析模型，可将文档图像转结构化Markdown，性能超传统pipeline登顶公开基准
practical_value: '- 电商场景下商品详情页截图、商家资质凭证、用户评论截图的结构化抽取，可直接复用开源OvisOCR2，替代原OCR+规则的pipeline方案，降低开发成本

  - 小参数多模态模型训练可复用「大模型RL训练→on-policy蒸馏到小模型→模型融合」的范式，兼顾推理性能和部署成本

  - 构建多模态配对训练集时，可参考HTML同源渲染生成合成数据的方案，低成本扩充长尾场景的训练样本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统pipeline式文档解析流程拆分细、维护成本高，此前端到端方案性能始终低于pipeline方案，同时工业落地需要低延迟、小参数量的文档解析能力。
### 方法关键点
1. 构建混合数据引擎：融合过滤后的真实文档标注数据、HTML同源渲染的<文档图像, Markdown标注>合成数据，覆盖更多长尾场景；
2. 训练链路：先做监督微调，再在4B参数量分支上基于多组件奖励做强化学习，随后将训练好的4B模型on-policy蒸馏到0.8B小模型，最后做模型融合提升效果。
### 关键结果数字
- OmniDocBench v1.6总分96.58，为首个登顶该榜的端到端方案，超越此前占优的pipeline方法；
- PureDocBench Avg3得分75.06，位列第一；
- 内部长尾场景基准上取得最优效果，泛化性、鲁棒性表现优异。
