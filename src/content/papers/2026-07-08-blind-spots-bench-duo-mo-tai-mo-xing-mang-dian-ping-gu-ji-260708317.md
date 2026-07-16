---
title: 'Blind-Spots-Bench: Evaluating Blind Spots in Multimodal Models'
title_zh: Blind-Spots-Bench：多模态模型盲点评估基准
authors:
- Matteo Santelmo
- Xiuying Wei
- Israa Fakih
- Felix Bauer
- Juan Garcia Giraldo
- Chengkun Li
- Etienne Bamas
- Emmanuel Abbé
affiliations:
- École Polytechnique Fédérale de Lausanne (EPFL), Switzerland
arxiv_id: '2607.08317'
url: https://arxiv.org/abs/2607.08317
pdf_url: https://arxiv.org/pdf/2607.08317
published: '2026-07-08'
collected: '2026-07-16'
category: Eval
direction: 多模态模型评测 · 盲点诊断基准
tags:
- Multimodal
- Benchmark
- Model Evaluation
- Blind Spot
- VLM
- LLM
one_liner: 构建含235个样例的多模态模型盲点评估基准，配套自动化测评流水线用于模型弱点诊断
practical_value: '- 可复用该基准「人类易解但AI易错」的样例构造思路，自研Agent/LLM4Rec业务专项压力测试集，提前识别文案生成、多模态理解类场景的错误

  - 直接引入该基准的自动评分流水线，优化业务侧模型选型评估流程，对比闭源/开源LLM、VLM在业务适配前的基础能力短板

  - 参考基准的任务分层taxonomy，对电商多模态搜推、商品文案生成、智能客服等场景的错误case做分类归因，精准定位模型迭代方向'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有主流AI基准普遍存在能力评估盲区，无法识别模型在人类看来极为简单的任务上的失败case，难以支撑模型弱点的精准诊断。
### 方法关键点
收集AI课程学生提交的原生问题，清洗标注后构建含235个样例的盲点评估数据集，配套适配LLM、VLM、图像生成模型的自动化评分流水线，设计专属任务分类体系。
### 关键结果数字
闭源前沿模型性能领先开源模型约10%，即使二者在现有公开基准上表现接近；没有模型能在所有任务类型上占优，部分任务对所有参评模型都存在挑战。
