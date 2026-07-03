---
title: 'AnyGroundBench: A Specialized-Domain Benchmark for Video Grounding in Vision-Language
  Models'
title_zh: AnyGroundBench：面向视觉语言模型视频定位的垂直领域评测基准
authors:
- Rintaro Otsubo
- Ryo Fujii
- Reina Ishikawa
- Taiki Kanaya
- Kanta Sawafuji
- Hiroki Kajita
- Shigeki Sakai
- Hideo Saito
- Ryo Hachiuma
affiliations:
- Keio University
- Keio AI Research Center
- Keio University School of Medicine
- NVIDIA
arxiv_id: '2607.02269'
url: https://arxiv.org/abs/2607.02269
pdf_url: https://arxiv.org/pdf/2607.02269
published: '2026-07-01'
collected: '2026-07-03'
category: Eval
direction: 多模态视频定位能力评测基准
tags:
- VLM
- Spatio-Temporal Video Grounding
- Benchmark
- Domain Adaptation
- In-Context Learning
one_liner: 构建覆盖5个垂直领域的视频时空定位评测基准，系统评估VLM的零样本与上下文学习适配能力
practical_value: '- 做电商短视频/直播多模态内容理解（如话术对应商品片段匹配、违规片段定位）时，不要直接用通用VLM零样本跑垂直场景，需优先做小样本域适配

  - 评测多模态推荐/Agent的视频理解能力时，可复用该基准「通用基准+垂直领域子数据集+分能力校验」的评测框架

  - 多模态VLM业务落地时，可优先验证ICL和少量LoRA微调在垂直视频时空定位任务上的收益，降低适配成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM的Spatio-Temporal Video Grounding（STVG）评测仅覆盖通用生活场景，无法衡量模型垂直领域适配能力，和实际业务场景严重脱节，且全量预训练覆盖所有领域数据不具备可行性。
### 方法关键点
1. 推出AnyGroundBench评测基准，覆盖动物、工业、体育、手术、公共安全5个垂直领域，将新采集的专家标注视频和现有公开数据集统一做高保真稠密时空标注
2. 配套专属训练子集，支持系统衡量模型的域迁移适配能力
3. 评测维度包含零样本泛化、In-Context Learning（ICL）能力，且测试约束贴合实际业务算力情况
### 关键结果
对15个SOTA VLM的评测显示，现有模型在垂直领域的零样本和ICL适配效果均不达标，暴露出时空推理能力的显著缺陷
